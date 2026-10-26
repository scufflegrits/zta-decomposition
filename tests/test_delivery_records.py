"""Delivery records preserve technical facts independently of customer decisions."""
from pathlib import Path
import tempfile
import unittest

from tools.audit_zta import audit
from tools.document_metadata import frontmatter


def table(name, parent, lineage, headers, rows):
    return (f'\n<!-- zta-table: id={name}; parent={parent}; lineage={lineage} -->\n\n'
            + '| ' + ' | '.join(headers) + ' |\n'
            + '|' + '|'.join('---' for _ in headers) + '|\n'
            + ''.join('| ' + ' | '.join(row) + ' |\n' for row in rows) + '\n')


class DeliveryRecordTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / 'README.md'
        self.base = frontmatter(dict(schema_version=1, id='DOC-FIXTURE', title='Fixture',
            document_type='guide', parent='ROOT', lineage=['ROOT'], owner='Engineering',
            owner_status='proposed', document_status='draft', implementation_status='unvalidated',
            baseline_date='2026-10-25'))
        self.base += table('TBL-PILLAR', 'ROOT', 'ROOT', ['Parent ID', 'Pillar ID'], [['ROOT', 'ZT-05']])
        self.base += table('TBL-CONTROL', 'ZT-05', 'ROOT>ZT-05', ['Parent ID', 'Control ID'], [['ZT-05', 'NET-04']])
        self.base += table('TBL-REQ', 'NET-04', 'ROOT>ZT-05>NET-04', ['Parent ID', 'Requirement ID'], [['NET-04', 'MAC-001']])
        self.base += table('TBL-TEST', 'MAC-001', 'ROOT>ZT-05>NET-04>MAC-001', ['Parent ID', 'Test ID'], [['MAC-001', 'TEST-003']])
        for name in ('result.txt', 'config.txt', 'decision.txt'):
            (self.root / name).write_text('Fixture artifact only')
        self.implementation = {
            'Parent ID': 'NET-04', 'Implementation ID': 'IMP-MAC-001', 'Scope': 'Site A peer link',
            'SOW reference': 'Fixture SOW-001', 'Baseline': 'baseline-1', 'Deployment state': 'Implemented',
            'Configuration': '[configuration](config.txt)', 'Requirement IDs': 'MAC-001', 'Test IDs': 'TEST-003',
            'Verification result': 'Passed', 'Verification basis': 'Selected link session verification',
            'Evidence IDs': 'EVD-001', 'Limitation': 'None', 'Operational impact': 'No disruption observed',
            'Residual risk': 'Other protections are separate', 'Compensating controls': 'None required for fixture',
        }
        self.evidence = {
            'Parent ID': 'TEST-003', 'Evidence ID': 'EVD-001', 'Artifact': '[execution](result.txt)',
            'Result': 'Pass', 'Reviewer': 'Fixture reviewer', 'Implementation IDs': 'IMP-MAC-001', 'Baseline': 'baseline-1',
        }
        self.acceptance = {
            'Parent ID': 'NET-04', 'Acceptance ID': 'ACC-MAC-001', 'Scope': 'Site A peer link',
            'SOW reference': 'Fixture SOW-001', 'Baseline': 'baseline-1', 'Implementation IDs': 'IMP-MAC-001',
            'Decision': 'Accepted as implemented', 'Decision basis': 'Reviewed selected outcome',
            'Authority': 'Fixture customer representative', 'Decision date': '2026-10-25',
            'Decision artifact': '[decision](decision.txt)',
        }

    def result(self, evidence=True, acceptance=True):
        text = self.base
        if evidence:
            text += table('TBL-EVIDENCE', 'TEST-003', 'ROOT>ZT-05>NET-04>MAC-001>TEST-003',
                          list(self.evidence), [list(self.evidence.values())])
        text += table('TBL-IMPL', 'NET-04', 'ROOT>ZT-05>NET-04',
                      list(self.implementation), [list(self.implementation.values())])
        if acceptance:
            text += table('TBL-ACCEPT', 'NET-04', 'ROOT>ZT-05>NET-04',
                          list(self.acceptance), [list(self.acceptance.values())])
        self.path.write_text(text)
        return audit(self.root)

    def codes(self, **kwargs):
        return {issue.code for issue in self.result(**kwargs).issues}

    def test_verified_and_accepted_implementation(self):
        self.assertEqual([], self.result().issues)

    def test_documented_unsupported_outcome_can_be_accepted_without_execution(self):
        self.implementation.update({'Deployment state': 'Not implemented', 'Configuration': '',
            'Verification result': 'Not executed', 'Evidence IDs': '', 'Test IDs': '',
            'Limitation': 'Ports lack support; replacing equipment would interrupt required work'})
        self.acceptance['Decision'] = 'Accepted with documented limitations'
        self.assertEqual([], self.result(evidence=False).issues)

    def test_customer_disposition_does_not_convert_failed_verification_to_pass(self):
        self.evidence['Result'] = 'Fail'
        self.implementation.update({'Verification result': 'Failed', 'Limitation': 'Failure under selected profile'})
        self.acceptance['Decision'] = 'Accepted with documented limitations'
        result = self.result()
        self.assertEqual([], result.issues)
        self.assertEqual('Failed', result.entities['IMP-MAC-001'].cells['Verification result'])

    def test_pending_decision_requires_no_final_authority_or_artifact(self):
        self.acceptance.update({'Decision': 'Pending review', 'Decision artifact': '', 'Authority': '', 'Decision date': ''})
        self.assertEqual([], self.result().issues)

    def test_positive_verification_needs_evidence(self):
        self.implementation['Evidence IDs'] = ''
        self.assertIn('implementation-evidence', self.codes(evidence=False, acceptance=False))

    def test_evidence_must_match_implementation_and_baseline(self):
        for column, value in [('Baseline', 'baseline-other'), ('Implementation IDs', 'IMP-OTHER')]:
            with self.subTest(column=column):
                original = self.evidence[column]
                self.evidence[column] = value
                self.assertIn('implementation-evidence', self.codes(acceptance=False))
                self.evidence[column] = original

    def test_failed_evidence_cannot_support_pass(self):
        self.evidence['Result'] = 'Fail'
        self.assertIn('implementation-evidence', self.codes(acceptance=False))

    def test_missing_configuration_or_decision_artifact(self):
        (self.root / 'config.txt').unlink()
        self.assertIn('delivery-artifact', self.codes())
        self.implementation['Configuration'] = '[configuration](result.txt)'
        (self.root / 'decision.txt').unlink()
        self.assertIn('delivery-artifact', self.codes())

    def test_customer_acceptance_needs_authority_date_and_artifact(self):
        for column in ('Authority', 'Decision date', 'Decision artifact'):
            with self.subTest(column=column):
                original = self.acceptance[column]
                self.acceptance[column] = ''
                self.assertTrue(self.codes() & {'delivery-record', 'delivery-artifact', 'acceptance-record'})
                self.acceptance[column] = original
        self.acceptance['Decision date'] = '2026-02-30'
        self.assertIn('acceptance-record', self.codes())

    def test_accepted_baseline_and_sow_match_referenced_implementation(self):
        for column in ('Baseline', 'SOW reference'):
            with self.subTest(column=column):
                original = self.acceptance[column]
                self.acceptance[column] = 'different'
                self.assertIn('acceptance-record', self.codes())
                self.acceptance[column] = original

    def test_simple_acceptance_cannot_hide_documented_limitation(self):
        self.implementation['Limitation'] = 'Selected port restriction'
        self.assertIn('acceptance-record', self.codes())

    def test_limitations_decision_requires_actual_limitation(self):
        self.acceptance['Decision'] = 'Accepted with documented limitations'
        self.assertIn('acceptance-record', self.codes())

    def test_invalid_status_and_missing_operational_context(self):
        self.implementation['Deployment state'] = 'green'
        self.assertIn('delivery-status', self.codes(acceptance=False))
        self.implementation['Operational impact'] = ''
        self.assertIn('delivery-record', self.codes(acceptance=False))

    def test_wrong_reference_kind_is_rejected(self):
        self.implementation['Requirement IDs'] = 'TEST-003'
        self.assertIn('delivery-reference', self.codes(acceptance=False))

    def test_unimplemented_protection_cannot_claim_pass(self):
        self.implementation.update({'Deployment state': 'Not implemented', 'Limitation': 'Unsupported hardware'})
        self.assertIn('delivery-status', self.codes(acceptance=False))

    def test_new_record_kinds_still_require_control_parent(self):
        self.implementation['Parent ID'] = 'MAC-001'
        self.assertIn('hierarchy-level', self.codes(acceptance=False))

    def test_references_cannot_cross_control_scope(self):
        self.base += table('TBL-OTHER-CONTROL', 'ZT-05', 'ROOT>ZT-05',
                           ['Parent ID', 'Control ID'], [['ZT-05', 'NET-05']])
        self.base += table('TBL-OTHER-REQ', 'NET-05', 'ROOT>ZT-05>NET-05',
                           ['Parent ID', 'Requirement ID'], [['NET-05', 'OTHER-001']])
        self.implementation['Requirement IDs'] = 'OTHER-001'
        self.assertIn('delivery-reference', self.codes(acceptance=False))

    def test_passed_claim_needs_evidence_for_every_listed_test(self):
        self.base += table('TBL-SECOND-TEST', 'MAC-001', 'ROOT>ZT-05>NET-04>MAC-001',
                           ['Parent ID', 'Test ID'], [['MAC-001', 'TEST-001']])
        self.implementation['Test IDs'] = 'TEST-003, TEST-001'
        self.assertIn('implementation-evidence', self.codes(acceptance=False))

    def test_external_decision_requires_local_record(self):
        self.acceptance['Decision artifact'] = '[decision](https://records.example.invalid/decision)'
        self.assertIn('delivery-artifact', self.codes())

    def test_acceptance_reference_requires_implementation_entity(self):
        self.acceptance['Implementation IDs'] = 'TEST-003'
        self.assertIn('delivery-reference', self.codes())


if __name__ == '__main__':
    unittest.main()
