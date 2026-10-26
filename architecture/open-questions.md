---
schema_version: 1
id: DOC-ARCH-QUESTIONS
title: Open engineering questions
document_type: architecture
parent: ROOT
lineage:
- ROOT
owner: Architecture / all pillar owners
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# Open engineering questions

The following details require additional specification.

| Item | Outstanding question |
|---|---|
| Catalyst hardware | Exact 9300/9400 SKUs, uplinks, line cards and IOS XE releases? |
| ISR routers | Exact ISR 4000 models, interfaces, modules and licenses? |
| Palo Alto | Exact models, interfaces, PAN-OS versions and tunnel configuration? |
| MACsec | Which physical ports and endpoint combinations can support mandatory encryption? |
| Windows 11 | Which MACsec supplicant/NIC model and deployment approach? |
| RHEL 9 | Which MACsec implementation, hardware acceleration and interoperability model? |
| Virtualization | How are host uplinks, management VMs and virtual networks isolated? |
| VLANs | What is the actual list of VLANs and allowed inter-VLAN communication matrix? |
| Identity services | Where are AD, PKI, RSA, ISE and PAM hosted and how are they integrated? |
| Telemetry | Which log collection and SIEM tools are available? |
| Automation | Which response integrations are implemented or proposed? |
| Data protection | What classification, auditing and encryption requirements apply? |
| Encryption | What cipher suites, key management and compliance requirements are mandated? |

These unknowns should not be filled in by assumption.

Record answers with a source, responsible reviewer and resulting decision or requirement. Unknowns must not become assumed inventory or supported capabilities.
