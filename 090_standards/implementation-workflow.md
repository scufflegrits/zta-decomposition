---
schema_version: 1
id: DOC-STD-IMPL-WORKFLOW
title: Per-control implementation workflow
document_type: standard
parent: ROOT
lineage: [ROOT]
owner: Architecture / Engineering
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-11-02'
---

# Per-control implementation workflow

Use this workflow to plan one bounded technical implementation under a pillar and control. The [implementation plan template](../050_implementation/010_plans/implementation-plan-template.md) is the engineer's input and the working roadmap. The [MACsec pilot plan](../050_implementation/010_plans/macsec-pilot.md) demonstrates the workflow. The implementation plan does not replace authoritative control requirements, tests, implementation evidence or customer decisions.

## Responsibilities and source of truth

- The engineer supplies the scope, program obligation, actual environment, hardware/software inventory, constraints, known decisions and unknowns in the implementation plan.
- AI reads the plan and its linked project documents, reports missing inputs, and asks focused questions before making hardware-specific recommendations.
- AI researches current, exact-product vendor documentation after enough identifying details are available. It saves the findings in a scoped record under `080_references/020_implementation-research/` and links that record from the implementation plan.
- AI drafts and revises the roadmap in the implementation plan, linking to existing requirements, tests and standards rather than copying their authoritative content.
- Engineers review the research, design, procedures and results. Vendor documentation is not installation evidence; only reviewed execution evidence supports technical validation.
- Jira manages delivery planning and status. Optional Jira links in the plan are manually maintained pointers. Jira synchronization and live issue checks are outside project scope.

The implementation plan is authoritative for the scope-specific intake, decisions and roadmap. The scoped research record is authoritative for the dated vendor-source review. Existing control documents remain authoritative for generic technical requirements and tests. The implementation and acceptance registers remain authoritative for actual deployment, verification evidence and customer disposition.

## Workflow

### 1. Create and fill in a plan

Copy the template to a new plan file under `050_implementation/010_plans/`. Give the effort a unique name and document ID. Fill in facts you know; use `Unknown` or `Not provided` for gaps. Do not infer exact models, configurations, contractual scope, approval authority or test criteria from the general architecture.

Choose a bounded scope, such as one link, peer pairing, site, workload path or control instance. Identify the applicable pillar and control, actual program obligation if known, desired outcome, system boundary, owner and decision authority. Record hardware with both ends of the connection, exact SKU/model, module/card/port, software release, license, media, speed and relevant configuration. Link existing documents instead of copying their contents.

### 2. Assess readiness and ask for missing inputs

Read the full plan and referenced control/architecture documents. Separate confirmed project constraints, user-provided facts, sourced facts, assumptions and unknowns. List blockers that prevent relevant research or safe planning. Ask the user for the smallest set of missing details needed to proceed.

Do not mark a plan implementation-ready while material facts remain unknown. A plan may still contain a clearly labeled preliminary roadmap for collecting those facts.

### 3. Research the specified implementation

When product, software and peer details are sufficiently specific, research current primary sources, prioritizing vendor configuration guides, release notes, compatibility matrices and data sheets. Use standards sources where they define behavior or test criteria. Check publication/release applicability and record the actual date each source was reviewed.

Create or update a scoped research record under `080_references/020_implementation-research/`. It must identify the implementation plan, exact researched scope, sources and applicable versions, findings, configuration constraints, limitations, source dates, research date, reviewer/status and unresolved questions. Link relevant entries in the central [vendor research register](../080_references/vendor-research.md) when it already assigns a source ID; do not imply that a general source listing is current verification for the selected bill of materials.

For every material claim, distinguish what the vendor explicitly documents, what is inferred, and what remains unverified. Cite direct source pages near the claim. If sources conflict or exact applicability is unclear, report the conflict and keep the finding unconfirmed. Do not convert vendor claims into local test results.

### 4. Draft a staged roadmap

Write the roadmap in the plan, with ordered work packages and explicit prerequisites, decisions, dependencies, owner or responsible role, expected output/evidence, source links and status. Include only applicable stages, but consider:

1. confirm obligation, scope and authorities;
2. complete inventory and source research;
3. resolve design choices, compatibility and operational impacts;
4. agree measurable criteria and review procedures;
5. prepare lab/pilot, change and rollback plans;
6. implement the approved bounded scope;
7. execute the linked tests and preserve failures/retests;
8. record actual implementation, evidence, limitations and customer disposition;
9. review remaining scope and decide whether to expand.

Every step must be traceable to a project requirement, test, decision, research finding, user decision or clearly labeled proposed task. Do not invent Jira issues, evidence IDs, approvals or customer decisions. Keep roadmap completion separate from technical validation and customer acceptance.

### 5. Derive candidate Jira stories incrementally

After the roadmap is reviewed, AI may propose Jira-ready stories for work that needs delivery tracking. The first story can collect missing inputs rather than attempt technical implementation. For example, a hardware-specific plan may begin with “Provide the make, model and software/OS version for both ends of the candidate link.” Its acceptance criteria should request exact identifying details, relevant modules/interfaces/licenses/media, peer identity, and a source or inventory record; unknown fields should be called out rather than guessed.

When that information is available, update the plan and research the exact product pairing. Then derive follow-on stories for research review, design decisions, test preparation, implementation and verification as appropriate. AI may draft story summaries, descriptions, acceptance criteria, dependencies and links to roadmap steps and control IDs. It must not invent issue keys, assign sprints or treat a proposed story as created work.

The Product Owner and engineering team decide which proposals become issues and how to group them. A roadmap work package may map to one story, several stories or no story. Jira remains the source for actual issue state and sprint planning. Add an optional manual issue link to the plan only after the issue exists; reciprocal links and synchronization are not required.

### 6. Execute, update and review

As work proceeds, record decisions, changes in scope, blocked items and outcomes in the plan. Preserve the original reviewed baseline for test runs. Put actual evidence and implementation facts in the existing control verification and implementation records; put customer disposition in the acceptance register. Update the plan with links and a concise status, not duplicate artifacts.

Before calling a roadmap complete, verify each technical claim against its required reviewed evidence and record open limitations. A documentation audit can check declared links and structures but cannot verify vendor claims, engineering adequacy, source currency, hardware behavior or evidence authenticity.

## Reusable instruction for AI

When asked to continue an implementation plan, use the plan's own AI handoff instructions and this workflow. Read the linked project sources first. Preserve user-provided facts and prior decisions. Identify unknowns and ask for critical missing inputs before hardware-specific research. Propose a first Jira story to collect missing inputs when that would unblock the work; after the details are supplied, research primary sources and store a dated, cited project record. Update the roadmap and propose any appropriate follow-on stories with acceptance criteria and dependencies. Do not claim vendor research is implementation verification, do not fabricate records, issue keys or approvals, and do not overwrite user input or historical outcomes.

## Completion criteria for the planning stage

A plan is ready to enter implementation when its scope and obligation are identified, required hardware/software facts are sufficiently complete, applicable current research is recorded and reviewed, operational impacts and residual risks are visible, measurable acceptance criteria and relevant tests are agreed, and the roadmap identifies accountable owners and required evidence. Readiness means the plan can guide work; it does not mean the control is implemented or validated.
