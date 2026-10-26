# Documentation and traceability conventions

<!-- zta-doc: id=DOC-STD-DOCS; parent=ROOT; lineage=ROOT -->

**Owner (proposed):** Documentation Engineering  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

## Authority and scope

The [README](../README.md) defines pillar entities; each pillar links to authoritative controls. Control requirements, tests and evidence have a single definition. Repeated mentions and cross-pillar links are references. Preserve stable IDs when moving documents. The original handoff and Mermaid guide are immutable provenance, excluded explicitly in `audit-config.json`; their examples are not new entity declarations.

Every managed Markdown document begins with one `zta-doc` comment containing globally unique `id`, immediate `parent`, and full `lineage` from ROOT through that parent. Document ownership is proposed until accepted. Document design status is distinct from technical validation.

## Traceable tables

Put one `zta-table` comment immediately before a detailed traceable table. Its `id` is globally unique. `parent` is a defined entity or ROOT, and `lineage` contains ROOT through that parent, with no omitted ancestors. Each row's Parent ID equals the table parent. Each row has exactly one identity column: `Pillar ID`, `Control ID`, `Requirement ID`, `Test ID`, `Evidence ID` or `Row ID`. Definitions use globally unique IDs across documents, tables and rows. A table under a requirement defines its tests; a table under a test defines its evidence. Tables listing controls from several parents must be split.

Descriptive matrices, inventories of unresolved questions and cross-reference indexes need no trace metadata because they do not define hierarchy entities. Do not use row positions as stable IDs. Use relative Markdown links to the authoritative parent document and readable ancestry breadcrumbs.

The HTML syntax is illustrated as inline code: `<!-- zta-table: id=TBL-EXAMPLE; parent=NET-04; lineage=ROOT>ZT-05>NET-04 -->`. Examples inside code fences or inline code are ignored by the auditor.

## Status and evidence

Use Required, Proposed, Verify or Validated. A required objective may separately need verification; write `Required objective / Verify`. For audited entity rows use one exact status or that combined objective status. Mark Validated only with reviewed evidence. A Validated row must have an `Evidence IDs` column naming defined Evidence IDs that descend from that row (or the evidence row itself), and local evidence artifacts must be linked using Markdown in an `Artifact` column. Evidence rows require a `Result` and `Reviewer`. Passed documentation integrity checks never validate hardware or configuration.

## Architecture references and promised decomposition

Use a `References` column with comma-separated entity IDs for machine-checked relationships; prose links support navigation. Use a `Decomposition` column with a relative Markdown file link when a row promises further decomposition. The auditor requires that target document to exist and declare the row ID as its parent. External links and prose mentions do not create hierarchy edges.

## Repository maintenance

Use UTF-8 Markdown, relative links, stable heading anchors and explicit source/review dates. Record vendor findings in the [research register](../references/vendor-research.md) with version and applicability details. Never infer capability from equipment class alone. Maintain ADRs for material decisions. Follow the [Mermaid standard r1.0.6](mermaid-best-practices-r1.0.6.md) for diagrams.

## Mermaid colors

All maintained project Mermaid diagrams must use built-in CSS named colors, such as `white`, `steelblue`, and `darkslategray`, instead of hexadecimal color values. This applies to theme configuration and every explicit node, edge, subgraph and CSS style declaration. Preserve semantic color roles and readable contrast when choosing named colors.

This project rule supersedes the hexadecimal-color guidance and examples in the imported Mermaid Best Practices Guide r1.0.5. The original root-level guide and handoff remain unchanged as provenance. The override is also recorded in the [project Mermaid standard r1.0.6](mermaid-best-practices-r1.0.6.md).

Run the [auditor](../tools/README.md) before review. The auditor supports a documented Markdown subset and declared relationships; it cannot infer a missing architecture concept from arbitrary prose. Record unknown engineering inputs in [open questions](../architecture/open-questions.md).
