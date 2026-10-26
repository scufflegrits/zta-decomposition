---
schema_version: 1
id: DOC-STD-RENDERS
title: Diagram verification record
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

# Diagram verification record

## Review scope

Four new or maintained Mermaid blocks were source-reviewed on October 24, 2026: the [physical topology](../architecture/physical-topology.md), the [site-local logical topology](../architecture/logical-topology.md), and the two blocks in the standalone [ZTA Project Guide](../zta-project-guide.md). Imported handoff and guide examples remain untouched.

Source checks covered front matter position, explicit base theme/ELK layout, top-down direction, matching subgraph/end counts, unique node/edge IDs, defined class assignments, absence of inline class syntax and bare Mermaid comments, and the required network order. Legends and mechanism-status explanations appear below each block. These checks are not a Mermaid parse or render.

All four maintained blocks now use CSS named colors in their theme and class styles, following the [ZTA project Mermaid standard](mermaid-best-practices-zta.md). Source checks found no remaining hexadecimal colors in these blocks. The palette retains blue endpoints, green network infrastructure, teal server resources, purple firewalls, amber-toned management resources and gray external networks. Line widths, dash patterns, labels and topology were preserved. The revised colors were subsequently inspected in the successful October 25 render review below.

## Initial renderer attempt

The available `/home/sysadmin/.venv/bin/mmdc` reports version 0.1.3 and is a Python `mermaid_cli`/Playwright wrapper, not the npm Mermaid CLI. Its template loads Mermaid from a CDN, so its Mermaid engine version was not established.

An SVG render was attempted for the physical topology with system Chromium and a Playwright executable-path configuration. Chromium exited during launch with `setsockopt: Operation not permitted` in crashpad. No SVG or PNG was produced. The remaining three blocks were not submitted to the same failing renderer. At that time, no JavaScript runtime was available for a browser-free parse check.

## October 25, 2026 — official CLI retry

After loading the user's shell setup and nvm, Node.js 24.22.1, npm 12.2.1 and the project-local official Mermaid CLI 12.0.0 were available. The npm CLI was invoked explicitly through `./node_modules/.bin/mmdc` to avoid the Python wrapper. A temporary Puppeteer configuration selected `/usr/bin/chromium` with browser sandboxing enabled.

Rendering the current physical topology to SVG again failed during Chromium startup with `setsockopt: Operation not permitted` in crashpad. This failure occurred before diagram rendering and produced no SVG or PNG. The other three blocks were not submitted to the same failing browser launcher. Installing and detecting the CLI has not removed the surrounding execution restriction.

A browser-free `mermaid.parse` attempt was made for all four current blocks using the installed Mermaid package. Each stopped with `DOMPurify.addHook is not a function` because no DOM implementation was available to the parser in Node.js. Installing `jsdom` into a temporary directory was attempted without changing project dependencies; it failed with `EAI_AGAIN` when resolving `registry.npmjs.org`. These are environment failures, not reported Mermaid syntax errors, and no successful parse is claimed.

At the end of this agent-side retry, SVG/PNG rendering and visual inspection were still pending. Source checks and the documentation auditor remain separate from parser and browser verification.

## October 25, 2026 — successful terminal render and artifact review

The user ran the prepared render script from a normal terminal. The console reported successful SVG and PNG output for all four current blocks. Eight nonempty image files were inspected under `/tmp/zta-render.uEYvwU`, using the project-local official Mermaid CLI 12.0.0, installed Mermaid 12.2.0, Puppeteer 25.16.0 and system Chromium selected by `executablePath`. PNG output was requested at scale 2 on a white canvas. Artifacts are temporary review files, not committed project deliverables.

| Source | Reviewed SVG and PNG basename | Visual findings |
|---|---|---|
| Physical topology | `physical-topology-1` | Site A is above Site B; device order, node containment, role colors and management dashes are visible. The WAN edge crosses the Site B title. |
| Site-local logical topology | `logical-topology-1` | VM production and management attachments are distinct, selected inter-VLAN traffic passes through the ISR, and management has no drawn route to production/WAN. Several attachment lines cross the Catalyst title area. |
| Project guide, block 1 | `zta-project-guide-1` | Two-site overview and management associations are readable. The WAN edge crosses the Site B title. |
| Project guide, block 2 | `zta-project-guide-2` | Objective-to-test progression, supporting inputs, auditor and future-evidence status are visible and readable. No obvious label clipping was observed. |

All four PNGs were visually inspected. Labels, arrows, node colors and group containment were reviewed. Named edge styles were also inspected in the SVG: connectivity uses `slategray`, north-south uses `dodgerblue`, management uses `darkgoldenrod` with `6 4` dashes, and logical-topology east-west edges use `darkorchid` with the session edge dashed. The workflow diagram uses default edge styling and its intended node classes.

**Network and project-guide verification status:** These four blocks rendered successfully to SVG and PNG and were visually reviewed. Title/edge crossings noted above remain layout refinement items before publication. No diagram source was changed after this artifact review, so the findings apply to the rendered source. No hosted Markdown viewer has been tested; its renderer may lay out the diagrams differently. The full seven-pillar control overlay remains a textual scaffold pending later diagram work.

## October 25, 2026 — documentation taxonomy

The new [taxonomy](../taxonomy.md#documentation-map) contains one maintained Mermaid block grouping document purposes. It uses a base theme, ELK layout, top-down direction, stable node IDs and semantic classes with CSS named colors. It is a navigation map, separate from the engineering ancestry chain.

An initial restricted-shell render failed at Chromium startup with `setsockopt: Operation not permitted`. After permission to run Chromium outside that restriction, project-local Mermaid CLI 12.0.0 rendered the block successfully to SVG and PNG using system Chromium with browser sandboxing enabled. Temporary artifacts are `/tmp/zta-taxonomy-review/taxonomy-1.svg` and `/tmp/zta-taxonomy-review/taxonomy-1.png`; they are review outputs, not committed deliverables.

The SVG was parsed as XML and the PNG was visually inspected. All five category boxes, labels, arrows and role colors are visible, with no obvious clipping or edge crossings. The intended hosted Markdown viewer remains untested. The four existing network/project-guide blocks were checked to be unchanged during the frontmatter migration; their earlier findings still apply. Imported guide examples were not edited or rendered in this change.

This verifies diagram syntax acceptance and the inspected render, not equipment compatibility, enforcement behavior or security validation. Architecture controls remain unvalidated.

## October 25, 2026 — ZTA decomposition ER diagram

The [ZTA decomposition ER diagram](../zta-decomposition-erDiagram.md) follows the standard (non-CSS) Mermaid r1.0.7 guide and the local named-color override. Its source uses native ER theme variables and `classDef` entity styling; it does not use embedded custom CSS. The available `/home/sysadmin/.venv/bin/mmdc` wrapper rendered the block to [`images/zta-decomposition-erDiagram.png`](../images/zta-decomposition-erDiagram.png) on a black background. The wrapper reports version 0.1.3 and loads Mermaid from a CDN, so the exact Mermaid engine version is not established. The rendered PNG was visually inspected: all entities and relationship connectors are present and legible, with no obvious overlap. It is embedded inline as a preview because the tall diagram's 1 px connectors became difficult to see when scaled to fit the editor pane; the editable Mermaid source is retained in a collapsed block. The user confirmed the inline preview makes the connectors visible in VS Code; the VS Code version is not recorded.
