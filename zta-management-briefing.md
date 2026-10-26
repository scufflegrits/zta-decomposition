---
schema_version: 1
id: DOC-ZTA-MANAGEMENT-BRIEFING
title: Using zta-decomposition to Support Program ZTA Delivery
document_type: guide
parent: ROOT
lineage: [ROOT]
owner: Architecture / Security Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-25'
---

# Using zta-decomposition to Support Program ZTA Delivery

**Management proposal:** Use this repository as an engineering foundation for implementing Zero Trust Architecture through the program’s AGIIL delivery process, with Confluence providing program visibility and Jira coordinating execution.

The project already organizes the proposed architecture around seven Zero Trust pillars, documents architectural constraints, and establishes identifiers linking controls, requirements and verification procedures. It provides a starting point for turning Statement of Work obligations into work that teams can estimate, execute and demonstrate.

The [MACsec delivery use case](zta-macsec-use-case.md) demonstrates this approach with proposed SOW-001 wording, a mapping to existing requirements and tests, suggested Jira story groups, and the evidence needed for acceptance. Its [table expansion walkthrough](zta-macsec-use-case.md#how-one-table-expands-into-the-next) shows how selecting a pillar row leads to controls, then requirements, tests and evidence. SOW-001 is an illustrative obligation, not an approved contract line item.

## Where zta-decomposition fits

The repository supplies the engineering content that becomes Jira work and ultimately supports acceptance. Confluence presents that content to the program; Jira manages its delivery. Teams use the repository to identify what must be researched, designed, implemented and proven.

| Project content | Contribution to program delivery |
|---|---|
| [Architecture views](architecture/overview.md) and [decisions](architecture/decisions/README.md) | Establish design boundaries and constraints for epics and stories |
| [Seven pillar documents](README.md#seven-pillars) | Identify engineering responsibilities and areas needing further decomposition |
| [Control definitions](controls/macsec/overview.md) | Describe the protection each work package must deliver |
| [Requirements](controls/macsec/requirements.md) | Supply measurable obligations for story acceptance criteria |
| [Verification procedures](controls/macsec/verification.md) | Define how teams will demonstrate that requirements are satisfied |
| [Procurement assessments](procurement/macsec-equipment-assessment.md) and [open questions](architecture/open-questions.md) | Identify research tasks, dependencies and unresolved equipment decisions |
| Stable identifiers and the [document index](index.md) | Give Confluence pages, Jira stories and evidence records consistent engineering references |
| [Documentation auditor](tools/README.md) | Check declared relationships and links for consistency |

For example, the repository already defines the path **ZT-05 → NET-04 → MAC-001 → TEST-003**: Network & Environment → MACsec → physical-port compatibility → ISR verification.

Once the program identifies an applicable SOW clause, that path can support linked Jira stories to:

1. Research the exact Catalyst and ISR ports, modules, software and licenses.
2. Review the compatibility requirement and measurable acceptance criteria.
3. Implement the approved configuration.
4. Execute verification, collect configuration and protected-session results, and submit artifacts for review.

The SOW clause and Jira records would be added as program work proceeds. The repository currently supplies the engineering starting point; it does not yet contain those contractual mappings, selected hardware configurations or execution evidence.

This makes zta-decomposition a reusable foundation for backlog development and technical review, with MACsec serving as the initial worked example for extending the approach across all seven pillars.

## Traceability from contractual obligation to accepted result

| Level | What it establishes | Example record |
|---|---|---|
| Statement of Work | Contractual obligation and acceptance authority | SOW clause identifier and exact text |
| Program outcome / epic | Deliverable addressing that obligation | Establish protected communications |
| Architecture / control | Design responsibility and enforcement approach | ZT-05 → NET-04: MACsec |
| Requirement | Measurable obligation | MAC-001: physical-port compatibility |
| Jira stories | Research, requirement definition, implementation and verification work | Linked stories with acceptance criteria |
| Test and artifacts | Procedure, actual result and supporting proof | TEST-003, configuration, counters and test report |
| Acceptance | Authorized review of results against requirements | Approval, exceptions and residual work |

These relationships may be many-to-many: several stories can satisfy one requirement, and one control can support several SOW clauses. Actual SOW mappings must be established with program leadership; they are not present today.

## How work enters a sprint

The Scrum Master coordinates story creation with engineering leads and the Product Owner. Each story identifies its parent epic, applicable SOW clauses, control and requirement IDs, dependencies, acceptance criteria, and expected deliverables.

| Story purpose | Expected completion evidence |
|---|---|
| Research | Sources, exact hardware/software applicability, findings, unresolved questions and recommendation |
| Requirements | Reviewed measurable requirements, SOW mapping and planned verification method |
| Implementation | Reviewed configuration or code, deployment record and change approval |
| Verification | Executed procedure, expected versus actual results, artifacts, reviewer and disposition |

A research story can finish with a documented finding that a capability is unsupported. Closing that story does not mean the associated security requirement is satisfied.

## How the tools work together

- **Confluence:** Management briefing, architecture summaries, decisions and delivery dashboards, linked to authoritative engineering records.
- **Jira:** Epics, stories, dependencies, ownership, acceptance criteria and links to delivered artifacts.
- **Repository:** Versioned architecture, stable identifiers, requirements, test procedures and automated documentation checks.
- **Approved evidence storage:** Durable artifacts with access controls, linked to test results and the exact implementation version tested.

**Recommended first increment:** Select one SOW obligation and one representative access scenario. Map the obligation, confirm hardware and design inputs, create the linked story set, implement the selected controls, and demonstrate reviewed evidence.

## Manual Jira traceability available now

The repository now provides optional **Jira epic** links on control rows, **Jira stories** on requirement and test rows, and **Verification stories** on future evidence rows. The example path can therefore be followed from a requirement to its delivery work, down to its tests, and then to the stories and artifacts supporting actual execution.

Program teams enter real links manually after issues are created and put the corresponding engineering IDs, SOW reference and repository baseline into each Jira description. Engineering owners maintain the table references; the Scrum Master coordinates story creation and the review cycle. Jira remains the source for assignees, sprints and delivery status.

This capability needs no software-factory integration or API access. Local checks validate declared link structure and consistency; reviewers confirm issue existence, purpose and reciprocal references. Authoritative cells remain blank until actual issues exist. The [use-case examples](zta-macsec-use-case.md#manual-jira-links-in-the-tables) are fictional, and the [manual Jira standard](standards/manual-jira-traceability.md) defines the working agreement.

Use [How to use this project](HOW-TO-USE.md) for the working process and its single [program adoption checklist](HOW-TO-USE.md#program-adoption-checklist) for agreements and approval references. Story completion, technical verification and contractual acceptance remain separate review outcomes. Live synchronization is a future option subject to software-factory approval.

**Management value:** Visibility from contractual obligation to delivered capability—and a clear distinction between work completed, requirements satisfied and results awaiting acceptance. The current repository is a foundation for that process; it does not yet demonstrate deployed ZTA or contractual compliance.

## Appendix A — Walking the MACsec traceability path

The path **ZT-05 → NET-04 → MAC-001 → TEST-003** crosses five documents, moving from an engineering responsibility to a proposed verification test. Read them in this order.

### 1. README — Define the pillar

The [Seven pillars table](README.md#seven-pillars) formally defines `ZT-05` as **Network & Environment**, with Network Engineering as its proposed owner.

It answers: **Which part of the architecture owns this concern?**

### 2. ZT-05 pillar document — Find the control

The [Network & Environment control index](pillars/ZT-05-network-environment.md#control-index) identifies the protections within that responsibility area. One entry links to `NET-04`, MACsec Ethernet link protection.

This document provides navigation and scope; the control’s authoritative definition lives in the next document.

It answers: **Which control addresses Ethernet link protection?**

### 3. MACsec control overview — Establish the protection objective

The [MACsec control overview](controls/macsec/overview.md) explicitly declares `ZT-05 → NET-04` in its control table.

It describes the objective of protecting wired Ethernet links, the need to verify exact equipment combinations, and the handling of unsupported links. Its status is **Required objective / Verify**.

It answers: **What protection are we trying to establish, and what are its boundaries?**

### 4. MACsec requirements — Identify the measurable obligation

The [MACsec requirements table](controls/macsec/requirements.md) explicitly declares `NET-04 → MAC-001`.

`MAC-001` requires identifying MACsec-capable ports. Its expected acceptance evidence includes exact SKU, module, port, software release, license, media, link speed, adjacent peer, and reviewed vendor sources.

It answers: **What specific obligation must engineering satisfy?**

### 5. MACsec verification plan — Define the demonstration

The [MAC-001 tests](controls/macsec/verification.md#mac-001-tests) explicitly declare `MAC-001 → TEST-003`.

`TEST-003` covers the selected ISR module, ports, license and release, then establishing protected sessions with the actual adjacent peer and inspecting counters. It remains **Proposed and unexecuted**.

It answers: **How will we demonstrate this part of the requirement?**

MAC-001 also has `TEST-001`, covering equipment and port inventory across both sites. **TEST-003 alone does not cover the entire requirement.**

### Document identity and engineering identity

Document identities and engineering identities are separate. For example, the verification file has document ID `DOC-MAC-VERIFY`, while its tables define several tests. Frontmatter attaches the file to its scope; table rows establish the individual engineering relationships.

### Turning the path into work

For the Scrum Master, these documents provide the source material for linked work:

| Work to organize | Primary engineering input |
|---|---|
| Research exact equipment compatibility | MAC-001 and [procurement assessments](procurement/macsec-equipment-assessment.md) |
| Refine and review acceptance criteria | MAC-001’s acceptance-evidence description |
| Configure the selected ISR and peer | NET-04, approved requirements and research findings |
| Execute verification and gather proof | TEST-003 and the evidence-record instructions |

The next link—**TEST-003 → reviewed evidence**—does not exist yet. The [evidence instructions](controls/macsec/verification.md#evidence-and-execution) explain how to record actual results and artifacts once execution occurs. The SOW mapping must also be added above this engineering chain.
