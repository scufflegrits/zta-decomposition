---
schema_version: 1
id: DOC-ZT-05
title: ZT-05 — Network & Environment
document_type: pillar
parent: ZT-05
lineage:
- ROOT
- ZT-05
owner: Network Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# ZT-05 — Network & Environment

**Ancestry:** `ROOT > ZT-05`. [Parent architecture](../README.md#seven-pillars).

Separate segmentation, admission, transport encryption and resource authorization. Exact SKUs, port capabilities, VLANs and permitted flows remain unresolved.

**Technologies:** Catalyst, ISR, Palo Alto, MACsec, proposed IPsec. Listing a technology does not establish deployment or validation.

## Control index

The rows below are references; definitions and parent declarations live in the linked control documents.

- [NET-01: Catalyst / ISE](../030_controls/040_network-segmentation/overview.md#net-01) — Network admission and VLAN policies.
- [NET-02: ISR 4000](../030_controls/040_network-segmentation/overview.md#net-02) — Selective inter-VLAN routing.
- [NET-03: Palo Alto](../030_controls/040_network-segmentation/overview.md#net-03) — Inter-site security enforcement.
- [NET-04: MACsec](../030_controls/020_macsec/overview.md) — Ethernet link protection.
- [NET-05: IPsec](../030_controls/040_network-segmentation/overview.md#net-05) — Proposed WAN transport protection.
- [NET-06: Management VLAN](../030_controls/030_management-isolation/overview.md) — Local-only management isolation.

[Physical topology](../020_architecture/physical-topology.md) and [equipment assessment](../070_procurement/macsec-equipment-assessment.md) provide context.
