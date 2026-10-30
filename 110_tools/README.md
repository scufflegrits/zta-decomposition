---
schema_version: 1
id: DOC-TOOLS-AUDIT
title: ZTA documentation auditor
document_type: tooling
parent: ROOT
lineage:
- ROOT
owner: Documentation Engineering
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-24'
---

# ZTA documentation auditor

**Status:** Implemented documentation integrity utility; does not validate security configuration

Run from the repository root with Python 3.10 or newer. YAML frontmatter parsing requires PyYAML, declared in `requirements.txt`. Install it in your preferred Python environment:

```bash
python3 -m pip install -r requirements.txt
python3 110_tools/generate_index.py --root . --check
python3 110_tools/audit_zta.py --root . --report audit-report.md
python3 -m unittest discover -s 100_tests -v
```

`--root` selects the tree to audit. `--report` writes a Markdown report at the supplied path, relative to the current working directory, and excludes that output from the current scan. Diagnostics include relative file paths, one-based line numbers and error codes. Exit status is 0 on a clean audit, 1 on integrity errors, and 2 on argument or report-write failures.

## Declared checks

- Recursively require one schema-valid YAML frontmatter block at the beginning of each managed Markdown file; reject legacy `zta-doc` declarations, duplicate keys, unsupported fields/types/statuses and malformed dates.
- Preserve original body line numbers and ignore frontmatter when discovering links, entity tables and heading anchors.
- Reject duplicate IDs across documents, tables and traceable rows, malformed metadata, missing parents, cycles, incorrect lineage and invalid pillar/control/requirement/test/evidence levels.
- Require traceable table metadata, consistent row parents and column counts, and compatible document/table scopes. Metadata without an adjacent table is an orphan.
- Check relative Markdown links and heading fragments, including images, full reference-style links, angle-bracket destinations with spaces, and one level of parentheses in ordinary destinations.
- Check declared `References` IDs and `Decomposition` links. A decomposition target must exist as a managed document with the corresponding row ID as its parent.
- Check optional `Jira epic`, `Jira stories` and `Verification stories` columns on the appropriate entity rows. Validate direct issue-key link syntax, matching URL keys, duplicate keys within a cell and conflicting destinations across rows. Blank cells are allowed; no network access is used. See the [manual Jira standard](../090_standards/manual-jira-traceability.md).
- Require a Validated row to reference descendant Evidence IDs. Each evidence record requires a local artifact file, result and reviewer. Human review must determine whether the artifact and result actually support the claim.
- Check `Implementation ID` and `Acceptance ID` records under control parents, with separate deployment, verification and customer-decision states. Check required operational context, scoped references, configuration/decision files, execution-baseline links and the records supporting positive claims. Documented limitations may be accepted without a technical pass or coverage percentage. See the [implementation/acceptance standard](../090_standards/implementation-acceptance.md).

See [documentation conventions](../090_standards/documentation-conventions.md) for the metadata schema. Fixtures exercise valid hierarchies, deliberate duplicates, missing parents, cycles, scope errors, malformed metadata, broken links, missing decomposition, unrelated/missing evidence and CLI exit behavior.

## Document index generation

Run `python3 110_tools/generate_index.py --root .` after adding, moving, removing or changing metadata on a document. The generator uses auditor discovery, groups maintained files by `document_type`, lists source imports separately and includes itself through this tooling document. `index.md`, `taxonomy.md` and `900_project-admin/TODO.md` are cataloged like other maintained documents. Generated report files are described by path without requiring local output to exist in a fresh checkout.

Use `--check` for a read-only freshness check; a missing or stale index returns 1. Successful generation/check returns 0; an output read/write error returns 2. Source integrity errors prevent generation. The standalone auditor does not check index freshness, so run both commands before review. The index body is generated; the taxonomy is maintained by hand.

## Scope and limits

`audit-config.json` contains explicit relative-path exclusion patterns. The original handoff and supplied guides under `080_references/010_guides/` are source imports with example IDs and potentially unavailable supplemental links; their internal examples are excluded. Links from managed files to these imports still require an existing target and a valid heading when a fragment is used. The generated `audit-report.md` is also excluded. Every matching Markdown file is listed in the report. Files under `.git`, `.agents`, `.codex`, `.aws`, `.venv`, `node_modules` and `__pycache__` are not documentation inputs.

The supported authoring subset uses ATX headings (`# Heading`), pipe tables, YAML document frontmatter, one-line `zta-table` comments, inline links, images and full/collapsed reference links. Fenced code, inline code and ordinary HTML comments are ignored when discovering declarations and links. Bare URLs, shortcut reference links, arbitrary HTML links, setext headings and advanced Markdown extensions are not audited. Escape table pipes with a backslash. The tool checks local targets and heading anchors without network requests; external destinations and evidence contents are not verified. Jira columns have an additional format check, but issue existence, type, status, reciprocal references and story coverage require manual review. Fictional examples in descriptive tables do not create audited Jira associations.

Jira cells on declared entity rows are also inspected before inline-code masking, so a key placed in backticks is rejected rather than treated as an empty field.

Explicit `References` and `Decomposition` columns declare generic architecture references and promises of decomposition. The auditor cannot infer unstated relationships from prose, determine missing engineering requirements, verify source currency, parse/render Mermaid, certify cryptography, or confirm physical isolation. A clean report is evidence of documentation consistency within this declared scope.

Implementation records additionally declare typed `Requirement IDs`, `Test IDs` and `Evidence IDs` associations; acceptance records declare `Implementation IDs`. These are scoped reference checks, not changes to engineering ancestry. The checks do not judge evidence authenticity, test sufficiency, the completeness of recorded scope, tolerable operational impact or the customer's authority to accept the stated SOW outcome. They do not grant acceptance or calculate ZTA completion percentages.
