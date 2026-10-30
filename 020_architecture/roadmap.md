---
schema_version: 1
id: DOC-ARCH-ROADMAP
title: Implementation roadmap
document_type: architecture
parent: ROOT
lineage:
- ROOT
owner: Architecture
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# Implementation roadmap

1. Establish modular documentation, ownership proposals and an ADR baseline. The initial documents and Git repository are established, and changes have been committed and pushed. Owner acceptance and a documented review workflow remain pending.
2. Extend the initial controls and traceability, using Network & Environment and MACsec as the model. Populate detailed requirements for the other pillars with engineering owners.
3. Finalize the physical, site-local and seven-pillar diagrams. The physical and site-local views contain embedded diagrams; the full seven-pillar overlay currently contains a relationship inventory. The four network/project-guide blocks have rendered successfully and were visually reviewed; recorded title/edge crossings still need layout refinement before publication. The separate documentation taxonomy diagram is also rendered and reviewed; see the [verification record](../090_standards/diagram-verification.md).
4. Use and extend the [repository auditor](../110_tools/README.md). It checks declared documentation structure, not equipment behavior or unstated requirements.
5. Resolve [engineering questions](open-questions.md): exact bill of materials, VLAN policy, identity flows, firewall design, endpoint compatibility and virtualization isolation.
6. Execute applicable tests, record actual configurations and results in the [implementation register](../050_implementation/macsec.md), and retain evidence. Record operational limitations, residual risk and customer disposition in the [acceptance register](../010_acceptance/macsec.md), following [ADR-014](010_decisions/ADR-014.md). Mark technical claims Validated only after suitable evidence review; customer acceptance with documented limitations remains a separate decision without coverage percentages.

The [MACsec verification plan](../030_controls/020_macsec/verification.md) contains unexecuted tests. Procurement approval, control deployment and security certification are not outcomes of scaffolding or a passing documentation audit.
