---
schema_version: 1
id: DOC-MAC-OVERVIEW
title: MACsec control overview
document_type: control
parent: NET-04
lineage:
- ROOT
- ZT-05
- NET-04
owner: Network Engineering / Endpoint Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# MACsec control overview

**Ancestry:** `ROOT > ZT-05 > NET-04`. [Parent pillar](../../060_pillars/ZT-05-network-environment.md).

<!-- zta-table: id=TBL-MAC-CONTROL; parent=ZT-05; lineage=ROOT>ZT-05 -->

| Parent ID | Control ID | Control | Status | Jira epic |
|---|---|---|---|---|
| ZT-05 | NET-04 | MACsec Ethernet link protection | Required objective / Verify |  |

Implement MACsec to the practical extent supported by hardware and customer-approved operational constraints, following [ADR-014](../../020_architecture/010_decisions/ADR-014.md). Inventory exact hardware, module, software, license and peer combinations. Document unsupported or operationally deferred protections, functional/workflow impact, residual exposure and available alternatives or compensating controls. Customer disposition may accept documented limitations without requiring a coverage percentage. No ordinary firewall dataplane interface or generic host uplink is assumed capable. The earlier universal-port objective remains in ADR-008 as history.

802.1X admits a device; MACsec protects a compatible Layer 2 link. MACsec does not provide resource authorization, public-WAN protection or application encryption. Evaluate IPsec and TLS separately. Encryption state must not be inferred from successful admission or a connected cable.

Use the [requirements](requirements.md), [verification plan](verification.md), [procurement questionnaire](../../070_procurement/macsec-equipment-assessment.md), and [compatibility findings](../../070_procurement/hardware-compatibility.md). Findings came from the handoff and have not been rechecked against current vendor documents. No proposed installation is validated.

The optional `Jira epic` cell is blank until actual delivery work is created. Follow the [manual Jira standard](../../090_standards/manual-jira-traceability.md); sample issue keys in the use-case guide are illustrative only.

Use the [implementation register](../../050_implementation/macsec.md) to record what was actually deployed and verified, and the [acceptance register](../../010_acceptance/macsec.md) for the customer decision. These source registers currently contain no actual records. An accepted limitation does not mean that an unsupported link encrypts traffic or passes a technical test.
