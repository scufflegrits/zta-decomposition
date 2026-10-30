---
schema_version: 1
id: DOC-ZT-04
title: ZT-04 — Data
document_type: pillar
parent: ZT-04
lineage:
- ROOT
- ZT-04
owner: Data Security
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# ZT-04 — Data

**Ancestry:** `ROOT > ZT-04`. [Parent architecture](../README.md#seven-pillars).

Define data access, classification and confidentiality requirements. Data inventory, classification rules, auditing and approved encryption profiles remain unresolved.

**Technologies:** AD permissions, file/database permissions, encryption. Listing a technology does not establish deployment or validation.

## Initial scope and related controls

[NET-04 MACsec](../030_controls/020_macsec/overview.md) protects compatible links; data authorization and application encryption require separate requirements.

## Next decomposition

The proposed owner must inventory resources, identify authoritative controls, define acceptance criteria and evidence, and record dependencies on other pillars. Detailed controls and test identifiers have not been invented for unspecified designs.
