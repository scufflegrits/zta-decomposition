---
schema_version: 1
id: DOC-ZTA-RESTRUCTURE-R100
title: Numbered directory restructure working plan
document_type: backlog
parent: ROOT
lineage: [ROOT]
owner: Documentation Engineering
owner_status: proposed
document_status: superseded
implementation_status: not-applicable
baseline_date: '2026-10-30'
---

# Numbered directory restructure working plan

## Objective and current scope

Introduce numeric prefixes on all maintained project directories, including nested directories, so the filesystem is easier to browse and reference. Preserve document filenames, engineering identifiers, declared ancestry, technical meaning and source provenance.

This document plans the migration. Creating it does not execute directory moves. The numbering and exceptions below are proposals for discussion before implementation.

## Proposed numbering convention

Use `NNN_name`: three digits, an underscore and the existing directory name. Start at `010` and normally increment by ten among siblings. Restart numbering under each parent. A directory is referenced by its full path, such as `020_architecture/010_decisions`; its prefix alone is not globally unique.

The request illustrated `10_acceptance` and `20_architecture`. Three digits preserve that ordering as `010_acceptance` and `020_architecture` and accommodate the current eleven top-level directories without the lexical sorting problem where `100_tests` would precede `20_architecture`. Two-digit prefixes with smaller gaps remain an alternative if matching the example exactly is preferred.

Retain the current alphabetical order at each level for the initial migration. The numbers establish navigation order; they do not indicate engineering ancestry, implementation priority or ZTA maturity. Do not renumber existing siblings simply to insert a directory later: use an available number in the gap. Adopt the same convention for future maintained directories. Revisit width or gap exhaustion explicitly before another migration.

## Complete directory mapping

| Current path | Proposed path |
|---|---|
| `acceptance/` | `010_acceptance/` |
| `architecture/` | `020_architecture/` |
| `architecture/decisions/` | `020_architecture/010_decisions/` |
| `controls/` | `030_controls/` |
| `controls/identity-authentication/` | `030_controls/010_identity-authentication/` |
| `controls/macsec/` | `030_controls/020_macsec/` |
| `controls/management-isolation/` | `030_controls/030_management-isolation/` |
| `controls/network-segmentation/` | `030_controls/040_network-segmentation/` |
| `images/` | `040_images/` |
| `implementation/` | `050_implementation/` |
| `pillars/` | `060_pillars/` |
| `procurement/` | `070_procurement/` |
| `references/` | `080_references/` |
| `references/guides/` | `080_references/010_guides/` |
| `standards/` | `090_standards/` |
| `tests/` | `100_tests/` |
| `tools/` | `110_tools/` |

Target tree, showing directories only:

```text
.
├── 010_acceptance
├── 020_architecture
│   └── 010_decisions
├── 030_controls
│   ├── 010_identity-authentication
│   ├── 020_macsec
│   ├── 030_management-isolation
│   └── 040_network-segmentation
├── 040_images
├── 050_implementation
├── 060_pillars
├── 070_procurement
├── 080_references
│   └── 010_guides
├── 090_standards
├── 100_tests
└── 110_tools
```

## Scope boundaries

- Number maintained project directories, including assets, tooling and tests.
- Keep root files in place, including this plan, README, index, taxonomy, package manifests, requirements and audit configuration. Moving root documents into new folders is a separate change.
- Preserve document, table, pillar, control, requirement, test, evidence, implementation and acceptance IDs. Preserve `parent`, `lineage` and `document_type` values: a directory rename does not change semantic relationships.
- Leave `.git`, `.agents`, `.codex`, `.aws`, dependency directories such as `node_modules`, virtual environments and caches such as `__pycache__` under their conventional names. Include their descendants in this exception. They are repository infrastructure, environment data or generated dependencies.
- Retain supplied source imports byte for byte when moving them. Historical path strings inside these imports may remain; distinguish them from active references during the stale-path review.
- Keep existing image bytes intact. Update embedding paths. Render again only if an embedded diagram itself must change, following the project diagram standard.
- Do not create unnumbered compatibility copies or symlinks. Retain this old-to-new mapping for manual repair of external bookmarks, Jira and Confluence links. External service edits are outside this local migration.

## Dependencies and implementation decisions

### Links, commands and exclusions

Update active relative Markdown links, image destinations, reference-style link definitions, inline path examples, shell commands, directory inventories and any directory names inside maintained diagrams. Resolve each existing link from its original source location, map both source and target, then calculate the new relative destination. Preserve fragments and existing escaping. Process nested mappings before broader parent mappings where textual replacement is needed; avoid unrestricted word replacement.

Change the import exclusion in `audit-config.json` from `references/guides/*.md` to `080_references/010_guides/*.md`. Keep the original handoff and generated-report exclusions. Check ignore rules and scripts for affected paths rather than renaming excluded environment directories.

Update the index generator's commands, static links and stale-index diagnostic. Regenerate `index.md` after source changes; do not hand-maintain its generated body. Update the README layout, HOW-TO-USE commands, taxonomy locations, tooling guide and documentation conventions.

### Python imports and execution

