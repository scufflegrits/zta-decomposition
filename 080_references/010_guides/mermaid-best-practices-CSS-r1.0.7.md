# Mermaid code conventions — embedded CSS edition

Use these conventions for new diagrams in this collection, whether written by hand
or generated with assistance. They are authoring conventions, not additional Mermaid
syntax rules. Existing diagrams and historical lessons may use older names and older
formatting; preserve them unless a rename or reformat is part of the requested change.


This is the **CSS r1.0.7 edition**, derived from
[the standard r1.0.7 guide](mermaid-best-practices-r1.0.7.md). It is a separate
alternative, revised from the CSS r1.0.6 baseline; both r1.0.6 files are unchanged. For new diagrams governed by this
edition, put all custom appearance rules in embedded `config.themeCSS`; do not
write `classDef`, inline `style`, or numeric `linkStyle` statements. Keep Mermaid
`class` statements to attach semantic classes to nodes and subgraphs.

The selector recipes and starter template below target **flowcharts with
`look: classic`**, checked with Mermaid **12.2.0** in Chromium. YAML configuration
requires Mermaid 10.5 or newer, but that minimum does not guarantee these SVG
selectors or named-edge features. The r1.0.7 diagram-type section adds separately tested ER and sequence examples;
other looks and viewer versions still need inspected selectors and render tests. Do not copy flowchart selectors
into a mind map, sequence diagram, or block diagram and assume they match.

## For AI agents: verify before you deliver

This guide is also given to AI agents that create or edit Mermaid diagrams. If you
are one, follow the rest of the guide as written, and add these steps. You may be
running in a chat on a web page, in a desktop app on Windows, macOS, or Linux, or in
a Linux terminal, so first work out what you can actually run.

### 1. Find out what you can run

