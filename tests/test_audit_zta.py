"""Behavior tests for broken and valid documentation fixtures, without dependencies."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

from tools.audit_zta import audit, render_report


DOC = '<!-- zta-doc: id=DOC-FIXTURE; parent=ROOT; lineage=ROOT -->\n'


def table(table_id, parent, lineage, identity, rows, extras=()):
    headers = ['Parent ID', identity, *extras]
    return (f'\n<!-- zta-table: id={table_id}; parent={parent}; lineage={lineage} -->\n\n'
            + '| ' + ' | '.join(headers) + ' |\n'
            + '|' + '|'.join('---' for _ in headers) + '|\n'
            + ''.join('| ' + ' | '.join(row) + ' |\n' for row in rows) + '\n')


def hierarchy():
    return (DOC + '# Fixture\n'
            + table('TBL-PILLAR', 'ROOT', 'ROOT', 'Pillar ID', [['ROOT', 'ZT-05']])
            + table('TBL-CONTROL', 'ZT-05', 'ROOT>ZT-05', 'Control ID', [['ZT-05', 'NET-04']])
            + table('TBL-REQ', 'NET-04', 'ROOT>ZT-05>NET-04', 'Requirement ID', [['NET-04', 'MAC-001']])
            + table('TBL-TEST', 'MAC-001', 'ROOT>ZT-05>NET-04>MAC-001', 'Test ID', [['MAC-001', 'TEST-003']]))


class AuditorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / 'README.md'
        self.path.write_text(hierarchy())

    def run_audit(self, text=None):
        if text is not None:
            self.path.write_text(text)
        return audit(self.root)

    def codes(self, text=None):
        return {i.code for i in self.run_audit(text).issues}

    def test_valid_hierarchy(self):
        self.assertEqual([], self.run_audit().issues)

    def test_duplicate_document_id_across_files(self):
        (self.root / 'other.md').write_text(DOC)
        self.assertIn('duplicate-id', self.codes())

    def test_duplicate_table_id(self):
        self.assertIn('duplicate-id', self.codes(hierarchy() + table('TBL-REQ', 'NET-04', 'ROOT>ZT-05>NET-04', 'Requirement ID', [['NET-04', 'MAC-002']])))

    def test_duplicate_row_id(self):
        self.assertIn('duplicate-id', self.codes(hierarchy() + table('TBL-DUP', 'NET-04', 'ROOT>ZT-05>NET-04', 'Requirement ID', [['NET-04', 'MAC-001']])))

    def test_missing_parent(self):
        self.assertIn('missing-parent', self.codes(hierarchy().replace('NET-04', 'NET-99', 1)))

    def test_wrong_grandparent_lineage(self):
        self.assertIn('lineage', self.codes(hierarchy().replace('lineage=ROOT>ZT-05>NET-04>MAC-001', 'lineage=ROOT>ZT-01>NET-04>MAC-001')))

    def test_cycle(self):
        text = DOC + table('TBL-A', 'ROW-B', 'ROOT>ROW-B', 'Row ID', [['ROW-B', 'ROW-A']])
        text += table('TBL-B', 'ROW-A', 'ROOT>ROW-A', 'Row ID', [['ROW-A', 'ROW-B']])
        self.assertIn('ancestry', self.codes(text))

    def test_orphaned_table(self):
        self.assertIn('orphan-table', self.codes(DOC + '<!-- zta-table: id=TBL-ORPHAN; parent=ROOT; lineage=ROOT -->\nSome prose.'))

    def test_missing_table_metadata(self):
        text = hierarchy().replace('<!-- zta-table: id=TBL-REQ; parent=NET-04; lineage=ROOT>ZT-05>NET-04 -->', '')
        self.assertIn('missing-table-metadata', self.codes(text))

    def test_missing_document_metadata(self):
        self.assertIn('document-metadata', self.codes('# No declaration\n'))

    def test_table_outside_document_scope(self):
        text = hierarchy() + table('TBL-OTHER', 'ROOT', 'ROOT', 'Pillar ID', [['ROOT', 'ZT-01']])
        text = text.replace('id=DOC-FIXTURE; parent=ROOT; lineage=ROOT',
                            'id=DOC-FIXTURE; parent=ZT-01; lineage=ROOT>ZT-01')
        self.assertIn('document-table-scope', self.codes(text))

    def test_malformed_url_is_reported_without_crashing(self):
        self.assertIn('broken-link', self.codes(hierarchy() + '\n[bad](https://[broken)\n'))

    def test_conflicting_row_and_table_parents(self):
        text = hierarchy().replace('| NET-04 | MAC-001 |', '| ZT-05 | MAC-001 |')
        self.assertIn('table-parent', self.codes(text))
        self.assertIn('hierarchy-level', self.codes(text))

    def test_requirement_under_wrong_kind(self):
        text = DOC + table('TBL-ROOT', 'ROOT', 'ROOT', 'Requirement ID', [['ROOT', 'MAC-001']])
        self.assertIn('hierarchy-level', self.codes(text))

    def test_broken_relative_link(self):
        result = self.run_audit(hierarchy() + '\n[missing](missing.md)\n')
        self.assertIn('broken-link', {i.code for i in result.issues})
        issue = next(i for i in result.issues if i.code == 'broken-link')
        self.assertEqual(self.path, issue.path)
        self.assertGreater(issue.line, 1)

    def test_heading_anchors_and_repeat_suffix(self):
        self.assertEqual(set(), self.codes(hierarchy() + '\n## Port `support`\n## Port `support`\n[ok](#port-support-1)\n'))
        self.assertIn('broken-anchor', self.codes(hierarchy() + '\n[bad](#missing)\n'))

    def test_reference_style_link(self):
        self.assertIn('broken-link', self.codes(hierarchy() + '\n[missing][target]\n[target]: absent.md\n'))
        self.assertIn('broken-link', self.codes(hierarchy() + '\n[missing][undefined]\n'))

    def test_links_with_spaces_and_parentheses(self):
        (self.root / 'notes (draft).txt').write_text('Notes')
        self.assertEqual(set(), self.codes(hierarchy() + '\n[file](<notes (draft).txt>)\n'))
        (self.root / 'notes(draft).txt').write_text('Notes')
        self.assertEqual(set(), self.codes(hierarchy() + '\n[file](notes(draft).txt)\n'))

    def test_fenced_and_inline_examples_are_not_entities(self):
        examples = '\n````markdown\n```\n' + hierarchy() + '\n```\n````\n'
        examples += '\n`<!-- zta-doc: id=DOC-FIXTURE; parent=ROOT; lineage=ROOT -->`\n'
        examples += '\n~~~text\n[bad](absent.md)\n~~~\n'
        self.assertEqual(set(), self.codes(hierarchy() + examples))

    def test_ordinary_comments_are_ignored(self):
        self.assertEqual(set(), self.codes(hierarchy() + '\n<!--\n[bad](missing.md)\n-->\n'))

    def test_missing_decomposition_file(self):
        text = hierarchy() + table('TBL-MORE', 'NET-04', 'ROOT>ZT-05>NET-04', 'Requirement ID', [['NET-04', 'MAC-002', '[detail](absent.md)']], ['Decomposition'])
        self.assertIn('decomposition', self.codes(text))

    def test_decomposition_document_parent(self):
        text = hierarchy() + table('TBL-MORE', 'NET-04', 'ROOT>ZT-05>NET-04', 'Requirement ID', [['NET-04', 'MAC-002', '[detail](detail.md)']], ['Decomposition'])
        child = self.root / 'detail.md'
        child.write_text('<!-- zta-doc: id=DOC-DETAIL; parent=MAC-001; lineage=ROOT>ZT-05>NET-04>MAC-001 -->\n')
        self.assertIn('decomposition', self.codes(text))
        child.write_text(child.read_text().replace('MAC-001', 'MAC-002'))
        self.assertEqual(set(), self.codes(text))

    def test_missing_architecture_reference(self):
        text = hierarchy() + table('TBL-MORE', 'NET-04', 'ROOT>ZT-05>NET-04', 'Requirement ID', [['NET-04', 'MAC-002', 'NET-99']], ['References'])
        self.assertIn('architecture-reference', self.codes(text))

    def test_validated_without_evidence(self):
        text = hierarchy() + table('TBL-MORE', 'NET-04', 'ROOT>ZT-05>NET-04', 'Requirement ID', [['NET-04', 'MAC-002', 'Validated']], ['Status'])
        self.assertIn('validated-evidence', self.codes(text))

    def test_validated_with_real_descendant_evidence(self):
        text = hierarchy().replace('| Requirement ID |', '| Requirement ID | Status | Evidence IDs |').replace('|---|---|\n| NET-04 | MAC-001 |', '|---|---|---|---|\n| NET-04 | MAC-001 | Validated | EVD-001 |')
        text += table('TBL-EVIDENCE', 'TEST-003', 'ROOT>ZT-05>NET-04>MAC-001>TEST-003', 'Evidence ID', [['TEST-003', 'EVD-001', '[log](session.txt)', 'Pass', 'Engineer']], ['Artifact', 'Result', 'Reviewer'])
        (self.root / 'session.txt').write_text('Actual session evidence in this fixture.')
        self.assertEqual(set(), self.codes(text))
        (self.root / 'session.txt').unlink()
        self.assertIn('evidence-record', self.codes(text))

    def test_unrelated_evidence_is_rejected(self):
        text = hierarchy() + table('TBL-MORE', 'NET-04', 'ROOT>ZT-05>NET-04', 'Requirement ID', [['NET-04', 'MAC-002', 'Validated', 'EVD-001']], ['Status', 'Evidence IDs'])
        text += table('TBL-EVIDENCE', 'TEST-003', 'ROOT>ZT-05>NET-04>MAC-001>TEST-003', 'Evidence ID', [['TEST-003', 'EVD-001', '[log](session.txt)', 'Pass', 'Engineer']], ['Artifact', 'Result', 'Reviewer'])
        (self.root / 'session.txt').write_text('Evidence')
        self.assertIn('validated-evidence', self.codes(text))

    def test_external_only_evidence_is_rejected(self):
        text = hierarchy() + table('TBL-EVIDENCE', 'TEST-003', 'ROOT>ZT-05>NET-04>MAC-001>TEST-003', 'Evidence ID', [['TEST-003', 'EVD-001', '[log](https://example.com/log)', 'Pass', 'Engineer']], ['Artifact', 'Result', 'Reviewer'])
        self.assertIn('evidence-record', self.codes(text))

    def test_malformed_metadata_and_row_width(self):
        self.assertIn('metadata', self.codes(DOC.replace('lineage=ROOT', 'lineage=ROOT; parent=ROOT')))
        self.assertIn('table-schema', self.codes(hierarchy().replace('| NET-04 | MAC-001 |', '| NET-04 | MAC-001 | extra |')))

    def test_exclusions_are_explicit_in_report(self):
        (self.root / 'import.md').write_text('Original import without metadata')
        (self.root / 'audit-config.json').write_text(json.dumps({'exclude': ['import.md']}))
        result = self.run_audit()
        self.assertEqual([], result.issues)
        self.assertIn('`import.md`', render_report(result))

    def test_generated_report_is_not_a_managed_document(self):
        report = self.root / 'audit-report.md'
        report.write_text('Generated report')
        self.assertEqual([], audit(self.root, report).issues)

    def test_invalid_config_is_an_error(self):
        (self.root / 'audit-config.json').write_text('{broken')
        self.assertIn('configuration', self.codes())

    def test_outside_repository_links_are_rejected(self):
        self.assertIn('outside-root', self.codes(hierarchy() + '\n[escape](../)\n'))

    def test_cli_exit_codes_and_written_report(self):
        script = Path(__file__).resolve().parents[1] / 'tools' / 'audit_zta.py'
        report = self.root / 'audit-report.md'
        command = [sys.executable, str(script), '--root', str(self.root), '--report', str(report)]
        good = subprocess.run(command, text=True, capture_output=True)
        self.assertEqual(0, good.returncode, good.stdout + good.stderr)
        self.assertIn('PASS', report.read_text())
        self.path.write_text(hierarchy() + '\n[missing](missing.md)\n')
        bad = subprocess.run(command, text=True, capture_output=True)
        self.assertEqual(1, bad.returncode)
        self.assertIn('broken-link', report.read_text())


if __name__ == '__main__':
    unittest.main()
