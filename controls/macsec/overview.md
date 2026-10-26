# MACsec control overview

<!-- zta-doc: id=DOC-MAC-OVERVIEW; parent=NET-04; lineage=ROOT>ZT-05>NET-04 -->

**Owner (proposed):** Network Engineering / Endpoint Engineering  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

**Ancestry:** `ROOT > ZT-05 > NET-04`. [Parent pillar](../../pillars/ZT-05-network-environment.md).

<!-- zta-table: id=TBL-MAC-CONTROL; parent=ZT-05; lineage=ROOT>ZT-05 -->

| Parent ID | Control ID | Control | Status |
|---|---|---|---|
| ZT-05 | NET-04 | MACsec Ethernet link protection | Required objective / Verify |

MACsec is desired on every wired Ethernet port. Exact hardware, module, software, license and peer combinations must be inventoried. Unsupported links require an architectural change, suitable hardware or a formally approved exception with compensating controls. No ordinary firewall dataplane interface or generic host uplink is assumed capable.

802.1X admits a device; MACsec protects a compatible Layer 2 link. MACsec does not provide resource authorization, public-WAN protection or application encryption. Evaluate IPsec and TLS separately. Encryption state must not be inferred from successful admission or a connected cable.

Use the [requirements](requirements.md), [verification plan](verification.md), [procurement questionnaire](../../procurement/macsec-equipment-assessment.md), and [compatibility findings](../../procurement/hardware-compatibility.md). Findings came from the handoff and have not been rechecked against current vendor documents. No proposed installation is validated.
