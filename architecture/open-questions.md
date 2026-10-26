# Open engineering questions

<!-- zta-doc: id=DOC-ARCH-QUESTIONS; parent=ROOT; lineage=ROOT -->

**Owner (proposed):** Architecture / all pillar owners  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

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
