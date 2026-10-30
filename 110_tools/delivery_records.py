"""Consistency checks for implementation and customer-disposition records."""
from datetime import date
import re


DEPLOYMENT_STATES = {'Planned', 'Implemented', 'Partially implemented', 'Not implemented'}
VERIFICATION_RESULTS = {'Not executed', 'Passed', 'Failed', 'Inconclusive', 'Not applicable'}
DECISIONS = {'Pending review', 'Accepted as implemented', 'Accepted with documented limitations',
             'Changes requested', 'Rejected'}


def identifiers(value):
    return list(filter(None, re.split(r'[,\s]+', value)))


def check_delivery_records(result, chain, local_target, destinations):
    def error(entity, code, message):
        result.error(entity.path, entity.line, code, message)

    def required(entity, columns):
        for column in columns:
            if not entity.cells.get(column):
                error(entity, 'delivery-record', f'{entity.id} requires {column}')

    def references(entity, column, kind, mandatory=False):
        ids = identifiers(entity.cells.get(column, ''))
        if mandatory and not ids:
            error(entity, 'delivery-reference', f'{entity.id} requires {column}')
        found = []
        for identity in ids:
            target = result.entities.get(identity)
            ancestry = chain(result, identity)
            if not target or target.kind != kind or not ancestry or entity.parent not in ancestry:
                error(entity, 'delivery-reference', f'{column}: {identity} must reference {kind} in control {entity.parent}')
            else:
                found.append(target)
        return found

    def artifact(entity, column, mandatory=False):
        value = entity.cells.get(column, '')
        if not value and not mandatory:
            return
        files = []
        for link in destinations(value):
            target = local_target(result, entity.path, entity.line, link)
            if target and target[0].is_file():
                files.append(target[0])
        if not files:
            error(entity, 'delivery-artifact', f'{entity.id} requires an existing local {column} file or local record of external artifacts')

    for entity in result.entities.values():
        row = entity.cells
        if entity.kind == 'Implementation ID':
            required(entity, ('Scope', 'SOW reference', 'Baseline', 'Deployment state', 'Verification result',
                              'Verification basis', 'Limitation', 'Operational impact', 'Residual risk', 'Compensating controls'))
            deployment = row.get('Deployment state')
            verification = row.get('Verification result')
            if deployment not in DEPLOYMENT_STATES:
                error(entity, 'delivery-status', f'Unsupported deployment state: {deployment!r}')
            if verification not in VERIFICATION_RESULTS:
                error(entity, 'delivery-status', f'Unsupported verification result: {verification!r}')
            requirements = references(entity, 'Requirement IDs', 'Requirement ID', mandatory=True)
            tests = references(entity, 'Test IDs', 'Test ID')
            evidence = references(entity, 'Evidence IDs', 'Evidence ID')
            for test in tests:
                if test.parent not in {item.id for item in requirements}:
                    error(entity, 'delivery-reference', f'{test.id} must descend from a listed requirement')
            for item in evidence:
                if item.parent not in {test.id for test in tests}:
                    error(entity, 'implementation-evidence', f'{item.id} must descend from a listed test')
                if entity.id not in identifiers(item.cells.get('Implementation IDs', '')) or item.cells.get('Baseline') != row.get('Baseline'):
                    error(entity, 'implementation-evidence', f'{item.id} must identify implementation {entity.id} and the same Baseline')
            artifact(entity, 'Configuration', deployment in {'Implemented', 'Partially implemented'})
            if verification in {'Passed', 'Failed', 'Inconclusive'} and (not tests or not evidence):
                error(entity, 'implementation-evidence', f'{verification} requires test and execution-evidence references')
            if verification == 'Passed':
                if deployment not in {'Implemented', 'Partially implemented'}:
                    error(entity, 'delivery-status', 'Passed implementation verification requires a deployed protection')
                if any(item.cells.get('Result', '').casefold() not in {'pass', 'passed'} for item in evidence):
                    error(entity, 'implementation-evidence', 'Passed requires passing evidence for the stated conclusion')
                for test in tests:
                    if not any(item.parent == test.id for item in evidence):
                        error(entity, 'implementation-evidence', f'Passed requires evidence for listed test {test.id}')
            if verification == 'Failed' and not any(item.cells.get('Result', '').casefold() in {'fail', 'failed'} for item in evidence):
                error(entity, 'implementation-evidence', 'Failed requires a failed execution record')
            if deployment != 'Implemented' and row.get('Limitation', '').casefold() == 'none':
                error(entity, 'delivery-record', 'Document the limitation or outstanding work for a protection not fully implemented')
        elif entity.kind == 'Acceptance ID':
            required(entity, ('Scope', 'SOW reference', 'Baseline', 'Decision', 'Decision basis'))
            implementations = references(entity, 'Implementation IDs', 'Implementation ID', mandatory=True)
            decision = row.get('Decision')
            if decision not in DECISIONS:
                error(entity, 'delivery-status', f'Unsupported acceptance decision: {decision!r}')
            if decision != 'Pending review':
                required(entity, ('Authority', 'Decision date'))
                artifact(entity, 'Decision artifact', mandatory=True)
                try:
                    value = row.get('Decision date', '')
                    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
                        raise ValueError()
                    date.fromisoformat(value)
                except ValueError:
                    error(entity, 'acceptance-record', 'Final decisions require a valid YYYY-MM-DD Decision date')
            else:
                artifact(entity, 'Decision artifact')
            if decision in {'Accepted as implemented', 'Accepted with documented limitations'}:
                for item in implementations:
                    if item.cells.get('Baseline') != row.get('Baseline') or item.cells.get('SOW reference') != row.get('SOW reference'):
                        error(entity, 'acceptance-record', f'{item.id} must match the accepted Baseline and SOW reference')
                if decision == 'Accepted as implemented':
                    for item in implementations:
                        if (item.cells.get('Deployment state') != 'Implemented'
                                or item.cells.get('Verification result') != 'Passed'
                                or item.cells.get('Limitation', '').casefold() != 'none'):
                            error(entity, 'acceptance-record', 'Use a documented-limitations decision when implementation, verification or limitations remain')
                elif not any(item.cells.get('Limitation', '').casefold() not in {'', 'none'} for item in implementations):
                    error(entity, 'acceptance-record', 'Acceptance with documented limitations requires a linked limitation')
