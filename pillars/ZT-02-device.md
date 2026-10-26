# ZT-02 — Device

<!-- zta-doc: id=DOC-ZT-02; parent=ZT-02; lineage=ROOT>ZT-02 -->

**Owner (proposed):** Endpoint Engineering  
**Document status:** Proposed reference architecture; implementation unvalidated  
**Baseline:** October 24, 2026

**Ancestry:** `ROOT > ZT-02`. [Parent architecture](../README.md#seven-pillars).

Evaluate network admission and endpoint trust signals. Supplicant, certificate lifecycle, posture inputs and admission failure behavior require engineering verification.

**Technologies:** Cisco ISE, IEEE 802.1X, Catalyst. Listing a technology does not establish deployment or validation.

## Initial scope and related controls

[Identity workflows](../controls/identity-authentication/overview.md) separate network admission, user authentication and PAM. [NET-01](../controls/network-segmentation/overview.md#net-01) is the authoritative network-admission control under ZT-05; do not duplicate it here.

## Next decomposition

The proposed owner must inventory resources, identify authoritative controls, define acceptance criteria and evidence, and record dependencies on other pillars. Detailed controls and test identifiers have not been invented for unspecified designs.
