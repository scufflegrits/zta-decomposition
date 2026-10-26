# Mermaid Best Practices — Project Standard r1.0.6

<!-- zta-doc: id=DOC-STD-MERMAID; parent=ROOT; lineage=ROOT -->

**Owner (proposed):** Documentation Engineering  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

**Version:** r1.0.6

This project standard applies the [imported Mermaid Best Practices Guide r1.0.5](../mermaid-best-practices-r1.0.5.md) with the color override below. The original guide is preserved unchanged at the repository root as provenance. For project diagrams, this override and the [documentation conventions](documentation-conventions.md#mermaid-colors) take precedence over the imported guide's hexadecimal-color guidance and examples.

## Project color override

All maintained project Mermaid diagrams must use built-in CSS named colors instead of hexadecimal values. Use names such as `white`, `steelblue`, and `darkslategray` in `themeVariables`, `classDef`, `style`, `linkStyle`, and `themeCSS` wherever colors are explicitly specified. Preserve semantic color roles and readable contrast. Quoted named colors are permitted in YAML, for example `background: "white"`.

## Other authoring conventions

New diagrams use YAML configuration first, `theme: base`, `layout: elk`, top-down architecture, stable uppercase node IDs, `SG_` subgraphs, semantic role classes and separately assigned named-edge styles. Use Markdown legends below diagrams. Render every edited block to SVG and PNG and inspect containment, labels, arrowheads, styling and contrast.

The imported guide links to supplemental examples not supplied with this project. These provenance links are outside the auditor's managed-document scope; they are not promised repository deliverables. Check the intended Markdown viewer separately, including its layout-engine behavior.

## Revision history

**r1.0.6:** Record the project-wide CSS named-color requirement, supersede imported hexadecimal-color guidance, and retain the original r1.0.5 guide as provenance. The document ID remains `DOC-STD-MERMAID` across the filename change.
