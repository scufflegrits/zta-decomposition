# Network admission, segmentation and WAN controls

<!-- zta-doc: id=DOC-CTRL-NETWORK; parent=ZT-05; lineage=ROOT>ZT-05 -->

**Owner (proposed):** Network Engineering  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

**Ancestry:** `ROOT > ZT-05`. [Parent pillar](../../pillars/ZT-05-network-environment.md).

<!-- zta-table: id=TBL-ZT05-CONTROLS; parent=ZT-05; lineage=ROOT>ZT-05 -->

| Parent ID | Control ID | Technology | Function | Status |
|---|---|---|---|---|
| ZT-05 | NET-01 | Catalyst / ISE | Network admission and VLAN policies | Required |
| ZT-05 | NET-02 | ISR 4000 | Selective inter-VLAN routing | Required |
| ZT-05 | NET-03 | Palo Alto | Inter-site security enforcement | Required |
| ZT-05 | NET-05 | IPsec | Proposed WAN transport protection | Proposed |

## NET-01

Catalyst and Cisco ISE govern applicable 802.1X/RADIUS network admission and VLAN policy. Network admission is distinct from user login, PAM approval and application access. Supplicants, EAP methods, certificate lifecycle, VLAN assignments, CoA behavior and failure modes require verification.

## NET-02

ISR 4000 routers handle selected authorized inter-VLAN flows. Define an explicit allow matrix and ISR ACLs. Local management VLANs must not be routed. VLAN membership alone does not encrypt traffic or authorize resources.

## NET-03

Palo Alto firewalls enforce applicable inter-site security rules on paths that traverse them. The topology does not put these firewalls on every local east-west path. Exact zones, policies and models are unresolved; test denied as well as allowed flows.

## NET-05

Palo Alto site-to-site IPsec is the current proposed mechanism for public-WAN protection. Approved protection is required, but the candidate, cipher profile, peer authentication, key lifecycle, selectors, routing and failure behavior are not finalized. Do not expose remote-user authentication.

[NET-04 MACsec](../macsec/overview.md) and [NET-06 management isolation](../management-isolation/overview.md) have separate authoritative definitions. Application TLS and resource authorization remain necessary according to the selected policies.
