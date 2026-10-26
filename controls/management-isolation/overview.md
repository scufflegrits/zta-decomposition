# Local management isolation

<!-- zta-doc: id=DOC-CTRL-MGMT; parent=NET-06; lineage=ROOT>ZT-05>NET-06 -->

**Owner (proposed):** Network Engineering / Systems  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

**Ancestry:** `ROOT > ZT-05 > NET-06`. [Parent pillar](../../pillars/ZT-05-network-environment.md).

<!-- zta-table: id=TBL-MGMT-CONTROL; parent=ZT-05; lineage=ROOT>ZT-05 -->

| Parent ID | Control ID | Control | Status |
|---|---|---|---|
| ZT-05 | NET-06 | Local-only non-routed management VLANs | Required |

Management VLANs are local, isolated and non-routed at each site. Do not route production into management, provide ISR or WAN routes, or extend a management VLAN between sites.

Approved access uses either an approved physical machine on a management switchport or an approved VM with exactly one management vNIC. Prohibit VM routing, forwarding, NAT, bridging or secondary network attachment that bypasses isolation. Validate host virtual-switch configuration, permissions and management-plane access; a one-vNIC VM alone proves little.

Acceptance planning must include denied production, ISR and WAN paths, absent inter-site Layer 2 extension, virtual-host bypass attempts, unauthorized attachment changes, and successful approved local management. Evidence must include configurations, negative tests and reviewer disposition. These tests are not yet executed or assigned requirement IDs.

See [ADR-005](../../architecture/decisions/ADR-005.md), [ADR-006](../../architecture/decisions/ADR-006.md), and the [local logical design](../../architecture/logical-topology.md).
