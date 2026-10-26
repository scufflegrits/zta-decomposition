---
schema_version: 1
id: DOC-STD-MERMAID
title: ZTA Project Mermaid Standard
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

# ZTA Project Mermaid Standard

**Profile version:** r1.0.6

This ZTA-specific profile adapts both supplied Mermaid r1.0.7 guides: the [standard edition](../references/guides/mermaid-best-practices-r1.0.7.md) and the [embedded CSS edition](../references/guides/mermaid-best-practices-CSS-r1.0.7.md). The standard edition is the default authoring basis; the CSS edition provides supplemental techniques when native styling is insufficient and the target renderer has been checked. This profile adds ZTA project rules, including named colors and preview-scale legibility. Its version is independent of the supplied guides. The superseded r1.0.6 import and previous root-level r1.0.5 guide were intentionally removed. For project diagrams, this profile and the [documentation conventions](documentation-conventions.md#mermaid-colors) take precedence over conflicting source examples.

## Project color override

All maintained project Mermaid diagrams must use built-in CSS named colors instead of hexadecimal values. Use names such as `white`, `steelblue`, and `darkslategray` in `themeVariables`, `classDef`, `style`, `linkStyle`, and `themeCSS` wherever colors are explicitly specified. Preserve semantic color roles and readable contrast. Quoted named colors are permitted in YAML, for example `background: "white"`.

## Other authoring conventions

New diagrams follow the supplied standard edition. Prefer Mermaid-native `themeVariables`, `classDef`, and `class` statements for appearance; avoid custom CSS unless the diagram type or a verified renderer limitation requires it. Do not add CSS only to force preview styling when a native Mermaid setting or class can express the same role. Keep the project named-color override below, and render in the intended viewer before relying on renderer-specific behavior.

For flowcharts use YAML configuration first, `theme: base`, `look: classic`, `layout: elk`, top-down architecture, stable uppercase node IDs, `SG_` subgraphs and semantic node/edge classes. Use the guide's diagram-specific guidance for ER or sequence diagrams rather than copying flowchart selectors. Use Markdown legends below diagrams. Render every edited block to SVG and PNG and inspect containment, labels, arrowheads, styling and contrast.

## Intended-preview legibility

Review each diagram in the intended preview at the size readers will see it. Check that relationship lines, cardinality markers, labels and boundaries remain distinguishable after the preview scales the diagram to fit. If they do not, simplify the layout or revise supported native styling first. If the intended preview still makes the diagram hard to read, include an inline rendered image and preserve the editable Mermaid source in a clearly identified source section. Keep the image synchronized with the source. Record the preview application and version when known, the renderer/engine and version when known, the rendered artifact path, and the visual findings in the [diagram verification record](diagram-verification.md). State explicitly when a target preview was not inspected.

Existing project diagrams use the earlier class-based style and retain their recorded verification status. This source-guide replacement does not change their Mermaid blocks or assert a CSS migration or new render review. Apply the current guide when creating diagrams; preserve existing source unless an edit or migration is part of the requested work.

The supplied guide contains examples and may reference supplemental material outside this project. Its internal links and example identifiers are outside the auditor's managed-document scope. Check the intended Markdown viewer separately, including its layout-engine behavior.

## Revision history

**r1.0.6:** Record the project-wide CSS named-color requirement, supersede imported hexadecimal-color guidance, and originally retain the r1.0.5 guide as provenance. That source was later intentionally removed. The document ID remains `DOC-STD-MERMAID` across the filename change.

**Source update — October 25, 2026:** Adapt both supplied Mermaid r1.0.7 guides into this local profile. Default to the standard edition's native authoring conventions; retain the CSS edition as supplemental guidance. Keep project-specific color and preview requirements and preserve existing diagram verification history.

**Project update — October 25, 2026:** Require visual review at intended-preview scale; add an inline rendered-image fallback with retained editable source when preview scaling obscures diagram details, and record the viewer and artifact in the verification record.
