---
schema_version: 1
id: DOC-ZTA-RESTRUCTURE-REVIEW-R103
title: Directory restructure r1.0.3 recommendations
document_type: backlog
parent: ROOT
lineage: [ROOT]
owner: Documentation Engineering
owner_status: proposed
document_status: superseded
implementation_status: not-applicable
baseline_date: '2026-10-30'
---

# Directory restructure r1.0.3 recommendations

Review of [request-restructure-r1.0.2.md](request-restructure-r1.0.2.md), checked against the repository on October 30, 2026. This document records recommendations for the next accepted plan. It does not execute the restructure or supersede r1.0.2 automatically.

## Assessment

Keep the proposed three-digit numbering, directory mapping, `000_import/` inbox and `900_project-admin/` scope. They provide a clear distinction between intake, engineering content and project administration. Keep stable engineering IDs, byte-preserved source imports, explicit path mapping and the shared Python test helper.

Before implementation, revise the Git workflow, revision retention and mapping semantics. These changes make the migration reproducible without losing working files or introducing a deliberately broken commit. The import workflow also needs a clearer distinction between requester instructions and supplied material.

## Verified repository baseline

| Observation | Review result |
|---|---|
| Current branch | `master` |
| Remote name | `main`, pointing to the GitHub repository |
| Upstream | `main/master`; local `master` is one commit ahead at review time |
| Existing working changes | Modified `index.md`; untracked `request-restructure.md`, r1.0.1 and r1.0.2 |
| Documentation audit before this review | Two duplicate-ID errors: the three existing plan files share `DOC-ZTA-REQUEST-RESTRUCTURE` |
| Unit tests | 68 of 70 pass; the two previously identified index-fixture failures remain |

The earlier clean audit is historical. The current working tree cannot pass the audit or regenerate its index until the duplicate plan IDs are addressed. This review uses its own document ID so it does not introduce another duplicate.

## Recommendations before implementation

### 1. Use the actual branch and an explicit migration baseline

Replace the hardcoded `main...HEAD` comparisons. In this repository, `main` is the remote name; it is not the current local base branch. Resolve and record the agreed local starting commit after preparing the baseline, then use that commit consistently for the migration diff and recovery record.

Suggested validation commands, with the placeholder replaced by the recorded full commit hash:

```bash
git diff --check <migration-base-commit> HEAD
git diff --stat <migration-base-commit> HEAD
git diff --summary -M <migration-base-commit> HEAD
git diff --check
git status --short
```

The first three inspect committed migration changes; the final two expose outstanding edits. Before committing, review the working-tree and staged diffs as well. Do not assume the remote branch includes the existing local commit.

### 2. Preserve revision files before consolidating them

Replace the instruction to delete all superseded drafts with an explicit preservation step. The current revision files are untracked, so Git history does not yet retain them. Also, `git mv` cannot move an untracked accepted revision without first tracking it.

Recommended policy:

- Keep one canonical working plan at the eventual `900_project-admin/request-restructure.md`, retaining `DOC-ZTA-REQUEST-RESTRUCTURE`.
- Keep requested review documents under distinct document IDs, as this r1.0.3 does. The auditor requires unique IDs, not a single file mentioning this plan.
- Before removing any older revision, record it in Git through the agreed workflow or preserve it at an agreed durable location. Record which revision became canonical.
- If older snapshots remain managed Markdown, give each snapshot a unique ID and mark it superseded where appropriate. Describe these as historical records, not new engineering entities. Adding an archive directory requires adding it to the directory mapping and numbering scheme.
- Do not add a broad auditor exclusion for planning documents merely to suppress duplicate IDs.

The accepted revision and any file-level moves must be identified explicitly in the mapping. Do not assume r1.0.2 or this recommendations document is automatically the accepted plan.

### 3. Commit a complete, passing migration

Keep the pre-existing fixture repair separate if commits are authorized. Make directory moves, reference updates, import changes, configuration updates and index regeneration one coherent migration commit after validation.

`git mv` stages a move; Git later infers renames from file similarity. A separate pure-rename commit is not necessary to preserve history or obtain a useful rename diff. It introduces an intentionally failing intermediate state and complicates rollback and bisecting.

If separate review commits are required by the program, settle that requirement first and document how each commit remains usable. The planning request itself does not require creating branches, commits or pushes now.

### 4. Separate declarative path mapping from move execution

Keep `restructure-map.tsv` as the single source of old-to-final path associations. Specify that it contains repository-relative paths using `/`, no duplicate sources, no conflicting targets and no synthetic source such as an em dash for new directories. Document its encoding, header convention and treatment of directory trailing slashes. Represent new directories as explicit creation actions in the plan, rather than rename rows.

For path translation:

1. Match an exact file mapping first.
2. Otherwise use the longest matching directory prefix at a path-component boundary.
3. Translate each original path exactly once; do not feed a translated result back through the mapping.
4. Resolve relative links against the original source, map the source and destination, then calculate the new relative link. Preserve fragments and encoding.

For filesystem operations, derive a separate move sequence. The existing parent-first approach can work, but child sources must then be resolved under the already-moved parent. Do not execute a nested-first TSV directly as shell moves. For example, the final path `020_architecture/010_decisions/` cannot be treated as an existing destination parent before `architecture/` is moved unless that state is deliberately created.

Require a dry-run report showing creates, moves and rewrites. Reject collisions, including case-only collisions, and never overwrite an existing destination automatically. Recognize already-completed moves on a retry or stop with a clear diagnostic; do not prefix paths twice.

### 5. Keep recovery scoped to migration-owned changes

Remove “abandon or reset the branch” as the default recovery instruction. A branch can still contain pre-existing untracked work, newly imported material or unrelated edits. Switching branches or reverting commits also does not necessarily restore those files.

