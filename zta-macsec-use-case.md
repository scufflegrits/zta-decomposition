---
schema_version: 1
id: DOC-ZTA-MACSEC-USE-CASE
title: MACsec delivery use case — From SOW to reviewed evidence
document_type: guide
parent: NET-04
lineage: [ROOT, ZT-05, NET-04]
owner: Architecture / Security Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-25'
---

# MACsec delivery use case — From SOW to reviewed evidence

This worked example supports the [management briefing](zta-management-briefing.md). It shows how zta-decomposition can supply engineering content for the program’s AGIIL delivery process, Confluence and Jira.

**Example status:** SOW-001 below is illustrative wording for this use case, not an approved contractual requirement. The SOW mapping, backlog and acceptance workflow are proposed. Referenced controls, requirements and tests already exist in the repository; selected hardware, Jira issues, executed tests and evidence do not.

## How one table expands into the next

Start with a table of broad responsibilities. Select one row, carry its identifier down as the parent of a new table, and define the smaller responsibilities needed to fulfill it. Repeat until the work can be tested. The identifier connects the tables; each child table supplies new detail.

The tables below are a reading aid summarizing existing definitions. Bold rows show the branch being followed. They do not declare duplicate engineering entities.

### A. Start with the seven pillars

The [README pillar table](README.md#seven-pillars) defines seven rows under ROOT:

| Parent reference | Row reference | Responsibility |
|---|---|---|
| ROOT | ZT-01 | User |
| ROOT | ZT-02 | Device |
| ROOT | ZT-03 | Application & Workload |
| ROOT | ZT-04 | Data |
| **ROOT** | **ZT-05** | **Network & Environment — select this row** |
| ROOT | ZT-06 | Automation & Orchestration |
| ROOT | ZT-07 | Visibility & Analytics |

**Pull down ZT-05.** Ask: What controls make up Network & Environment? ZT-05 becomes the parent reference for the next table.

### B. Expand the selected pillar into controls

| Parent reference | Row reference | Control |
|---|---|---|
| ZT-05 | NET-01 | Network admission and VLAN policies |
| ZT-05 | NET-02 | Selective inter-VLAN routing |
| ZT-05 | NET-03 | Inter-site security enforcement |
| **ZT-05** | **NET-04** | **MACsec Ethernet link protection — select this row** |
| ZT-05 | NET-05 | Proposed WAN transport protection |
| ZT-05 | NET-06 | Local management isolation |

The [ZT-05 document](pillars/ZT-05-network-environment.md#control-index) collects links to these controls. Their authoritative definitions are distributed across the [network control overview](controls/network-segmentation/overview.md), [MACsec overview](controls/macsec/overview.md) and [management-isolation overview](controls/management-isolation/overview.md). The consolidated view above is for explanation.

**Pull down NET-04.** Ask: What specific obligations must MACsec satisfy? NET-04 becomes the parent reference for the next table. NET-01, NET-02 and the other siblings follow their own branches; they do not become MACsec requirements.

### C. Expand the selected control into requirements

The [MACsec requirements table](controls/macsec/requirements.md) expands NET-04:

| Parent reference | Row reference | Requirement |
|---|---|---|
| **NET-04** | **MAC-001** | **Identify MACsec-capable ports — select this row** |
| NET-04 | MAC-002 | Verify supported cipher suites |
| NET-04 | MAC-003 | Validate MKA interoperability |
| NET-04 | MAC-004 | Reject unintended plaintext fallback |
| NET-04 | MAC-005 | Meet required link throughput |
| NET-04 | MAC-006 | Provide useful operational telemetry |

The actual table also records acceptance evidence and status. Those columns explain what would satisfy each obligation; they do not replace the parent/child relationship.

**Pull down MAC-001.** Ask: Which tests demonstrate port and equipment compatibility? MAC-001 becomes the parent reference for the next table.

### D. Expand the selected requirement into tests

The [MAC-001 test table](controls/macsec/verification.md#mac-001-tests) contains two children:

| Parent reference | Row reference | Test |
|---|---|---|
| MAC-001 | TEST-001 | Exact equipment and port inventory across both sites |
| **MAC-001** | **TEST-003** | **ISR 4000 MACsec verification — select this row** |

**Pull down TEST-003 when execution occurs.** Its evidence table will contain actual evidence records, each with TEST-003 as its parent and its own unique Evidence ID, artifact link, result and reviewer. No evidence rows are created in advance. A failed result remains part of the history; it does not prove satisfaction.

MAC-002 through MAC-006 have their own test tables in the same verification document. Keeping those tables separate preserves each test’s immediate requirement parent.

### What is carried down, and what is added?

At every expansion, the selected row’s ID becomes the next table’s parent. Its full ancestry is retained in table metadata. New child rows receive new stable IDs and more specific content. For the MAC-001 test table, the metadata states:

```text
parent = MAC-001
lineage = ROOT > ZT-05 > NET-04 > MAC-001
```

The table then defines TEST-001 and TEST-003 under that parent. The parent requirement remains defined once in the requirements document. The auditor checks the declared IDs, parents and ancestry; engineering reviewers determine whether the decomposition is complete and the tests are sufficient.

The same pattern applies to every pillar, but the repository currently develops the MACsec branch most fully. The other pillar documents provide starting scopes and references; they do not yet all contain equivalent detailed requirements and test tables.

SOW-001 and Jira stories connect to this structure through references. A story may address several rows, and a requirement may need several stories. They do not change the engineering parent IDs. For example, a research story references MAC-001, while a verification story references TEST-003 and the artifacts produced by its execution.

## 1. Proposed SOW-001 — MACsec implementation

> The Contractor shall engineer, implement, and verify Media Access Control Security (MACsec) protection for wired Ethernet links at Site A and Site B in accordance with the program-approved Zero Trust Architecture. The solution shall provide link confidentiality and integrity, authenticated peer key agreement, approved cryptographic profiles, prevention of unauthorized plaintext fallback, and operational telemetry sufficient to demonstrate protection status and support incident investigation.
>
> The Contractor shall identify the hardware, interfaces, software, licensing, and peer dependencies necessary to meet the required coverage; document unsupported links; and submit proposed remediation or exceptions with compensating controls for approval by the designated program authority. The Contractor shall deliver traceable requirements, reviewed design and configuration records, verification procedures, execution results, and supporting artifacts demonstrating satisfaction of the approved requirements and performance criteria. MACsec shall complement the architecture’s identity, device, segmentation, application, and data controls; link protection shall not itself constitute authorization to access a resource.

Before adoption, program leadership must confirm coverage, applicable standards and cryptographic policy, numeric performance targets, deliverables, exception authority and acceptance authority. Unsupported links remain unmet scope until remediated or formally dispositioned; they are not silently removed from coverage.

## 2. Connect the obligation to existing engineering definitions

**Proposed program mapping:** `SOW-001 → delivery epic → ZT-05 → NET-04 → MAC-001…MAC-006 → tests → reviewed evidence → program acceptance`.

The epic organizes delivery. The existing engineering ancestry remains `ROOT → ZT-05 → NET-04 → requirements → tests → evidence`; SOW and Jira relationships supplement it rather than changing entity parents.

| Existing engineering reference | Contribution to SOW-001 | Verification reference |
|---|---|---|
| ZT-05 and NET-04 | Network responsibility and MACsec protection objective | Entire MACsec verification plan |
| MAC-001 | Exact port, equipment and peer compatibility | TEST-001: inventory; TEST-003: ISR verification |
| MAC-002 | Supported, approved cipher and protection profile | TEST-002 |
| MAC-003 | Peer key agreement and lifecycle interoperability | TEST-004 |
| MAC-004 | Rejection of unintended plaintext fallback | TEST-005 |
| MAC-005 | Approved throughput, latency and MTU criteria | TEST-006 |
| MAC-006 | Useful session, counter and failure telemetry | TEST-007 |

Use the authoritative [pillar](pillars/ZT-05-network-environment.md), [control](controls/macsec/overview.md), [requirements](controls/macsec/requirements.md) and [verification plan](controls/macsec/verification.md). This table references those entities and does not redefine them. Engineering must review whether the existing requirements fully cover the adopted SOW wording and add missing decomposition through review.

## 3. Organize delivery in Jira

**Proposed epic:** Implement and demonstrate MACsec coverage for SOW-001 at both sites.

The Product Owner prioritizes the work; the Scrum Master coordinates story creation and dependencies with engineering leads. The following are suggested story groups, not existing Jira issues or a requirement to fit all work into one sprint. Split them by site, link or equipment combination when needed.

| Story group | Engineering inputs | Acceptance criteria and deliverables |
|---|---|---|
| Research compatibility | MAC-001; procurement questionnaire; vendor research | Inventory every in-scope link and both peers; identify exact equipment/software/licensing; provide reviewed vendor findings and an unsupported-link disposition proposal |
| Baseline requirements and design | SOW-001; NET-04; MAC-001 through MAC-006 | Review SOW coverage; approve protection profiles, permitted protocol exceptions, numeric performance criteria, design and verification procedures; identify authorities and remaining dependencies |
| Implement selected links | Approved design and applicable MAC requirements | Complete the approved change; retain reviewed configuration and equipment/version records; perform agreed implementation checks; link remaining verification work |
| Verify and assemble proof | TEST-001 through TEST-007, as applicable to the selected scope | Execute approved procedures; record expected and actual results, raw artifacts, failures, retests and reviewer disposition; demonstrate coverage of the approved requirements |

Each story should carry the SOW reference, epic link, relevant engineering IDs, repository baseline, scope, owner, dependencies, acceptance criteria and artifact location. Store these as agreed Jira fields or a consistent story template. No Jira or Confluence integration is currently automated by this repository.

A research story may close with an unsupported-capability finding. An implementation story may close after its approved configuration work while verification remains open. Neither closure alone establishes requirement satisfaction or SOW acceptance.

### Manual Jira links in the tables

The repository now supports these optional columns without Jira API access. The following tables are **fictional examples**: `ZTA` is a sample project key, and `jira.example.invalid` is a deliberately non-operational address. No issues have been created. These descriptive tables reference engineering entities; they do not redefine them or populate the authoritative tables, whose Jira cells remain blank.

Start with the control row and its delivery epic:

| Parent reference | Control reference | Control | Jira epic |
|---|---|---|---|
| ZT-05 | NET-04 | MACsec Ethernet link protection | [ZTA-100](https://jira.example.invalid/browse/ZTA-100) |

Pull down NET-04 into the requirement table. Attach the stories doing work directly against each requirement:

| Parent reference | Requirement reference | Requirement | Jira stories |
|---|---|---|---|
| NET-04 | MAC-001 | Identify MACsec-capable ports | [ZTA-101](https://jira.example.invalid/browse/ZTA-101), [ZTA-102](https://jira.example.invalid/browse/ZTA-102) |
| NET-04 | MAC-002 | Verify supported cipher suites | [ZTA-103](https://jira.example.invalid/browse/ZTA-103) |

Pull down MAC-001 into its test table. Attach the work specific to those tests:

| Parent reference | Test reference | Test | Jira stories |
|---|---|---|---|
| MAC-001 | TEST-001 | Equipment and port inventory | [ZTA-104](https://jira.example.invalid/browse/ZTA-104) |
| MAC-001 | TEST-003 | ISR MACsec verification | [ZTA-105](https://jira.example.invalid/browse/ZTA-105), [ZTA-106](https://jira.example.invalid/browse/ZTA-106) |

The story purpose stays in Jira. In this example the proposed work is:

| Fictional issue key | Proposed purpose | Engineering references |
|---|---|---|
| ZTA-100 | Coordinate MACsec delivery for illustrative SOW-001 | NET-04 and the applicable requirements |
| ZTA-101 | Research the exact Catalyst/ISR peer combination | MAC-001 |
| ZTA-102 | Review compatibility scope and acceptance criteria | MAC-001 |
| ZTA-103 | Define and review the approved protection profile | MAC-002 |
| ZTA-104 | Complete and review both-site equipment inventory | MAC-001, TEST-001 |
| ZTA-105 | Configure the selected link and prepare verification | MAC-001, TEST-003; other requirements as applicable |
| ZTA-106 | Execute ISR verification and submit actual artifacts for review | MAC-001, TEST-003 |

These stories illustrate one branch of the backlog; additional work and tests are needed for MAC-002 through MAC-006 and the full SOW scope. The epic and issue relationships must also be recorded in Jira. A story can reference several engineering rows, and a row can reference several stories. Parent IDs and engineering ancestry stay unchanged.

When TEST-003 is actually executed, its evidence records can include ZTA-106 in `Verification stories`, alongside the real Evidence ID, artifact, result and reviewer. Do not create an evidence row merely to hold a planned story. A Jira link alone is not an execution artifact.

### A reciprocal Jira story example

For fictional ZTA-106, a proposed Jira description could contain:

```text
SOW reference: illustrative SOW-001 (replace with adopted clause/source)
Delivery epic: ZTA-100
Engineering references: NET-04, MAC-001, TEST-003
Source documents: controls/macsec/requirements.md; controls/macsec/verification.md
Engineering baseline: <approved repository commit or release and document links>
Scope: <selected Site A link, exact peers, ports, software and configuration revision>
Dependencies: reviewed compatibility findings, approved profile and configuration
Acceptance: execute the approved TEST-003 procedure; record expected/actual results;
            provide session/counter artifacts and reviewer disposition;
            create actual evidence records and link unresolved failures/retests
Artifact location: <approved durable storage location>
Reviewer: <program-designated engineering reviewer>
```

The Scrum Master coordinates creation and dependencies. The engineering owner adds the actual issue links to the repository and a reviewer checks both directions. Jira holds story status, assignee, sprint and estimates. The repository holds engineering definitions and technical validation status. The [manual Jira standard](standards/manual-jira-traceability.md) defines link syntax and maintenance responsibilities.

Local checks validate the declared links on authoritative entity rows; they do not contact Jira, verify these fictional examples, confirm issue type/status or prove acceptance. Software-factory access is only needed for future live checks or synchronization.

## 4. Follow one link down to proof

For a selected Catalyst-to-ISR link at Site A, use `SOW-001 → ZT-05 → NET-04 → MAC-001 → TEST-003` as the example reference path. The delivery epic and stories link to that path.

Research first identifies the exact ports, modules, software, licenses and peer combination. Engineering then approves the configuration and protection profile. Implementation produces the actual configuration record. Verification executes TEST-003 against the selected ISR and adjacent peer, establishing protected sessions and examining counters.

The resulting evidence record must identify the test, exact link and equipment, tested configuration revision, date, executor, expected and actual results, raw artifact locations and reviewer. Preserve failed executions and retests. Assign an Evidence ID only when an actual record is created, following the [evidence instructions](controls/macsec/verification.md#evidence-and-execution).

Evidence may include reviewed compatibility findings, configuration exports, session/counter captures and a signed or otherwise approved test report. Use approved storage and retain durable artifact identifiers. For externally stored artifacts, the current auditor requires a local evidence record; its existence check does not authenticate the external artifact or establish that it proves the claim.

Passing TEST-003 supports the ISR portion of MAC-001. It does not establish all-site inventory coverage, plaintext-fallback behavior, performance or complete satisfaction of SOW-001. Those claims require the other applicable tests and reviewed evidence.

## 5. Present progress and request acceptance

Confluence can present a summary linking SOW-001, the epic, engineering definitions, selected hardware, requirement coverage, test results, artifacts, exceptions and outstanding decisions. Jira tracks delivery state; the repository retains versioned engineering definitions; approved evidence storage retains execution artifacts.

Before requesting acceptance, engineering should demonstrate that every in-scope link and requirement has reviewed results or an explicitly approved disposition. The designated program authority determines acceptance against the adopted SOW and agreed criteria. A passing documentation audit verifies declared consistency; it does not establish contractual acceptance or deployed security behavior.

## 6. Decisions needed to adopt the example

Use the single [program adoption checklist](HOW-TO-USE.md#program-adoption-checklist) to record decisions and approval references before adopting this illustrative workflow. [How to use this project](HOW-TO-USE.md) provides the operational steps; this document supplies the worked example.

The [documentation TODO](TODO.md) links to that checklist and separately tracks future software-factory integration work.

**Value demonstrated:** zta-decomposition gives management a reviewable path from an obligation to specific work, and gives the delivery team concrete engineering references for producing the proof that obligation requires.
