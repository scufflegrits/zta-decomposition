---
schema_version: 1
id: DOC-STD-JIRA
title: Manual Jira traceability
document_type: standard
parent: ROOT
lineage: [ROOT]
owner: Documentation Engineering / Engineering leads
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-25'
---

# Manual Jira traceability

The repository supports manually maintained Jira links without API credentials, synchronization or software-factory access. Engineering IDs retain their existing meaning and parentage. Jira references identify delivery work associated with an entity; they are not new hierarchy entities or evidence of requirement satisfaction.

## Columns and syntax

| Entity table | Optional column | Purpose |
|---|---|---|
| Control | `Jira epic` | Delivery epic or epics associated with the control |
| Requirement | `Jira stories` | Research, design, requirements and implementation work directly associated with the requirement |
| Test | `Jira stories` | Preparation, implementation or execution work directly associated with the test |
| Implementation | `Jira stories` | Work associated with the actual scoped protection or documented limitation |
| Evidence | `Verification stories` | Verification work that produced the actual evidence record |

Existing control, requirement and test tables contain blank Jira cells ready for real references. No evidence rows are created until execution produces actual records. The columns remain optional for future tables; missing columns and blank cells do not fail the audit. Blank means no Jira link has been recorded, not that no work is required. Reviewers must decide whether work has actually been created.

Use a direct inline Markdown link whose label is exactly the issue key and whose URL ends in `/browse/KEY`. The supported key convention is an uppercase project identifier, optionally containing digits or underscores, followed by a hyphen and a positive issue number. Use the same actual key in both label and destination.

For example, the syntax is `[PROJECT-123](https://your-jira-host/context/browse/PROJECT-123)`. Replace the host, optional context path and key with actual values. Prefer the program's approved HTTPS base URL; HTTP is supported for environments whose approved Jira address requires it. Do not put credentials in URLs.

Separate multiple links with commas. Leave unavailable references empty; do not use `TBD`, a dash, bare keys, inline-code keys, reference-style links, descriptive labels, board URLs or comment/query fragments. Put the story's purpose in Jira or accompanying prose rather than inside the link cell.

The same issue can appear on several engineering rows. Each row can reference several issues. Links are direct associations: an epic on a control is not automatically inherited by its requirements, and a requirement's research story need not appear on every test.

## Manual working agreement

Follow the proposed roles and operational steps in [How to use this project](../HOW-TO-USE.md#who-does-what). Record program decisions and approval references in its single [adoption checklist](../HOW-TO-USE.md#program-adoption-checklist). This standard supplies Jira field syntax, the reciprocal-reference template, change-handling rules and local-check limits.

Keep delivery status, assignee, sprint, estimates and dependencies in Jira. Keep technical Required/Proposed/Verify/Validated statuses and evidence disposition in engineering records. At execution, follow the [evidence conventions](documentation-conventions.md#status-and-evidence) and [implementation/acceptance record rules](implementation-acceptance.md). Customer disposition of documented limitations stays separate from test results. A closed story does not itself validate a requirement or authorize SOW acceptance.

## Suggested Jira description fields

Use these fields in the description or program-approved custom fields; no Jira administrator change is required to use a description template.

```text
SOW reference and authoritative source:
Delivery epic:
Engineering IDs and source-document links:
Engineering baseline (reviewed commit or release):
Scope (site, link, equipment, software and configuration):
Story purpose and dependencies:
Acceptance criteria and reviewer/approval authority:
Expected deliverables and approved artifact location:
Actual test execution / evidence references, when available:
```

For research, acceptance can be a reviewed compatibility finding, including unsupported capability. For implementation, define the configuration/change deliverables and link outstanding verification. For verification, require execution results and reviewed artifacts. Replace the illustrative SOW-001 reference with an adopted program obligation before using this as contractual traceability.

## Changes and exceptions

When a story splits, link the relevant resulting stories and explain the disposition in Jira; preserve the relationship to any original work already performed. When a story is superseded, retain historical references needed to interpret prior evidence and identify the replacement in Jira. When the visible key or approved Jira base address changes, review affected table links together. Avoid deleting an old execution record when a retest is performed.

Use one destination per issue key across this repository. Multiple Jira instances that reuse the same keys require an agreed namespacing convention before their links can coexist; the current auditor reports conflicting destinations. Future integration can retain instance/internal identifiers and automate reconciliation after software-factory approval. No such integration is required for this manual workflow.

## Local checks and review limits

The auditor checks Jira columns on their permitted entity kinds, comma-separated inline-link syntax, key format, direct HTTP(S) browse URLs, matching label/destination keys, duplicate keys within a cell and conflicting destinations across declared entity rows. Host-name case and default ports are normalized for comparison. The checks make no network requests.

It cannot determine whether an issue exists, is an epic or story, has the right scope, links back to the engineering record, or is complete. It does not validate descriptive example tables, enforce story coverage, or reconcile issue keys that change. Human review supplies these checks. Run the [document checks](../110_tools/README.md) before review and use the [MACsec use case](../zta-macsec-use-case.md#manual-jira-links-in-the-tables) for fictional worked examples.
