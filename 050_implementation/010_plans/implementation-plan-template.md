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

Copy this file to a new file under `050_implementation/010_plans/` for each control campaign or bounded implementation. Assign a unique document ID and update its title and baseline date. For one cohort, one plan is enough; use a parent campaign and child cohort plans when the control spans materially different configurations. Fill in facts you know; use `Unknown` or `Not provided` for gaps. Do not guess. Follow the [per-control implementation workflow](../../090_standards/implementation-workflow.md).

## AI handoff

Read this entire plan, the linked control/architecture documents and the workflow standard before proposing work. Preserve user input and decisions. For a fleet, normalize the inventory, propose compatibility cohorts with explicit criteria, and ask for engineering review before treating groupings as approved. Create or use child plans for materially different cohorts; research each cohort's exact hardware/software pairing. Ask about critical missing inputs rather than infer. For relevant PDFs that are publicly downloadable and permitted for local retention, save the original and a Markdown reading copy in the research area; record source URL, version, retrieval date, checksum and extraction tool/version. Detect the active OS/shell and use local tools and path conventions available there, including Cygwin where applicable; do not assume Debian utilities. Follow the PDF handling instructions in the workflow standard, and cite the original PDF/page as the authority. Cite sources and separate documented facts, inferences and unknowns. Update the AI-maintained readiness, cohort register and roadmap sections below. Do not fabricate issue IDs, test results, evidence, approvals or customer decisions. Keep this plan for inventory/cohort roll-up (parent) or scoped work (child); use the project's existing documents/registers for authoritative requirements, tests, implementation results, evidence and acceptance.

## Plan status

- **Planning state:** Intake
- **Implementation state:** Not started
- **Last reviewed:** Not yet reviewed
- **Roadmap readiness:** Not assessed
- **Scoped research record:** Not created

## 1. Implementation identity and objective

- **Plan name / unique ID:** <fill in>
- **Plan level:** Single cohort / Parent campaign / Child cohort
- **Parent plan ID:** <ID or Not applicable>
- **Child plan IDs:** <IDs or Not applicable>
- **Cohort ID and definition:** <ID and technical equivalence criteria, or Pending intake>
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

For a single-cohort or child plan, list its member links and both ends. For a parent campaign, use this as the fleet inventory and add one row per endpoint; give both ends the same Link ID. AI may propose Cohort IDs after inventory review, but an engineer must approve the grouping. “Unknown” is a valid entry; a product family alone is not exact compatibility evidence.

| Link ID | Cohort ID | Role / end | Site | Manufacturer and exact model/SKU | Module/card and exact port | Software/OS release | License | Media and speed | Peer / connected system | Source or inventory record |
|---|---|---|---|---|---|---|---|---|---|---|
| <fill in> | Pending | <fill in> | <fill in> | <fill in> | <fill in> | <fill in> | <fill in> | <fill in> | <fill in> | <fill in> |

### Cohort register (parent campaign plans)

AI proposes cohort groupings only after reviewing the complete inventory. Record why relevant hardware, software, licensing, media, topology and peer variables do or do not permit findings to be reused. Keep uncertain devices in separate provisional cohorts until resolved.

| Cohort ID | Equivalence criteria | Member Link IDs | Differences / applicability limits | Child plan | Research status | Implementation status |
|---|---|---|---|---|---|---|

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

AI updates these sections while preserving the input above. In a parent campaign, maintain the cohort register and link each child plan. In a child plan, keep the specific cohort definition and member Link IDs visible.

### Readiness assessment

- **State:** Not assessed
- **Facts sufficient for research:** Not assessed
- **Facts sufficient for a safe implementation plan:** Not assessed
- **Blocking questions for the user:** Not assessed
- **Assumptions or inferences:** None recorded

### Research record

- **Record path(s):** Not created; parent campaign plans link cohort-specific child research records here or in the cohort register
- **Research date and scope:** Not researched
- **Summary:** Not researched
- **Unresolved source/applicability questions:** Not assessed

## 5. AI-maintained implementation roadmap

AI drafts an ordered, scoped roadmap after intake and inventory review. A parent campaign roadmap establishes cohort boundaries and child plans before cohort-specific research; a single-cohort or child plan proceeds to research and technical planning. Link each work package to its source requirement, test, research finding or decision. Keep generic requirement and test definitions in their authoritative control documents.

| Order | Work package / decision gate | Prerequisites | Owner | Expected output or evidence | Source links | Status |
|---|---|---|---|---|---|---|

### Candidate Jira stories

AI may draft stories from the roadmap in stages. For multiple cohorts, begin with inventory collection and cohort review, then derive research/design/test/implementation stories by cohort as appropriate. Start with a story that gathers missing inputs if those inputs block research; derive hardware-specific stories only after the inventory and research exist. These are proposals, not actual Jira issues. The team decides what to create and how to group it. Do not assign issue keys or sprints until the work exists in Jira. Jira is not synchronized with this plan.

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
