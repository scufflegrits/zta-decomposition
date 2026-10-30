---
schema_version: 1
id: DOC-ARCH-LOGICAL
title: Site-local VLAN and virtualization design
document_type: architecture
parent: ROOT
lineage:
- ROOT
owner: Network Engineering / Systems
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# Site-local VLAN and virtualization design

This view illustrates the logical design pattern for each site. VLAN IDs, subnet assignments, exact virtual-network attachments and the traffic matrix are not yet specified.

## Site-local logical topology

This pattern applies independently at Site A and Site B. Production groups A and B illustrate segmentation roles; their names, number and mapping to actual VLANs are not approved inventory. The Catalyst group shows VLAN separation within the switching fabric. The virtual-host group shows a common host boundary, with separate production and management attachments that require isolation verification.

```mermaid
---
config:
  # Base supports the project role palette.
  theme: base
  # Keep the site-local view top-down using ELK.
  layout: elk
  # Use CSS named colors as required by project standard r1.0.6.
  themeVariables:
    background: "white"
    primaryTextColor: "darkslategray"
    lineColor: "slategray"
    edgeLabelBackground: "white"
    clusterBkg: "white"
    clusterBorder: "lightslategray"
  # HTML line breaks keep explanatory node labels compact.
  flowchart:
    htmlLabels: true
    nodeSpacing: 35
    rankSpacing: 55
---
%% Apply this pattern separately at each site; do not connect management sites.
%% VLAN groups and virtual attachments are logical, not an exact port inventory.
flowchart TB
  SITE_LOCAL_CLIENTS_01["Windows 11 / RHEL 9 workstations"]
  SITE_LOCAL_SERVERS_01["Physical Windows / RHEL servers"]
  SITE_LOCAL_ADMIN_01["Approved physical management machine"]

  subgraph SG_LOCAL_VM_HOST["GENERIC VIRTUALIZATION HOST - vendor unspecified"]
    SITE_LOCAL_VM_01["VM-01: Windows Server<br/>Production vNIC"]
    SITE_LOCAL_VM_02["VM-02: RHEL Server<br/>Production vNIC"]
    SITE_LOCAL_VSW_PROD_01["Production virtual network<br/>Attachment and permissions: Verify"]
    SITE_LOCAL_VM_03["VM-03: Approved management workstation<br/>Exactly one vNIC: management only"]
    SITE_LOCAL_VSW_MGMT_01["Separate management virtual network<br/>No forwarding / NAT / bridge to production"]
  end

  subgraph SG_LOCAL_CATALYST["CISCO CATALYST 9300 / 9400 - logically separated VLANs"]
    SITE_LOCAL_VLAN_A["Production VLAN group A<br/>Illustrative workstation segment"]
    SITE_LOCAL_VLAN_B["Production VLAN group B<br/>Illustrative server / workload segment"]
    SITE_LOCAL_MGMT_01["Local management VLAN<br/>No routing; no inter-site extension"]
  end

  SITE_LOCAL_RTR_01["Cisco ISR 4000<br/>ACLs permit selected inter-VLAN flows only"]
  SITE_LOCAL_FW_01["Palo Alto firewall<br/>Policy for traversing inter-site flows"]
  WAN_CARRIER["PUBLIC WAN<br/>Site-to-site IPsec: Proposed"]
  SITE_LOCAL_MGMT_INTERFACES_01["Approved device management interfaces<br/>Local attachment design: Verify"]

  SITE_LOCAL_CLIENTS_01 edge_local_clients_vlan@<--> SITE_LOCAL_VLAN_A
  SITE_LOCAL_SERVERS_01 edge_local_servers_vlan@<--> SITE_LOCAL_VLAN_B
  SITE_LOCAL_VM_01 edge_local_vm01_vsw@<--> SITE_LOCAL_VSW_PROD_01
  SITE_LOCAL_VM_02 edge_local_vm02_vsw@<--> SITE_LOCAL_VSW_PROD_01
  SITE_LOCAL_VSW_PROD_01 edge_local_vsw_vlan@<-->|"Production attachment: Verify"| SITE_LOCAL_VLAN_B
  SITE_LOCAL_VLAN_A edge_local_vlan_a_rtr@<-->|"Selected E/W: ISR ACLs"| SITE_LOCAL_RTR_01
  SITE_LOCAL_VLAN_B edge_local_vlan_b_rtr@<-->|"Selected E/W: ISR ACLs"| SITE_LOCAL_RTR_01
  SITE_LOCAL_RTR_01 edge_local_rtr_fw@<-->|"Ethernet MACsec: Verify"| SITE_LOCAL_FW_01
  SITE_LOCAL_FW_01 edge_local_fw_wan@<-->|"North-south"| WAN_CARRIER

  SITE_LOCAL_VM_01 edge_local_vm_east_west@-.->|"Example same-host E/W: workload authorization"| SITE_LOCAL_VM_02

  SITE_LOCAL_ADMIN_01 edge_local_admin_mgmt@---|"Approved physical management switchport"| SITE_LOCAL_MGMT_01
  SITE_LOCAL_VM_03 edge_local_vm03_vsw_mgmt@--- SITE_LOCAL_VSW_MGMT_01
  SITE_LOCAL_VSW_MGMT_01 edge_local_vsw_mgmt_vlan@---|"Management attachment: Verify"| SITE_LOCAL_MGMT_01
  SITE_LOCAL_MGMT_01 edge_local_mgmt_interfaces@--- SITE_LOCAL_MGMT_INTERFACES_01

  classDef nodeEndpoint fill:aliceblue,stroke:royalblue,color:midnightblue,stroke-width:2px
  classDef nodeServer fill:lightcyan,stroke:darkcyan,color:darkslategray,stroke-width:2px
  classDef nodeNetwork fill:honeydew,stroke:forestgreen,color:darkgreen,stroke-width:2px
  classDef nodeFirewall fill:lavender,stroke:darkorchid,color:indigo,stroke-width:2px
  classDef nodeManagement fill:cornsilk,stroke:darkgoldenrod,color:saddlebrown,stroke-width:2px
  classDef nodeExternal fill:gainsboro,stroke:slategray,color:darkslategray,stroke-width:2px
  classDef edgeConnectivity stroke:slategray,stroke-width:2px
  classDef edgeEastWest stroke:darkorchid,stroke-width:3px
  classDef edgeLogicalEastWest stroke:darkorchid,stroke-width:2px,stroke-dasharray:6 4
  classDef edgeNorthSouth stroke:dodgerblue,stroke-width:4px
  classDef edgeManagement stroke:darkgoldenrod,stroke-width:3px,stroke-dasharray:6 4
  classDef groupBoundary fill:white,stroke:lightslategray,stroke-width:2px

  class SITE_LOCAL_CLIENTS_01 nodeEndpoint
  class SITE_LOCAL_SERVERS_01,SITE_LOCAL_VM_01,SITE_LOCAL_VM_02 nodeServer
  class SITE_LOCAL_VSW_PROD_01,SITE_LOCAL_VLAN_A,SITE_LOCAL_VLAN_B,SITE_LOCAL_RTR_01 nodeNetwork
  class SITE_LOCAL_FW_01 nodeFirewall
  class SITE_LOCAL_ADMIN_01,SITE_LOCAL_VM_03,SITE_LOCAL_VSW_MGMT_01,SITE_LOCAL_MGMT_01,SITE_LOCAL_MGMT_INTERFACES_01 nodeManagement
  class WAN_CARRIER nodeExternal
  class SG_LOCAL_VM_HOST,SG_LOCAL_CATALYST groupBoundary
  class edge_local_clients_vlan,edge_local_servers_vlan,edge_local_vm01_vsw,edge_local_vm02_vsw,edge_local_vsw_vlan,edge_local_rtr_fw edgeConnectivity
  class edge_local_vlan_a_rtr,edge_local_vlan_b_rtr edgeEastWest
  class edge_local_vm_east_west edgeLogicalEastWest
  class edge_local_fw_wan edgeNorthSouth
  class edge_local_admin_mgmt,edge_local_vm03_vsw_mgmt,edge_local_vsw_mgmt_vlan,edge_local_mgmt_interfaces edgeManagement
```

