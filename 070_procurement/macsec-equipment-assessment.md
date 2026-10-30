---
schema_version: 1
id: DOC-PROC-MAC
title: MACsec equipment assessment
document_type: procurement
parent: NET-04
lineage:
- ROOT
- ZT-05
- NET-04
owner: Procurement / Network Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# MACsec equipment assessment

[Parent control](../030_controls/020_macsec/overview.md); [requirements](../030_controls/020_macsec/requirements.md).

Require vendors to answer the following for exact hardware models, software releases and licensing:

**Hardware and ports:** Which exact SKUs, interfaces, modules, link speeds and media support MACsec? Are there partial-port restrictions or dependencies on ASICs or NICs?

**Encryption:** Which AES-GCM cipher suites, XPN options, replay protections and confidentiality settings are supported?

**Authentication and key management:** What MKA, EAP-TLS, certificate, pre-shared key and lifecycle options are supported?

**Interoperability:** Can the exact endpoints establish compatible MACsec sessions? Are VLAN trunks, link aggregation and chosen interfaces supported?

**Licensing:** What OS release and software licenses are required?

**Operational behavior:** What happens when MKA negotiation fails, a peer reboots, keys rotate, or a link fails? Can mandatory encryption fail closed?

**Performance:** What throughput, MTU impact, CPU consumption and hardware acceleration characteristics apply?

**Monitoring:** What CLI/API commands, logs and counters prove that MACsec is active?

**Endpoint support:** Are Windows 11, RHEL 9, and generic virtualization-host uplinks compatible with the intended MACsec design?

**Acceptance:** Can the vendor demonstrate a proof of concept with the exact equipment and configuration before procurement approval?

## Required assessment record

For each exact link record site, asset/port IDs, both peer SKUs and modules, OS/firmware, license, media/speed, capability source and version, supported protection profile, interoperability test reference and proposed disposition. Obtain an exact bill of materials before marking compatibility confirmed.

Vendor answers and a proof of concept support review. Document unsupported links, operational tradeoffs and proposed disposition under [ADR-014](../020_architecture/010_decisions/ADR-014.md); obtain the actual procurement/customer decisions from the designated authorities. This document grants no procurement approval.
