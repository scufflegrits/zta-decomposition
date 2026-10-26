---
schema_version: 1
id: DOC-MAC-VERIFY
title: MACsec verification plan
document_type: verification
parent: NET-04
lineage:
- ROOT
- ZT-05
- NET-04
owner: Network / Endpoint Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# MACsec verification plan

**Ancestry:** `ROOT > ZT-05 > NET-04`. [Parent control](overview.md); [requirements](requirements.md).

All tests are Proposed and unexecuted. TEST-003 retains its handoff meaning and MAC-001 parent. Numeric performance targets, approved cipher profiles and selected peers are prerequisites, not assumed defaults.

## MAC-001 tests

**Ancestry:** `ROOT > ZT-05 > NET-04 > MAC-001`.

<!-- zta-table: id=TBL-MAC-001-TESTS; parent=MAC-001; lineage=ROOT>ZT-05>NET-04>MAC-001 -->

| Parent ID | Test ID | Test | Procedure / acceptance basis | Status |
|---|---|---|---|---|
| MAC-001 | TEST-001 | Exact equipment and port inventory | Compare both sites against vendor matrices and the actual bill of materials; identify every unsupported link. | Proposed |
| MAC-001 | TEST-003 | ISR 4000 MACsec verification | Verify selected ISR module, ports, license and release; establish protected sessions with the actual adjacent peer and inspect counters. | Proposed |

## MAC-002 tests

**Ancestry:** `ROOT > ZT-05 > NET-04 > MAC-002`.

<!-- zta-table: id=TBL-MAC-002-TESTS; parent=MAC-002; lineage=ROOT>ZT-05>NET-04>MAC-002 -->

| Parent ID | Test ID | Test | Procedure / acceptance basis | Status |
|---|---|---|---|---|
| MAC-002 | TEST-002 | Cipher and protection configuration | Inspect both peers and negotiate the approved cipher, replay and confidentiality profile; reject incompatible profiles. | Proposed |

## MAC-003 tests

**Ancestry:** `ROOT > ZT-05 > NET-04 > MAC-003`.

<!-- zta-table: id=TBL-MAC-003-TESTS; parent=MAC-003; lineage=ROOT>ZT-05>NET-04>MAC-003 -->

| Parent ID | Test ID | Test | Procedure / acceptance basis | Status |
|---|---|---|---|---|
| MAC-003 | TEST-004 | Peer and MKA lifecycle | Exercise each selected endpoint/switch/router pairing, rekey, peer reboot and relevant trunk/aggregation combinations. | Proposed |

## MAC-004 tests

**Ancestry:** `ROOT > ZT-05 > NET-04 > MAC-004`.

<!-- zta-table: id=TBL-MAC-004-TESTS; parent=MAC-004; lineage=ROOT>ZT-05>NET-04>MAC-004 -->

| Parent ID | Test ID | Test | Procedure / acceptance basis | Status |
|---|---|---|---|---|
| MAC-004 | TEST-005 | Plaintext fallback rejection | Inject mismatched keys, invalid credentials, loss of negotiation and recovery; verify forbidden payload cannot pass unprotected. | Proposed |

## MAC-005 tests

**Ancestry:** `ROOT > ZT-05 > NET-04 > MAC-005`.

<!-- zta-table: id=TBL-MAC-005-TESTS; parent=MAC-005; lineage=ROOT>ZT-05>NET-04>MAC-005 -->

| Parent ID | Test ID | Test | Procedure / acceptance basis | Status |
|---|---|---|---|---|
| MAC-005 | TEST-006 | Throughput and MTU | Run representative traffic at approved numeric targets and packet sizes; capture throughput, latency, loss and CPU/acceleration data. | Proposed |

## MAC-006 tests

**Ancestry:** `ROOT > ZT-05 > NET-04 > MAC-006`.

<!-- zta-table: id=TBL-MAC-006-TESTS; parent=MAC-006; lineage=ROOT>ZT-05>NET-04>MAC-006 -->

| Parent ID | Test ID | Test | Procedure / acceptance basis | Status |
|---|---|---|---|---|
| MAC-006 | TEST-007 | Operational telemetry | Correlate protected sessions, rekey, failures and forbidden plaintext attempts with CLI/API counters and logs. | Proposed |

## Evidence and execution

For each execution record an immutable Evidence ID, immediate Test ID parent, complete ancestry, exact equipment/software/licensing, approved configuration and targets, date, executor, procedure, expected and actual results, raw artifact links, exception disposition and reviewer. Preserve failed results and retest history. Do not manufacture placeholder evidence rows or mark a test Validated because a plan exists.

When evidence is available, add a traceable table under its Test ID using columns `Parent ID | Evidence ID | Artifact | Result | Reviewer`. A validated requirement or test must explicitly reference evidence from its descendant test/evidence chain in an `Evidence IDs` column. Evidence artifacts must exist locally for the auditor's file check; external artifacts require a documented local evidence record. No evidence records exist yet.
