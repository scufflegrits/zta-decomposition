---
schema_version: 1
id: DOC-IMPL-MAC
title: MACsec implementation register
document_type: implementation
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

# MACsec implementation register

Record the actual protections and documented limitations under NET-04 using the [implementation/acceptance standard](../090_standards/implementation-acceptance.md). Research source findings remain in [compatibility findings](../070_procurement/hardware-compatibility.md); execution proof belongs under the [tests](../030_controls/020_macsec/verification.md).

**Current recorded state:** No actual implementation records have been entered. No deployment or verification claim is made. Do not infer a green or red delivery result from an empty register.

## Record actual outcomes

Use one row for each clearly identified scope and outcome. Record supported ports and installed router modules precisely; separate unsupported ports or operationally deferred protections. Document why further protection would disrupt functionality or impose undue process, residual exposure, alternatives and the customer disposition reference through the acceptance register. Use observed facts and labeled unknowns rather than assumed capabilities.

The following is a fenced template, not an empty active table or a placeholder implementation row. Add traceable metadata with a unique table ID, parent NET-04 and lineage ROOT>ZT-05>NET-04 before an actual populated table.

```markdown
| Parent ID | Implementation ID | Scope | SOW reference | Baseline | Deployment state | Configuration | Requirement IDs | Test IDs | Verification result | Verification basis | Evidence IDs | Limitation | Operational impact | Residual risk | Compensating controls | Jira stories |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Read the linked [customer acceptance register](../010_acceptance/macsec.md) alongside these technical facts. Customer acceptance of a documented limitation never changes this register's verification result to Passed.
