---
schema_version: 1
id: DOC-ZTA-RESTRUCTURE-REVISION-LOG
title: Numbered directory restructure revision log
document_type: backlog
parent: ROOT
lineage: [ROOT]
owner: Documentation Engineering
owner_status: proposed
document_status: in-review
implementation_status: not-applicable
baseline_date: '2026-10-30'
---

# Numbered directory restructure revision log

Rationale for each revision of the numbered directory restructure instructions. The canonical instruction holds only what to do; this log holds why it changed. Entries are append-only: add a new section for each revision and do not rewrite earlier ones.

This log is a historical record. The migration does not rewrite paths inside it, and the stale-path review excludes it. It links only to sibling snapshot files that move with it into `900_project-admin/`. It deliberately does not link the r1.0.0 file or the canonical instruction, because the filename `request-restructure.md` changes from one to the other during the migration.

## Revision summary

| Revision | Kind | Snapshot | Summary |
|---|---|---|---|
| r1.0.0 | Plan | r1.0.0 snapshot (`request-restructure.md` before migration) | Original working plan: three-digit numbering, complete directory mapping, scope boundaries, Python import approach, known test failures. |
| r1.0.1 | Plan | [r1.0.1](request-restructure-r1.0.1.md) | Added `000_import/` staging, machine-readable mapping, lockfile exclusion, stale-path command, shared test helper. Rationale in that file's Revision Notes. |
| r1.0.2 | Plan | [r1.0.2](request-restructure-r1.0.2.md) | Added `900_project-admin/` and reserved prefix ranges; moved `TODO.md` and the plan. Rationale in that file's Revision Notes. |
| r1.0.3 | Review | [r1.0.3](request-restructure-r1.0.3.md) | Review of r1.0.2: actual branch and migration base, preservation of untracked revisions, single passing migration commit, declarative mapping semantics, import trust model, narrowed audit exceptions. |
| r1.0.4 | Instructions | [r1.0.4](request-restructure-r1.0.4.md) | Rewrote the plan as implementation instructions, adopting most r1.0.3 recommendations. No rationale recorded in the file. |
| r1.0.5 | Instructions | [r1.0.5](request-restructure-r1.0.5.md) | Corrected type and approval status, fixed planning-record IDs, defined the three commits, scoped the migration script, added the execution record. Rationale and r1.0.3 disposition in that file's Revision Notes. |
| r1.0.6 | Instructions | [r1.0.6](request-restructure-r1.0.6.md) | Fixed the stale-path pattern, kept active admin documents in the scan, added a field-level metadata inventory. Removed revision notes from the canonical document. Rationale reconstructed below. |
| r1.0.7 | Instructions | Canonical | Moved rationale to this log, restored the revision number, replaced the metadata inventory with an auditor-based comparison. Rationale below. |

## r1.0.6 (2026-10-30)

r1.0.6 recorded no rationale of its own. The entries below are reconstructed from its differences from r1.0.5 and from the review discussion that followed.

| # | Change | Rationale |
|---|---|---|
| 1 | Stale-path boundary changed from `[^A-Za-z0-9_/-]` to `[^A-Za-z0-9_-]`. | r1.0.5's boundary excluded `/`, so parent-relative links such as `../architecture/overview.md`, the main thing the scan exists to find, never matched. Excluding `_` still prevents numbered components such as `080_references/` from matching. |
| 2 | File list built with `git ls-files -z --cached --others --exclude-standard` and `xargs -0 -r`. | Handles filenames containing spaces and an empty file list. |
| 3 | Stale-path exclusions narrowed to version-named snapshots and exact artifact files. | r1.0.5 excluded everything matching `900_project-admin/(request-\|restructure)`, which also hid the canonical instruction and the execution record from the scan. |
| 4 | Added `restructure-baseline-metadata.json` with original and migration-base inventories and a field-level comparison. | r1.0.5 asked for a metadata comparison without a checkable method. |
| 5 | Added r1.0.5 as a snapshot (`DOC-ZTA-RESTRUCTURE-R105`). | r1.0.6 became canonical. |
| 6 | Removed the revision line and Revision Notes from the canonical document. | Intended to keep the canonical document operational, with history in the snapshots. In practice this left r1.0.6's own changes unexplained and the document unable to state its revision; corrected in r1.0.7. |

## r1.0.7 (2026-10-30)

Review of r1.0.6 against the auditor's data model and the earlier revisions. r1.0.6 content is retained except where a row below changes it.

| # | Change | Rationale |
|---|---|---|
| 1 | Created this revision log as the single home for revision rationale, and listed it in the planning-records table with its own ID. | r1.0.6 removed rationale from the canonical document so that it stays operational. That intent is kept, but its own changes then had nowhere to be recorded. A separate append-only log keeps the instruction focused and the history complete. |
| 2 | Restored a revision line in the canonical document body, and the rule that each future revision updates it. | After the move, the canonical file is named `request-restructure.md` and nothing else states its revision. The approval record asks for "Approved revision". Frontmatter cannot carry a revision because `document_metadata.py` accepts only a fixed set of fields. |
| 3 | The revision log is treated like the snapshots: no reference rewrite, excluded from the stale-path scan, links only to sibling snapshot files. | Its rationale necessarily quotes old paths; rewriting them would falsify the record. Avoiding a link to `request-restructure.md` prevents a link that would silently retarget from r1.0.0 to the canonical instruction when the files move. |
| 4 | Replaced the JSON metadata inventory with an inventory dumped from `audit_zta.audit()`, compared with `diff` after path mapping and link normalization. | r1.0.6 specified a `scope` field that does not exist in frontmatter (in the auditor, scope is a check, not a value), and kinds ("document, table or traceable row") that differ from the auditor's `doc`, `table`, `Pillar ID`, `Control ID` and so on. A second parser written to a prose spec can disagree with the auditor about what a row is. Reusing the auditor's parser removes that risk, and resolving link targets to repository paths before comparing turns r1.0.6's separate "expected rewrite" calculation into an ordinary equality check. Recorded as a decision in the approval record so it can be replaced before approval. |
| 5 | Dropped the separate pre-correction ("original") inventory. The preparation commit is verified by reviewing its diff against the preservation commit. | The preservation commit already contains the original files byte for byte. A diff of the next commit shows exactly what changed, which is a more direct check than comparing two inventories, and removes the problem of where to store an inventory captured before `900_project-admin/` exists. |
| 6 | Stale-path matches may be classified by section, for example the canonical mapping table. | The canonical instruction contains about 30 intentional old paths. Requiring a per-line reason for each adds clerical work without catching anything more. |
| 7 | Replaced fixed counts ("seven planning files", "six snapshots") with references to the table. | Each new revision made the counts wrong in three places. |
| 8 | Added r1.0.6 as a snapshot (`DOC-ZTA-RESTRUCTURE-R106`). | r1.0.7 becomes canonical. |
| 9 | Added the comparison method to the approval record. | The approver should explicitly confirm the simplified method, or replace it, before execution. |
