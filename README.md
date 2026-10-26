# Zero Trust Architecture Decomposition

<!-- zta-doc: id=DOC-ZTA-README; parent=ROOT; lineage=ROOT -->

**Owner (proposed):** Architecture / Security Engineering  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

This repository documents a proposed two-site Zero Trust Architecture organized around the seven DoD pillars. It is a reference design, not an as-built configuration or compliance certification.

## Start here

For a self-contained introductory review, read the [ZTA Project Guide](zta-project-guide.md), with network and MACsec traceability diagrams.

- [Architecture overview](architecture/overview.md), [physical topology](architecture/physical-topology.md), [site-local design](architecture/logical-topology.md), and [control overlay](architecture/seven-pillar-control-overlay.md).
- [Architecture decisions](architecture/decisions/README.md) and [documentation conventions](standards/documentation-conventions.md).
- [MACsec overview](controls/macsec/overview.md), [requirements](controls/macsec/requirements.md), and [verification plan](controls/macsec/verification.md).
- [Equipment assessment](procurement/macsec-equipment-assessment.md), [compatibility findings](procurement/hardware-compatibility.md), [vendor research](references/vendor-research.md), and [standards references](references/standards.md).
- [Open engineering questions](architecture/open-questions.md) and [implementation roadmap](architecture/roadmap.md).

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

Run the standard-library auditor and its regression tests:

```bash
python3 tools/audit_zta.py --root . --report audit-report.md
python3 -m unittest discover -s tests -v
```

See [auditor usage and limits](tools/README.md). The report is generated output. The original [handoff](zta-decomposition-handoff.md) and [Mermaid guide](mermaid-best-practices-r1.0.5.md) are preserved as provenance; the modular documents are the working definitions. This directory is not currently an initialized Git repository; version-control initialization and review workflows remain setup tasks.