The tests currently use imports such as `from tools.audit_zta import audit`. A literal replacement with `from 110_tools.audit_zta import audit` is invalid Python syntax.

Proposed approach: keep the tool modules together in `110_tools/`. In test setup, resolve that directory from the repository location and prepend it to the Python import search path before importing `audit_zta`, `document_metadata` and `generate_index` by their existing module names. Update the subprocess test's explicit script path. The scripts already support direct execution with sibling imports; verify those paths after the move. Use unittest discovery with an explicit numbered test directory.

Avoid creating a separate package, adding dependencies or retaining an unnumbered `tools` alias solely for this migration. If other consumers of package-style imports are discovered, review them before choosing the final import approach.

### Existing test failures

The October 30 assessment found a current index and a clean documentation audit, with 68 of 70 unit tests passing. The two failures are `test_index_generation_and_freshness` and `test_index_updates_after_move_and_escapes_labels`: generated index prose includes three Mermaid-guide links absent from their temporary fixture repositories.

Reproduce this baseline before migration. Repair the fixtures to provide the intended linked resources, or adjust generator behavior if review establishes those links should be conditional. Prefer the smallest correction consistent with the generator's documented contract. Keep this correction distinguishable in the diff; do not weaken link checking or exclude failing tests. Require the entire suite to pass at completion.

## Implementation sequence

1. Settle the draft choices below. Capture repository status and identify any unrelated edits to preserve. Inventory tracked and relevant untracked project files, hidden project directories, links and automation; reconcile the mapping before moving anything.
2. Record the baseline: index freshness, audit results and test results. Resolve the known fixture failures as described above. Record image/source-import checksums and existing metadata/ID relationships for post-move comparison.
3. Prepare one explicit old-to-new path mapping and check for destination collisions, missing sources and unmanaged files. Include each nested directory. Work on a dedicated branch and leave unrelated edits intact.
4. Move maintained directories, then their children using the new parent paths. Update active references, configuration, Python imports, subprocess paths and executable command examples in the same migration. Apply the mapping once to avoid double-prefixing paths.
5. Update the directory naming rule in the documentation conventions. Update this plan's progress while retaining the mapping as migration history. Regenerate the document index.
6. Run the validation below. Review every remaining old-path match: permit this plan's mapping, historical source content and intentional isolated fixtures only when justified. Repair active references, including those in code fences that the documentation auditor intentionally ignores.
7. Review the complete diff and rename summary for accidental content changes. Prepare the migration for review with its verification results and external-link follow-up list. Commit or publish only under the applicable working agreement; this planning request does not require either action.

## Validation and completion criteria

Run these commands from the repository root after migration:

```bash
python3 110_tools/generate_index.py --root .
python3 110_tools/generate_index.py --root . --check
python3 110_tools/audit_zta.py --root . --report audit-report.md
python3 -m unittest discover -s 100_tests -v
git diff --check
git diff --stat
git diff --summary
```

- Every maintained directory and descendant follows the agreed numeric convention. Only the documented infrastructure/environment exceptions remain unnumbered. No old maintained directory remains populated.
- The auditor exits successfully and the generated index is current. The new plan is a managed document with valid metadata and appears in the index.
- All unit tests pass, including direct CLI/subprocess execution and index freshness/link tests. Add or adapt a focused check proving numbered tool-directory imports and the moved guide exclusions work; retain malformed-document and broken-link coverage.
- Active local links and image embeds resolve. Review command examples and diagram labels separately because the auditor does not interpret code fences or Mermaid. Validate edited Mermaid blocks under the existing diagram standard if diagram content changes.
- Document and entity IDs, ancestry, scope and technical statuses match the pre-migration baseline, except for explicitly reviewed corrections. Source imports and images match their recorded checksums.
- Review remaining old paths and document intentional historical/fixture occurrences. Inventory known external references for their owners to update; do not claim external bookmarks or Jira/Confluence links were verified by the local audit.
- The diff contains the intended renames, reference/import/configuration changes, naming documentation and generated index updates. No dependency churn, security configuration changes or unrelated rewrites occur.

## Recovery

Use the pre-migration commit and explicit path mapping as recovery references. Before committing, reverse the mapped moves and restore only migration-owned edits if needed, preserving unrelated work. After committing, prepare a normal revert of the migration commit for review. Avoid broad resets or deletion-based cleanup. Retain the baseline records needed to compare a retry.

## Decisions to settle and progress

| Choice | Proposed default | State |
|---|---|---|
| Prefix width | Three digits, `010`, `020`, etc. | Draft |
| Initial sibling order | Current alphabetical order | Draft |
| Scope of “all directories” | All maintained directories; conventional infrastructure/environment exceptions above | Draft |
| Root files | Keep existing filenames and locations | Draft |
| Tool imports | Explicit resolved tool path for test imports; direct script execution | Draft |
| Old paths | Mapping retained; no compatibility aliases | Draft |

- [x] Inspect the current layout and path-sensitive tooling.
- [x] Save this working plan with a complete proposed mapping.
- [ ] Settle the proposed choices.
- [ ] Capture baseline and repair the two existing test failures.
- [ ] Execute directory moves and update references/tooling.
- [ ] Complete validation and review the migration diff.
