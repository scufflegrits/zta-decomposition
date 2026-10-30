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

This backlog tracks document maintenance. Engineering design inputs remain in [open questions](../020_architecture/open-questions.md) and implementation sequencing remains in the [roadmap](../020_architecture/roadmap.md). Remove items when they are completed; Git history keeps the record.

## Governance

- [ ] Review and record program adoption decisions in the single [adoption checklist](../HOW-TO-USE.md#program-adoption-checklist). Maintain outcomes and approval references there.
- [ ] Coordinate any future Jira synchronization with the software factory. Manual linking is available now; live issue checks and updates are not implemented.

## Tooling

- [ ] Evaluate a reversible MkDocs site proof of concept using isolated Python dependencies. Test curated navigation over the existing Markdown, Mermaid rendering and preview readability, and theme/hosting options before adopting it.

## Diagrams

- [ ] Refine the known title/edge crossings in network diagrams and rerender every edited block; see the [diagram verification record](../090_standards/diagram-verification.md).
- [ ] Verify maintained diagrams in the intended presentation viewer and record the viewer and findings.

## Records

- [ ] Populate actual implementation and customer disposition records as work occurs, following the [record standard](../090_standards/implementation-acceptance.md). The registers currently contain no deployment or acceptance claims.
