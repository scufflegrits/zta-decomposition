---
schema_version: 1
id: DOC-ADR-INDEX
title: Architecture decision index
document_type: navigation
parent: ROOT
lineage:
- ROOT
owner: Architecture
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-24'
---

# Architecture decision index

ADR-001 through ADR-013 preserve the identifiers and statuses in the handoff. Required means an established architecture constraint; it does not mean the implementation was tested. ADR-009 remains Proposed.

- [ADR-001 — Physical-site-only user authentication](ADR-001.md): Required.
- [ADR-002 — No WAN remote-user authentication](ADR-002.md): Required.
- [ADR-003 — Preserve the Cisco/Palo Alto topology](ADR-003.md): Required.
- [ADR-004 — Selective inter-VLAN routing](ADR-004.md): Required.
- [ADR-005 — Local isolated management VLANs](ADR-005.md): Required.
- [ADR-006 — Approved management attachments](ADR-006.md): Required.
- [ADR-007 — Vendor-neutral virtualization](ADR-007.md): Required.
- [ADR-008 — MACsec coverage objective](ADR-008.md): Required objective / Verify.
- [ADR-009 — Public WAN transport protection](ADR-009.md): Proposed.
- [ADR-010 — Top-down architecture diagrams](ADR-010.md): Required.
- [ADR-011 — External diagram legends](ADR-011.md): Required.
- [ADR-012 — Hierarchical traceability](ADR-012.md): Required.
- [ADR-013 — Modular documentation](ADR-013.md): Required.

New material decisions receive the next unused stable ID and include decision, rationale, status, consequences, alternatives, owner and source. Record any explicit user change to the baseline rather than silently overwriting its meaning.
