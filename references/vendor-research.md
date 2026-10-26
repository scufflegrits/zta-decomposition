---
schema_version: 1
id: DOC-REF-RESEARCH
title: Research register
document_type: reference
parent: ROOT
lineage:
- ROOT
owner: Architecture / Network Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# Research register

**Research status:** Handoff findings, Verify. Imported October 24, 2026. Vendor pages have not been fetched or revalidated during scaffolding. The handoff provides titles, URLs, version context and impacts; publication dates and exact bill-of-material applicability require source review. [Hardware findings](../procurement/hardware-compatibility.md) preserve the conclusions.

The following manufacturer and standards sources support the research findings recorded during the design discussions. They are references, not substitutes for verifying the final bill of materials.

### Standards and Zero Trust

**REF-001 — DoD Zero Trust Reference Architecture, Version 2.0**  
https://dodcio.defense.gov/Portals/0/Documents/Library/%28U%29ZT_RA_v2.0%28U%29_Sep22.pdf

**REF-002 — DoD Zero Trust Capability Execution Roadmap**  
https://dodcio.defense.gov/Portals/0/Documents/Library/ZTCapabilityExecutionRoadmap.pdf

**REF-003 — NIST SP 800-207, Zero Trust Architecture**  
https://doi.org/10.6028/NIST.SP.800-207

### Cisco

**REF-004 — Catalyst 9300 MACsec Configuration Guide, IOS XE 26.x**  
Includes restrictions for C9300-48UXM/C9300-48UN, EtherChannel member interfaces, cipher suites, and licensing.  
https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/26-x/configuration_guide/sec/b_26x_sec_9300_cg/macsec_encryption.html

**REF-005 — Catalyst 9400 MACsec Configuration Guide, IOS XE 17.17.x**  
Includes supervisor and line-card limitations.  
https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9400/software/release/17-17/configuration_guide/sec/b_1717_sec_9400_cg/macsec_encryption.html

**REF-006 — Cisco ISR 4000 Ethernet WAN Modules Data Sheet**  
Documents the MACsec module comparison.  
https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/datasheet-c78-730527.html

**REF-007 — Cisco ISR 4000 Family Data Sheet**  
Discusses ISR MACsec using the NIM-2GE-CU-SFP.  
https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/data_sheet-c78-732542.html

**REF-008 — Cisco Secure Client 5.x Feature and Operating-System Matrix**  
Documents Windows support for MACsec in Network Access Manager.  
https://www.cisco.com/c/en/us/td/docs/security/vpn_client/anyconnect/Cisco-Secure-Client-5/feature/guide/cisco-secure-client-features-licenses-and-oss-release-5.html

### Red Hat

**REF-009 — RHEL 9 Configuring and Managing Networking**  
Includes MACsec configuration using NetworkManager/nmcli.  
https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_and_managing_networking/index

### Palo Alto Networks

**REF-010 — Palo Alto Networks NGFW Clusters**  
Documents MACsec on supported HSCI cluster interfaces beginning with PAN-OS 11.1.5. Does not establish ordinary firewall dataplane MACsec capability.  
https://docs.paloaltonetworks.com/ngfw/administration/ngfw-clustering/ngfw-clusters

### Project authoring reference

**REF-011 — Mermaid code conventions, standard edition r1.0.7**
User-supplied [Mermaid code conventions r1.0.7 guide](guides/mermaid-best-practices-r1.0.7.md), received October 25, 2026 and preserved as imported source material. It is the governing Mermaid guide for this project. The [ZTA project standard](../standards/mermaid-best-practices-zta.md) adds the mandatory named-color override. The separately supplied [embedded CSS edition](guides/mermaid-best-practices-CSS-r1.0.7.md) remains cataloged as an alternate source, not the governing convention.

### Reference maintenance requirements

For new vendor findings, record the publication title, source URL, applicable hardware/software versions, finding, architectural impact, review date and status.

Maintain external research in `references/vendor-research.md` rather than scattering unsupported claims throughout the repository.

For each new or revisited finding, record its stable reference ID, source title/URL, publication date if available, applicable hardware/software/licenses, precise finding, architectural impact, actual review date, reviewer and status. Distinguish the date a finding was imported from the date a vendor source was checked.
