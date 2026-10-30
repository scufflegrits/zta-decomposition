---
schema_version: 1
id: DOC-ZT-01
title: ZT-01 — User
document_type: pillar
parent: ZT-01
lineage:
- ROOT
- ZT-01
owner: Identity/IAM
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# ZT-01 — User

**Ancestry:** `ROOT > ZT-01`. [Parent architecture](../README.md#seven-pillars).

Keep network admission, user authentication and privileged elevation separate. User presence at Site A or Site B is required; credential workflows and service locations remain unresolved.

**Technologies:** AD, PKI access cards, RSA tokens, PAM. Listing a technology does not establish deployment or validation.

## Initial scope and related controls

[Identity workflows](../030_controls/010_identity-authentication/overview.md) separate network admission, user authentication and PAM. [NET-01](../030_controls/040_network-segmentation/overview.md#net-01) is the authoritative network-admission control under ZT-05; do not duplicate it here.

## Next decomposition

The proposed owner must inventory resources, identify authoritative controls, define acceptance criteria and evidence, and record dependencies on other pillars. Detailed controls and test identifiers have not been invented for unspecified designs.
