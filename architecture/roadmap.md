# Implementation roadmap

<!-- zta-doc: id=DOC-ARCH-ROADMAP; parent=ROOT; lineage=ROOT -->

**Owner (proposed):** Architecture  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

1. Establish modular documentation, ownership proposals and an ADR baseline. This scaffold supplies the initial documents; owner acceptance and Git workflow setup remain pending.
2. Extend the initial controls and traceability, using Network & Environment and MACsec as the model. Populate detailed requirements for the other pillars with engineering owners.
3. Finalize the physical, site-local and seven-pillar diagrams. The physical and site-local views contain embedded diagrams; the full seven-pillar overlay currently contains a relationship inventory. The four maintained blocks have rendered successfully and were visually reviewed; recorded title/edge crossings still need layout refinement before publication.
4. Use and extend the [repository auditor](../tools/README.md). It checks declared documentation structure, not equipment behavior or unstated requirements.
5. Resolve [engineering questions](open-questions.md): exact bill of materials, VLAN policy, identity flows, firewall design, endpoint compatibility and virtualization isolation.
6. Execute acceptance tests, record configurations and actual results, review exceptions and attach evidence. Mark Validated only after suitable evidence review.

The [MACsec verification plan](../controls/macsec/verification.md) contains unexecuted tests. Procurement approval, control deployment and security certification are not outcomes of scaffolding or a passing documentation audit.
