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

These requirement identifiers are preserved from the handoff. Acceptance details below are proposed elaborations for engineering review. Requirements remain Required objectives; compatibility and implementation require verification.

<!-- zta-table: id=TBL-MAC-REQUIREMENTS; parent=NET-04; lineage=ROOT>ZT-05>NET-04 -->

| Parent ID | Requirement ID | Requirement | Acceptance evidence | Status |
|---|---|---|---|---|
| NET-04 | MAC-001 | Identify MACsec-capable ports | Exact SKU/module/port, release, license, media, link speed and peer inventory; vendor source and review. | Required |
| NET-04 | MAC-002 | Verify supported cipher suites | Approved common cipher profile, XPN/replay/confidentiality settings and matching peer configuration. | Required |
| NET-04 | MAC-003 | Validate MKA interoperability | Exact peer session establishment, certificate/key lifecycle, VLAN trunk and aggregation behavior where applicable. | Required |
| NET-04 | MAC-004 | Reject unintended plaintext fallback | Mandatory protection fails closed during negotiation failure, invalid keys, reboot and link recovery. | Required |
| NET-04 | MAC-005 | Meet required link throughput | Approved numeric throughput/latency targets and MTU workload pass; targets must be agreed before execution. | Required |
| NET-04 | MAC-006 | Provide useful operational telemetry | Correlated counters, session state and failure/rekey events distinguish protected, failed and plaintext conditions. | Required |

Each requirement is covered by the [verification plan](verification.md). Vendor documentation supports compatibility findings; it does not prove installation behavior. Requirements may be marked Validated only after actual tests, evidence references and review.

MAC-004 must identify any discovery/authentication or other protocol traffic permitted outside protected payload traffic under the approved policy. Do not claim all Ethernet frames are encrypted without documenting protocol behavior and an agreed measurement method.
