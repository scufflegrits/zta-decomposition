---
schema_version: 1
id: DOC-ARCH-PHYSICAL
title: Two-site physical topology
document_type: architecture
parent: ROOT
lineage:
- ROOT
owner: Network Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-24'
---

# Two-site physical topology

This preserves the handoff's required device order. Site A is above Site B. Nodes summarize equipment classes; they are not a bill of materials. Management lines represent local attachment only, not routing through the ISR.

```mermaid
---
config:
  theme: base
  layout: elk
  themeVariables:
    background: "white"
    primaryTextColor: "darkslategray"
    lineColor: "slategray"
    edgeLabelBackground: "white"
    clusterBkg: "white"
    clusterBorder: "lightslategray"
  flowchart:
    htmlLabels: true
    nodeSpacing: 35
    rankSpacing: 55
---
%% Enterprise topology overview.
%% Security mechanisms are annotated, not presumed deployed.
flowchart TB
  subgraph SG_SITE_A["SITE A - PHYSICAL PRESENCE REQUIRED"]
    SITE_A_CLIENTS_01["Windows 11 / RHEL Workstations"]
    SITE_A_SERVERS_01["Windows Servers"]
    SITE_A_VM_HOST_01["Generic Virtualization Host"]
    SITE_A_MGMT_01["Local Management VLAN - No Routing"]
    SITE_A_SW_01["Cisco Catalyst 9300 / 9400"]
    SITE_A_RTR_01["Cisco ISR 4000 - Selective VLAN Routing"]
    SITE_A_FW_01["Palo Alto Firewall"]
  end

  WAN_CARRIER["PUBLIC WAN - IPsec Proposed"]

  subgraph SG_SITE_B["SITE B - PHYSICAL PRESENCE REQUIRED"]
    SITE_B_FW_01["Palo Alto Firewall"]
    SITE_B_RTR_01["Cisco ISR 4000 - Selective VLAN Routing"]
    SITE_B_SW_01["Cisco Catalyst 9300 / 9400"]
    SITE_B_CLIENTS_01["Windows 11 / RHEL Workstations"]
    SITE_B_SERVERS_01["Windows Servers"]
    SITE_B_VM_HOST_01["Generic Virtualization Host"]
    SITE_B_MGMT_01["Local Management VLAN - No Routing"]
  end

  SITE_A_CLIENTS_01 edge_a_clients_sw@<--> SITE_A_SW_01
  SITE_A_SERVERS_01 edge_a_servers_sw@<--> SITE_A_SW_01
  SITE_A_VM_HOST_01 edge_a_vm_sw@<--> SITE_A_SW_01
  SITE_A_MGMT_01 edge_a_mgmt_sw@--- SITE_A_SW_01
  SITE_A_SW_01 edge_a_sw_rtr@<-->|"MACsec: Verify"| SITE_A_RTR_01
  SITE_A_RTR_01 edge_a_rtr_fw@<-->|"MACsec: Verify"| SITE_A_FW_01
  SITE_A_FW_01 edge_a_fw_wan@<-->|"N/S"| WAN_CARRIER

  WAN_CARRIER edge_wan_b_fw@<-->|"N/S"| SITE_B_FW_01
  SITE_B_FW_01 edge_b_fw_rtr@<-->|"MACsec: Verify"| SITE_B_RTR_01
  SITE_B_RTR_01 edge_b_rtr_sw@<-->|"MACsec: Verify"| SITE_B_SW_01
  SITE_B_SW_01 edge_b_sw_clients@<--> SITE_B_CLIENTS_01
  SITE_B_SW_01 edge_b_sw_servers@<--> SITE_B_SERVERS_01
  SITE_B_SW_01 edge_b_sw_vm@<--> SITE_B_VM_HOST_01
  SITE_B_SW_01 edge_b_sw_mgmt@--- SITE_B_MGMT_01

  classDef nodeEndpoint fill:aliceblue,stroke:royalblue,color:midnightblue,stroke-width:2px
  classDef nodeNetwork fill:honeydew,stroke:forestgreen,color:darkgreen,stroke-width:2px
  classDef nodeServer fill:lightcyan,stroke:darkcyan,color:darkslategray,stroke-width:2px
  classDef nodeFirewall fill:lavender,stroke:darkorchid,color:indigo,stroke-width:2px
  classDef nodeManagement fill:cornsilk,stroke:darkgoldenrod,color:saddlebrown,stroke-width:2px
  classDef nodeExternal fill:gainsboro,stroke:slategray,color:darkslategray,stroke-width:2px
  classDef edgePhysical stroke:slategray,stroke-width:2px
  classDef edgeNorthSouth stroke:dodgerblue,stroke-width:4px
  classDef edgeManagement stroke:darkgoldenrod,stroke-width:3px,stroke-dasharray:6 4
  classDef groupSite fill:white,stroke:lightslategray,stroke-width:2px

  class SITE_A_CLIENTS_01,SITE_B_CLIENTS_01 nodeEndpoint
  class SITE_A_SERVERS_01,SITE_B_SERVERS_01,SITE_A_VM_HOST_01,SITE_B_VM_HOST_01 nodeServer
  class SITE_A_SW_01,SITE_B_SW_01,SITE_A_RTR_01,SITE_B_RTR_01 nodeNetwork
  class SITE_A_FW_01,SITE_B_FW_01 nodeFirewall
  class SITE_A_MGMT_01,SITE_B_MGMT_01 nodeManagement
  class WAN_CARRIER nodeExternal
  class SG_SITE_A,SG_SITE_B groupSite

  class edge_a_clients_sw,edge_a_servers_sw,edge_a_vm_sw edgePhysical
  class edge_a_sw_rtr,edge_a_rtr_fw,edge_b_fw_rtr,edge_b_rtr_sw edgePhysical
  class edge_b_sw_clients,edge_b_sw_servers,edge_b_sw_vm edgePhysical
  class edge_a_mgmt_sw,edge_b_sw_mgmt edgeManagement
  class edge_a_fw_wan,edge_wan_b_fw edgeNorthSouth
```

**Legend:** Blue nodes are endpoints; green network infrastructure; teal servers and virtualization hosts; purple firewalls; amber management; gray external networks. Gray links show connectivity, blue links show north-south site-boundary traffic, and amber dashed links show local management attachment. Bidirectional arrows describe connectivity, not an allow rule. Encryption labels identify mechanisms and status.

**Interpretation:** The path is Catalyst → ISR → Palo Alto → WAN → Palo Alto → ISR → Catalyst. IPsec is proposed between Palo Alto peers; the WAN label does not claim encryption is active. All Ethernet links, including endpoint and host uplinks without individual labels, require [MACsec compatibility assessment](../procurement/hardware-compatibility.md). Ordinary firewall dataplane MACsec is unconfirmed. No link is asserted validated.

**Render review:** See [diagram verification](../standards/diagram-verification.md). ELK is the intended layout; a target Markdown viewer may differ.
