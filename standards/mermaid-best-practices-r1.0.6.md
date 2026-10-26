---
schema_version: 1
id: DOC-STD-MERMAID
title: Mermaid Best Practices — Project Standard r1.0.6
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

# Mermaid Best Practices — Project Standard r1.0.6

**Version:** r1.0.6

This project standard applies alongside the supplied [Mermaid code conventions](../references/guides/mermaid-best-practices-r1.0.6.md), stored as imported source material. The previous root-level r1.0.5 guide was intentionally removed. For project diagrams, this standard and the [documentation conventions](documentation-conventions.md#mermaid-colors) take precedence over any conflicting color examples in the supplied guide. An updated guide is planned; see [TODO](../TODO.md).

## Project color override

All maintained project Mermaid diagrams must use built-in CSS named colors instead of hexadecimal values. Use names such as `white`, `steelblue`, and `darkslategray` in `themeVariables`, `classDef`, `style`, `linkStyle`, and `themeCSS` wherever colors are explicitly specified. Preserve semantic color roles and readable contrast. Quoted named colors are permitted in YAML, for example `background: "white"`.

## Other authoring conventions

New diagrams use YAML configuration first, `theme: base`, `layout: elk`, top-down architecture, stable uppercase node IDs, `SG_` subgraphs, semantic role classes and separately assigned named-edge styles. Use Markdown legends below diagrams. Render every edited block to SVG and PNG and inspect containment, labels, arrowheads, styling and contrast.

The supplied guide contains examples and may reference supplemental material outside this project. Its internal links and example identifiers are outside the auditor's managed-document scope. Check the intended Markdown viewer separately, including its layout-engine behavior.

## Revision history

**r1.0.6:** Record the project-wide CSS named-color requirement, supersede imported hexadecimal-color guidance, and originally retain the r1.0.5 guide as provenance. That source was later intentionally removed; the supplied r1.0.6 reference now resides in `references/guides/`. The document ID remains `DOC-STD-MERMAID` across the filename change.
