---
schema_version: 1
id: DOC-STD-DOCS
title: Documentation and traceability conventions
document_type: standard
parent: ROOT
lineage:
- ROOT
owner: Documentation Engineering
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-24'
---

# Documentation and traceability conventions

## Authority and scope

The [README](../README.md) defines pillar entities; each pillar links to authoritative controls. Control requirements, tests and evidence have a single definition. Repeated mentions and cross-pillar links are references. Preserve stable IDs when moving documents. The original handoff and supplied guides under `references/guides/` are source imports, excluded explicitly in `audit-config.json`; their examples are not new entity declarations. Imports retain their original content and do not require project frontmatter. Generated audit reports are also excluded.

Every managed Markdown document begins on its first line with YAML frontmatter, bounded by `---`. This replaces the legacy `zta-doc` comment and visible owner, document-status and baseline headers. Keep table metadata and entity statuses in the body. One authoritative metadata block prevents duplicate fields from drifting.

## Document frontmatter

```yaml
---
schema_version: 1
id: DOC-EXAMPLE
title: Example architecture document
document_type: architecture
parent: ROOT
lineage: [ROOT]
owner: Architecture
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: "2026-10-24"
---
```

All fields are required; unknown fields and duplicate YAML keys are rejected. Use single-line strings, integer `schema_version: 1`, and a list of identifier strings for `lineage`. Dates must be quoted ISO dates. Preserve existing IDs, ancestry and baseline dates during metadata-only changes; use the date of the actual baseline for a new document. A file move does not create a new identity.

| Field | Meaning and allowed values |
|---|---|
| `id` | Globally unique document ID across documents, tables and entity rows |
| `title` | Human-readable document title, normally matching its first heading |
| `document_type` | `navigation`, `guide`, `architecture`, `decision`, `pillar`, `control`, `requirements`, `verification`, `procurement`, `reference`, `standard`, `tooling`, `backlog` |
| `parent` | Immediate authoritative entity parent, or `ROOT` |
| `lineage` | Full ordered ancestry from `ROOT` through the immediate parent |
| `owner` | Responsible team; use the existing proposed assignment until accepted |
| `owner_status` | `proposed`, `accepted` |
| `document_status` | `draft`, `in-review`, `approved`, `superseded` |
| `implementation_status` | `unvalidated` for architecture/technical claims; `not-applicable` for navigation, standards and tooling documents without deployment claims |
| `baseline_date` | Date of the document baseline; not an automatic last-modified timestamp |

Document approval and owner acceptance are explicit review outcomes. Migration does not grant either. Implementation validation remains attached to individual controls and reviewed evidence; schema version 1 deliberately provides no document-wide `validated` value. ADR decision statuses, research findings and table-row statuses remain separate body fields.

## Catalog and taxonomy

The [document index](../index.md) is generated from frontmatter and auditor discovery. It lists maintained documents by type, source imports separately, and the local generated report. Regenerate it with `python3 tools/generate_index.py --root .`; check freshness with `python3 tools/generate_index.py --root . --check`. Commit index changes alongside source changes.

The [taxonomy](../taxonomy.md) is a curated explanation of document categories and engineering relationships. `document_type` classifies a file's purpose; it does not change entity ancestry. The category table and diagram are navigation aids, while declared parent/lineage fields and entity tables establish traceability. Update the taxonomy when the categories or engineering workflow change.

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

This project rule supersedes conflicting hexadecimal-color guidance in source examples. The supplied guide is stored in `references/guides/`; the previous root-level guide was intentionally removed. The original handoff remains unchanged as provenance. The override is also recorded in the [project Mermaid standard r1.0.6](mermaid-best-practices-r1.0.6.md).

Run the [auditor](../tools/README.md) before review. The auditor supports a documented Markdown subset and declared relationships; it cannot infer a missing architecture concept from arbitrary prose. Record unknown engineering inputs in [open questions](../architecture/open-questions.md).