Record the migration base, file inventory, checksums and ownership of edits. Before committing, reverse only the migration's mapped moves and edits. After committing, prepare a normal revert of the complete migration commit. Preserve the fixture repair unless there is a reason to revert it independently. Do not use a broad reset or cleanup command as routine recovery.

## Import workflow refinements

### 6. Treat the request file as descriptive input

Revise step 2, which currently says an `IMPORT-REQUEST.md` can direct the agent. That file can itself arrive inside supplied material. Treat its destination hints and handling notes as input to interpret within the user's authorized import request. It must not independently authorize execution, permission changes, overwrites or expanded scope.

Allow routine placement and creation of a numbered destination when the user's import request already authorizes them. Ask for clarification when the classification is materially ambiguous or an action would overwrite existing work. Creating a new directory alone should not force another approval round.

### 7. Make import completion recoverable

Use copy, verify, record, validate, then clear staging as the default sequence. Remove a staged source only after its permanent artifact and provenance entry are safely retained. For a partial failure, keep unresolved originals in staging and record the failure so a retry does not create duplicates.

Specify the minimum import-log fields:

| Field | Purpose |
|---|---|
| Batch and item identity | Stable way to distinguish repeated imports and retries |
| Original relative path, size and SHA-256 | Identifies the supplied bytes |
| Source and received date | Author/vendor/URL when known; explicitly Unknown otherwise |
| Destination and classification | States where the artifact belongs |
| Handling and outcome | Verbatim copy, derived content, unresolved or failed |
| Destination checksum | Confirms a verbatim copy or identifies a derived artifact |
| Source relationship | Links derived content to retained source material or its durable source record |

An import log records provenance; it does not by itself validate technical evidence or make a document authoritative. Preserve the existing evidence review and acceptance requirements.

### 8. Narrow audit exceptions and correct the Git-ignore claim

Continue skipping the staging inbox rather than listing each drop as an indexed source import. Prefer a root-relative skip for `000_import/`: adding its name to the global `IGNORED_DIRS` skips any path component with that name, including an accidentally nested directory. Existing `rglob` discovery also enumerates directories before filtering; a skip is not necessarily traversal pruning. Improve traversal only if inbox volume warrants it.

For permanent verbatim imports, exclude individual files or deliberately designated source-only subtrees. Avoid blanket exclusions for a mixed directory containing maintained frontmatter documents.

Replace “staged files are therefore never committed by accident” with “ordinary Git add operations ignore staged content.” Ignore rules do not protect already tracked files or prevent forced adds. Validate the intended behavior with `git check-ignore` and `git ls-files -- 000_import/`; only the README should be tracked. Use a temporary non-sensitive sample to check staging behavior and remove only that sample afterward.

## Validation and editorial refinements

### 9. Strengthen targeted checks

Retain the full suite, auditor and index freshness checks. Add focused coverage for the new failure modes:

- A nested original path translates once to its final path; an exact file mapping overrides its directory mapping.
- Relative links survive moving both their source and destination, including fragments and supported escaped destinations.
- Numbered tool imports work through unittest discovery and direct CLI execution from a working directory outside the repository.
- Staged malformed Markdown is absent from audit inputs and the index. Adding or removing a staged file leaves generated index content unchanged.
- The moved guide exclusion works while a neighboring maintained document still undergoes validation.
- Destination collisions are rejected before any move. A retry does not double-prefix or overwrite paths.

Keep the stale-path search as a review aid. `git grep` sees tracked files only, so pair it with an inventory of relevant untracked project files, excluding staging, dependencies and environment data. A result in a fixture or historical source needs review; it is not automatically an error. Do not use raw text replacement on npm package paths.

### 10. Correct small inconsistencies

- The range `010`–`899` offers 89 multiples of ten from `010` through `890`, not 89 free slots after the current mapping. Eleven are already allocated, leaving 78 default-step slots, plus the intervening gaps.
- State that initial alphabetical ordering is a migration convention. New directories can use gaps without requiring permanent alphabetic order or sibling renumbering.
- Keep `000_import/README.md` as the intentionally unaudited tracked exception; include it in manual link review.
- Recount links and working-tree changes at execution time. The r1.0.1 quantities are historical estimates, not migration preconditions.
- Keep standing naming and import rules in documentation conventions. Let the plan and import log record decisions and work without becoming a second authoritative ruleset.

## Recommended execution order for the accepted plan

1. Settle the remaining draft choices and select the canonical revision. Preserve older untracked drafts before consolidation.
2. Capture the current branch, tracked/untracked state and ownership of existing edits. Prepare the dedicated work branch when implementation is authorized.
3. Resolve duplicate plan IDs and repair the two known test-fixture failures without weakening validation. Obtain a passing audit, current index and passing tests. Record this baseline and its commit when applicable.
4. Finalize the mapping, file inventory, checksums, new-directory actions and dry-run report. Choose the accepted plan's precise file move.
5. Perform moves and reference updates as one working change. Add staging behavior, the import log, documentation rules and focused checks.
6. Regenerate the index and run the full validation. Compare preserved IDs, ancestry, source bytes and images against the recorded baseline.
7. Review the complete migration diff against the recorded base, including outstanding working/staged changes and known external-link follow-ups. Commit or publish only under the applicable working agreement.

## Review disposition

Recommended direction: retain r1.0.2's structure and incorporate the corrections above before executing it. No directories, existing revision files, configuration, tests or index were changed as part of this review.

Revision r1.0.3 records recommendations only. The next accepted canonical plan should identify which recommendations were adopted and preserve its revision history through the agreed retention process.
