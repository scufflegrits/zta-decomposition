---
schema_version: 1
id: DOC-SCRATCH-TABLE-DECOMPOSITION
title: Scratch — Following one cell down through the tables
document_type: guide
parent: ROOT
lineage: [ROOT]
owner: Architecture / Security Engineering
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-25'
---

# Scratch — Following one cell down through the tables

Read from top to bottom. **The bold ID cell is the one we pull down.** That ID becomes the parent of every row in the next table. The other rows remain available for their own separate expansions.

These are descriptive copies for illustration, not additional entity definitions. The final evidence table is an illustrative layout only; no execution or evidence is claimed.

## Tree view

Read each indentation as “is a child of.” This view expands ZT-05 and its MACsec branch; the other branches are shown by name. The same parent/child relationships appear in the tables below.

```text
ROOT — Zero Trust Architecture
├── ZT-01 — User
├── ZT-02 — Device
├── ZT-03 — Application & Workload
├── ZT-04 — Data
├── ZT-05 — Network & Environment
│   ├── NET-01 — Network admission and VLAN policies
│   ├── NET-02 — Selective inter-VLAN routing
│   ├── NET-03 — Inter-site security enforcement
│   ├── NET-04 — MACsec Ethernet link protection
│   │   ├── MAC-001 — Identify MACsec-capable ports
│   │   │   ├── TEST-001 — Equipment and port inventory
│   │   │   └── TEST-003 — ISR 4000 MACsec verification
│   │   │       └── Future evidence records — none created yet
│   │   ├── MAC-002 — Verify supported cipher suites
│   │   │   └── TEST-002 — Cipher and protection configuration
│   │   ├── MAC-003 — Validate MKA interoperability
│   │   │   └── TEST-004 — Peer and MKA lifecycle
│   │   ├── MAC-004 — Reject unintended plaintext fallback
│   │   │   └── TEST-005 — Plaintext fallback rejection
│   │   ├── MAC-005 — Meet required link throughput
│   │   │   └── TEST-006 — Throughput and MTU
│   │   └── MAC-006 — Provide useful operational telemetry
│   │       └── TEST-007 — Operational telemetry
│   ├── NET-05 — Proposed WAN transport protection
│   └── NET-06 — Local management isolation
├── ZT-06 — Automation & Orchestration
└── ZT-07 — Visibility & Analytics
```

The table walkthrough follows **ZT-05 → NET-04 → MAC-001 → TEST-003**. The future-evidence line shows where actual records will attach; it is not a declared entity. Every test can eventually have its own evidence records. All listed tests remain proposed and unexecuted.

## 1. Top table — The seven pillars

Source: [README pillar table](README.md#seven-pillars).

| Parent | Pillar reference | Pillar |
|---|---|---|
| ROOT | ZT-01 | User |
| ROOT | ZT-02 | Device |
| ROOT | ZT-03 | Application & Workload |
| ROOT | ZT-04 | Data |
| ROOT | **ZT-05** | Network & Environment |
| ROOT | ZT-06 | Automation & Orchestration |
| ROOT | ZT-07 | Visibility & Analytics |

↓ Pull **ZT-05** down. Expand Network & Environment into its controls.

## 2. ZT-05 becomes the parent — Network controls

Source: [ZT-05 control index](pillars/ZT-05-network-environment.md#control-index), linking to the authoritative control definitions.

| Parent | Control reference | Control |
|---|---|---|
| ZT-05 | NET-01 | Network admission and VLAN policies |
| ZT-05 | NET-02 | Selective inter-VLAN routing |
| ZT-05 | NET-03 | Inter-site security enforcement |
| ZT-05 | **NET-04** | MACsec Ethernet link protection |
| ZT-05 | NET-05 | Proposed WAN transport protection |
| ZT-05 | NET-06 | Local management isolation |

↓ Pull **NET-04** down. Expand MACsec into its requirements.

## 3. NET-04 becomes the parent — MACsec requirements

Source: [MACsec requirements](controls/macsec/requirements.md).

| Parent | Requirement reference | Requirement |
|---|---|---|
| NET-04 | **MAC-001** | Identify MACsec-capable ports |
| NET-04 | MAC-002 | Verify supported cipher suites |
| NET-04 | MAC-003 | Validate MKA interoperability |
| NET-04 | MAC-004 | Reject unintended plaintext fallback |
| NET-04 | MAC-005 | Meet required link throughput |
| NET-04 | MAC-006 | Provide useful operational telemetry |

↓ Pull **MAC-001** down. Expand port compatibility into its tests.

## 4. MAC-001 becomes the parent — Compatibility tests

Source: [MAC-001 tests](controls/macsec/verification.md#mac-001-tests).

| Parent | Test reference | Test |
|---|---|---|
| MAC-001 | TEST-001 | Exact equipment and port inventory across both sites |
| MAC-001 | **TEST-003** | ISR 4000 MACsec verification |

↓ Pull **TEST-003** down. After execution, attach its actual evidence records.

## 5. TEST-003 becomes the parent — Evidence from execution

Source: [Evidence instructions](controls/macsec/verification.md#evidence-and-execution). This is a future layout, not an existing evidence record.

| Parent | Evidence reference | Artifact | Actual result | Reviewer |
|---|---|---|---|---|
| TEST-003 | Assigned when the actual record is created | Actual configuration/session-counter artifacts or their local evidence record | Recorded after execution | Assigned reviewer’s disposition |

There is no further cell to pull down in this example. The artifacts and review support the test result. Passing this test supports part of MAC-001; the other applicable tests and requirements still need their own proof.

## What moved between the tables?

**ZT-05** → becomes the parent of the control rows.

**NET-04** → becomes the parent of the requirement rows.

**MAC-001** → becomes the parent of the test rows.

**TEST-003** → becomes the parent of actual evidence records.

Each expansion adds detail while preserving the selected ID and its ancestry. SOW references and Jira links attach to the relevant rows; they do not replace these parent relationships. See the [worked use case](zta-macsec-use-case.md) for those delivery links.

## Implementation and customer disposition view

The original tree shows engineering ancestry. This second view shows how actual delivery and customer records attach to the same control and reference the relevant engineering definitions. Example A and B are hypothetical outcomes; no operational records or approvals currently exist in the source registers.

```text
NET-04 — MACsec
├── Engineering definitions
│   └── MAC-001 → TEST-003 → actual execution evidence when available
├── Implementation records (reference requirements, tests and evidence)
│   ├── Example A — selected supported switch/router link
│   │   ├── Exact ports, installed router module and configuration baseline
│   │   ├── Implemented / Passed — hypothetical result with reviewed proof
│   │   └── Functional/workflow impact, residual risk and limitations recorded
│   └── Example B — identified unsupported ports
│       ├── Hardware finding and operational impact of replacement recorded
│       ├── Not implemented / Not executed — technical facts stay visible
│       └── Residual exposure and alternatives documented
└── Customer acceptance record (references implementation records)
    ├── Scope, applicable SOW, baseline, authority, date and decision artifact
    └── Accepted with documented limitations — hypothetical A+B disposition
```

In the authoritative hierarchy, implementation and acceptance rows are direct children of NET-04; engineering definitions retain their existing parents. Evidence remains under its test. The two organizational labels in the tree are navigation aids, not new engineering entities. Customer acceptance does not turn B into an encrypted link or a passed test.

For the corresponding table layout, see the [worked outcome example](zta-macsec-use-case.md#implementation-and-customer-disposition-example). Actual records belong in the [implementation register](implementation/macsec.md) and [acceptance register](acceptance/macsec.md). No percentage determines the acceptance decision.
