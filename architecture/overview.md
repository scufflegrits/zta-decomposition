---
schema_version: 1
id: DOC-ARCH-OVERVIEW
title: Architecture overview
document_type: architecture
parent: ROOT
lineage:
- ROOT
owner: Architecture
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# Architecture overview

The design contains geographically separated Site A and Site B with comparable equipment classes: Catalyst 9300/9400 switches, ISR 4000 routers, Palo Alto firewalls, Windows servers, Windows 11 and RHEL 9 workstations, and generic virtualization hosts with multiple VMs.

Identity technologies include AD, PKI cards, RSA tokens, PAM, ISE and 802.1X. Their hosting locations and integrations are undecided. No availability, redundancy, IP addressing or licensing configuration is implied.

Read the [physical topology](physical-topology.md) for the required device sequence, [local logical design](logical-topology.md) for management and virtualization constraints, and [seven-pillar overlay](seven-pillar-control-overlay.md) for distinct enforcement responsibilities.

North-south traffic crosses a defined site boundary. East-west communication stays within the boundary under consideration. A physical link may carry both classifications at different boundaries. Same-VLAN, same-host VM and ISR-routed flows may avoid the Palo Alto firewall; enforcement must be placed on the actual path.

All [decisions](decisions/README.md) remain in force. Resolve [open questions](open-questions.md) before describing configurations as implemented or validated.
