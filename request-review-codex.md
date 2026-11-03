---
schema_version: 1
id: DOC-CODEX-PROJECT-ASSESSMENT
title: 'Project assessment: Zero Trust Architecture Decomposition'
document_type: guide
parent: ROOT
lineage: [ROOT]
owner: Documentation Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-11-02'
---

# Project assessment: Zero Trust Architecture Decomposition

## What the project is

This is a **docs-as-code planning framework for a proposed two-site Zero Trust Architecture**, organized around the seven DoD pillars. It tries to connect program obligations to engineering controls, requirements, tests, evidence, implementation records, and customer decisions.

The architecture has concrete constraints: users authenticate from Site A or B, the site network path is Catalyst → ISR → Palo Alto → public WAN, management networks stay local and isolated, and virtualization remains vendor neutral. MACsec is the most developed example. Its records distinguish technical verification from a customer accepting documented limitations.

The project is clear that it is **not an as-built design, security certification, or evidence of customer acceptance**. The actual implementation and acceptance registers are empty, and the hardware compatibility findings have not been independently rechecked. That framing is stated plainly in the [README](README.md) and the [MACsec records](050_implementation/macsec.md).

## What it does well

- **It keeps claims honest.** Proposed design, unverified compatibility, unexecuted tests, implementation facts, and customer decisions have distinct statuses and records. That reduces the chance that a polished document or passing audit gets mistaken for deployed security.
- **It gives traceability a usable shape.** Stable IDs connect pillars to controls, requirements, tests, and evidence. The MACsec branch demonstrates the intended flow, and the [use case](zta-macsec-use-case.md) labels its SOW and Jira examples as fictional.
- **It understands the limits of automation.** The auditor checks declared metadata, links, ancestry, and evidence references; the docs acknowledge that it cannot establish requirement completeness, test quality, artifact authenticity, or security configuration. That boundary is well described in the [tool guide](110_tools/README.md).
- **It captures real design hazards.** The architecture notes that some traffic bypasses the firewall, management isolation needs host-level controls, and MACsec only protects compatible links. Those are useful prompts for engineering review.

## What seems unclear or risky

- **The program context is still mostly hypothetical.** The SOW mapping, Jira workflow, ownership, evidence handling, baselines, and acceptance authority are all awaiting recorded agreements in the [adoption checklist](HOW-TO-USE.md). Without those inputs, this is a strong proposed process rather than a program-ready one.
- **The architecture has major unresolved inputs.** Exact equipment, VLAN policy, identity flows, firewall design, endpoint compatibility, and virtualization isolation remain open in [engineering questions](020_architecture/open-questions.md). The design is not yet specific enough to validate end-to-end.
- **The coverage is uneven.** MACsec has detailed requirements and tests; most other pillars are responsibility summaries. The repository itself notes this in the guide and roadmap. Readers could overestimate how complete the overall ZTA design is because the MACsec branch is much more mature.
- **Some core constraints need an explicit source and rationale.** Physical-site-only authentication and the required device sequence are marked as established constraints, but the documents I reviewed do not connect them to a specific threat model, contract clause, or approved program decision. They may be valid constraints; their authority and rationale should be easy to find.
- **The process could become heavier than the delivery.** The traceability model is thorough, but maintaining many documents and manual Jira links adds work. It needs a small real delivery pilot to show that the records help engineers and reviewers make decisions rather than mainly satisfying the framework.

## What I’d improve next

1. **Anchor the baseline in program facts:** identify the authoritative SOW scope, actual sites and equipment, decision makers, and existing evidence and change-control systems. Record sources and approvals in the checklist.
2. **Resolve the high-impact architecture questions first:** especially identity flows, allowed inter-VLAN traffic, management isolation, virtualization paths, and exact network hardware. Link answers to reviewed decisions or requirements.
3. **Pilot one bounded real scenario end to end.** MACsec is an available candidate, but use actual equipment and an actual obligation. Track the effort to maintain the documents and Jira links, then adjust the workflow based on what reviewers need.
4. **Expand the other pillars from real requirements and flows.** Give each control an owner, measurable requirements, and verification approach before treating the seven-pillar framework as a complete architecture.
5. **Revalidate vendor research against the actual bill of materials** before using it for procurement or design decisions. The project currently labels those findings as unverified.

My overall read: **a thoughtful, unusually careful documentation and traceability prototype with good integrity boundaries, but not yet a validated architecture or demonstrated delivery process.** The next meaningful step is to attach it to real program inputs and run a small pilot.

This assessment was based on reading the project files; no files were changed during that review.
