---
schema_version: 1
id: DOC-MAC-REQ
title: MACsec requirements
document_type: requirements
parent: NET-04
lineage:
- ROOT
- ZT-05
- NET-04
owner: Network Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# MACsec requirements

**Ancestry:** `ROOT > ZT-05 > NET-04`. [Parent control](overview.md).

These requirement identifiers are preserved from the handoff. Acceptance details below are proposed elaborations for engineering review. Requirements remain Required objectives for their agreed application; compatibility and claimed implementation require verification. Under [ADR-014](../../architecture/decisions/ADR-014.md), record applicability and operational limitations per implementation and request customer disposition. Acceptance with limitations does not change the technical requirement or its test result to satisfied/passed.

<!-- zta-table: id=TBL-MAC-REQUIREMENTS; parent=NET-04; lineage=ROOT>ZT-05>NET-04 -->

| Parent ID | Requirement ID | Requirement | Acceptance evidence | Status | Jira stories |
|---|---|---|---|---|---|
| NET-04 | MAC-001 | Identify MACsec-capable ports | Exact SKU/module/port, release, license, media, link speed and peer inventory; vendor source and review. | Required |  |
| NET-04 | MAC-002 | Verify supported cipher suites | Approved common cipher profile, XPN/replay/confidentiality settings and matching peer configuration. | Required |  |
| NET-04 | MAC-003 | Validate MKA interoperability | Exact peer session establishment, certificate/key lifecycle, VLAN trunk and aggregation behavior where applicable. | Required |  |
| NET-04 | MAC-004 | Reject unintended plaintext fallback | Mandatory protection fails closed during negotiation failure, invalid keys, reboot and link recovery. | Required |  |
| NET-04 | MAC-005 | Meet required link throughput | Approved numeric throughput/latency targets and MTU workload pass; targets must be agreed before execution. | Required |  |
| NET-04 | MAC-006 | Provide useful operational telemetry | Correlated counters, session state and failure/rekey events distinguish protected, failed and plaintext conditions. | Required |  |

Each requirement is covered by the [verification plan](verification.md). Vendor documentation supports compatibility findings; it does not prove installation behavior. Requirements may be marked Validated only after actual tests, evidence references and review.

Use `Jira stories` for actual research, design or implementation work directly associated with a requirement. Leave it blank until links are available; maintain story status in Jira. See the [manual Jira standard](../../standards/manual-jira-traceability.md).

MAC-004 must identify any discovery/authentication or other protocol traffic permitted outside protected payload traffic under the approved policy. Do not claim all Ethernet frames are encrypted without documenting protocol behavior and an agreed measurement method.

Record deployed scope and verification separately in the [implementation register](../../implementation/macsec.md), with customer disposition in the [acceptance register](../../acceptance/macsec.md). Keep Required as the obligation status unless technical validation is actually supported; do not replace it with a customer-acceptance label. Applicable numeric performance criteria remain test criteria, not a percentage of ZTA completion.
