# Architecture overview

<!-- zta-doc: id=DOC-ARCH-OVERVIEW; parent=ROOT; lineage=ROOT -->

**Owner (proposed):** Architecture  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

The design contains geographically separated Site A and Site B with comparable equipment classes: Catalyst 9300/9400 switches, ISR 4000 routers, Palo Alto firewalls, Windows servers, Windows 11 and RHEL 9 workstations, and generic virtualization hosts with multiple VMs.

Identity technologies include AD, PKI cards, RSA tokens, PAM, ISE and 802.1X. Their hosting locations and integrations are undecided. No availability, redundancy, IP addressing or licensing configuration is implied.

Read the [physical topology](physical-topology.md) for the required device sequence, [local logical design](logical-topology.md) for management and virtualization constraints, and [seven-pillar overlay](seven-pillar-control-overlay.md) for distinct enforcement responsibilities.

North-south traffic crosses a defined site boundary. East-west communication stays within the boundary under consideration. A physical link may carry both classifications at different boundaries. Same-VLAN, same-host VM and ISR-routed flows may avoid the Palo Alto firewall; enforcement must be placed on the actual path.

All [decisions](decisions/README.md) remain in force. Resolve [open questions](open-questions.md) before describing configurations as implemented or validated.
