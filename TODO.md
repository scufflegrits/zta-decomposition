---
schema_version: 1
id: DOC-ZTA-TODO
title: Documentation TODO
document_type: backlog
parent: ROOT
lineage:
- ROOT
owner: Documentation Engineering
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-25'
---

# Documentation TODO

This backlog tracks document maintenance. Engineering design inputs remain in [open questions](architecture/open-questions.md) and implementation sequencing remains in the [roadmap](architecture/roadmap.md).

- [ ] Model the tables and their relationships in an embedded Mermaid `erDiagram` and save it to `zta-decomposition-erDiagram.md`. Follow the project diagram standard and render and visually review the diagram.
- [ ] Review and record program adoption decisions in the single [adoption checklist](HOW-TO-USE.md#program-adoption-checklist). Maintain outcomes and approval references there.
- [ ] Coordinate any future Jira synchronization with the software factory. Manual linking is available now; live issue checks and updates are not implemented.

- [x] Replace the supplied r1.0.6 guide with [Mermaid CSS r1.0.7](references/guides/mermaid-best-practices-CSS-r1.0.7.md). Removed the superseded import, reconciled the [project Mermaid standard](standards/mermaid-best-practices-r1.0.6.md) and documentation conventions, updated REF-011 and source links, regenerated the index and checked documentation integrity.
- [ ] Refine the known title/edge crossings in network diagrams and rerender every edited block; see the [diagram verification record](standards/diagram-verification.md).
- [ ] Verify maintained diagrams in the intended presentation viewer and record the viewer and findings.

- [ ] Populate actual implementation and customer disposition records as work occurs, following the [record standard](standards/implementation-acceptance.md). The registers currently contain no deployment or acceptance claims.
