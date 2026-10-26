---
schema_version: 1
id: DOC-ZT-03
title: ZT-03 — Application & Workload
document_type: pillar
parent: ZT-03
lineage:
- ROOT
- ZT-03
owner: Systems/Virtualization
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# ZT-03 — Application & Workload

**Ancestry:** `ROOT > ZT-03`. [Parent architecture](../README.md#seven-pillars).

Define resource permissions and workload authorization. Hypervisor selection, application inventory, service identities and workload policy remain unresolved.

**Technologies:** Windows, RHEL, vendor-neutral VMs. Listing a technology does not establish deployment or validation.

## Initial scope and related controls

[NET-06 management isolation](../controls/management-isolation/overview.md) applies to management VMs and host isolation.

## Next decomposition

The proposed owner must inventory resources, identify authoritative controls, define acceptance criteria and evidence, and record dependencies on other pillars. Detailed controls and test identifiers have not been invented for unspecified designs.
