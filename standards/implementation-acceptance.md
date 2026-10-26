---
schema_version: 1
id: DOC-STD-DELIVERY
title: Implementation and customer acceptance records
document_type: standard
parent: ROOT
lineage:
- ROOT
owner: Architecture / Security Engineering
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-25'
---

# Implementation and customer acceptance records

Use these records to answer: What did we implement? Did it behave as claimed? What limitations remain? What did the customer decide against the applicable contract Statement of Work (SOW) requirements?

Follow [ADR-014](../architecture/decisions/ADR-014.md). Report decisions and supporting facts without calculating a coverage percentage. The [adoption checklist](../HOW-TO-USE.md#program-adoption-checklist) remains the single place to record program working agreements.

## Three separate conclusions

| Conclusion | Recorded as | Basis |
|---|---|---|
| Deployed protection | Deployment state | Actual identified equipment, scope and configuration |
| Observed behavior | Verification result | Test executions and reviewed evidence for that scope/baseline |
| Customer disposition | Decision | Authorized decision artifact against the applicable SOW |

Customer acceptance with limitations can coexist with a protection not implemented, not tested or observed to fail. Those technical facts remain unchanged. A documented limitation does not itself grant acceptance; a decision must actually be recorded. Where there is no customer decision, report Pending review.

## Implementation records

Add actual rows to a traceable table under the applicable Control ID, using `Implementation ID` as its identity column. Allocate a stable ID such as `IMP-MAC-001` only when recording actual scope. Each row covers one identifiable link or a clearly bounded group with the same outcome; split different port capabilities, baselines, verification results or limitations into separate records. Identify both peers, site, model/module/port, media and software/licensing in Scope or linked inventory. Preserve unsupported or deferred scope as records rather than hiding it.

| Column | Required content |
|---|---|
| Parent ID / Implementation ID | Authoritative control parent and globally unique implementation identity |
| Scope | Exact instance or bounded group and linked inventory |
| SOW reference | Adopted clause/source reference; nonempty human-reviewed text, not a new hierarchy parent |
| Baseline | Exact reviewed configuration/engineering baseline identifier; use one consistent identifier in linked execution records |
| Deployment state | Planned, Implemented, Partially implemented, Not implemented |
| Configuration | Local file link or local record of externally stored configuration; required for Implemented and Partially implemented |
| Requirement IDs / Test IDs | Comma-separated existing engineering IDs; requirements required, tests required for executed verification |
| Verification result | Not executed, Passed, Failed, Inconclusive, Not applicable |
| Verification basis | What conclusion the tests support, why tests do not apply, or what remains unexecuted |
| Evidence IDs | Current execution evidence supporting this scope/baseline; required for Passed, Failed and Inconclusive |
| Limitation | Specific constraint or outstanding work; write None only when there is none for the stated scope |
| Operational impact | Observed or investigated effect on functionality, performance and user/administrative workflow; distinguish projected from measured effects |
| Residual risk | Remaining exposure and uncertainty |
| Compensating controls | Identified alternatives, or None with explanation where relevant |
| Jira stories | Optional actual delivery links under the manual Jira rules |

Tests must belong to the listed requirements in the same control. Evidence must belong to the listed tests and include `Implementation IDs` and `Baseline` columns identifying the implementation and exact matching baseline. Use ordinary plain-text IDs and baseline values in audited fields. General evidence rules still require an actual local artifact/record, result and reviewer. Preserve earlier failures and retests; list the evidence supporting the current verification conclusion here and link history in the execution records.

Passed means the listed applicable tests passed for this implementation's stated scope; every listed test needs passing evidence. It does not validate all requirements globally. Failed requires failed evidence. Reviewer judgment determines test sufficiency, evidence authenticity and operational acceptability. A limitation alone is not an audit error; missing facts or unsupported claims are.

## Customer acceptance records

Add actual decisions, or an actual submission awaiting review, to a traceable table under the Control ID with `Acceptance ID` as its identity column. This is the management-facing decision summary. Link one or more implementation records; the acceptance record has the same control parent, rather than becoming a parent of the requirements/tests.

| Column | Required content |
|---|---|
| Parent ID / Acceptance ID | Control parent and globally unique acceptance-record identity |
| Scope / SOW reference / Baseline | Exact decision scope, applicable contract obligation and reviewed baseline |
| Implementation IDs | Comma-separated records of the outcomes being considered |
| Decision | Pending review, Accepted as implemented, Accepted with documented limitations, Changes requested, Rejected |
| Decision basis | Rationale and explicit disposition of limitations and operational tradeoffs |
| Authority / Decision date | Named designated authority and YYYY-MM-DD date for a final decision |
| Decision artifact | Existing local approval/review file or local record of externally stored decision; required for a final decision |

Accepted as implemented requires linked records that are Implemented, Passed and have Limitation set to None for their stated scope. Accepted with documented limitations requires at least one linked documented limitation and an actual decision artifact; it does not require every protection to be deployed or every test to pass. In either accepted state, the implementation records must match the accepted SOW reference and baseline. Record the actual scope of the decision, not a wider claim. Changes requested and Rejected preserve the customer's recorded disposition; Pending review claims no final acceptance.

Use text statuses; optional color cues may aid presentation but cannot replace the status or its proof. Preserve decision history and create a new dated record when a baseline or decision changes. Do not overwrite an earlier acceptance so it appears to cover later changes. Retain configuration and evidence baselines referenced by historical decisions.

## Registers and templates

The [MACsec implementation register](../implementation/macsec.md) and [acceptance register](../acceptance/macsec.md) contain the source records once work occurs. Their fenced templates are examples of column structure, not declarations. The [use case](../zta-macsec-use-case.md#implementation-and-customer-disposition-example) and [ZTA decomposition tree](../zta-decomposition-tree.md#implementation-and-customer-disposition-view) show fictional outcomes separately. No fabricated implementation, evidence or acceptance rows are populated in the source registers.

## Audit limits

The auditor checks field presence, allowed states, control-scoped references, configuration/decision file existence, execution-evidence linkage and baseline consistency, and evidence/decision requirements for positive claims. It does not determine whether the selected scope is complete, the tests are sufficient, the artifacts are authentic, operational impact is tolerable or the signer has contractual authority. It does not calculate percentages, grant acceptance or reject a record merely because a limitation exists.
