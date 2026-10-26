---
schema_version: 1
id: DOC-ACCEPT-MAC
title: MACsec customer acceptance register
document_type: acceptance
parent: NET-04
lineage:
- ROOT
- ZT-05
- NET-04
owner: Architecture / Security Engineering
owner_status: proposed
document_status: draft
implementation_status: unvalidated
baseline_date: '2026-10-25'
---

# MACsec customer acceptance register

This is the management-facing source for actual customer disposition against the applicable contract SOW requirements. It references the [implementation register](../implementation/macsec.md) and follows the [record standard](../standards/implementation-acceptance.md).

**Current recorded state:** No submission or customer acceptance decisions have been recorded. Implementation and verification are not claimed. Project planning direction is recorded in [ADR-014](../architecture/decisions/ADR-014.md); it is not an acceptance artifact for deployed work.

## Record the decision and its basis

Use Pending review for an actual submission awaiting a decision. After a decision, record its authority, date, artifact and rationale, including the disposition of hardware limitations and operational tradeoffs. Use Accepted with documented limitations when the customer accepts such an outcome. Preserve the unchanged deployment and verification facts in the linked implementation records. No percentage is needed.

The following is a fenced template, not an active acceptance claim. For actual records add traceable metadata with a unique table ID, parent NET-04 and lineage ROOT>ZT-05>NET-04.

```markdown
| Parent ID | Acceptance ID | Scope | SOW reference | Baseline | Implementation IDs | Decision | Decision basis | Authority | Decision date | Decision artifact |
|---|---|---|---|---|---|---|---|---|---|---|
```

The decision should explain what was delivered, how it was verified, any approved limitations or unresolved gaps, and the acceptance decision against the applicable contract Statement of Work (SOW) requirements. Existing files and consistent references support review; human reviewers establish the legitimacy and extent of acceptance.