**Legend:** Blue nodes are workstations; teal nodes are server workloads; green nodes are network infrastructure or logical production segments; purple nodes are firewalls; amber nodes are management-only resources; gray is the external WAN. Gray lines show attachment or transit connectivity. Purple solid lines show the selected inter-VLAN east-west path through ISR policy; the purple dashed arrow shows an example logical same-host session. Blue lines show north-south site-boundary traffic. Amber dashed lines show local management attachment, with no routing implied. Node colors describe roles, not trust or validation.

**Interpretation:** Read workstation-to-server inter-VLAN traffic through the ISR, with ACLs defining permitted reachability and workload controls defining resource access. Same-host VM traffic can remain on the production virtual network; same-VLAN traffic can also remain local. These paths need appropriate virtual-network, host and application enforcement and do not necessarily traverse the ISR or Palo Alto. The example session arrow shows a possible initiation direction, not an approved allow rule.

The management VLAN has no routed path into production, the ISR/firewall transit path or the WAN. The two virtual networks share a host boundary; their separation must be enforced and tested. No dedicated physical host NIC count, hypervisor product or detailed uplink design is implied. No logical association or common enclosure proves isolation.

Encryption labels identify mechanisms and status, not completed deployment. MACsec compatibility must be assessed for every physical Ethernet attachment, including Catalyst-to-ISR links represented by logical routing edges here. Virtual vNIC lines do not assert virtual-link MACsec. Use the [physical topology](physical-topology.md) for the required Catalyst → ISR → Palo Alto → WAN device sequence.

**Diagram verification:** Rendered to SVG and PNG with Mermaid CLI 12.0.0 and visually reviewed on October 25, 2026 after execution from a normal terminal. Attachment lines cross the Catalyst heading area; this remains a layout refinement item. See the [verification record](../090_standards/diagram-verification.md).

Production workstations, Windows servers, RHEL workloads and VM production vNICs attach to approved VLANs. The ISR handles selected authorized inter-VLAN communications. Same-VLAN and same-host virtual traffic require appropriate host, application or virtual-network controls; do not assume firewall traversal.

The management VLAN has no production route, ISR route, WAN route or inter-site extension. Management access requires either an approved physical machine on a management switchport or an approved management VM with exactly one vNIC attached to management. Device management interfaces and necessary management services must be designed without adding a routed bypass.

A generic host may run VM-01 (Windows Server, production VLAN), VM-02 (RHEL Server, production VLAN) and VM-03 (approved management workstation, one management vNIC). These are illustrative labels, not inventory IDs. No hypervisor vendor is selected.

One vNIC does not prove isolation. Validate host forwarding, NAT, bridging, virtual-switch permissions, attachment privileges and the host management plane. Document how management dependencies work locally before implementation. See [management isolation](../030_controls/030_management-isolation/overview.md).

The future traffic matrix must record source, destination, service, purpose, direction, enforcement point, authorization conditions and test reference. Include local production, inter-site, identity services, same-host VM and explicit management-denial cases. No default allow matrix is supplied.
