---
schema_version: 1
id: DOC-IMPL-MACSEC-PILOT
title: MACsec first-link implementation plan
document_type: implementation
parent: NET-04
lineage:
- ROOT
- ZT-05
- NET-04
owner: Network Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-11-02'
---

# MACsec first-link implementation plan

This is the first project instance of the [per-control implementation workflow](../../090_standards/implementation-workflow.md), using the [implementation plan template](implementation-plan-template.md). It is an intake and preliminary roadmap, not an approved design or deployment record. **No exact link, hardware inventory, vendor research, configuration, execution evidence or customer decision has been supplied for this pilot.**

## Plan status

- **Planning state:** Intake; awaiting bounded link selection and exact hardware details
- **Implementation state:** Not started
- **Last reviewed:** 2026-11-02; project documentation only
- **Roadmap readiness:** Preliminary sequence only; hardware-specific planning is blocked on inventory
- **Scoped research record:** [MACsec first-link research record](../../080_references/020_implementation-research/macsec-first-link.md); research not started

## 1. Implementation identity and objective

- **Plan ID:** DOC-IMPL-MACSEC-PILOT
- **Pillar:** ZT-05 — Network & Environment
- **Control:** NET-04 — MACsec Ethernet link protection
- **Control overview:** [MACsec control](../../030_controls/020_macsec/overview.md)
- **Requirements:** [MACsec requirements MAC-001–MAC-006](../../030_controls/020_macsec/requirements.md)
- **Verification:** [MACsec verification plan TEST-001–TEST-007](../../030_controls/020_macsec/verification.md)
- **Program/SOW obligation and source:** Not provided; example SOW-001 in the use case is illustrative only.
- **Desired outcome:** Determine whether MACsec can be implemented on one selected, bounded Ethernet link under the project's operational constraints; if approved and feasible, implement and verify that scope, documenting limitations and customer disposition separately.
- **Initial candidate scope:** One switch-to-router link at one site, subject to owner confirmation. Site, peers, interfaces and direction are not selected.
- **Out of scope:** Generalizing findings to other ports, models, sites or peer combinations; claiming all-link coverage; asserting deployed protection or customer acceptance.
- **Engineering owner / reviewer:** Network Engineering proposed; individuals not assigned.
- **Decision and exception authority:** Not provided.

## 2. Known project context and required input

The repository's proposed architecture names Catalyst 9300/9400 switches, ISR 4000 routers, Palo Alto firewalls, Windows 11 and RHEL 9 endpoints, and generic virtualization hosts. This is class-level context only; it does not identify the pilot's actual equipment or prove MACsec compatibility. The existing [compatibility findings](../../070_procurement/hardware-compatibility.md) were copied from an earlier handoff and have not been revalidated against current sources or a selected bill of materials.

Before hardware-specific research, provide the exact selected link and both peers, including:

- Site, device roles, manufacturer/model/SKU, chassis, supervisor/line card or network module, and exact interfaces/ports.
- Software release and relevant feature/license state on each peer.
- Media/transceiver, link speed, interface mode, VLAN/trunk and aggregation use.
- Current configuration and traffic/protocols that must continue to work.
- Applicable SOW clause or program requirement, change/lab constraints, and the designated engineering reviewer and decision authority.
- Required cipher/security profile, performance/MTU targets and permitted behavior during negotiation failure, if already specified. Unknown values remain open decisions.

| Role / end | Site | Manufacturer and exact model/SKU | Module/card and exact port | Software/release | License | Media and speed | Peer / connected system | Source or inventory record |
|---|---|---|---|---|---|---|---|---|
| Switch | Not selected | Not provided | Not provided | Not provided | Not provided | Not provided | Candidate router; not selected | Not provided |
| Router | Not selected | Not provided | Not provided | Not provided | Not provided | Not provided | Candidate switch; not selected | Not provided |

### Current configuration and traffic

- **Topology:** Proposed site path is Catalyst → ISR → Palo Alto → public WAN; the candidate link is not selected. See [physical topology](../../020_architecture/physical-topology.md).
- **Current interface/configuration and traffic:** Not provided.
- **Availability, redundancy and maintenance constraints:** Not provided.
- **Change window, rollback and lab access:** Not provided.
- **Management and monitoring paths:** Not provided.

## 3. Constraints and decisions

- MACsec is a Layer 2 link protection. It does not establish user/resource authorization, application encryption or public-WAN protection.
- Implement only where exact hardware/software support and operational impact are understood; do not infer support from a product family.
- Document unsupported or deferred scope, functionality/workflow impact, residual exposure, alternatives and customer disposition. A customer decision does not change a technical test result.
- Keep technical performance targets numeric and agreed before execution. Do not use a coverage percentage as acceptance.
- **Known decisions:** Apply [ADR-014](../../020_architecture/010_decisions/ADR-014.md); no pilot-specific design or exception decisions recorded.
- **Open blockers:** Exact bounded link and complete peer inventory; applicable obligation; current source validation; approved MACsec/MKA profile and protocol behavior; numeric performance criteria; test/lab/change approach; named reviewers and authorities.

