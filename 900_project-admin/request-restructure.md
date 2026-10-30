---
schema_version: 1
id: DOC-ZTA-REQUEST-RESTRUCTURE
title: Numbered directory restructure implementation instructions
document_type: backlog
parent: ROOT
lineage: [ROOT]
owner: Documentation Engineering
owner_status: proposed
document_status: approved
implementation_status: not-applicable
baseline_date: '2026-10-30'
---

# Numbered directory restructure implementation instructions

Revision r1.0.7. The rationale for this and earlier revisions is kept in the [restructure revision log](restructure-revision-log.md), not in this document.

## Authority and outcome

Once approved (see [Approval record](#approval-record)), these are the authoritative instructions for restructuring this repository. Apply them when executing the migration. Creating this instruction document does not itself execute moves, create commits or publish changes.

Number all maintained project directories and their descendants. Establish an import inbox and a project administration directory. Preserve technical meaning, engineering identifiers, semantic ancestry, evidence relationships and source provenance. Complete the migration with passing checks and a reviewable diff.

This is a one-time migration instruction, so it is a `backlog` document kept in `900_project-admin/`. Standing rules that outlive the migration (directory naming, administration scope, import handling) are written into `090_standards/documentation-conventions.md` as part of the migration; that document, not this one, governs future work.

## Approval record

| Field | Value |
|---|---|
| Approved by | scufflegrits |
| Approval date | 2026-10-30 |
| Approved revision | r1.0.7 |
| Metadata comparison method | Waived; see simplified execution |

**Simplified execution.** The owner directed a lighter execution than this document describes. The migration is validated by the existing auditor (links, IDs, ancestry, scope), index freshness check, full unit suite and the stale-path review. The inventory comparison, checksum file, committed migration script and execution record are not produced. Where later sections require those artifacts, this paragraph takes precedence. The mapping, naming, planning-record, import and administration rules apply unchanged.

Do not begin execution until this table is filled in. When it is, set `document_status: approved` in this document's frontmatter, and set `owner_status: accepted` if Documentation Engineering has accepted ownership. Approval happens before the preparation commit, so the approved status is already part of the migration base.

## Directory naming

Use `NNN_name`: three digits, an underscore and the descriptive directory name. Restart numbering under each parent. Allocate content directories in increments of ten initially; use available gaps for later additions without renumbering existing directories. Initial sibling order is alphabetical; subsequent additions do not have to preserve alphabetical order.

| Root prefix range | Purpose |
|---|---|
| `000` | Import staging |
| `010`–`899` | Maintained content, assets, tests and tools |
| `900`–`999` | Project administration |

Reserve `000` and `900`–`999` for use at the root. Below the root, use content prefixes beginning at `010`. Refer to directories by their full paths, because sibling prefixes are not globally unique. Numbers express navigation order, not engineering ancestry, delivery priority or security maturity.

The content range provides 89 default-step positions, of which the initial eleven content directories occupy eleven. Additional numbers between those positions remain available.

## Required directory mapping

| Existing directory | Final directory |
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

Create `000_import/` and `900_project-admin/` as new directories.

Move `TODO.md` to `900_project-admin/TODO.md`. Keep the README, index, taxonomy, HOW-TO-USE, ZTA guides, original handoff, audit configuration, package manifests and requirements at the root. Keep standing documentation rules under `090_standards/`. The administration directory holds backlogs, plans, mapping files, execution records, revision logs, import logs and project review records; it must not become a second home for engineering definitions or standards.

## Planning records

Inventory every file in the table below before execution and preserve its original bytes. Resolve duplicate IDs and final locations exactly as listed.

| Current file | Final path | Final ID | Final `document_status` |
|---|---|---|---|
| `request-restructure.md` | `900_project-admin/request-restructure-r1.0.0.md` | `DOC-ZTA-RESTRUCTURE-R100` | `superseded` |
| `request-restructure-r1.0.1.md` | `900_project-admin/request-restructure-r1.0.1.md` | `DOC-ZTA-RESTRUCTURE-R101` | `superseded` |
| `request-restructure-r1.0.2.md` | `900_project-admin/request-restructure-r1.0.2.md` | `DOC-ZTA-RESTRUCTURE-R102` | `superseded` |
| `request-restructure-r1.0.3.md` | `900_project-admin/request-restructure-r1.0.3.md` | `DOC-ZTA-RESTRUCTURE-REVIEW-R103` (unchanged) | `superseded` |
| `request-restructure-r1.0.4.md` | `900_project-admin/request-restructure-r1.0.4.md` | `DOC-ZTA-RESTRUCTURE-INSTRUCTIONS` (unchanged) | `superseded` |
| `request-restructure-r1.0.5.md` | `900_project-admin/request-restructure-r1.0.5.md` | `DOC-ZTA-RESTRUCTURE-R105` | `superseded` |
| `request-restructure-r1.0.6.md` | `900_project-admin/request-restructure-r1.0.6.md` | `DOC-ZTA-RESTRUCTURE-R106` | `superseded` |
| `request-restructure-r1.0.7.md` (this document) | `900_project-admin/request-restructure.md` | `DOC-ZTA-REQUEST-RESTRUCTURE` (unchanged) | `approved` once the approval record is complete |
| `restructure-revision-log.md` | `900_project-admin/restructure-revision-log.md` | `DOC-ZTA-RESTRUCTURE-REVISION-LOG` (unchanged) | unchanged |

Rules for these records:

- The canonical instruction always lives at `900_project-admin/request-restructure.md` and keeps `DOC-ZTA-REQUEST-RESTRUCTURE`. It states its own revision number in its first paragraph. Historical records are snapshots named `request-restructure-rX.Y.Z.md`. Apply the listed filename mappings to avoid a collision with the canonical filename.
- Change only the `id` and `document_status` frontmatter fields of a snapshot. Do not edit snapshot bodies.
- The revision log is the single place for revision rationale. It is append-only history: add entries, never rewrite earlier ones.
- Snapshots and the revision log are historical records. The migration's reference rewrite skips them and the stale-path review excludes them; old paths inside them are expected. Their only links point to sibling planning files that move together into `900_project-admin/`, so those links stay valid without rewriting. The log does not link to `request-restructure.md`, because that filename changes meaning during the migration.
- Commit every file in the table unmodified in a preservation commit before any metadata change (see [Baseline and Git workflow](#baseline-and-git-workflow)).
- A future revision follows the same pattern: the old canonical becomes a numbered snapshot with a new unique ID and `superseded` status, the new revision takes the canonical path and ID and updates its revision number, and the rationale is appended to the revision log.
- No subdirectory is created for snapshots while there are fewer than about ten. If one is added later, it takes a numbered name under `900_project-admin/` and is added to the mapping.

## Exceptions and preservation

- Leave `.git`, `.agents`, `.codex`, `.aws`, dependency directories, virtual environments and caches under their conventional names. Their descendants are also exempt. This includes `node_modules`, `.venv`, `venv` and `__pycache__`.
- Exempt transient batch directories and supplied subdirectories inside `000_import/` from numeric naming.
- Preserve filenames except for the renames listed in [Planning records](#planning-records) or a documented collision resolution.
- Preserve document and entity IDs, `parent`, `lineage`, `document_type`, technical status and scope. The planning-record ID and status changes above are the only permitted metadata corrections; do not change engineering IDs to make the migration pass.
- Preserve the original planning files in a local preservation commit before metadata correction. Include only the planning files and intended existing edits, and preserve unrelated work. Do not delete an untracked file on the assumption that Git already retains it.
- Preserve supplied source imports and image bytes. Historical paths inside verbatim sources and planning records may remain. Update active embedding links and maintained instructions.
- Leave `package.json` and `package-lock.json` unchanged. Package-owned paths inside them, such as `"tests/types"`, are not migration targets.
- Do not create old-path compatibility copies or symlinks. Record known external bookmarks and Jira/Confluence references for their owners; external service edits are outside this migration.

## Baseline and Git workflow

Inventory the actual working tree before any move. Record the current branch, upstream, commit, tracked and relevant untracked files, existing changes and ownership of those changes. Do not assume a branch named `main`: when this revision was written, the local branch was `master`, tracking `main/master`, where `main` is the remote name. Recheck these facts at execution.

Create a dedicated work branch, then make these commits in order:

1. **Preservation commit.** Add every planning-record file exactly as it is. This commit records history; it is not expected to pass the audit, because it still contains duplicate IDs. Do not include the pre-existing `index.md` modification, which is regenerated in the next commit.
2. **Preparation commit.** Apply the planning-record ID and status corrections. Repair the two known index-test fixtures: the generated index links three Mermaid guides that the temporary test repositories do not contain. Supply the intended fixture resources unless review establishes that the generator contract requires conditional links. Do not weaken link validation or skip failing tests. Regenerate `index.md`. The audit, index freshness check and full unit suite must all pass at this commit. Record its hash as the migration base.
3. **Migration commit.** Directory and file moves, reference rewrites, import changes, configuration, documentation, the execution record and index updates, all in one passing commit. Git infers renames from similarity; `git mv` does not require a separate rename-only commit.

Verify the preparation commit by reviewing `git diff <preservation-commit> <migration-base-commit>`: it may contain only the planning-record `id`/`document_status` lines, the fixture repair and the regenerated `index.md`. Record the review result in the execution record. No separate pre-correction inventory is needed; the preservation commit itself is that record.

Review and commit only intended files. Publishing, pushing, merging and external application updates require the applicable working agreement and are not required to complete the local restructure.

## Mapping and move execution

Write `900_project-admin/restructure-map.tsv` as UTF-8, with a header `old_path` and `new_path` separated by a tab. Each row contains two repository-relative paths using `/`. Directory paths end in `/`; file paths do not. Do not include absolute paths, `..` components, duplicate sources or conflicting targets. List nested directory associations before parent associations for readability. Include `TODO.md` and every planning-record file move.

Represent new directories as creation actions in the execution record, not rows with invented old paths.

Use the mapping consistently for moves, reference translation, inventory comparison and stale-path review. Translation rules are:

1. Prefer an exact file mapping.
2. Otherwise use the longest matching directory prefix at a path-component boundary.
3. Translate each original path once. Never pass a translated path through the mapping again.
4. Resolve each relative link from its original source location, map source and destination, and calculate the new relative link. Preserve heading fragments, encoding and supported escaping.

Do not rewrite references inside planning snapshots, the revision log, verbatim source imports or `restructure-map.tsv`.

Derive a filesystem move sequence separately from the declarative mapping. When moving parents first, resolve child source locations under their already-moved parents. Do not execute TSV rows directly as shell moves.

Produce a dry-run report of directory creation, moves and reference edits. Check missing sources, unmanaged files, existing destinations and case-only collisions before mutation. Never overwrite a destination automatically. On retry, recognize completed operations or stop with a diagnostic; do not double-prefix names or silently replace files.

### Migration script

The script that performs the dry run, moves, reference rewrite and inventory comparison is a one-time execution artifact, not a maintained tool.

- Commit it as `900_project-admin/restructure_migrate.py` in the migration commit so reviewers can see exactly what ran. Do not place it in `110_tools/`, document it in the tooling guide, or maintain it after the migration.
- Its checks (exact-file and nested-directory mapping, one-time translation, moved relative links with fragments, collision rejection, safe retry, link normalization in the inventory, and the stale-path scanner cases listed under [Validation and completion](#validation-and-completion)) run as a built-in self-test, for example `python3 900_project-admin/restructure_migrate.py --self-test`, before the real run. They are not added to `100_tests/` and do not run in the permanent suite.
- Record the self-test output and the dry-run report summary in the execution record.

### Metadata and byte comparison

The comparison reuses the project auditor's own parser. `audit_zta.audit()` already reads every managed document's frontmatter and every declared table and traceable row (`Entity` records with `id`, `parent`, `kind`, `lineage` and `cells`). The migration script dumps that parsed result to a flat inventory; it does not implement a second parser.

1. **Base inventory.** At the migration base, run the script's inventory mode, which calls `audit()` on the repository and writes `900_project-admin/restructure-inventory-base.tsv`. One line per document and per entity, tab-separated, with columns `path`, `kind`, `id`, `parent`, `lineage` and `fields`. For a document, `fields` holds every frontmatter field; for a table or row entity, it holds every parsed cell. Fields are written as sorted `key=value` pairs. Before writing, the script normalizes every Markdown link destination inside a field to the repository-relative path it resolves to from that file, then translates both `path` and those resolved targets through the mapping. Lines are sorted by `kind`, `id`, `path`.
2. **Final inventory.** After the moves and rewrites, run the same mode to write `900_project-admin/restructure-inventory-final.tsv`, normalizing link destinations the same way (no mapping step, since paths are already final).
3. **Compare.** `diff restructure-inventory-base.tsv restructure-inventory-final.tsv`. Because both sides use final paths and resolved link targets, a relative link that was correctly rewritten produces no difference, while a changed ID, parent, lineage, status or other cell value does.
4. **Expected differences.** The only permitted differences are the added lines for new managed documents created by the migration (the execution record and the import log). List them in the execution record before running the diff. Any other difference, such as a reviewed inline path example inside a cell, is either fixed or recorded with its reason. Unexplained differences fail completion.

Write `900_project-admin/restructure-baseline-checksums.tsv` at the migration base with a tab-separated header `source_path`, `size_bytes`, `sha256` for preserved source imports and images. Compare their bytes at mapped final paths.

These inventories, the checksum file and the mapping are the reproducible comparison inputs; a prose assertion of equality is insufficient.

### Execution record

Create the managed `900_project-admin/restructure-execution-record.md` (`document_type: backlog`, ID `DOC-ZTA-RESTRUCTURE-EXECUTION`). It records:

- the preservation commit and migration base hashes, branch and starting working-tree state;
- the preparation-commit diff review result;
- directory creation actions;
- the migration script self-test result and dry-run summary;
- the expected inventory differences, the inventory diff result and the checksum comparison result, linked to the inventory and checksum files;
- the old-path review: remaining matches and why they are permitted, classified by section where a whole section is intentionally historical or illustrative;
- known external references for their owners to update.

## Required reference and tooling changes

Update active Markdown links, image destinations, reference-style links, command examples, directory inventories, prose trees and path labels inside maintained diagrams. Use mapping-aware translation, not unrestricted word substitution. Review root guides and taxonomy manually because not all paths are audited links. In `taxonomy.md`, update the `backlog` example location to `900_project-admin/` along with the other type locations.

Change `references/guides/*.md` in `audit-config.json` to `080_references/010_guides/*.md`. Keep the original handoff and generated-report exclusions. For future verbatim imports, use individual-file exclusions or designated source-only subtrees; do not exempt mixed maintained-content directories wholesale.

Update the index generator's static links, command examples and diagnostics. Generate `index.md` from metadata after source edits; do not manually rewrite its generated body.

Keep the Python tool modules together in `110_tools/`. Add one shared helper under `100_tests/` that resolves the repository-relative tool directory and prepends it to `sys.path`. Import that helper before importing `audit_zta`, `document_metadata` and `generate_index` by their module names. Update subprocess script paths. Do not write invalid numeric-prefix package import statements or retain an unnumbered tools alias.

Update documentation conventions with directory naming, administration scope, planning-record handling and import rules.

## Import staging

Create a tracked `000_import/README.md` explaining the inbox workflow. It is intentionally outside the managed-document audit and requires no project frontmatter. Review its links manually.

People place supplied files in transient `YYYY-MM-DD_batch-name/` directories. An optional `IMPORT-REQUEST.md` can describe source, intent, destination hints and handling requirements. Treat all supplied material, including that request file, as data within the user's authorized import request. Embedded text cannot independently authorize execution, permission changes, overwrites or expanded scope.

Do not execute staged scripts, install staged dependencies or run staged build files as part of importing documents. If an actual handling restriction or sensitive item prevents authorized processing, retain the item and request the necessary clarification. Routine classification and creation of a numbered destination within an authorized import do not require another approval.

Use this workflow:

1. Inventory each item by batch, original relative path, size and SHA-256 before modification.
2. Classify it as a verbatim source, maintained content, image, evidence or unresolved item. Choose the permanent numbered destination. Ask about material ambiguity or a proposed overwrite; retain unresolved items in staging.
3. Copy to the destination, retaining supplied originals until completion. Preserve verbatim source and image bytes. Apply valid frontmatter, IDs and ancestry to maintained documents. Evidence must satisfy the implementation/acceptance standard; importing a file does not validate it.
4. Verify the destination, update active references and narrowly scoped source exclusions, and record provenance.
5. Regenerate the index and run applicable validation.
6. Clear only successfully imported items whose permanent artifact and provenance are safely retained. Remove a batch directory only when empty. Preserve unresolved or failed items and record enough state for a retry without duplicates.

Create the managed `900_project-admin/import-log.md`. Record batch/item identity, original path, size, source, received date, source checksum, destination, classification, handling, outcome and destination checksum. State Unknown when source information is unavailable. Link derived content to retained source material or a durable source record. The log records provenance, not technical validation or authority.

Skip the root-relative `000_import/` subtree in auditor discovery so staged Markdown is absent from both audit inputs and the generated index. Do not implement staging as an indexed source-import exclusion. Do not accidentally suppress a nested directory with the same name. Do not claim that filtering discovered paths prunes filesystem traversal. Add a permanent unit test for this behavior in `100_tests/`; unlike the migration script's checks, it guards a lasting feature.

Add these Git ignore rules:

```gitignore
/000_import/*
!/000_import/README.md
```

Ordinary Git add operations then ignore staged content. Ignore rules do not protect already tracked files or prevent forced adds. Verify with `git check-ignore` and `git ls-files -- 000_import/`; only the README may be tracked. Use a temporary non-sensitive sample for this check and remove only that sample afterward.

## Execution sequence

1. Confirm the approval record is complete. Inventory and preserve existing work, create the work branch and make the preservation commit. Make the passing preparation commit, review its diff against the preservation commit, and record its hash as the migration base.
2. Create the administration directory, mapping, execution record and migration script. Run the script's self-test. Write the base inventory and checksum file. Run the dry run and resolve collisions before moving anything.
3. Move maintained directories, `TODO.md` and the planning records. Update active references, Python imports, subprocess paths, configuration and command examples as one working change.
4. Add staging behavior, its README and ignore rules, the import log, standing documentation rules and the staging unit test.
5. Regenerate the document index. Write the final inventory, run the inventory diff and checksum comparison, and run all completion checks.
6. Review the complete migration diff against the recorded base, including staged and unstaged changes. Complete the execution record and prepare one passing migration commit.

## Validation and completion

From the repository root, run:

```bash
python3 110_tools/generate_index.py --root .
python3 110_tools/generate_index.py --root . --check
python3 110_tools/audit_zta.py --root . --report audit-report.md
python3 -m unittest discover -s 100_tests -v
git diff --check
git diff --cached --check
git status --short
```

Stale-path review covers tracked and untracked non-ignored project files. Use null-delimited filenames throughout. Exclude only the staging subtree, the package manifests, the migration artifacts, and the historical planning records (version-named snapshots and the revision log). The canonical instruction, execution record, import log and other active administration documents remain in scope.

```bash
git ls-files -z --cached --others --exclude-standard \
  | grep -zvE '^(000_import/|package(-lock)?\.json$|900_project-admin/(request-restructure-r[0-9]+\.[0-9]+\.[0-9]+\.md|restructure-revision-log\.md|restructure-map\.tsv|restructure_migrate\.py|restructure-inventory-(base|final)\.tsv|restructure-baseline-checksums\.tsv)$)' \
  | xargs -0 -r grep -InE -- '(^|[^A-Za-z0-9_-])(acceptance|architecture|controls|images|implementation|pillars|procurement|references|standards|tests|tools)/|(^|[^A-Za-z0-9_-])TODO\.md'
```

The boundary deliberately permits `/`, so `../architecture/overview.md`, `../../controls/macsec/overview.md` and `../TODO.md` are detected. It excludes `_`, digits and hyphens, so numbered directory components do not match their unnumbered suffixes. A `TODO.md` occurrence is a review candidate even when correctly located; resolve it from its source location.

Classify every returned match. Where a whole section is intentionally historical or illustrative, such as this document's [Required directory mapping](#required-directory-mapping) table and old-path examples, classify the section once with its file, line range and reason. Classify other matches individually. Check any ignored but relevant project-owned files separately against the execution inventory. No matches is a normal outcome; distinguish grep's no-match status from command/read failures. The migration script's self-test includes scanner cases for parent-relative links, numbered paths, filenames containing spaces, and confirmation that active administration documents are scanned.

Review committed migration changes with the recorded full baseline commit hash in place of `<migration-base-commit>`:

```bash
git diff --check <migration-base-commit> HEAD
git diff --stat <migration-base-commit> HEAD
git diff --summary -M <migration-base-commit> HEAD
```

Before committing, also review staged and unstaged content; a comparison of commits alone cannot show it.

Completion requires all of the following:

- The approval record is complete and this document's status is `approved`.
- All maintained directories follow the numbering convention; only documented infrastructure and staging exceptions remain. No old maintained directory remains populated.
- The canonical instruction is at `900_project-admin/request-restructure.md` with ID `DOC-ZTA-REQUEST-RESTRUCTURE`. `TODO.md` and the revision log are in administration. Every snapshot carries the ID and `superseded` status in [Planning records](#planning-records), with an unchanged body. The audit passes and the index is current.
- The preparation-commit diff contains only the permitted changes.
- The full test suite passes. The migration script's self-test passed and its output is in the execution record.
- Numbered tool imports work through unittest discovery. Direct CLI execution also works with an absolute script path from outside the repository and an explicit repository `--root`.
- Malformed staged Markdown is absent from audit inputs and the index; adding and removing it leaves generated index content unchanged. Moved source exclusions work while neighboring maintained documents are still audited.
- Active links and images resolve. Review command examples, prose trees and diagram path labels manually. Render and visually review edited Mermaid blocks under the project diagram standard.
- The inventory diff shows only the listed expected differences, each other difference being fixed or explained. Preserved source imports and images match the checksum file at mapped final paths.
- Only the inbox README is tracked under staging. Known external-reference changes are recorded without claiming external verification.
- Every stale-path match is either repaired or classified in the execution record.
- The final diff contains the intended migration and additions, with no package dependency churn, security configuration changes or unrelated rewrites.

## Recovery

Retain the migration base, preservation commit, explicit mapping, base inventory, checksums and ownership of edits. Before committing, reverse only migration-owned moves and edits while preserving unrelated and untracked work. After committing, prepare a normal revert of the complete migration commit. Keep the preservation and preparation commits unless there is a separate reason to revert them. Do not use broad resets or deletion-based cleanup as routine recovery.