| Where you are                                         | What you can do                                                                                     |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Chat or web page with no code execution               | Nothing renders. Check the source by hand against [review before sharing](#review-before-sharing), deliver it, and say it is unrendered. |
| Interface that previews Mermaid for you               | The preview is one viewer with its own Mermaid version. Look at it, but report it by name, not as an `mmdc` render. |
| Sandbox that runs code but cannot install or browse   | Use `mmdc` if it is already present; otherwise use the [parse check](#4-if-you-cannot-render-parse-and-say-so). |
| Linux or macOS terminal, container, or desktop shell  | Render with `mmdc`. Install it if missing and permitted.                                             |
| Windows desktop (PowerShell or Command Prompt)        | Render with `mmdc`, which npm installs as `mmdc.cmd`. Use the Python script below rather than Bash. |

Check whether `mmdc` is installed:

```text
Linux, macOS:   command -v mmdc || npx --no-install mmdc --version
PowerShell:     Get-Command mmdc; npx --no-install mmdc --version
Command Prompt: where mmdc
```

A diagram you have not rendered is unverified, however correct the source looks.
See [renderer identity and evidence](#renderer-identity-and-evidence) and the
[reusable audit workflow](#reusable-audit-workflow) for the r1.0.7 verification path.
Record both the renderer and the Mermaid library version. A command named `mmdc`
can be an unrelated Python wrapper: `mmdc --version` alone does not identify the
Mermaid library. The npm Mermaid CLI uses Puppeteer; a Python wrapper may use
Playwright and different configuration keys. Check `--help` before passing browser
configuration. The initial trial used `/home/sysadmin/.venv/bin/mmdc` (wrapper
0.1.3), Playwright, and a CDN-loaded Mermaid library. That wrapper's `-p` file uses
`executable_path`, not Puppeteer's `executablePath`. Other installations may have
an official npm CLI instead. Report the implementation actually invoked.

### 2. Render every block you changed

Save this script with your file-writing tool and run it with `python3` (Linux and
macOS) or `py` (Windows). It extracts each Mermaid block from a Markdown file into
its own `.mmd` file, so every output maps to one block, then renders an SVG for the
checks in [verifying a render](#verify-a-render) and a PNG to look at:

```python
"""Render every mermaid block in a Markdown file with mmdc.

Usage: python render_blocks.py diagram.md [background] [puppeteer-config.json]
Works on Linux, macOS, and Windows. Prints the output folder and one line per block.
"""
import re, shutil, subprocess, sys, tempfile
from pathlib import Path

source = Path(sys.argv[1])
background = sys.argv[2] if len(sys.argv) > 2 else 'white'
puppeteer = sys.argv[3] if len(sys.argv) > 3 else None

mmdc = shutil.which('mmdc')  # finds mmdc.cmd on Windows too
if not mmdc:
    sys.exit('mmdc not found: install @mermaid-js/mermaid-cli or use the parse check')

out = Path(tempfile.mkdtemp(prefix='mermaid-review-'))
version = subprocess.run([mmdc, '--version'], capture_output=True, text=True).stdout.strip()
print(f'mmdc {version}; output in {out}')

text = source.read_text(encoding='utf-8')
blocks = re.findall(r'^```mermaid\n(.*?)^```', text, re.S | re.M)
if not blocks:
    sys.exit('No Mermaid blocks found')
failures = 0
for i, block in enumerate(blocks, 1):
    mmd = out / f'block-{i}.mmd'
    mmd.write_text(block, encoding='utf-8')
    for ext, extra in (('svg', []), ('png', ['-s', '2'])):
        cmd = [mmdc, '-i', str(mmd), '-o', str(mmd.with_suffix('.' + ext)), '-b', background, *extra]
        if puppeteer:
            cmd += ['-p', puppeteer]
        result = subprocess.run(cmd, capture_output=True, text=True)
        status = 'ok' if result.returncode == 0 else 'FAILED: ' + (result.stderr.strip().splitlines() or ['no output'])[0]
        print(f'block {i} {ext}: {status}')
        failures += result.returncode != 0
sys.exit(1 if failures else 0)
```

Pass the diagram's canvas color as the background: `'#0b1120'` for the dark
template, `white` for a light card. If you can view images, open each PNG and
inspect it; reading the SVG text is not a visual check. If you cannot view images,
say that the layout was not inspected.

If a diagram contains emoji, check for an emoji font before rendering
(`fc-list | grep -i emoji` on Linux). Without one, report the emoji as unverified:
the PNG will show fallback symbols or empty boxes that most readers will not see.

**SVG for checks, PNG for looking.** Each format has a job:

| Format | Use it for                                                                                          |
| ------ | --------------------------------------------------------------------------------------------------- |
| SVG    | Text checks: edge styles, `themeCSS` rules, canvas color, measured positions. Also a deliverable for browser-based destinations. |
| PNG    | Looking at the drawing. Most agent image viewers accept PNG, not SVG. Also the deliverable for destinations that are not browsers (Word, slides, some wikis). |

Make both directly with `mmdc`, as the script does. The Markdown block is the
deliverable; rendered files are review artifacts unless the user asked for an image.
When they do, use SVG for web pages and PNG at `-s 2` to `-s 4` for everything else.

**Never convert the SVG to PNG with a non-browser tool.** Mermaid draws labels as
HTML inside `<foreignObject>` elements and lays them out using a browser's font
measurements. Converting the starter template's SVG with `cairosvg` produced every
box and line but none of the 19 labels, and lost the canvas color; ImageMagick 6
refused the file. Turning off `htmlLabels` brought the text back as SVG `<text>`,
but the words overlapped and spilled out of their boxes. Treat `rsvg-convert`,
Inkscape, ImageMagick, and other non-browser converters as unreliable for Mermaid
output, and the same for previewing an SVG in a tool that is not a browser.

**The official npm CLI drives Chromium through Puppeteer.** Independently packaged
commands named `mmdc` may use Playwright instead. Identify the implementation before
choosing browser options. If you are tempted to:

- **Screenshotting the `mmdc` SVG** in a headless browser is an acceptable way to
  view it, because a browser renders `<foreignObject>` correctly. Prefer asking
  `mmdc` for the PNG; it is one step and uses the same engine.
- **Building your own HTML page** that loads Mermaid from a CDN and screenshotting it
  is a different renderer: whatever Mermaid version the page loads, with that
  page's fonts and CSS. Report it as that, with its version, not as an `mmdc` render,
  and use it only when `mmdc` cannot run.

### 3. If `mmdc` is missing or will not start

Install it where you have permission and network access:
`npm install @mermaid-js/mermaid-cli`, then run it with `npx mmdc` or add the
package's `node_modules/.bin` folder to the path for the script. It drives a
headless Chrome, which it may also need to download
(`npx puppeteer browsers install chrome-headless-shell`). Common failures:

- **Chrome refuses to start as root** (Linux containers). Pass a Puppeteer config,
  the script's third argument, containing `{"args": ["--no-sandbox"]}`.
- **The browser download is blocked.** Point the same config at an installed
  Chrome, Chromium, or Edge with `"executablePath"`. If none exists, you cannot
  render.
- **Several `mmdc` versions are present.** A global install and a project install
  can differ by a major version. Record the one you actually ran.

### 4. If you cannot render, parse and say so

Mermaid's own parser runs in Node on any operating system, with no browser. It
catches syntax errors and returns the configuration it read, which exposes a
dropped setting such as an unquoted hex color. After `npm install mermaid jsdom`,
save this as `parse.mjs` and run `node parse.mjs block-1.mmd block-2.mmd`:

```javascript
import { JSDOM } from 'jsdom';
import fs from 'fs';
const dom = new JSDOM('<!doctype html><body></body>');
globalThis.window = dom.window;
globalThis.document = dom.window.document;
const mermaid = (await import('mermaid')).default;
mermaid.initialize({ startOnLoad: false });
let failed = false;
for (const f of process.argv.slice(2)) {
  try {
    const r = await mermaid.parse(fs.readFileSync(f, 'utf8'));
    console.log(f, 'PARSED', JSON.stringify(r?.config ?? {}));
  } catch (e) {
    failed = true;
    console.log(f, 'FAILED', e.message.split('\n').slice(0, 3).join(' | '));
  }
}
process.exitCode = failed ? 1 : 0;
```

A parse proves only that the syntax was accepted. It does not check layout,
containment, styles, or contrast, so never report it as a render.

### 5. Report what you verified

End with what ran, which blocks were rendered, previewed, parsed, or only read,
which checks passed, and what you could not check. For example: "Rendered both
blocks with mmdc 11.16.0 on Linux and inspected the PNGs; edge styles confirmed
in the SVG; the GitHub dagre copy was not rendered."

### 6. Do not widen the change

Apply these conventions to what you create or were asked to edit. Leave older class
names, init directives, and formatting in untouched diagrams alone, and mention them
instead of converting them.

## Naming

Mermaid IDs are references to drawing elements, not program variables. Keep the ID
stable when changing a displayed label, device model, address, or course title.

| Element               | Convention                                                                  | Example                                               |
| --------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------- |
| Node ID               | Uppercase words separated by underscores; scope, role, then optional number | `SITE_A_SW_01`, `SITE_A_RTR_01`, `TRAINING_COURSE_01` |
| Annotation node ID    | Uppercase purpose prefix, then the item it describes                        | `LEGEND_WILD_CARD`, `RULE_TIEBREAKERS`                |
| Subgraph ID           | `SG_` followed by an uppercase descriptive scope                            | `SG_SITE_A`, `SG_TRAINING`, `SG_LEGEND`               |
| Edge ID               | `edge_` followed by lowercase endpoint roles and optional purpose           | `edge_site_a_sw_rtr_data`                             |
| Invisible layout edge | `layout_` followed by its endpoint roles                                    | `layout_course_01_03`                                 |
| Node role class       | `node` followed by a descriptive role in camelCase                          | `nodeNetwork`, `nodeServer`, `nodeNote`               |
| Node status class     | `state` followed by a status in camelCase                                   | `statePending`, `stateUnavailable`                    |
| Edge CSS rule         | Select the named path by `data-id`; describe its meaning in a CSS comment | `.flowchart-link[data-id="edge_server_switch_data"]` |
| Subgraph class        | `group` followed by the grouping role in camelCase                          | `groupSite`, `groupStage`, `groupWrapper`             |
| Layout CSS rule       | Hide paths named with the `layout_` prefix | `path[data-id^="layout_"]` |

Use ASCII letters, digits, and underscores for IDs, beginning with a letter.
Avoid bare `end` and punctuation-heavy IDs even where a particular parser accepts
them. Put spaces, Unicode symbols, addresses, and human-readable punctuation in
quoted labels. These conservative choices make IDs easier to search and rename.

- Keep node, subgraph, and edge IDs distinct within a Mermaid block. Class names
  use their own prefixes so their purpose is obvious during review.
- Reuse the same ID for the same entity across related views when practical;
  each block still needs its own declarations and styles.
- Prefer meaningful scope names over unexplained abbreviations. Familiar roles
  such as `SW`, `RTR`, and `FW` are fine when the displayed labels explain them.
- Add a purpose suffix when two connections share endpoints, such as `_data`
  and `_management`. Use `_01`, `_02` for repeated peers consistently.
- Name edges that need styling or another explicit reference. Ordinary edges
  need not acquire IDs merely to satisfy the naming table.
- Give legend swatches and rules or note cards a purpose prefix (`LEGEND_`,
  `RULE_`, `NOTE_`) so they are never mistaken for entities in the drawing.
- Rename an ID with a script that skips quoted labels, not with a plain
  find-and-replace, which can also rewrite label and title text. See
  [renaming an ID](#rename-an-id).

## Source organization

Use this order within each Mermaid block:

1. YAML front matter with the diagram's configuration. It must be the first line.
1. A header comment saying what the diagram shows and, for a diagram that is
   edited repeatedly, how to update it (for example, how to record a result).
1. The diagram declaration and direction, such as `flowchart TB`.
1. Subgraphs and node declarations, with each node's full label defined once.
1. Meaningful connections, grouped by workflow or traffic path.
1. Layout-only connections, clearly commented and placed in their intended group.
1. `class` assignments for node roles, statuses, and subgraphs at the bottom.

The CSS definitions are already in the front matter's `themeCSS: |` block. Group
those rules by node role, status, edge meaning, subgraph, and layout helper. Edge
rules target stable named-edge attributes directly; they do not need `class`
assignments.

### Formatting

- **Indent two spaces per level,** in both the front matter and the diagram body.
  YAML requires spaces and two is its usual convention; using the same width below
  the front matter gives the whole block one rule. Mermaid ignores body indentation,
  so this is for readers, and two spaces keeps deeply nested subgraphs narrow.
  Never use tabs: they are invalid in YAML.
- **Omit semicolons on Mermaid statements.** Inside `themeCSS`, use ordinary CSS:
  one property per line and a semicolon after every declaration. Put the opening
  brace after the selector and the closing brace on its own line, as in the starter.
  This is an intentional distinction between the two languages.
- Use YAML's literal block scalar `themeCSS: |`, not its folded scalar. Indent the
  CSS two spaces under `themeCSS`, and each declaration two more spaces.
- Inside that literal scalar, comments are CSS `/* comments */`, not YAML `#`
  comments or Mermaid `%%` comments. Outside it, front matter uses YAML comments.
- Put each declaration, connection, and style statement on its own line. Prefer a
  single connection per line when it has a name, label, or special style.
- `A & B --> C & D` is fine for unnamed, unlabeled structural edges. It draws an
  arrow from every node on the left to every node on the right (four here), so add
  a comment when that fan-out is not obvious. Short invisible chains remain useful
  for list layout.

### Comments

- Use `%%` comments on their own lines to explain a layout constraint or unusual
  relationship. Comments should explain intent rather than repeat the syntax.
- **Never leave a bare `%%` line.** A line containing only `%%` breaks parsing when it
  appears before the diagram declaration, with an error such as "Parse error on
  line 1". Inside the diagram body it is currently harmless, but use `%% ---` as a
  separator everywhere so the rule needs no exceptions (see the
  [formatting lessons](mermaid-lessons-r1.0.6.md#known-bugs--hard-limitations)).
- **No `%%` comment of any kind may appear above front matter's opening `---`.**
  That is a parse error too.
- Outside `themeCSS`'s literal scalar, front-matter comments use `#`. Put a comment
  above each setting or a closely related group of settings explaining its purpose.
  Inside the CSS scalar, use `/* ... */` comments.

## Configuration

Keep each diagram self-contained. Its palette, layout engine, and spacing belong in
its own front matter, so the diagram looks the same when copied or previewed
without an external `--configFile`, theme JSON file, or stylesheet.

### Front matter

Configure every new diagram with YAML front matter: a `config:` block between two
`---` lines at the very top of the diagram.

```text
---
# Comments inside front matter start with #.
config:
  # The only built-in theme meant to be customized.
  theme: base
  # Keep the SVG structure consistent with the CSS recipes.
  look: classic
  layout: elk
  themeVariables:
    # Quote hex colors: an unquoted # starts a YAML comment.
    background: "#0b1120"
---
%% Mermaid comments go after the closing ---.
flowchart TB
```

Rules:

- **It must be the diagram's first line.** Nothing goes above the opening `---`,
  not even a `%%` comment.
- **Indent nested settings two spaces** under their parent, with spaces only.
- **Use quoted hex for color-related `themeVariables`.** Prefer readable CSS named
  colors only in CSS-consuming contexts; see the color/background decision table.
- **Quote hex values in YAML settings.** `background: #0b1120` parses as an
  empty value followed by a comment. YAML accepting a name does not establish
  theme-engine support. Inside the `themeCSS: |` literal, write normal CSS, such as
  `fill: #172b46;` or `fill: lavender;`; CSS hex values there need no quotes.
- **YAML front matter requires Mermaid 10.5 or newer.** Older hosts can ignore or
  reject it. This minimum does not guarantee the newer named-edge, ER grouping,
  selector, or layout behavior used below; test the actual viewer version.
- Use one configuration form per diagram, never both.

Add settings to solve a demonstrated problem, and record the intended renderer when
relying on version-specific features. To see which Mermaid version a viewer runs,
render a block containing only `info`. These settings come up often:

| Setting                          | Use it when                                                                                                     |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `flowchart.htmlLabels`           | Labels use `<b>`, `<br/>`, or other HTML. Set it to `true`.                                                     |
| `flowchart.wrappingWidth`        | Long node-label lines wrap at the default of about 200px. Raise it (for example 400). It does not widen edge labels, whose space is set by the calculated edge, and it is not a minimum box width. |
| `flowchart.subGraphTitleMargin`  | A subgraph title crowds the first node. It takes `top` and `bottom` values. Prefer it to padding the title with blank HTML. |
| `markdownAutoWrap`               | Deliberate line breaks in Markdown String labels wrap again. Set it to `false`. It is a top-level key, not under `flowchart`. |

A label is part of the layout: changing its text or line breaks changes its size and
can move nearby nodes and arrows. Fix label content before reaching for these settings.

### Fallback: the init directive

Before front matter, configuration went in a JSON comment placed before the diagram
declaration: `%%{init: { "theme": "base", "layout": "elk" }}%%`. Mermaid marks it as
deprecated, but it still works, including on GitHub. Use it only for a diagram that
must render in a viewer older than Mermaid 10.5. Converting an existing diagram is
not required, but do it when the diagram is being substantially edited; the MLB
bracket's conversion changed nothing in its render.

### Layout engine: ELK or dagre

**Recommendation:** request `layout: elk` for hierarchical flowchart architectures
when the host provides it. Use explicit `layout: dagre` for compatibility or a
verified local-direction requirement. Preserve the author's LR/TB/TD orientation.
ELK is a preference, not a guarantee against overlapping labels or escaped groups.

The current [official layout documentation](https://mermaid.js.org/intro/syntax-reference.html#selecting-layout-algorithms)
describes ELK as bundled/default in the full build and Dagre as the fallback for
the tiny build. Older/custom integrations may need a loader registered; do not
infer availability or defaults from an `mmdc` major version. Sequence diagrams
use their own renderer, not this flowchart engine choice. ER also supports layout
selection in the audited release; check its native documentation and version.

In the locally installed Mermaid 12.2.0 full build, both engines were actually
loaded and rendered. This does not establish a GitHub/VS Code installation's
capabilities. GitHub's official diagram documentation does not promise ELK support;
older community reports are not a current compatibility guarantee.

Test copies with **both** front-matter settings. Change the copy's own `layout`
value rather than relying on a CLI config override. Preserve nodes, labels, edges,
and direction; render both copies and inspect dimensions, containment, title
clearance, and named-edge geometry. Record warnings/fallbacks. Identical output
or a requested configuration string alone does not prove that an engine executed.
The audit runner records loaded Dagre/ELK module evidence and node geometry.

**Inherited local observations:** older bracket renders ignored local subgraph
direction under ELK; Dagre's documented flowchart limitation applies when group
members connect outside their group. Treat these as reasons to test, not universal
proof that a particular drawing silently switched engines. In the audited ELK
routes, `flowchart.curve` did not determine the orthogonal route shape. Dagre offers
`basis`, `linear`, `monotoneX`, and `step` options; inspect their actual bends and
arrowheads. The inherited `elk.mrtree` cross-group crash was a versioned observation;
this collection continues to recommend plain `elk`, without certifying other variants.

## Labels and relationships

Quote displayed node and subgraph labels. Use consistent capitalization and
terminology, and use Markdown Strings or HTML (`<b>`, `<br/>`, with `htmlLabels`
enabled) for intentional multiline or bold labels when the target renderer supports
them.

Choose arrows by meaning: `-->` for directional flow, `<-->` for bidirectional
communication, and `---` for an association with no claimed direction. Explain
special line patterns in a legend. An invisible link is a placement aid and must
not replace a real prerequisite or network relationship.

Keep details near what they describe: device-specific information belongs in node
labels; shared link information belongs on connections. Move long explanations
into prose below the drawing. Prefer `SG_` IDs for group references, but decide
whether a connection really targets a whole group or an individual member.

A subgraph ID used as an edge endpoint denotes a group-level relationship.
It does not imply fan-out to every member, bonded physical links, or access policy.
That subgraph is then structural, not decoration: removing its `subgraph`/`end`
wrapper orphans every node that was inside it, because the edge pointed at the
group rather than at any member.

## Emoji in labels

An emoji can make a diagram faster to scan: a server, a database, or a warning is
recognized before its label is read. Use one when it adds that, and leave it out when
it only decorates. Unlike prose, a diagram is drawn with the fonts of whichever
machine renders it, so emoji need more care here than in text.

### Rules

- **Labels only.** Never put an emoji in a node, subgraph, or edge ID or a class
  name; those stay ASCII (see [naming](#naming)).
- **One emoji, at the start, with text that says the same thing.** Write
  `"🗄️ Application database"`, not `"🗄️"` alone and not `"🗄️ DB"`. A reader
  without emoji fonts, or using a screen reader, still gets the meaning.
- **Use the [emoji vocabulary](#appendix-emoji-vocabulary-for-diagrams), one meaning
  per emoji.** If a diagram gives an emoji a project-specific meaning, put it in the
  diagram's legend.
- **Status still needs its text and its status class.** `"🚧 Backup server - PLANNED"`
  can add a cue to the `PLANNED` label and the `statePending` dashed border; it
  cannot replace either.
- **Be sparing.** Mark node roles or statuses, not every node, and keep emoji off
  edge labels unless the edge's meaning is the point.
- **Do not use arrow emoji** (such as ➡️ or ↔️). Mermaid already draws direction,
  and a second arrow inside a label competes with the real one.

### Characters that break

- **Keep the variation selector.** Some emoji are two code points: the symbol plus
  an invisible U+FE0F that requests the color form. Without it, ⚠ (`U+26A0` alone) rendered as a
  black text symbol even on a machine with an emoji font. The vocabulary lists which
  entries need it; copying the glyph from there keeps it.
- **Avoid multi-part emoji.** Sequences joined with a zero-width joiner, such as
  ❤️‍🩹 (health check), rendered as two empty boxes without an emoji font. Every
  vocabulary entry is a single symbol.
- **Shortcodes do not work.** `:rocket:` stays literal text inside a Mermaid label.
  Shortcodes are a GitHub Markdown feature; use the Unicode character.

### Whose fonts decide

| Output                                             | Emoji drawn with                         |
| -------------------------------------------------- | ---------------------------------------- |
| PNG from `mmdc`                                    | The rendering machine's fonts, baked in  |
| SVG, or a diagram viewed live (GitHub, VS Code)    | Each reader's fonts, so it can vary      |

Rendered with `mmdc 11.16.0` and the Noto Color Emoji font, every vocabulary entry
drew in color. With that font hidden, the same source drew monochrome symbols and box
widths shifted slightly. Before rendering a diagram with emoji on Linux, check for an
emoji font with `fc-list | grep -i emoji`; if there is none, the PNG shows what a
reader without emoji fonts sees, not what most readers see. Emoji change label
width, so re-render after adding or removing one.

## Layout

Render the complete diagram before adding any layout aid. Cross-boundary links can
override local subgraph direction; do not assume that adding `direction TB` will
force a group's internal arrangement.

### Keep connections clear of titles

A cross-boundary edge must not pass through a subgraph title or node label. Larger
CSS title fonts change the space those labels need. `subGraphTitleMargin` adds room
inside a group but does not guarantee that an incoming edge avoids its centered
title. Check the actual PNG after every font or connection change.

For a top-to-bottom diagram with an incoming edge through a group's title, first
try an overall `flowchart LR` direction so cross-group connections enter a side.
Re-render the complete diagram: do not assume the change fixed every route. If
that does not resolve it, reorganize the logical grouping or use an explicitly
labeled ingress component only when it represents a real component. Do not add
fictional traffic paths or move a node out of its ownership group just for spacing.
Title/edge overlap is a failed visual check even if parsing, CSS selector matches,
and computed styles all pass. Record and resolve the failure before reporting the
diagram as visually verified.

Neither engine lets you set sibling order directly. ELK's layered algorithm starts
from an order loosely based on declaration order, then swaps neighbors to reduce
edge crossings across the whole diagram. Changing one sibling's size can reorder the
others, and a change that works on a small test graph often stops working in the
full drawing. When placement is wrong, try these in order and re-render after each:

1. **Try declaration order.** Declare related nodes next to each other, such as each
   playoff seed next to its opponent. This helps in small or bracket-shaped drawings
   but is not reliable once the graph has competing structure; reordering the same
   four sibling subgraphs twice gave two different wrong orders.
1. **Merge nodes that always travel together.** When two entities share every
   connection, one node with a two-line label removes edges and crossings, as in
   `AL_SEED_04_05` for two seeds that play each other.
1. **Reduce the number of siblings.** Wrapping some siblings in a new parent subgraph
   gives the crossing pass a simpler problem. This was the lever that reliably fixed
   a cluttered row of host groups. Add a wrapper only when the grouping also makes
   sense to a reader.
1. **Add a pass-through node for a skipped stage.** An edge that jumps a column
   can cross the edges inside it. A dashed placeholder in that column, declared in
   order with its neighbors, lets the engine route it with them; a `bye` node in a
   bracket's Wild Card column removed every crossing to its right. Give it a
   visible label and a status-style dashed border so it is not mistaken for a
   real stage.
1. **Add invisible links.** Use `~~~` within the owning group, name it `layout_*`,
   and hide them with `path[data-id^="layout_"]` in embedded CSS if
   global strokes make them visible. Do not assign classes to layout edges.
   A hidden link still constrains ranks and spacing.

Under ELK, a chain of invisible links tends to become a stacked column, not a row.
That is useful for a tidy list inside one group, but chaining sibling subgraphs to
force a horizontal row turns the row into a staircase.

If exact placement still matters after these steps, the drawing may need a
different tool. Layout aids must never change what the diagram means.

### Two columns for a long list

One invisible chain stacks a long list into a tall column, and no chain spreads it
into one wide row. Two alternating chains give two columns, read across the rows:

```text
subgraph SG_PROGRAM["Program training"]
  PROGRAM_COURSE_01["Course 1"]
  ...
  PROGRAM_COURSE_08["Course 8"]

  %% Layout only; courses may be completed in any order.
  PROGRAM_COURSE_01 layout_course_01_03@~~~ PROGRAM_COURSE_03 layout_course_03_05@~~~ PROGRAM_COURSE_05 layout_course_05_07@~~~ PROGRAM_COURSE_07
  PROGRAM_COURSE_02 layout_course_02_04@~~~ PROGRAM_COURSE_04 layout_course_04_06@~~~ PROGRAM_COURSE_06 layout_course_06_08@~~~ PROGRAM_COURSE_08
end

%% Hide named layout edges with the themeCSS selector shown below; no classDef.
```

Put this rule in the diagram's existing `themeCSS: |` block:

```css
path[data-id^="layout_"] {
  opacity: 0 !important;
  visibility: hidden !important;
}
```

For eight courses in the orientation guide, one chain measured 314 × 891 px, no
chain 1,749 × 147 px, and two chains 485 × 471 px
([measured example](mermaid-lessons-r1.0.6.md#two-columns-for-long-lists-a-measured-example)).
The result is compact, not a rigid grid: columns need not be equal width and rows
need not align. Keep real prerequisite arrows separate from the chains, and try
realistic label lengths before trusting the shape.

### Page-level patterns

Two patterns, both checked under dagre in the MLB bracket:

- **Invisible wrapper subgraph.** A subgraph whose label is a single space shows no
  title. A `groupWrapper` class with a CSS stroke of `none` and a fill matching the canvas
  hides the box while giving its contents a solid background. Define that class
  in embedded CSS:

  ```css
  .cluster.groupWrapper rect {
    fill: white !important;
    stroke: none !important;
  }
  ```

  ```text
  subgraph SG_BRACKET[" "]
    direction LR
    ...
  end
  class SG_BRACKET groupWrapper
  ```

- **Stacking blocks.** Invisible links between subgraphs order whole sections, such
  as a drawing, a rules strip, and a legend: `SG_BRACKET ~~~ SG_RULES ~~~ SG_LEGEND`.
  These links connect groups rather than nodes and are usually left unnamed;
  comment them. Keep them invisible and inspect the final SVG.

## Styles

### Embed the stylesheet; retain semantic class assignments

Use **one `themeCSS: |` block per diagram** inside its own YAML `config`. For the
flowchart recipes, use `theme: base` and `look: classic`; ER and sequence controls
are described separately in the diagram-type section. Put palette defaults in `themeVariables`, and
custom shape, text, status, edge, and subgraph rules in embedded CSS. Prefer named
CSS colors there when they provide the intended appearance; retain hex for exact
shades. Color-related `themeVariables` use quoted hex instead. Choose export
backgrounds explicitly, separately from theme calculation. A stylesheet never
requires a separate file in this edition.

**Do not create `classDef`, inline `style`, `linkStyle`, or inline `:::` statements.**
Use bottom-of-block `class` statements for node roles, statuses, and subgraph groups.
A class need not have a `classDef`: Mermaid emits its name into the SVG, where
embedded CSS can select it. Define every assigned class in the stylesheet. Use one
assignment per role/status, for example `class BACKUP_SERVER nodeServer` and
`class BACKUP_SERVER statePending`. A comma-separated list is for element IDs,
not class names: `class SERVER_01,SERVER_02 nodeServer`.

Keep classes semantic (`nodeServer`, `statePending`, `groupSite`), not paint-based
(`greenBox`). Mermaid element IDs remain uppercase; classes retain the naming table's
camelCase prefixes. Preserve existing diagrams unless asked to convert them.

### Selector recipes for classic flowcharts

These selectors address Mermaid's generated SVG. They are not a universal DOM API.
Recheck their matches and computed styles when changing Mermaid versions or looks.

| Purpose | Selector pattern | Properties |
| --- | --- | --- |
| Node shape | `.node.nodeServer .label-container` | `fill`, `stroke`, `stroke-width` |
| Node HTML label | `.node.nodeServer .nodeLabel` | `color` |
| Node SVG label | `.node.nodeServer text` | `fill` |
| Status border | `.node.statePending .label-container` | `stroke-dasharray` |
| Site box | `.cluster.groupSite rect` | `fill`, `stroke`, `stroke-width` |
| Site title HTML label | `.cluster.groupSite .nodeLabel` | `color` |
| Site title SVG text | `.cluster.groupSite text` | `fill` |
| Site title size | `.cluster.groupTitleLarge .cluster-label` | `font-size`, `font-weight` |
| Named edge path | `.flowchart-link[data-id="edge_server_switch_data"]` | `stroke`, `stroke-width`, `stroke-dasharray` |
| Named invisible helper | `path[data-id^="layout_"]` | `opacity`, `visibility` |

Invisible `~~~` paths can retain `data-id` while **omitting `flowchart-link`**.
Therefore the helper rule deliberately selects `path[data-id^="layout_"]`, not
`.flowchart-link[data-id^="layout_"]`. In a fixture that actually declares a named
helper, require this selector to match at least one path and check its computed
opacity and visibility. Only a diagram with no helpers may treat that rule as optional.

Use both HTML-label and SVG-text selectors in role rules so text and fill remain
paired. The `.label-container` selector covers tested rectangles and cylinder
outlines without accidentally filling the small empty rectangle inside `.label`.
For an unfamiliar shape, inspect its SVG and add an explicit selector if needed.
Do not paint every descendant `path`: that can color icons and unrelated details.

Use descendant (space) selectors and attribute selectors. **Convention: avoid the `>`
child combinator** in `themeCSS`; the inherited guide observed configurations being
dropped with it. Do not confuse that restriction with YAML's scalar syntax: use
`themeCSS: |`, never `themeCSS: >`.

### CSS precedence, role, and status

Mermaid generates its own scoped CSS and sometimes inline styles. Put `!important`
on each custom appearance declaration in this edition, and keep semantic selectors
specific (for example `.node.nodeServer .label-container`, rather than `rect`).
This is a tested convention, not a guarantee against arbitrary host CSS. Do not
combine these rules with legacy `classDef` or inline styles; their inline important
values can win. Inspect computed styles if the expected appearance does not apply.

A role owns fill, text color, border color, and border width. A status owns the dash
pattern and still requires visible text such as `PLANNED`. Keep these property sets
separate so CSS order does not silently change the role palette. Keep the stylesheet
in role, status, edge, subgraph, then layout order. Do not rely on class-assignment
order to resolve CSS conflicts.

CSS declaration semicolons are required by this convention. Mermaid statement
semicolons remain omitted. Give each property its own line, including `!important`:

```css
.node.statePending .label-container {
  stroke-dasharray: 6 4 !important;
}
```

### Named edges and arrowheads

**Do not rely on `class edge_name edgeData` for embedded CSS.** Mermaid can consume
an edge class assignment without retaining that class on the SVG path. Name an edge
in its Mermaid connection and select `.flowchart-link[data-id="edge_name"]` in CSS.
The path qualifier avoids styling the separate edge-label element, which can share
that `data-id`. Group several explicit selectors with commas when paths share a style.
If the target SVG does not retain `data-id`, inspect it and document a tested selector
for that viewer; do not silently substitute a numeric edge index.

Edge CSS colors the path, **not automatically the arrowhead marker**. Keep the theme's
`lineColor` readable so shared arrowheads remain visible. Do not recolor a shared
marker to fix one edge: it can alter unrelated arrows. Preserve direction and patterns
in the connection syntax, and inspect arrowheads, labels, and path styles separately.
Do not claim matching colored markers unless actually verified.

### Choosing a palette and legends

Choose either a dark canvas with light text, or a light card with dark text. Pair
shape fills and text colors in the same role's CSS. Set the background in front matter
and pass the same background to the renderer (`-b '#0b1120'` for the starter). The
background variable alone does not reliably paint the export canvas. A light card
on a dark page needs white-filled group boxes or a white wrapper to keep its labels
and connectors readable. A theme change will not redesign explicit CSS colors.

Do not communicate status or connection meaning only through color. Use labels,
line patterns, and a prose edge legend. With more than four node-role classes, build
a `SG_LEGEND` subgraph whose swatches have the same `class` assignments as the real
nodes. Style that group through embedded CSS as well. This keeps the key and drawing
synchronized without duplicating color rules.

## Color formats and background decisions

**Official behavior:** Mermaid's [theme documentation](https://mermaid.js.org/config/theming.html#color-and-color-calculation)
limits its color-calculation contract to hex values. **Convention:** use quoted
six-digit `"#RRGGBB"` values for color-related `themeVariables`. YAML accepting
`white` only proves valid YAML; it does not prove Mermaid can derive the intended
palette. Named inputs may happen to work in a tested release without being a
portable theming contract. Non-color settings such as `darkMode` remain booleans.

**CSS convention:** prefer readable named colors in `themeCSS`, or supported
`classDef` properties in the standard edition. Keep exact hex shades where needed.
These values are consumed as CSS, unlike theme color calculations. CSS hex values
are unquoted. For `classDef`, the tested subset is named CSS colors and 3/6-digit
hex. An unescaped `fill:rgb(240,248,255)` control was rejected by the 12.2.0 parser
at the function syntax; normal browser CSS support does not establish support in
Mermaid's `classDef` grammar. Escaped/function variants remain unverified here.

| Context / intention | Choice | Reason / verification |
| --- | --- | --- |
| Color-related `themeVariables` | Quoted `"#RRGGBB"` | Official color-calculation contract; YAML validity alone is insufficient |
| Embedded `themeCSS: |` | Named CSS color; unquoted hex for precision | Normal CSS declarations, semicolons, and this edition's selectors/precedence rules |
| Standard-edition `classDef` color | Named CSS color or unquoted hex | Keep semantic role/status classes; test other color-function syntax before use |
| CLI export canvas | `-b white` or `-b '#0b1120'` | CLI explicitly sets the export background; record implementation and inspect output |
| Source-only light flowchart on dark UI | White-filled wrapper containing all nodes and edges | An actual SVG shape backs the content; outside margin may remain transparent |
| Light ER card on dark UI | Tested native ER grouping with white group fill | Version-specific; older hosts may lack ER subgraphs or have different selectors |
| Light sequence on dark UI | Light actors plus a native white `rect` message region | Protect messages and notes; check lifelines and arrows outside the region |
| Portable opaque SVG asset | Add a viewBox-sized background rectangle | Actual SVG paint survives inline and image embedding; inspect the resulting asset |
| Transparent SVG / PNG | Explicit transparent export plus light/dark composites | Host background will show through; it is not an opaque light card |

### What paints the background

`themeVariables.background` participates in palette derivation. It does **not**
guarantee a painted root SVG canvas. SVG shapes (`rect`, node/entity backgrounds)
paint their own areas; CSS `background-color` paints the element it actually matches.
The host editor's page background is a separate surface visible through transparent
parts of an inline SVG or transparent image. An SVG can have an opaque content card
and transparent outer margins. PNG may also retain alpha: it is opaque only when
rendered/composited onto an opaque background, not merely because it is PNG.

**Local finding, Mermaid 12.2.0/classic:** `themeCSS`'s `svg { background-color: white; }`
is scoped to `#diagram-id svg`, which does not match the root SVG. The rule can be
present in the SVG while doing nothing. Neither `:root` nor `&` solved root paint
in the audited build. Do not prescribe these as cross-renderer fixes. Match the
compiled selector and check the root's computed background, then inspect pixels.

For CLI images, set `-b white` and inspect SVG plus PNG. For a portable SVG, use
`scripts/opaque_svg.py input.svg --output output-opaque.svg --color white`: it adds
a real background rectangle first in paint order without changing diagram source.
Broad host CSS can still affect an inline SVG; embedding the opaque asset with
Markdown image syntax isolates it from the page's selectors. This is the fallback
when a host cannot render the source-only light-card example correctly.

### Renderer identity and evidence

Distinguish **official documentation**, **versioned local observations**, **actual
editor-extension observations**, **authoring conventions**, and **unverified claims**.
The tests for r1.0.7 use the locally installed full Mermaid 12.2.0 ESM distribution
and Python Playwright/Chromium, not the older CDN wrapper. The official npm CLI
12.0.0 is identified and tested separately. A name such as `mmdc` or its version
string does not establish which JavaScript library or browser ran.

Record executable path, CLI implementation/version, Mermaid library version and
build, requested and observed layout evidence, browser engine/version, and editor
extension ID/version where tested. The official npm CLI uses Puppeteer; independent
wrappers may use Playwright (`executablePath` versus `executable_path` in their
browser config). Never label an offline browser render an npm CLI render.

No actual GitHub or VS Code preview was run for this audit. Browser dark/light
host simulations are useful regression checks, not certification of those hosts.
Use GitHub's documented `info` diagram to identify its Mermaid version. VS Code
requires the actual preview implementation/extension and its version to be recorded.

## Reusable audit workflow

From this repository's `mermaid/` directory, with Python Playwright, PyYAML,
Chromium, and a local full Mermaid install available:

```bash
/home/sysadmin/.venv/bin/python -B scripts/audit_mermaid.py \
  mermaid-best-practices-r1.0.7.md mermaid-best-practices-CSS-r1.0.7.md \
  DoDAF_Guide_r1.0.8.md \
  --mermaid-dist node_modules/mermaid/dist \
  --output /tmp/mermaid-r1.0.7-review --engines --no-sandbox
```

The final browser option is environment-specific; omit it when Chromium's sandbox
works. The runner reads local assets through intercepted requests and blocks
external network requests. It extracts every fenced block with front matter,
records block number and enclosing document section, invokes Mermaid's parser,
renders SVG and transparent/light/dark PNGs at natural dimensions, and writes
`audit.json` plus `audit.md`. Its metadata identifies the local library and browser;
its results separately record CLI/editor checks as untested unless actually run.

The statuses are **PASS**, **FAIL**, **NOT TESTED**, and **NOT SUPPORTED**. Do not
collapse an absent preview or an unmatched optional selector into PASS. The scanner
flags color-format violations, duplicate flowchart declarations, invalid/missing
class references, and unbalanced subgraphs. These are deterministic conservative
checks for this collection's syntax, not a general Mermaid grammar. The actual
Mermaid parser remains authoritative for syntax acceptance.

CSS checks examine retained rules, the **compiled/scoped** selector matches, and
computed declarations. Check the root background independently of node fills.
Unknown configuration keys are compared with this build's defaults and reported
as unsupported/unverified, not silently accepted. Recognized settings can still be
ignored by a diagram type or host; inspect requested versus effective appearance.
The contrast check estimates foreground/background pairs from computed leaf text,
HTML backgrounds, and covering shapes in both host modes. Its 4.5:1 threshold is
a conservative text screening convention, not a full accessibility certification.
Gradients, opacity, nested graphics, and geometry-based background choices require
manual review. Absence of a flagged sample does not prove the drawing is accessible.

Open each changed PNG, including full-resolution wide/tall diagrams. Record visual
review separately: automation leaves it **NOT TESTED**. Do not declare a diagram
visually correct from parsing, CSS retention, selector counts, or contrast estimates
alone. Browser host simulations do not reproduce an unknown extension's CSS.

## Diagram-type styling and minimal light examples

The following examples were rendered with the local full Mermaid 12.2.0 build and
Chromium. They are source-level light cards/regions on simulated white and dark
hosts, not claims about an untested VS Code extension or GitHub's current build.
All color-related theme variables use quoted hex. Export with `-b white`, or add
an actual SVG background rectangle, when the **whole canvas** must be opaque.

| Type | Configuration and contrast controls | Background and compatibility |
| --- | --- | --- |
| Flowchart | `theme: base`, classic shapes, explicit layout; role fill/text and edge color | White-filled wrapper contains nodes and edges; verify label/title clearance in both engines |
| ER | Native `erDiagram`, entity/attribute palettes, relationship labels/lines, cardinality markers | Native ER group provides a light card in tested 12.2.0; older versions need an opaque export fallback |
| Sequence | Actor, signal, note and lifeline palette; native `sequence` options | Native white message `rect` plus light actors; outer margins remain transparent; ELK/Dagre do not lay out sequences |

The [flowchart](https://mermaid.js.org/syntax/flowchart.html),
[ER](https://mermaid.js.org/syntax/entityRelationshipDiagram.html), and
[sequence](https://mermaid.js.org/syntax/sequenceDiagram.html) syntax references
have different grammars and controls. A flowchart class recipe is not a sequence
actor-styling API. In particular, ER supports its own classes in current versions;
older renderers may not support the same class/subgraph syntax.

### Flowchart: actual white backing shape

The wrapper is intentionally presentational. Its label is a space, all semantic
connections stay inside it, and its white fill is real SVG paint. It does not
represent ownership or network isolation. Direction remains LR.

```mermaid
---
config:
  theme: base
  look: classic
  layout: elk
  # Hex values participate in Mermaid's color calculations.
  themeVariables:
    darkMode: false
    background: "#ffffff"
    primaryTextColor: "#191970"
    lineColor: "#475569"
    edgeLabelBackground: "#ffffff"
  themeCSS: |
    .cluster.groupLight rect {
      fill: white !important;
      stroke: none !important;
    }
    .node.nodeService .label-container {
      fill: aliceblue !important;
      stroke: steelblue !important;
    }
    .node.nodeService .nodeLabel,
    .node.nodeService text {
      color: midnightblue !important;
      fill: midnightblue !important;
    }
---
%% A source-only light card; wrapper has no domain meaning.
flowchart LR
  subgraph SG_LIGHT[" "]
    CLIENT_APP["Client"]
    SERVICE_API["API"]
    CLIENT_APP -->|"Request"| SERVICE_API
  end
  class CLIENT_APP,SERVICE_API nodeService
  class SG_LIGHT groupLight
```

### ER: headers, compartments, relationships, and markers

Do not reuse `.node .label-container` or old `.er.entityBox` recipes blindly.
The 12.2.0 classic ER renderer in this audit uses `.node .outer-path` for entity
outlines, `.row-rect-odd` / `.row-rect-even` for attributes, `.divider` for cell
boundaries, `.relationshipLine` for connectors, and `marker.er` for cardinalities.
The older `.er.entityBox`, `.er.attributeBoxEven`, `.er.relationshipLine`, and
`.er text` selectors matched nothing in the regression fixture. Accepted config
keys such as `er.fill`/`er.stroke` also did not establish that the requested
header/outline colors were actually used; inspect the rendered styles.

These are **versioned SVG observations**, not permanent Mermaid selector APIs.
Keep header and attribute fills distinguishable, pair text with each fill, and
check relationship labels, row dividers, crow's-foot paths, and open cardinality
circles independently. Theme defaults are useful even when CSS overrides are used.

```mermaid
---
config:
  theme: base
  look: classic
  layout: elk
  # Explicit header, attribute, text, and backing-card palette.
  themeVariables:
    darkMode: false
    background: "#ffffff"
    primaryColor: "#f0f8ff"
    primaryTextColor: "#191970"
    textColor: "#191970"
    lineColor: "#64748b"
    clusterBkg: "#ffffff"
    clusterBorder: "#ffffff"
    attributeBackgroundColorOdd: "#ffffff"
    attributeBackgroundColorEven: "#f1f5f9"
  themeCSS: |
    .cluster rect {
      fill: white !important;
      stroke: none !important;
    }
    .node .outer-path path[fill]:not([fill="none"]) {
      fill: aliceblue !important;
    }
    .node .outer-path path[fill="none"] {
      stroke: steelblue !important;
    }
    .row-rect-odd path[fill]:not([fill="none"]) {
      fill: white !important;
    }
    .row-rect-even path[fill]:not([fill="none"]) {
      fill: whitesmoke !important;
    }
    .row-rect-odd path[fill="none"],
    .row-rect-even path[fill="none"],
    .divider path {
      stroke: slategray !important;
    }
    .node .nodeLabel,
    .node text {
      color: midnightblue !important;
      fill: midnightblue !important;
    }
    .edgeLabel span,
    .edgeLabel text {
      color: midnightblue !important;
      fill: midnightblue !important;
      background-color: white !important;
    }
    .relationshipLine {
      stroke: slategray !important;
    }
    marker.er path {
      stroke: slategray !important;
      fill: none !important;
    }
    marker.er circle {
      stroke: slategray !important;
      fill: white !important;
    }
---
%% ER grouping is native syntax in the tested 12.2.0 build.
erDiagram
  subgraph SG_LIGHT[" "]
    ACCOUNT ||--o{ REQUEST : submits
    ACCOUNT {
      int account_id PK
      string name
    }
    REQUEST {
      int request_id PK
      int account_id FK
    }
  end
```

### Sequence: native controls and tested CSS

The native palette controls actor boxes/text, lifelines, signals, and notes.
In the audited build, `rect.actor` and `text.actor tspan` are distinct targets;
using a broad `.actor { fill: ... }` rule can accidentally affect text. The
[documented sequence classes](https://mermaid.js.org/syntax/sequenceDiagram.html#styling)
include `.actor-line`, `.messageLine0`, `.messageLine1`, `.messageText`, `.note`, and
`.noteText`; their matches and computed styles still need checking in the actual
renderer. Sequence messages and participant order are semantic, so do not change
them to imitate a flowchart orientation. Native `rect rgb(...)` syntax is a
sequence-region color, not a `themeVariables` value or a `classDef` declaration.

```mermaid
---
config:
  theme: base
  # Sequence uses its native renderer, not flowchart layout settings.
  themeVariables:
    darkMode: false
    background: "#ffffff"
    actorBkg: "#f0f8ff"
    actorTextColor: "#191970"
    actorBorder: "#64748b"
    actorLineColor: "#64748b"
    signalColor: "#64748b"
    signalTextColor: "#191970"
    noteBkgColor: "#ffffff"
    noteTextColor: "#191970"
  themeCSS: |
    rect.actor {
      fill: aliceblue !important;
      stroke: slategray !important;
    }
    text.actor,
    text.actor tspan {
      fill: midnightblue !important;
    }
    .messageText {
      fill: midnightblue !important;
    }
    .actor-line,
    .messageLine0,
    .messageLine1 {
      stroke: slategray !important;
    }
    .note {
      fill: white !important;
      stroke: slategray !important;
    }
    .noteText {
      fill: midnightblue !important;
    }
---
%% White backing for messages; actors have their own opaque fills.
sequenceDiagram
  participant CLIENT as Client
  participant API as API
  rect rgb(255,255,255)
    CLIENT->>API: Submit request
    API-->>CLIENT: Accepted
    Note over CLIENT,API: Messages have a white backing
  end
```

The ER/sequence selectors above are independent of the flowchart role selectors.
No flowchart `classDef`, inline `style`, or `linkStyle` statements are introduced.

## Starter template

This retained dark-palette example expects a matching dark host or an explicit
opaque dark export. For live source on both host themes, use the light-card
examples above. A `background` theme variable alone does not paint its outer canvas.

This self-contained flowchart shows two sites, data connections, a management
request, and a planned backup server. It is an illustrative topology, not a claim
about access policy, actual backup operation, speed, or redundancy. Copy the complete
fenced block. Its CSS selector contract is `look: classic`, Mermaid 12.2.0; also
verify the viewer in which the Markdown will be presented.

```mermaid
---
config:
  # Base supports explicit theme defaults beneath the CSS overrides.
  theme: base
  # The selector recipes below target classic flowchart shapes.
  look: classic
  # Keep owned nodes within their site boxes where supported.
  layout: elk
  # Supply readable defaults, including neutral arrowhead markers.
  themeVariables:
    darkMode: true
    background: "#0b1120"
    primaryTextColor: "#e6edf7"
    textColor: "#e6edf7"
    lineColor: "#94a3b8"
    edgeLabelBackground: "#111827"
    clusterBkg: "#111827"
    clusterBorder: "#475569"
    titleColor: "#e6edf7"
  # Leave space between nodes, ranks, and the site titles.
  flowchart:
    nodeSpacing: 35
    rankSpacing: 55
    subGraphTitleMargin:
      top: 8
      bottom: 12
  # All custom appearance travels with this diagram as ordinary CSS.
  themeCSS: |
    .node.nodeNetwork .label-container {
      fill: darkslateblue !important;
      stroke: lightskyblue !important;
      stroke-width: 2px !important;
    }
    .node.nodeNetwork .nodeLabel,
    .node.nodeNetwork text {
      color: aliceblue !important;
      fill: aliceblue !important;
    }
    .node.nodeServer .label-container {
      fill: darkslategray !important;
      stroke: aquamarine !important;
      stroke-width: 2px !important;
    }
    .node.nodeServer .nodeLabel,
    .node.nodeServer text {
      color: honeydew !important;
      fill: honeydew !important;
    }
    .node.nodeStorage .label-container {
      fill: indigo !important;
      stroke: plum !important;
      stroke-width: 2px !important;
    }
    .node.nodeStorage .nodeLabel,
    .node.nodeStorage text {
      color: lavender !important;
      fill: lavender !important;
    }
    .node.nodeOperator .label-container {
      fill: midnightblue !important;
      stroke: cyan !important;
      stroke-width: 2px !important;
    }
    .node.nodeOperator .nodeLabel,
    .node.nodeOperator text {
      color: lightcyan !important;
      fill: lightcyan !important;
    }
    /* Status changes the border pattern, not the server's role colors. */
    .node.statePending .label-container {
      stroke-dasharray: 6 4 !important;
    }
    /* Data paths share a rule; named paths do not need edge classes. */
    .flowchart-link[data-id="edge_site_a_app_sw_data"],
    .flowchart-link[data-id="edge_site_a_db_sw_data"],
    .flowchart-link[data-id="edge_site_a_sw_fw_data"],
    .flowchart-link[data-id="edge_site_a_fw_carrier_data"],
    .flowchart-link[data-id="edge_site_b_fw_carrier_data"],
    .flowchart-link[data-id="edge_site_b_sw_fw_data"] {
      stroke: lightslategray !important;
      stroke-width: 2px !important;
    }
    .flowchart-link[data-id="edge_site_a_admin_fw_management"] {
      stroke: cyan !important;
      stroke-width: 2px !important;
      stroke-dasharray: 3 3 !important;
    }
    .flowchart-link[data-id="edge_site_b_backup_sw_planned"] {
      stroke: gold !important;
      stroke-width: 2px !important;
      stroke-dasharray: 6 4 !important;
    }
    .cluster.groupSite rect {
      fill: #111827 !important;
      stroke: lightslategray !important;
      stroke-width: 1px !important;
    }
    .cluster.groupSite .nodeLabel,
    .cluster.groupSite text {
      color: aliceblue !important;
      fill: aliceblue !important;
    }
    .cluster.groupTitleLarge .cluster-label {
      font-size: 20px !important;
    }
    /* Hide named helpers even if a broad edge rule is added later. */
    path[data-id^="layout_"] {
      opacity: 0 !important;
      visibility: hidden !important;
    }
---
%% Two sites joined by a carrier network, with a management path and a
%% planned backup server. Replace with verified topology before use.
flowchart TB
  %% 1. Ownership: declare each full node label once inside its site.
  %% Change quoted labels freely; keep IDs stable for edges and class assignments.
  %% SG_ identifies a boundary, not another device or a security guarantee.
  subgraph SG_SITE_A["Site A - application services"]
    SITE_A_ADMIN_01["Admin workstation"]
    SITE_A_SW_01["Access switch"]
    SITE_A_FW_01["Edge firewall / router"]
    SITE_A_APP_01["Application server"]
    SITE_A_DB_01[("Application database")]
  end

  %% The carrier is outside both sites; its internal topology is out of scope.
  WAN_CARRIER["Carrier network"]

  subgraph SG_SITE_B["Site B - backup services"]
    SITE_B_FW_01["Edge firewall / router"]
    SITE_B_SW_01["Access switch"]
    SITE_B_BACKUP_01["Backup server - PLANNED"]
  end

  %% 2. Data path: solid double arrows mean bidirectional connectivity.
  %% Labels describe link purpose, not measured speed or verified access policy.
  %% Name edges that share styles; names survive unrelated edge insertions.
  %% Each chain is written from inside a site toward the carrier, so both WAN
  %% links leave through the bottom of their site and never cross a site title.
  SITE_A_APP_01 edge_site_a_app_sw_data@<-->|"Service network"| SITE_A_SW_01
  SITE_A_DB_01 edge_site_a_db_sw_data@<-->|"Database network"| SITE_A_SW_01
  SITE_A_SW_01 edge_site_a_sw_fw_data@<-->|"LAN transit"| SITE_A_FW_01
  SITE_A_FW_01 edge_site_a_fw_carrier_data@<-->|"WAN uplink"| WAN_CARRIER
  SITE_B_FW_01 edge_site_b_fw_carrier_data@<-->|"WAN uplink"| WAN_CARRIER
  SITE_B_SW_01 edge_site_b_sw_fw_data@<-->|"LAN transit"| SITE_B_FW_01

  %% 3. Logical management path: dotted arrow identifies the initiating host.
  %% It does not imply a separate cable or the absence of return traffic.
  SITE_A_ADMIN_01 edge_site_a_admin_fw_management@-.->|"HTTPS / SSH management"| SITE_A_FW_01

  %% 4. Planned connection: the dashed line and label both indicate future work.
  %% Do not imply that backups already run merely because this node is present.
  SITE_B_BACKUP_01 edge_site_b_backup_sw_planned@---|"Planned attachment"| SITE_B_SW_01

  %% Assign semantic classes; all definitions are in themeCSS above.
  class SITE_A_SW_01,SITE_A_FW_01,SITE_B_FW_01,SITE_B_SW_01,WAN_CARRIER nodeNetwork
  class SITE_A_APP_01,SITE_B_BACKUP_01 nodeServer
  class SITE_A_DB_01 nodeStorage
  class SITE_A_ADMIN_01 nodeOperator
  class SITE_B_BACKUP_01 statePending
  class SG_SITE_A,SG_SITE_B groupSite
  class SG_SITE_A,SG_SITE_B groupTitleLarge
```

**Legend:** solid double arrows show bidirectional data connectivity. The dotted cyan
arrow shows management initiation; the dashed gold line shows a planned connection.
Arrowheads retain the neutral theme color. The backup server's dashed border and
`PLANNED` label identify its status. Site boxes group ownership, not isolation.

To adapt this template:

1. Replace quoted labels and actual relationships before adjusting layout.
1. Retain stable node and named-edge IDs. On edge renames, update `data-id` selectors
   in `themeCSS` as well as the connection statement.
1. Add or remove node and group assignments at the bottom. A second status needs its
   own `class` statement and its own CSS rule; do not merge its palette into a role.
1. Remove the planned label, status assignment, and planned connection pattern
   together when commissioning the backup server.
1. Render SVG and PNG with matching background `-b '#0b1120'`. Check rule retention,
   selector matches, computed styles, labels, containment, and arrowheads.

## Review before sharing

- Confirm each node's label is defined once and all IDs are distinct.
- Check that every class assignment names an existing node or subgraph and a class
  addressed by `themeCSS`. Check each edge selector against an existing named path.
- Confirm one embedded `themeCSS: |` block, `theme: base`, and `look: classic` for
  the flowchart selector recipes. No external CSS dependency is needed.
- Confirm no `classDef`, inline `style`, or `linkStyle` Mermaid statements were added.
- Verify CSS uses semicolons, one property per line, and `!important` for appearance.
- Check HTML-label `color` and SVG-text `fill`; checking shape fill alone is insufficient.
- Recheck assignments after removing or renaming an edge or node.
- Verify arrows, labels, and legends describe the real workflow or topology.
- Confirm front matter starts the block and hex values in YAML settings are quoted.
  Hex values inside the CSS literal use normal unquoted CSS syntax.
- Check emoji against [emoji in labels](#emoji-in-labels): labels only, each beside
  matching text, from the vocabulary, with no shortcodes or multi-part sequences.
- Check for bare `%%` comment lines: `grep -nE '^\s*%%\s*$' file.md` prints nothing.
- Check for inline class assignments in new diagrams: `grep -n ':::' file.md` prints
  nothing inside Mermaid blocks.
- Count `subgraph` and `end` lines; the two numbers must match. A misplaced `end`
  silently nests a sibling inside another subgraph, and inconsistent indentation
  hides it: `grep -cE '^\s*subgraph\b' file.md; grep -cE '^\s*end\s*$' file.md`.
- After moving a node to a different subgraph, search for its ID in every `~~~`
  chain. A stale chain can collapse a subgraph to a sliver or pull the node back
  into its old box.
- Render in the target viewer and inspect wrapping, containment, arrowheads, and contrast.
  Require cross-boundary edges to clear group titles and node labels.
- For a diagram that may be read on a dark page, export with `-b transparent` and
  check the PNG composited over a dark color, for example
  `magick out.png -background '#0d1117' -flatten out-on-dark.png`
  (ImageMagick 6: `convert`).
- Confirm CSS rule retention in the SVG and computed browser styles, not only appearance; see
  [verifying a render](#verify-a-render).
- Record what was actually verified: source accuracy, a successful render, measured
  layout, and visual inspection are separate claims. Note the viewer and its Mermaid
  version.

See the [formatting lessons](mermaid-lessons-r1.0.6.md) for observed layout gotchas
and the [authoring reference](mermaid-reference.md) for fuller syntax examples.
Official references: [flowchart syntax, IDs, and classes](https://mermaid.js.org/syntax/flowchart.html),
[configuration](https://mermaid.js.org/config/configuration.html),
and [theme configuration](https://mermaid.js.org/config/theming.html).

## Appendix: Rename and verification procedures

### Rename an ID

A plain find-and-replace can rewrite label and title text as well as the ID; the
[formatting lessons](mermaid-lessons-r1.0.6.md#bulk-renaming-ids-safely) record both
cases. This script changes an ID only inside Mermaid blocks, only as a whole token,
and never inside a quoted label:

````bash
python3 - diagram.md SITE_B_SW_01 SITE_B_SW_02 <<'EOF'
import re, sys
path, old, new = sys.argv[1:]
token = re.compile(rf'(?<![\w-]){re.escape(old)}(?![\w-])')
lines, inside, count = [], False, 0
for line in open(path, encoding='utf-8'):
    if line.strip() == '```mermaid':
        inside = True
    elif inside and line.startswith('```'):
        inside = False
    elif inside:
        parts = re.split(r'("[^"]*")', line)
        for i in range(0, len(parts), 2):
            parts[i], n = token.subn(new, parts[i])
            count += n
        line = ''.join(parts)
    lines.append(line)
open(path, 'w', encoding='utf-8').writelines(lines)
print(f'{count} replacement(s) of {old} -> {new} outside quoted labels')
EOF
````

Then:

1. Compare the reported count with the declaration, connections, and `class` lines
   you expected to change.
1. Search for the old ID. Any remaining matches should be prose or labels that you
   intend to keep.
1. Search for the corrupted shape, not only the new ID: the new ID or a fragment of
   it inside a quoted label or subgraph title. Confirming that the new ID exists
   says nothing about a label three lines away.
1. Rename related edge IDs, such as `edge_site_b_sw_fw_data`, separately; the script
   does not match an ID embedded in a longer name.
1. Re-render and compare the drawing with the previous render. A damaged title is
   easy to miss in a source diff.

### Verify a render

A successful render proves accepted syntax, not successful styling. Verify all of:

1. **Rule retention:** custom selectors and declarations appear in the SVG's style
   element. A dropped YAML scalar can otherwise leave an apparently valid diagram.
1. **Selector matches:** each required selector matches its intended SVG element.
   An edge path and its label can share `data-id`; keep `.flowchart-link` in the selector.
1. **Computed appearance:** load the SVG in a browser and inspect `getComputedStyle`.
   This proves the CSS cascade selected the intended values. Inline `style` attributes
   can be empty when embedded CSS works correctly; do not use the old inline-edge-style
   procedure as the CSS edition's success test.
1. **Visual result:** open the browser-rendered PNG. Check wrapping, contrast, glyphs,
   arrowheads, legends, group containment, and invisible helpers.

For example, in the browser console with the rendered SVG open:

```javascript
const svg = document.querySelector('svg');
const edge = svg.querySelector('.flowchart-link[data-id="edge_site_a_admin_fw_management"]');
if (!edge) throw new Error('Named management path selector matched nothing');
const edgeStyle = getComputedStyle(edge);
console.log(edgeStyle.stroke, edgeStyle.strokeWidth, edgeStyle.strokeDasharray);
const server = svg.querySelector('.node.nodeServer.statePending .label-container');
if (!server) throw new Error('Pending server shape selector matched nothing');
console.log(getComputedStyle(server).strokeDasharray);
const label = svg.querySelector('.node.nodeServer .nodeLabel');
if (label) console.log(getComputedStyle(label).color);
```

For the starter, expect management stroke `rgb(0, 255, 255)` (cyan), width `2px`,
and dash array equivalent to `3px, 3px`. Expect the pending server border dash array
`6px, 4px`. Browser serialization can use commas, spaces, RGB values, or pixel units;
compare normalized values rather than requiring a literal source spelling.

Check **each** custom role and status, the site box and title, every named-edge rule,
and any layout helper. Inspect shared arrowheads separately: path colors do not
propagate to markers. A stylesheet rule appearing in the SVG does not establish that
it matched or won the cascade. A successful computed-style test does not replace
opening the PNG. Report the renderer, Mermaid library version, exact checks run,
and anything unverified. Re-render after the last change.

## Appendix: Emoji vocabulary for diagrams

A small, fixed set chosen for architecture and process diagrams. Every entry is a
single symbol; entries listing `U+FE0F` need that invisible character kept, so copy
the glyph from this table rather than retyping it. Arrow emoji are left out on
purpose (see [emoji in labels](#emoji-in-labels)).

| Emoji | Code points | Meaning |
| ----- | ----------- | ------- |
| **Status** | | |
| ✅ | `U+2705` | Complete, passed, or verified |
| ❌ | `U+274C` | Failed or rejected |
| ⚠️ | `U+26A0 U+FE0F` | Warning or caution |
| ℹ️ | `U+2139 U+FE0F` | Information |
| 🚧 | `U+1F6A7` | In progress or planned |
| ⏸️ | `U+23F8 U+FE0F` | Paused |
| ⛔ | `U+26D4` | Blocked or prohibited |
| 🚨 | `U+1F6A8` | Active incident or alert |
| **Systems and services** | | |
| 🖥️ | `U+1F5A5 U+FE0F` | Server, host, or console |
| 💻 | `U+1F4BB` | Workstation or client |
| ⚙️ | `U+2699 U+FE0F` | Service, process, or settings |
| 🗄️ | `U+1F5C4 U+FE0F` | Database or structured storage |
| 💾 | `U+1F4BE` | Disk, backup, or restore point |
| ☁️ | `U+2601 U+FE0F` | Cloud service or hosted resource |
| 🐳 | `U+1F433` | Container or container image |
| 📦 | `U+1F4E6` | Package or artifact |
| **Networking** | | |
| 🌐 | `U+1F310` | Network, internet, or DNS |
| 🔌 | `U+1F50C` | Physical link or port |
| 📡 | `U+1F4E1` | Wireless or radio link |
| 🔗 | `U+1F517` | Tunnel, route, or relationship |
| 🚦 | `U+1F6A6` | Traffic policy or QoS |
| 🧱 | `U+1F9F1` | Firewall or network boundary |
| 🗺️ | `U+1F5FA U+FE0F` | Topology, site, or map |
| **Security and operations** | | |
| 🛡️ | `U+1F6E1 U+FE0F` | Security control or protection |
| 🔒 | `U+1F512` | Encryption or restricted access |
| 🔑 | `U+1F511` | Credential, key, or certificate |
| 👤 | `U+1F464` | User or account |
| 👥 | `U+1F465` | Group, role, or team |
| 📊 | `U+1F4CA` | Monitoring or metrics |
| ⏱️ | `U+23F1 U+FE0F` | Timing or latency |
| 🔄 | `U+1F504` | Restart, retry, or sync |
| 🔧 | `U+1F527` | Configuration or repair |
| 🧪 | `U+1F9EA` | Test or experiment |
| 🔍 | `U+1F50D` | Inspection or review |
| 🚀 | `U+1F680` | Release or deployment |
| **Notes** | | |
| 📝 | `U+1F4DD` | Note or documentation |
| 💡 | `U+1F4A1` | Tip or idea |
| 📌 | `U+1F4CC` | Important reference |

## Revision history

**CSS r1.0.7 (Oct. 25, 2026).** Corrected theme-variable color scope, separated
palette and canvas handling, added type-specific light examples and selector
contracts, qualified layout/host claims, and added reproducible parser/render,
computed-style, contrast, and engine checks. See
[the r1.0.7 audit](mermaid-guide-audit-r1.0.7.md) for actual results and limitations.
Older entries below record historical policy; r1.0.7 supersedes their broad
recommendation of named colors inside theme variables.


**CSS r1.0.6 (Oct. 25, 2026).** Prefer CSS named colors when they provide the
intended appearance, for readability and maintainability. Retain hex colors where
precise colors are necessary, across embedded CSS, theme variables, and export
backgrounds.

**CSS r1.0.5 (Oct. 25, 2026).** Separate embedded-CSS edition. Replaced authoring
instructions and the starter's `classDef` rules with readable `themeCSS: |` rules;
retained semantic node/subgraph `class` assignments. Added classic-flowchart selector
recipes, named-edge attribute selectors, CSS precedence, arrowhead limits, and
computed-style verification. The original guide is unchanged. Validation evidence
for this edition is recorded in
[the companion evaluation](mermaid-best-practices-CSS-r1.0.5-evaluation.md).

### Inherited source history

The entries below describe the original guide's development and earlier renders;
they are provenance, not claims that those versions tested this CSS edition.


**r1.0.5 (Oct. 24, 2026).** New [emoji in labels](#emoji-in-labels) section and
[emoji vocabulary](#appendix-emoji-vocabulary-for-diagrams) appendix, self-contained
so an agent needs only this file. Tested with `mmdc 11.16.0` with and without an
emoji font: the variation selector, multi-part sequences, and shortcodes behave as
described. Added an emoji font check to the agent steps and the review checklist.

**r1.0.4 (Oct. 24, 2026).** Agent section: when to use SVG and PNG, why to take the
PNG from `mmdc` rather than converting the SVG (tested: `cairosvg` dropped every
label and the canvas color, ImageMagick 6 refused the file, and turning off
`htmlLabels` left overlapping text), and how driving Chromium directly relates to
`mmdc`.

**r1.0.3 (Oct. 24, 2026).** Added [For AI agents: verify before you deliver](#for-ai-agents-verify-before-you-deliver):
what to do in a chat, a Mermaid preview, a sandbox, a Linux or macOS shell, or on
Windows; a cross-platform Python script that renders each block with `mmdc`;
browser failures; a labeled parse-check fallback; and reporting what was verified.
The starter template was rendered with `mmdc 11.16.0` for this revision, and its
edge styles matched the expected values.

**r1.0.2 (Oct. 24, 2026).** Rules carried over from the
[formatting lessons r1.0.6](mermaid-lessons-r1.0.6.md):

- Corrected: dagre honors a subgraph's `direction` only while none of its nodes
  connects outside it.
- Corrected: declaration order is a weak lever for sibling order. Added fewer
  siblings, pass-through nodes, and the ELK column effect of invisible chains to
  the Layout steps, plus the two-column pattern for long lists.
- Curve choices under dagre (`monotoneX`, `step` caveats), the ELK-variant warning,
  and the `info` block for checking a viewer's Mermaid version.
- `subGraphTitleMargin`, `markdownAutoWrap`, and the edge-label limit of
  `wrappingWidth`.
- Light-card palettes: the `background` variable does not reliably paint the
  canvas, and gray lines fade on dark pages.
- Subgraph IDs as edge endpoints are structural.
- Review checklist: `subgraph`/`end` count, stale `~~~` chains, dark composite
  command, and recording what was verified. Rename steps: search for corrupted labels.

**r1.0.1 (Oct. 24, 2026).** Lessons from the MLB playoff diagrams:

- YAML front matter is the default configuration form; the init directive is the
  fallback for viewers older than Mermaid 10.5. Starter template converted.
- Two-space indentation and no statement semicolons, replacing four spaces and
  required semicolons.
- Classes are assigned only with `class` statements; inline `:::` is not used in
  new diagrams. Added the class syntax that fails.
- Precise bare-`%%` behavior, and no `%%` above front matter.
- ELK ignores `flowchart.curve`; removed the template's unused `curve` setting.
  GitHub dagre check now changes the copy's own `layout` setting.
- New Layout section: declaration order, merged nodes, wrapper subgraphs, and
  stacked blocks. New guidance on light-card palettes and in-diagram legends.
- Naming table: annotation node prefixes and more subgraph class examples.