## 4. Readiness and research

### Readiness assessment

- **State:** Intake; not ready for hardware-specific research or configuration planning.
- **Facts sufficient for research:** No. Exact peers, ports, releases, licenses and media are missing.
- **Facts sufficient for implementation planning:** No. The pilot link, obligation, profile, performance criteria and change constraints are not established.
- **Questions for the user:** Select the pilot link/site and provide the inventory details listed above; identify the applicable obligation and review/exception authority; provide any already-approved MACsec profile and performance criteria.
- **Assumptions/inferences:** The switch-to-router link is only a candidate chosen to make the pilot concrete; it is not an approved scope or a claim that the actual devices support MACsec.

### First candidate Jira story (proposal only; no Jira issue exists)

**Summary:** Provide the exact hardware and software inventory for one candidate MACsec link.

**Purpose:** Gather enough identifying information to research whether MACsec is supported and how to implement it for the selected peer pair.

**Acceptance criteria:** For both ends, provide site and device role; manufacturer, exact model/SKU and chassis; relevant module/NIC and exact interface/port; running software/firmware/OS version; license/feature state; media and link speed; peer identity; current interface mode/configuration and relevant VLAN/trunk/aggregation details; and an inventory, configuration or other source record. Mark unavailable details Unknown and identify who can provide them; do not infer them from the product family.

**Roadmap links:** Steps 1–2; MAC-001 and TEST-001. After this information is reviewed and added to the plan, AI can research the exact pair and propose the next stories. This story is not created or tracked in Jira yet.

### Research record

- **Record:** [MACsec first-link research record](../../080_references/020_implementation-research/macsec-first-link.md)
- **Status:** Not started; waiting for exact equipment and software inputs.
- **Research date and source review:** None. No current vendor source has been checked for the pilot.
- **Summary:** No hardware-specific conclusion established.

## 5. Preliminary roadmap

Steps after intake are proposed sequencing, not an approved configuration procedure. Hardware-specific tasks remain gated on the exact inventory and research record.

| Order | Work package / decision gate | Prerequisites | Owner | Expected output or evidence | Source links | Status |
|---|---|---|---|---|---|---|
| 1 | Select one link and confirm the program obligation, boundaries and decision authorities | User/program input | Program lead and Network Engineering | Bounded scope and sourced obligation in this plan | Adoption checklist; ADR-014 | Blocked |
| 2 | Inventory both peers, interfaces, software, licenses, media, speed and current configuration | Step 1 scope | Network Engineering | Reviewed exact inventory and baseline; candidate first Jira story is drafted above | MAC-001; TEST-001 | Blocked |
| 3 | Research current vendor support and implementation guidance for the exact peer pair | Complete Step 2 inventory | AI research draft; engineering reviewer | Dated, cited research record with documented limits and open questions | MACsec first-link research record; vendor research register | Not started |
| 4 | Decide applicable profile, permitted protocol behavior, functionality impact and numeric performance criteria | Reviewed research; program/security decisions | Network Engineering and designated authority | Approved design decisions and measurable targets | MAC-002–MAC-006; ADR-014 | Not started |
| 5 | Define lab/pilot configuration, failure behavior, rollback and reviewed test procedure | Steps 2–4 | Network Engineering / Endpoint Engineering | Approved change and test plan scoped to the peer pair | TEST-001–TEST-007 as applicable | Not started |
| 6 | Implement the bounded link under the approved change process | Approved design, change and rollback plan | Network Engineering | Configuration baseline and change record | Implementation record standard | Not started |
| 7 | Execute applicable compatibility, MKA, fail-closed, performance and telemetry tests | Step 6; criteria agreed | Test executor and reviewer | Actual results, artifacts, failures/retests and reviewer disposition | MACsec verification plan | Not started |
| 8 | Record deployed scope, technical result, limitations and evidence; request customer disposition if required | Reviewed execution evidence and applicable SOW | Engineering owner / designated authority | Implementation and acceptance records with linked artifacts | [Implementation register](../macsec.md); [acceptance register](../../010_acceptance/macsec.md) | Not started |
| 9 | Review residual scope and decide whether to expand to another link/control | Pilot review | Architecture / program authority | Documented expansion, redesign or stop decision | Roadmap and open questions | Not started |

## 6. Decisions and progress log

| Date | Decision / change / outcome | Source or authority | Roadmap impact |
|---|---|---|---|
| 2026-11-02 | Created this preliminary pilot plan from current project documentation; no actual implementation inputs were available. | Project baseline review | Steps 1–3 remain blocked on scope and exact inventory. |

## 7. Closeout links

- **Implementation register record:** None; no implementation claim.
- **Verification tests and evidence:** None; tests are unexecuted.
- **Customer acceptance record:** None; no submission or decision.
- **Remaining limitations / follow-up:** All hardware-specific compatibility and implementation questions remain open.
