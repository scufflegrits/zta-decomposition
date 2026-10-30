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

## Project status

This repository is a documentation and traceability framework prototype for planning and demonstrating how the program could decompose Zero Trust Architecture (ZTA) work and connect it to delivery evidence.

The draft structure covers seven ZTA pillars, architecture decisions, control and requirement documents, a MACsec use case, verification planning, manual Jira traceability, implementation and acceptance registers, a management briefing, FAQ, project guide and Mermaid diagrams. The document index is generated from document metadata.

The intended trace runs from a contract SOW line item through ZTA pillars and controls to requirements, research, Jira stories, implementation evidence and a customer acceptance record. Jira links are manual for now. The project does not yet contain actual deployment or customer acceptance claims; populate the registers as program work occurs.

## Overall assessment

The documentation foundation and proposed workflow are well developed. The repository is ready for review and discussion with management and engineering stakeholders as a proposed approach. It is not yet a validated program process: owners, adoption decisions, authoritative SOW mapping, real evidence and customer acceptance still need to come from the program.

## Start here

Read [How to use this project](HOW-TO-USE.md) for the working process, proposed roles and the single [program adoption checklist](HOW-TO-USE.md#program-adoption-checklist).

Browse the complete [document index](index.md) or the [visual taxonomy](taxonomy.md). Outstanding documentation work is tracked in [TODO](900_project-admin/TODO.md).

For a self-contained introductory review, read the [ZTA Project Guide](zta-project-guide.md), with network and MACsec traceability diagrams.

- [Architecture overview](020_architecture/overview.md), [physical topology](020_architecture/physical-topology.md), [site-local design](020_architecture/logical-topology.md), and [control overlay](020_architecture/seven-pillar-control-overlay.md).
- [Architecture decisions](020_architecture/010_decisions/README.md) and [documentation conventions](090_standards/documentation-conventions.md).
- [ZTA decomposition briefing](zta-decomposition-briefing.md), [MACsec delivery use case](zta-macsec-use-case.md), and [manual Jira traceability](090_standards/manual-jira-traceability.md).
- [Questions and critical review](zta-decomposition-faq.md) for program leadership, engineering, architecture and delivery teams.
- [MACsec overview](030_controls/020_macsec/overview.md), [requirements](030_controls/020_macsec/requirements.md), and [verification plan](030_controls/020_macsec/verification.md).
- [Equipment assessment](070_procurement/macsec-equipment-assessment.md), [compatibility findings](070_procurement/hardware-compatibility.md), [vendor research](080_references/vendor-research.md), and [standards references](080_references/standards.md).
- [Implementation records](050_implementation/macsec.md), [customer acceptance decisions](010_acceptance/macsec.md), and [record rules](090_standards/implementation-acceptance.md).
- [Open engineering questions](020_architecture/open-questions.md) and [implementation roadmap](020_architecture/roadmap.md).

## Repository layout

| Location | Contents |
|---|---|
| `000_import/` | Inbox for material to bring into the project; staged files are not committed or audited. See its README |
| `010_acceptance/` | Customer disposition against applicable contract SOW requirements and decision artifacts |
| `020_architecture/` | Architecture views, decisions, open questions and implementation roadmap |
| `030_controls/` | Authoritative control definitions; MACsec includes detailed requirements and verification procedures |
| `040_images/` | Rendered diagrams and other images embedded by documents |
| `050_implementation/` | Actual deployed protections, limitations, operational impacts and verification references |
| `060_pillars/` | Responsibilities and control references for each of the seven pillars |
| `070_procurement/` | Equipment assessments and compatibility findings awaiting verification |
| `080_references/` | Standards references and vendor research; supplied guides under `010_guides/` |
| `090_standards/` | Documentation, traceability and Mermaid conventions; diagram verification record |
| `100_tests/` and `110_tools/` | Regression tests and the documentation auditor and index generator |
| `900_project-admin/` | Documentation backlog, migration plans and import log |

## Seven pillars

<!-- zta-table: id=TBL-ZT-PILLARS; parent=ROOT; lineage=ROOT -->

| Parent ID | Pillar ID | Pillar | Primary technologies | Proposed owner |
|---|---|---|---|---|
| ROOT | ZT-01 | [User](060_pillars/ZT-01-user.md) | AD, PKI access cards, RSA tokens, PAM | Identity/IAM |
| ROOT | ZT-02 | [Device](060_pillars/ZT-02-device.md) | Cisco ISE, IEEE 802.1X, Catalyst | Endpoint Engineering |
| ROOT | ZT-03 | [Application & Workload](060_pillars/ZT-03-application-workload.md) | Windows, RHEL, vendor-neutral VMs | Systems/Virtualization |
| ROOT | ZT-04 | [Data](060_pillars/ZT-04-data.md) | AD permissions, file/database permissions, encryption | Data Security |
| ROOT | ZT-05 | [Network & Environment](060_pillars/ZT-05-network-environment.md) | Catalyst, ISR, Palo Alto, MACsec, proposed IPsec | Network Engineering |
| ROOT | ZT-06 | [Automation & Orchestration](060_pillars/ZT-06-automation-orchestration.md) | Proposed ISE CoA, PAM workflows and response integrations | Security Engineering |
| ROOT | ZT-07 | [Visibility & Analytics](060_pillars/ZT-07-visibility-analytics.md) | Identity, endpoint, network, PAM and workload logs | SOC/Detection Engineering |

## Method

Functional decomposition divides architecture by responsibility. Hierarchical traceability links `Pillar → Control → Requirement → Test → Evidence` using stable identifiers and full ancestry. Docs-as-code uses Markdown, Mermaid, version control and automated consistency checks. Each control has one authoritative definition; other pillars link to it.

## Established constraints

Users must be physically present at Site A or Site B to initiate authorized authentication. No off-site remote-user authentication is exposed from the WAN. Authorized inter-site resource access and authentication service traffic remain separate policy decisions.

Each site preserves `Catalyst → ISR → Palo Alto → public WAN`. ISRs provide selected authorized inter-VLAN routing. Management VLANs are site-local, isolated, non-routed and never stretched over the WAN. Approved management access uses a physical management switchport or an approved VM with exactly one management-connected vNIC; host isolation must also be verified.

Virtualization stays vendor-neutral. Following [ADR-014](020_architecture/010_decisions/ADR-014.md), implement MACsec where supported and operationally appropriate without reducing required functionality or imposing undue process. Record hardware/workflow limitations, residual risk and customer disposition; acceptance is based on documented outcomes against the applicable SOW, not a coverage percentage. The earlier universal-port objective is preserved in ADR-008 for history. Palo Alto IPsec is a proposed WAN protection mechanism. Connectivity and encryption never imply authorization.

## Status and integrity

`Required` records an established requirement; `Proposed` an unfinished design; `Verify` an unconfirmed capability; `Validated` requires reviewed test evidence. Nothing in this scaffold asserts a validated installation.

From the repository root, run the auditor and its regression tests with Python 3.10 or newer. Install the Python dependencies once, then run the checks:

```bash
python3 -m pip install -r requirements.txt
python3 110_tools/generate_index.py --root . --check
python3 110_tools/audit_zta.py --root . --report audit-report.md
python3 -m unittest discover -s 100_tests -v
```

See [auditor usage and limits](110_tools/README.md). The report is generated output. The original [handoff](zta-decomposition-handoff.md) and supplied [Mermaid code conventions r1.0.7 guide](080_references/010_guides/mermaid-best-practices-r1.0.7.md) are source references; the modular documents are the working definitions.

Maintain diagrams using the [ZTA project Mermaid standard](090_standards/mermaid-best-practices-zta.md), including CSS named colors. The four network and project-guide Mermaid blocks rendered successfully to SVG and PNG and were visually reviewed on October 25, 2026. Title/edge crossings remain to be refined before publication, and the intended presentation viewer remains untested. See the [diagram verification record](090_standards/diagram-verification.md) for scope and findings, including the taxonomy review. The documentation auditor does not parse or render Mermaid, and neither check validates security controls.

## Version control

The Git repository is initialized. The `master` branch tracks `main/master`, where `main` is the remote name. The configured remote is [scufflegrits/zta-decomposition](https://github.com/scufflegrits/zta-decomposition), using `git@github.com:scufflegrits/zta-decomposition.git` for fetch and push.

Review changes before committing and run the documentation auditor and regression tests above. Program adoption agreements are tracked in the [central checklist](HOW-TO-USE.md#program-adoption-checklist).
