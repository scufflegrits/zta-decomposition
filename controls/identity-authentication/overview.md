# Identity and authentication workflows

<!-- zta-doc: id=DOC-CTRL-IDENTITY; parent=ZT-01; lineage=ROOT>ZT-01 -->

**Owner (proposed):** Identity/IAM  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

**Ancestry:** `ROOT > ZT-01`. [Parent pillar](../../pillars/ZT-01-user.md).

Users authenticate using PKI access cards or RSA tokens as appropriate to the workflow, with applicable AD integration. A user must be physically present at Site A or Site B to initiate authorized authentication. Public WAN remote-user authentication is not exposed.

Keep these decisions separate:

1. Network admission: [NET-01](../network-segmentation/overview.md#net-01), using applicable 802.1X and ISE policy.
2. User authentication: approved PKI/RSA/AD workflow.
3. Privileged elevation: PAM authorization and accountability.
4. Network reachability: ISR ACLs and Palo Alto rules on the actual traffic path.
5. Application and data authorization: resource-specific permissions.

Physical presence at Site A does not automatically forbid authorized access to Site B resources or approved inter-site authentication service traffic. Such flows require explicit policy. Service locations, dependencies, certificate validation, token integration, offline behavior and PAM workflow remain open. Define how physical presence is enforced and tested before claiming the restriction is implemented.

See [ADR-001](../../architecture/decisions/ADR-001.md) and [ADR-002](../../architecture/decisions/ADR-002.md). Detailed identity control decomposition awaits the approved flows.
