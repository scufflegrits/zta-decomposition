---
schema_version: 1
id: DOC-ZTA-AI-HANDOFF
title: Project handoff for AI agents
document_type: guide
parent: ROOT
lineage: [ROOT]
owner: Architecture / Security Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-11-06'
---

# Project handoff for AI agents

Read this file first when continuing work in this repository. It is a short orientation and current starting point; the linked project documents contain the authoritative details.

## What this project is

This repository is a docs-as-code planning and traceability framework for a proposed two-site Zero Trust Architecture organized around the seven DoD pillars. It is a reference design and engineering workflow, not an as-built configuration, security certification or customer acceptance record.

The intended trace is:

`SOW obligation → pillar → control → requirement → test → evidence → implementation record → customer acceptance`

MACsec under ZT-05 / NET-04 is the most developed technical branch. The other pillars are less decomposed. The repository explicitly separates design proposals, vendor research, actual testing, deployed implementation and customer disposition. Do not describe a document audit or vendor statement as proof that a control is deployed or validated.

## Start here

1. Read [README](README.md) for the architecture, repository map and integrity limits.
2. Read [How to use this project](HOW-TO-USE.md) for the working process and program-adoption checklist.
3. For technical implementation, follow the [per-control implementation workflow](090_standards/implementation-workflow.md) and copy the [implementation plan template](050_implementation/010_plans/implementation-plan-template.md).
4. Use the [MACsec first-link plan](050_implementation/010_plans/macsec-pilot.md) as the current example. It is an intake and preliminary roadmap; its hardware-specific research has not started.
5. For detailed agent and review rules, read [review handoff r1.0.2](900_project-admin/review-handoff-r1.0.2.md). For document authoring and IDs, read [documentation conventions](090_standards/documentation-conventions.md).

## Current starting point

The next useful engineering input is a bounded MACsec candidate link and an exact inventory for both ends. The pilot currently lacks the selected site/link, device SKUs, modules and ports, software/OS versions, feature licenses, media/speed, current configuration, applicable program obligation, approved profile/performance criteria, and named technical reviewer or decision authority.

The architecture names equipment families, but those names do not identify the actual bill of materials or establish MACsec support. Existing compatibility findings are historical handoff research and have not been revalidated against a selected configuration. No actual MACsec implementation, execution evidence or customer acceptance has been recorded.

For a larger fleet, use a parent campaign plan for the complete inventory and cohort roll-up. Use child plans for materially different compatibility cohorts. AI may propose cohort groupings based on exact endpoints, modules/ports, software, licenses, media, peer pairings and relevant configuration; an engineering owner reviews the grouping before cohort-specific research. Keep research and verification claims scoped to the exact applicable cohort and deployed outcome.

## How to continue an implementation

- Read the plan, its linked control/requirements/tests, architecture decisions and the workflow standard before proposing technical steps.
- Preserve user-provided facts. Mark missing details as unknown and ask for the smallest input set that unblocks the next step. Do not infer exact equipment, contract scope, approval authority, configuration or acceptance criteria.
- If missing inventory blocks research, draft a candidate Jira story to collect it. For a link, request both endpoints, site, exact make/model/SKU, relevant modules and ports, software/OS release, licenses, media/speed, peer, configuration context and an inventory/source record. The team decides whether to create the story.
- After exact details are supplied, research current primary sources for the specific hardware/software/peer combination. Save dated findings under `080_references/020_implementation-research/`, distinguish documented facts from inference and unknowns, and cite source versions and applicable pages.
- For relevant PDFs that can be retained, save the original and a frontmatter-managed Markdown reading copy beside the scoped research record. Record source URL/title/version, retrieval date, SHA-256, extraction tool/version and limitations. The original PDF is authoritative. Detect the active OS/shell and use tools and paths available there, including Cygwin or Debian; do not silently install tools or upload documents to external converters. If suitable local extraction is unavailable, report the blocker and ask.
- Draft an ordered roadmap and candidate follow-on Jira stories with acceptance criteria and dependencies. Jira manages actual issues, sprints and delivery status; this project does not synchronize with Jira or check live issues. Issue links in project documents are optional and maintained manually.
- Record actual deployment and test outcomes in the authoritative implementation and verification records. Record customer decisions separately in the acceptance register. Preserve failures, limitations and retests. Do not invent evidence, issue keys, approvals or acceptance.

## Important project boundaries

- Project decisions and statuses can describe the proposed baseline; they do not establish that the program has adopted it. Owners and roles remain proposed until recorded as accepted.
- SOW-001 and Jira examples in the use case are illustrative. Do not treat sample keys or `jira.example.invalid` links as real work.
- The auditor checks declared document structure and relationships. It cannot determine requirement completeness, vendor-source currency, equipment behavior, evidence authenticity, or authority to accept a contract outcome.
- The [review handoff](900_project-admin/review-handoff-r1.0.2.md) records the configured GitHub repository as public. Before adding actual SOW text, inventories, configurations or evidence, verify current repository visibility and whether program policy permits storing that information there.
- Do not commit, push, publish or create external Jira work unless the user asks. Preserve source imports and historical revision snapshots.

## Useful references

- Architecture: [overview](020_architecture/overview.md), [open questions](020_architecture/open-questions.md), and [architecture roadmap](020_architecture/roadmap.md).
- MACsec: [control](030_controls/020_macsec/overview.md), [requirements](030_controls/020_macsec/requirements.md), [verification plan](030_controls/020_macsec/verification.md), [implementation register](050_implementation/macsec.md), and [acceptance register](010_acceptance/macsec.md).
- Research and records: [vendor research register](080_references/vendor-research.md), [implementation/acceptance record standard](090_standards/implementation-acceptance.md), and [documentation auditor guide](110_tools/README.md).
- Backlog: [project TODO](900_project-admin/TODO.md). The generated [document index](index.md) is the full catalog.

## Checks after documentation changes

Run the index freshness check, documentation audit and whitespace check. Run unit tests when changing auditor/tool behavior or when the user asks for tests. A clean document audit establishes consistency within its declared checks only.

```bash
python3 110_tools/generate_index.py --root . --check
python3 110_tools/audit_zta.py --root .
git diff --check
```
