---
schema_version: 1
id: DOC-ARCH-OVERLAY
title: Seven-pillar control relationships
document_type: architecture
parent: ROOT
lineage:
- ROOT
owner: Security Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# Seven-pillar control relationships

This logical relationship inventory is the basis for the future overlay diagram. It does not place identity services at either site or imply direct physical connections.

The existing logical control overlay was accepted as a useful architecture view.

It must show the following relationships without redrawing the complete two-site physical topology.

| Pillar | Primary control relationship |
|---|---|
| User | AD/PKI/RSA authenticates the user; PAM mediates privileged requests |
| Device | Cisco ISE evaluates applicable 802.1X/RADIUS admission and authorization |
| Application & Workload | Windows, RHEL and applications enforce resource permissions |
| Data | File/database permissions and encryption protect information |
| Network & Environment | Catalyst, ISR and Palo Alto enforce their respective network policies |
| Automation & Orchestration | Proposed integrations can trigger quarantine, blocking or revocation |
| Visibility & Analytics | Identity, device, network, PAM and workload telemetry supports detection and investigation |

Re-use these established identifiers across diagrams:

| Component ID | Meaning |
|---|---|
| SITE_A_CLIENTS_01 | Site A endpoint group |
| SITE_B_CLIENTS_01 | Site B endpoint group |
| SITE_A_SW_01 | Site A Catalyst switch |
| SITE_B_SW_01 | Site B Catalyst switch |
| SITE_A_RTR_01 | Site A ISR router |
| SITE_B_RTR_01 | Site B ISR router |
| SITE_A_FW_01 | Site A Palo Alto firewall |
| SITE_B_FW_01 | Site B Palo Alto firewall |
| SITE_A_SERVERS_01 | Site A servers |
| SITE_B_SERVERS_01 | Site B servers |
| SITE_A_VM_HOST_01 | Site A virtualization host |
| SITE_B_VM_HOST_01 | Site B virtualization host |
| SITE_A_MGMT_01 | Site A management VLAN |
| SITE_B_MGMT_01 | Site B management VLAN |
| CTRL_USER_AUTH | AD/PKI/RSA user authentication |
| CTRL_ISE | Cisco ISE network authorization |
| CTRL_PAM | Privileged access control |
| CTRL_APP_AUTH | Application/workload authorization |
| CTRL_DATA_AUTH | Data access authorization |
| CTRL_TELEMETRY | Monitoring and security telemetry |
| CTRL_RESPONSE | Proposed automation and response |

The overlay must clearly separate network admission, user authentication, privileged elevation, routed reachability, application authorization and data authorization.

Logical relationships should not be mistaken for direct physical cables.

Authoritative definitions: [identity workflows](../030_controls/010_identity-authentication/overview.md), [network controls](../030_controls/040_network-segmentation/overview.md), [MACsec](../030_controls/020_macsec/overview.md), and [management isolation](../030_controls/030_management-isolation/overview.md). Application, data, automation and visibility details remain in their respective [pillar documents](../README.md#seven-pillars).
