---
schema_version: 1
id: DOC-IMPL-PLAN-TEMPLATE
title: Per-control implementation plan template
document_type: implementation
parent: ROOT
lineage: [ROOT]
owner: Architecture / Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-11-02'
---

# Per-control implementation plan template

Copy this file to a new file under `050_implementation/010_plans/` for each bounded implementation. Assign a unique document ID and update its title and baseline date. Fill in facts you know; use `Unknown` or `Not provided` for gaps. Do not guess. Follow the [per-control implementation workflow](../../090_standards/implementation-workflow.md).

## AI handoff

Read this entire plan, the linked control/architecture documents and the workflow standard before proposing work. Preserve the user's input and decisions. Identify material unknowns and ask for them before hardware-specific recommendations. Once the scope is sufficiently specific, research current primary sources for the exact hardware/software and save a dated research record in `080_references/020_implementation-research/`. Cite sources and separate documented facts, inferences and unknowns. Update the AI-maintained readiness and roadmap sections below. Do not fabricate issue IDs, test results, evidence, approvals or customer decisions. Keep this plan for scope, decisions and roadmap; use the project's existing documents/registers for authoritative requirements, tests, implementation results, evidence and acceptance.

## Plan status

- **Planning state:** Intake
- **Implementation state:** Not started
- **Last reviewed:** Not yet reviewed
- **Roadmap readiness:** Not assessed
- **Scoped research record:** Not created

## 1. Implementation identity and objective

- **Plan name / unique ID:** <fill in>
- **Pillar ID and name:** <fill in>
- **Control ID and name:** <fill in>
- **Control overview:** <link to authoritative control document>
- **Requirements and tests:** <links to authoritative documents and relevant IDs>
- **Program/SOW obligation and source:** <exact clause or Not provided>
- **Desired outcome:** <what this implementation should accomplish>
- **Scope:** <site, system, path, link, workload, or bounded set>
- **Out of scope:** <explicit exclusions>
- **Engineering owner / reviewer:** <names or roles; distinguish proposed from accepted>
- **Decision and exception authority:** <name/role or Not provided>

## 2. Environment and hardware input

List both ends of each relevant link or interaction. Add rows as needed. “Unknown” is a valid entry; a product family alone is not exact compatibility evidence.

| Role / end | Site | Manufacturer and exact model/SKU | Module/card and exact port | Software/release | License | Media and speed | Peer / connected system | Source or inventory record |
|---|---|---|---|---|---|---|---|---|
| <fill in> | <fill in> | <fill in> | <fill in> | <fill in> | <fill in> | <fill in> | <fill in> | <fill in> |

### Current configuration and traffic

- **Current topology and relevant interfaces:** <fill in or link>
- **Traffic and protocols that must continue to work:** <fill in or Unknown>
- **Current security and key-management configuration:** <fill in or Not provided>
- **Availability, redundancy and maintenance constraints:** <fill in or Unknown>
- **Management and monitoring paths:** <fill in or Unknown>
- **Change window, rollback and lab access:** <fill in or Unknown>

## 3. Constraints, impacts and decisions

- **Required standards, policy or profiles:** <source and specific obligation, or Unknown>
- **Operational/functionality constraints:** <fill in>
- **Performance, MTU or availability targets:** <numeric targets or Not agreed>
- **Known compatibility limits:** <sourced finding or Unknown>
- **Residual risk / compensating controls:** <fill in or Not assessed>
- **Decisions already made:** <decision, authority, date and source; or None>
- **Open questions / blockers:** <fill in; do not silently resolve>

## 4. AI-maintained readiness and research

AI updates these sections while preserving the input above.

### Readiness assessment

- **State:** Not assessed
- **Facts sufficient for research:** Not assessed
- **Facts sufficient for a safe implementation plan:** Not assessed
- **Blocking questions for the user:** Not assessed
- **Assumptions or inferences:** None recorded

### Research record

- **Record path:** Not created
- **Research date and scope:** Not researched
- **Summary:** Not researched
- **Unresolved source/applicability questions:** Not assessed

## 5. AI-maintained implementation roadmap

AI drafts an ordered, scoped roadmap after intake and research. Link each work package to its source requirement, test, research finding or decision. Keep generic requirement and test definitions in their authoritative control documents.

| Order | Work package / decision gate | Prerequisites | Owner | Expected output or evidence | Source links | Status |
|---|---|---|---|---|---|---|

### Candidate Jira stories

AI may draft stories from the roadmap in stages. Start with a story that gathers missing inputs if those inputs block research; derive hardware-specific stories only after the inventory and research exist. These are proposals, not actual Jira issues. The team decides what to create and how to group it. Do not assign issue keys or sprints until the work exists in Jira. Jira is not synchronized with this plan.

| Candidate summary | Purpose and acceptance criteria | Roadmap steps / engineering IDs | Dependencies | Jira issue link (optional; add only after creation) |
|---|---|---|---|---|

## 6. Decisions and progress log

Record material plan changes and decisions with date, source/authority and impact on scope, roadmap or prior evidence. Do not overwrite earlier test results or approvals.

| Date | Decision / change / outcome | Source or authority | Roadmap impact |
|---|---|---|---|

## 7. Closeout links

- **Implementation register record:** Not created
- **Verification tests and evidence:** Not executed
- **Customer acceptance record:** Not submitted
- **Remaining limitations / follow-up:** Not assessed
