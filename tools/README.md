# ZTA documentation auditor

<!-- zta-doc: id=DOC-TOOLS-AUDIT; parent=ROOT; lineage=ROOT -->

**Owner (proposed):** Documentation Engineering  
**Status:** Implemented documentation integrity utility; does not validate security configuration

Run from the repository root with Python 3.10 or newer. No third-party packages are required.

```bash
python3 tools/audit_zta.py --root . --report audit-report.md
python3 -m unittest discover -s tests -v
```

`--root` selects the tree to audit. `--report` writes a Markdown report at the supplied path, relative to the current working directory, and excludes that output from the current scan. Diagnostics include relative file paths, one-based line numbers and error codes. Exit status is 0 on a clean audit, 1 on integrity errors, and 2 on argument or report-write failures.

## Declared checks

- Recursively require one document metadata declaration per managed Markdown file.
- Reject duplicate IDs across documents, tables and traceable rows, malformed metadata, missing parents, cycles, incorrect lineage and invalid pillar/control/requirement/test/evidence levels.
- Require traceable table metadata, consistent row parents and column counts, and compatible document/table scopes. Metadata without an adjacent table is an orphan.
- Check relative Markdown links and heading fragments, including images, full reference-style links, angle-bracket destinations with spaces, and one level of parentheses in ordinary destinations.
- Check declared `References` IDs and `Decomposition` links. A decomposition target must exist as a managed document with the corresponding row ID as its parent.
- Require a Validated row to reference descendant Evidence IDs. Each evidence record requires a local artifact file, result and reviewer. Human review must determine whether the artifact and result actually support the claim.

See [documentation conventions](../standards/documentation-conventions.md) for the metadata schema. Fixtures exercise valid hierarchies, deliberate duplicates, missing parents, cycles, scope errors, malformed metadata, broken links, missing decomposition, unrelated/missing evidence and CLI exit behavior.

## Scope and limits

`audit-config.json` contains explicit relative-path exclusion patterns. The original handoff and Mermaid guide are preserved imports with example IDs and unavailable supplemental links; their internal examples are excluded. Links from managed files to these imports still require an existing target and a valid heading when a fragment is used. The generated `audit-report.md` is also excluded. Every matching Markdown file is listed in the report. Files under `.git`, `.agents`, `.codex`, `.aws`, `.venv`, `node_modules` and `__pycache__` are not documentation inputs.

The supported authoring subset uses ATX headings (`# Heading`), pipe tables, one-line ZTA metadata comments, inline links, images and full/collapsed reference links. Fenced code, inline code and ordinary HTML comments are ignored when discovering declarations and links. Bare URLs, shortcut reference links, arbitrary HTML links, setext headings and advanced Markdown extensions are not audited. Escape table pipes with a backslash. The tool checks local targets and heading anchors without network requests; external URLs and evidence contents are not verified.

Only explicit `References` and `Decomposition` columns create machine-checkable architecture references or promises of decomposition. The auditor cannot infer unstated relationships from prose, determine missing engineering requirements, verify source currency, parse/render Mermaid, certify cryptography, or confirm physical isolation. A clean report is evidence of documentation consistency within this declared scope.
