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

This project profile applies alongside the supplied [Mermaid CSS r1.0.7 guide](../references/guides/mermaid-best-practices-CSS-r1.0.7.md), stored as imported source material. Its filename/version identifies the local named-color profile; the supplied guide has its own edition number. The superseded r1.0.6 import and previous root-level r1.0.5 guide were intentionally removed. For project diagrams, this profile and the [documentation conventions](documentation-conventions.md#mermaid-colors) take precedence over conflicting color examples in source material.

## Project color override

All maintained project Mermaid diagrams must use built-in CSS named colors instead of hexadecimal values. Use names such as `white`, `steelblue`, and `darkslategray` in `themeVariables`, `classDef`, `style`, `linkStyle`, and `themeCSS` wherever colors are explicitly specified. Preserve semantic color roles and readable contrast. Quoted named colors are permitted in YAML, for example `background: "white"`.

## Other authoring conventions

New diagrams follow the supplied CSS edition: place custom appearance rules in embedded `config.themeCSS`, with Mermaid `class` statements attaching semantic classes. Do not introduce `classDef`, inline `style` or numeric `linkStyle` in new diagrams. Use CSS named colors in the embedded CSS and theme variables.

For flowcharts use YAML configuration first, `theme: base`, `look: classic`, `layout: elk`, top-down architecture, stable uppercase node IDs, `SG_` subgraphs and semantic node/edge classes. Use the guide's diagram-specific guidance for ER or sequence diagrams rather than copying flowchart selectors. Use Markdown legends below diagrams. Render every edited block to SVG and PNG and inspect containment, labels, arrowheads, styling and contrast.

Existing project diagrams use the earlier class-based style and retain their recorded verification status. This source-guide replacement does not change their Mermaid blocks or assert a CSS migration or new render review. Apply the current guide when creating diagrams; preserve existing source unless an edit or migration is part of the requested work.

The supplied guide contains examples and may reference supplemental material outside this project. Its internal links and example identifiers are outside the auditor's managed-document scope. Check the intended Markdown viewer separately, including its layout-engine behavior.

## Revision history

**r1.0.6:** Record the project-wide CSS named-color requirement, supersede imported hexadecimal-color guidance, and originally retain the r1.0.5 guide as provenance. That source was later intentionally removed. The document ID remains `DOC-STD-MERMAID` across the filename change.

**Source update — October 25, 2026:** Replace the supplied r1.0.6 import with the embedded CSS r1.0.7 edition under `references/guides/`. Adopt its authoring rules for new diagrams while retaining the local named-color profile and existing diagram verification history.
