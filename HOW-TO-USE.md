---
schema_version: 1
id: DOC-ZTA-HOW-TO-USE
title: How to use this project
document_type: guide
parent: ROOT
lineage: [ROOT]
owner: Architecture / Security Engineering
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-25'
---

# How to use this project

Use zta-decomposition to turn a program obligation into engineering definitions, delivery work and reviewed proof. Start with one obligation and one bounded scenario, then follow the workflow below. Use the [MACsec example](zta-macsec-use-case.md) alongside this guide to see the tables and fictional Jira references filled out.

The repository is a proposed engineering baseline. MACsec is the most developed branch; other pillars still need further decomposition. The example SOW-001 wording and Jira keys are illustrative. No deployed control or contractual acceptance is claimed.

## Choose the right document

| Need | Start here |
|---|---|
| Find the project entry points | [README](README.md) |
| Follow the working process | This guide |
| Understand the architecture and traceability | [Project guide](zta-project-guide.md) |
| Explain the project approach and benefits | [ZTA decomposition briefing](zta-decomposition-briefing.md) |
| Prepare for questions and critical review | [ZTA decomposition FAQ](zta-decomposition-faq.md) |
| See one branch expanded into tables and stories | [MACsec use case](zta-macsec-use-case.md#how-one-table-expands-into-the-next) |
| Look up a document or its owner | [Document index](index.md) |
| Review actual protection and customer decisions | [Implementation register](implementation/macsec.md) and [acceptance register](acceptance/macsec.md) |
| Find authoring rules | [Documentation conventions](standards/documentation-conventions.md) and [manual Jira standard](standards/manual-jira-traceability.md) |

## Program adoption checklist

This is the single authoritative checklist of working agreements needed to adopt this approach. The briefing, use case and TODO link here rather than maintain separate lists. Record links to existing program decisions where they already apply. For each item, enter the agreed outcome, approver, date and durable decision reference in the final column. Blank means agreement has not been recorded here; it does not assert that the program has no existing policy.

| Agreement | What to settle | Agreed outcome and approval reference |
|---|---|---|
| SOW mapping and scope | Adopted clause/source, covered sites/resources/links, deliverables, exclusions and mapping to engineering requirements | |
| Roles and authority | Accepted engineering/document owners, Product Owner, Scrum Master, reviewers, exception authority and program acceptance authority | |
| Jira working agreement | Approved base address/project, who creates issues and maintains reciprocal links, description fields and link-review cadence | |
| Verification and acceptance | Operationally appropriate protection scope, acceptable functionality/workflow impacts, test criteria and proof; customer disposition of documented limitations under ADR-014, separately from technical results and without coverage percentages | |
| Evidence handling | Approved storage, durable references, access, retention, review and preservation of failures/retests | |
| Baselines and change review | Repository commit/release convention, contributor review process and impact review when requirements, configurations or stories change, split or are superseded | |
| Program presentation | Confluence location, ownership and links to authoritative records so summaries stay aligned with engineering and delivery work | |

The proposed roles and workflow below support review of these agreements. Local document development and optional blank Jira columns can be used while decisions are being recorded. Acceptance claims require the applicable program decisions and reviewed evidence. The auditor does not approve this checklist or verify external decision records.

## Who does what

These responsibilities are proposed until the program records its assignments above.

| Role | Responsibility |
|---|---|
| Program leadership / Product Owner | Confirm delivery outcomes, authoritative SOW mapping and backlog priorities |
| Scrum Master | Coordinate story creation, dependencies and the agreed review cycle |
| Engineering owner / story author | Develop definitions and procedures, maintain table-to-Jira links, implement work and record results |
| Engineering reviewer | Review scope, criteria, configuration, evidence and reciprocal references |
| Designated program authority | Disposition exceptions and determine acceptance within assigned authority |

## 1. Select an obligation and find its engineering scope

Identify the actual SOW clause and a bounded delivery scenario: for example, a selected link at one site. Find the relevant [pillar](README.md#seven-pillars), then follow its control index. Review the architecture and decisions before proposing a change. Record unresolved hardware or design inputs in [open questions](architecture/open-questions.md) and research findings in the [research register](references/vendor-research.md).

Document the SOW-to-engineering association in the delivery epic/story and its linked program record. SOW references supplement the engineering hierarchy; they do not become new parents in the current schema.

## 2. Expand the selected row into actionable detail

Select a pillar row and expand it into controls. Select a control and expand it into measurable requirements. Select a requirement and define its tests. Each selected row's identifier becomes the next table's parent; preserve the full ancestry in table metadata. Keep one authoritative definition per entity and link to it from other documents.

For example, the existing branch is `ROOT → ZT-05 → NET-04 → MAC-001 → TEST-003`. The [table walkthrough](zta-macsec-use-case.md#how-one-table-expands-into-the-next) shows each expansion. TEST-003 covers part of MAC-001; the other applicable tests remain necessary.

Use the [documentation conventions](standards/documentation-conventions.md) for frontmatter, unique identifiers, table metadata and status. Define expected evidence and measurable acceptance criteria before execution. Create no placeholder evidence rows. Review whether the decomposition fully covers the obligation; the auditor cannot discover missing engineering concepts.

## 3. Create delivery work and link both directions

With the engineering leads and Product Owner, the Scrum Master coordinates research, requirements/design, implementation and verification work. Split stories by scope where needed and identify dependencies. Use the [Jira description template](standards/manual-jira-traceability.md#suggested-jira-description-fields) to record the SOW source, engineering IDs, document links, reviewed baseline, scope, acceptance criteria and expected artifacts.

After actual issues exist, manually add `Jira epic` links to controls, `Jira stories` to requirements/tests and later `Verification stories` to real evidence records. Leave cells empty until links are available. A reviewer opens each link and confirms its purpose and reciprocal engineering references. Keep sprint, assignee and delivery status in Jira. No API access is required; use the [manual Jira rules](standards/manual-jira-traceability.md) for exact syntax and story-change handling.

## 4. Implement, execute and collect proof

Perform the approved work and retain its actual configuration/code revision and change record. Execute the reviewed procedures against the identified equipment and configuration. Capture expected versus actual results, date, executor, artifacts and reviewer disposition. Preserve failures and retest history.

Record the exact protection and any deferred/unsupported scope in the [implementation register](implementation/macsec.md), including operational impact, limitations, residual risk and alternatives. Follow the [record standard](standards/implementation-acceptance.md). Create actual evidence records under their immediate Test ID using the [evidence instructions](controls/macsec/verification.md#evidence-and-execution). A local evidence artifact or documented local record for externally stored artifacts is needed for the current auditor. Store the proof in the approved location and link it durably. Technical validation requires reviewed descendant evidence; a closed Jira story or passing documentation audit cannot supply that proof.

## 5. Review results and report delivery

Review the documented implementation scope, actual results, limitations, operational tradeoffs and residual risk. Under [ADR-014](architecture/decisions/ADR-014.md), request customer disposition against the applicable contract SOW requirements without calculating a completion percentage. Record the authority, date, decision basis and artifact in the [acceptance register](acceptance/macsec.md). Accepted with documented limitations may coexist with Not implemented, Not executed or Failed technical outcomes; keep those facts visible. A research story can finish with an unsupported-capability finding while its technical obligation remains unmet.

Use Confluence to summarize progress and link the SOW, epic, engineering baseline, evidence and decisions. Preserve authoritative engineering definitions in the repository and delivery state in Jira. Refer to the adoption checklist above when a missing working agreement prevents a claim from being assessed.

## 6. Maintain and check the baseline

When a definition changes, review its impact on child rows, stories, tests and previous evidence. Preserve IDs when moving files and retain the baseline that each execution actually tested. Follow the program's recorded review process before committing or publishing changes.

Use Python 3.10 or newer and install `requirements.txt` in your Python environment. From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 tools/generate_index.py --root .
python3 tools/audit_zta.py --root . --report audit-report.md
python3 tools/generate_index.py --root . --check
git diff --check
```

Run `python3 -m unittest discover -s tests -v` when changing auditor or tooling behavior. Render and visually inspect edited Mermaid blocks under the [diagram standard](standards/mermaid-best-practices-r1.0.6.md). Review the complete diff, stage the intended source and index changes, then commit and push through the agreed workflow. The generated audit report is local output. See [tool usage and limits](tools/README.md) for the checks' exact scope.

The [TODO](TODO.md) tracks documentation maintenance; the [roadmap](architecture/roadmap.md) tracks broader engineering sequencing. Record adoption agreements in the checklist above and link to them from those trackers.
