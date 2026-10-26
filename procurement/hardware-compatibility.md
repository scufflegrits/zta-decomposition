# Hardware compatibility findings

<!-- zta-doc: id=DOC-PROC-COMPAT; parent=NET-04; lineage=ROOT>ZT-05>NET-04 -->

**Owner (proposed):** Procurement / Network Engineering  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

**Status:** Verify. These findings are copied from the October 24, 2026 handoff, not independently revalidated here. They do not establish a supported installation. See [vendor research](../references/vendor-research.md) for source IDs and versions.


| Vendor/product | Finding | Design consequence |
|---|---|---|
| Catalyst 9300 | C9300-48UXM and C9300-48UN support MACsec on their first 16 downlinks and applicable uplink-module ports, not the remaining 32 downlinks | Require model-specific port inventories |
| Catalyst 9400 | Support varies with supervisor and line-card combinations; C9400-SUP-1XL-Y supervisor ports do not support MACsec | Verify every selected module/port |
| Cisco ISR 4000 | Cisco identifies the NIM-2GE-CU-SFP as MACsec-capable; built-in front-panel GE ports are not listed as MACsec-capable in the referenced module comparison | Validate modules and licensing |
| Windows 11 | Cisco Secure Client Network Access Manager documents Windows IEEE 802.1AE support | Validate endpoint software and NIC performance |
| RHEL 9 | Red Hat documents Linux MACsec configuration | Validate interoperable MKA and throughput |
| Palo Alto | Documented MACsec support exists for specific HSCI NGFW cluster links | Do not assume ordinary firewall dataplane ports support MACsec |

These are vendor-document findings, not proof that a particular proposed installation is compatible.


The inventory must cover both ends of every endpoint, host, switch, router and firewall link. Include supervisor/line-card dependencies, partial-port restrictions, media, speed, software, licenses, MKA, cipher support and hardware acceleration. Record exceptions with owner, rationale, compensating controls, approval and review date.
