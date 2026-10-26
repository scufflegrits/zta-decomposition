---
schema_version: 1
id: DOC-ZTA-README
title: Zero Trust Architecture Decomposition
document_type: navigation
parent: ROOT
lineage:
- ROOT
owner: Architecture / Security Engineering
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-24'
---

# Zero Trust Architecture Decomposition

This repository documents a proposed two-site Zero Trust Architecture organized around the seven DoD pillars. It is a reference design, not an as-built configuration or compliance certification.

## Start here

Read [How to use this project](HOW-TO-USE.md) for the working process, proposed roles and the single [program adoption checklist](HOW-TO-USE.md#program-adoption-checklist).

Browse the complete [document index](index.md) or the [visual taxonomy](taxonomy.md). Outstanding documentation work is tracked in [TODO](TODO.md).

For a self-contained introductory review, read the [ZTA Project Guide](zta-project-guide.md), with network and MACsec traceability diagrams.

- [Architecture overview](architecture/overview.md), [physical topology](architecture/physical-topology.md), [site-local design](architecture/logical-topology.md), and [control overlay](architecture/seven-pillar-control-overlay.md).
- [Architecture decisions](architecture/decisions/README.md) and [documentation conventions](standards/documentation-conventions.md).
- [Management briefing](zta-management-briefing.md), [MACsec delivery use case](zta-macsec-use-case.md), and [manual Jira traceability](standards/manual-jira-traceability.md).
- [MACsec overview](controls/macsec/overview.md), [requirements](controls/macsec/requirements.md), and [verification plan](controls/macsec/verification.md).
- [Equipment assessment](procurement/macsec-equipment-assessment.md), [compatibility findings](procurement/hardware-compatibility.md), [vendor research](references/vendor-research.md), and [standards references](references/standards.md).
- [Open engineering questions](architecture/open-questions.md) and [implementation roadmap](architecture/roadmap.md).

## Repository layout

| Location | Contents |
|---|---|
| `architecture/` | Architecture views, decisions, open questions and implementation roadmap |
| `pillars/` | Responsibilities and control references for each of the seven pillars |
| `controls/` | Authoritative control definitions; MACsec includes detailed requirements and verification procedures |
| `procurement/` | Equipment assessments and compatibility findings awaiting verification |
| `references/` | Standards references and vendor research |
| `standards/` | Documentation, traceability and Mermaid conventions; diagram verification record |
| `tools/` and `tests/` | Documentation auditor and regression tests |

## Seven pillars

<!-- zta-table: id=TBL-ZT-PILLARS; parent=ROOT; lineage=ROOT -->

| Parent ID | Pillar ID | Pillar | Primary technologies | Proposed owner |
|---|---|---|---|---|
| ROOT | ZT-01 | [User](pillars/ZT-01-user.md) | AD, PKI access cards, RSA tokens, PAM | Identity/IAM |
| ROOT | ZT-02 | [Device](pillars/ZT-02-device.md) | Cisco ISE, IEEE 802.1X, Catalyst | Endpoint Engineering |
| ROOT | ZT-03 | [Application & Workload](pillars/ZT-03-application-workload.md) | Windows, RHEL, vendor-neutral VMs | Systems/Virtualization |
| ROOT | ZT-04 | [Data](pillars/ZT-04-data.md) | AD permissions, file/database permissions, encryption | Data Security |
| ROOT | ZT-05 | [Network & Environment](pillars/ZT-05-network-environment.md) | Catalyst, ISR, Palo Alto, MACsec, proposed IPsec | Network Engineering |
| ROOT | ZT-06 | [Automation & Orchestration](pillars/ZT-06-automation-orchestration.md) | Proposed ISE CoA, PAM workflows and response integrations | Security Engineering |
| ROOT | ZT-07 | [Visibility & Analytics](pillars/ZT-07-visibility-analytics.md) | Identity, endpoint, network, PAM and workload logs | SOC/Detection Engineering |

## Method

Functional decomposition divides architecture by responsibility. Hierarchical traceability links `Pillar → Control → Requirement → Test → Evidence` using stable identifiers and full ancestry. Docs-as-code uses Markdown, Mermaid, version control and automated consistency checks. Each control has one authoritative definition; other pillars link to it.

## Established constraints

Users must be physically present at Site A or Site B to initiate authorized authentication. No off-site remote-user authentication is exposed from the WAN. Authorized inter-site resource access and authentication service traffic remain separate policy decisions.

Each site preserves `Catalyst → ISR → Palo Alto → public WAN`. ISRs provide selected authorized inter-VLAN routing. Management VLANs are site-local, isolated, non-routed and never stretched over the WAN. Approved management access uses a physical management switchport or an approved VM with exactly one management-connected vNIC; host isolation must also be verified.

Virtualization stays vendor-neutral. MACsec on every wired Ethernet port is a required objective subject to compatibility verification or explicit exceptions. Palo Alto IPsec is a proposed WAN protection mechanism. Connectivity and encryption never imply authorization.

## Status and integrity

`Required` records an established requirement; `Proposed` an unfinished design; `Verify` an unconfirmed capability; `Validated` requires reviewed test evidence. Nothing in this scaffold asserts a validated installation.

From the repository root, run the auditor and its regression tests with Python 3.10 or newer. Install the Python dependencies once, then run the checks:

```bash
python3 -m pip install -r requirements.txt
python3 tools/generate_index.py --root . --check
python3 tools/audit_zta.py --root . --report audit-report.md
python3 -m unittest discover -s tests -v
```

See [auditor usage and limits](tools/README.md). The report is generated output. The original [handoff](zta-decomposition-handoff.md) and supplied [Mermaid guide](references/guides/mermaid-best-practices-r1.0.6.md) are source references; the modular documents are the working definitions.

Maintain diagrams using the [project Mermaid standard r1.0.6](standards/mermaid-best-practices-r1.0.6.md), including CSS named colors. The four network and project-guide Mermaid blocks rendered successfully to SVG and PNG and were visually reviewed on October 25, 2026. Title/edge crossings remain to be refined before publication, and the intended presentation viewer remains untested. See the [diagram verification record](standards/diagram-verification.md) for scope and findings, including the taxonomy review. The documentation auditor does not parse or render Mermaid, and neither check validates security controls.

## Version control

The Git repository is initialized. The `master` branch tracks `main/master`, where `main` is the remote name. The configured remote is [scufflegrits/zta-decomposition](https://github.com/scufflegrits/zta-decomposition), using `git@github.com:scufflegrits/zta-decomposition.git` for fetch and push.

Review changes before committing and run the documentation auditor and regression tests above. Program adoption agreements are tracked in the [central checklist](HOW-TO-USE.md#program-adoption-checklist).
