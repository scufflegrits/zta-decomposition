---
schema_version: 1
id: DOC-ZTA-FAQ
title: ZTA decomposition — Questions and critical review
document_type: guide
parent: ROOT
lineage: [ROOT]
owner: Architecture / Security Engineering
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-25'
---

# ZTA decomposition — Questions and critical review

These answers support discussion of the [briefing](zta-decomposition-briefing.md) with program leadership, the chief engineer, chief architect and delivery teams. They describe the current project and proposed working approach, not completed program adoption. For the operating process, use [How to use this project](HOW-TO-USE.md); record adoption decisions in its single [checklist](HOW-TO-USE.md#program-adoption-checklist).

## Purpose and value

### Why use zta-decomposition? I thought Confluence and Jira could do all of this.

They may be sufficient with the right structure and working agreements. The contribution here is a defined engineering model: stable identities, explicit parent relationships, versioned requirements and tests, scoped implementation records, evidence links and customer decisions. The repository packages that model with local consistency checks and a worked example; it does not claim those concepts are exclusive to Markdown or Git.

The proposed division is engineering definitions in the repository, delivery work in Jira and program presentation in Confluence. If the program already maintains equivalent authoritative records and controls in its existing tools, reuse those capabilities and avoid creating a competing source. A pilot should establish whether this repository adds value.

### Are we buying another product or replacing existing tools?

This is currently a documentation repository with Python utilities, not a hosted application or deployed security product. The proposed approach keeps Jira and Confluence in use. Adoption still has costs: engineering maintenance, reviews, approved hosting and coordination with existing program processes.

### What problem does it solve beyond better-looking documentation?

It makes the relationship between an obligation, engineering work, observed behavior and customer disposition explicit. A reviewer can follow a requirement to its tests and inspect the evidence behind a particular implementation claim. That is useful only if the underlying records are accurate and maintained; attractive tables alone deliver no security benefit.

### What tangible value has been demonstrated so far?

The project has a navigable architecture scaffold, detailed MACsec requirements and test definitions, record schemas and an auditor with regression tests. Those are demonstrated documentation/tooling capabilities. Reduced delivery time, fewer defects, customer acceptance and deployed security improvement have not been demonstrated on program work.

### How would we decide whether to adopt it?

Pilot one actual obligation and a bounded implementation using the [MACsec use case](zta-macsec-use-case.md) as a guide. Assess whether engineers can maintain the links during normal work, reviewers can find the proof, and the customer can understand the outcome. Compare the effort and usefulness with the existing process; simplify, adapt or stop if it creates duplicate work without a corresponding benefit.

## Chief engineer and customer acceptance

### Does a passing audit mean the architecture is correct or the equipment is secure?

No. The auditor checks declared metadata, IDs, relationships, links and specified record conditions. It cannot determine whether the design is sufficient, configuration is safe, tests are adequate or evidence is authentic. A clean audit supports engineering review; it does not replace that review or execution.

### Where is the proof that we implemented something correctly?

The [implementation register](implementation/macsec.md) identifies the exact scope, deployed configuration, baseline, applicable tests and evidence. Actual evidence records remain under their tests and link the artifacts, results and reviewer. The [acceptance register](acceptance/macsec.md) separately records what the customer decided. Both registers are currently unpopulated; no implementation is claimed.

### Can a configuration screenshot or a closed Jira story prove the requirement is satisfied?

It can contribute evidence, but it does not establish satisfaction by itself. A configuration shows settings; reviewed execution results must demonstrate the behavior claimed for the actual scope and baseline. A closed story establishes a delivery-work outcome under its acceptance criteria, which may be research or configuration work rather than successful operational verification.

### Are the current verification plans detailed enough to execute immediately?

They provide test identities and procedure/acceptance bases, not complete equipment-specific runbooks. Exact peers, commands, approved profiles, numeric performance criteria, workload conditions and functional checks need engineering development and review. The current MACsec tests remain proposed and unexecuted.

### If a switch supports MACsec only on its first 16 ports, is the deliverable a failure?

Not automatically. Record the actual model and port limits, what was implemented and verified, what remains unprotected, operational impacts, residual exposure and alternatives. The designated customer authority can accept the documented outcome with limitations against the applicable SOW requirements. Unsupported ports remain identified as unprotected; they do not acquire a passing test result through acceptance.

### Without a completion percentage, how does management know whether the work is acceptable?

Use separate text states for deployment, verification and customer disposition, supported by scope-specific records. Review what was delivered, its behavior, limitations and the actual decision artifact. The [record standard](standards/implementation-acceptance.md) defines these states; no percentage substitutes for that review.

### Does avoiding disruption let engineers skip security requirements whenever they are inconvenient?

No. [ADR-014](architecture/decisions/ADR-014.md) calls for documented operational tradeoffs and customer disposition, not unilateral acceptance by an engineer. Record measured or investigated impacts, alternatives and residual risk. Preserve an unmet requirement or failed result as a technical fact even when the customer accepts the documented outcome.

### What if the customer accepts a limitation but a mandatory program requirement still applies?

Identify the conflict and refer it to the authority responsible for that requirement. A disposition must be within the decision maker's assigned authority and tied to the adopted contractual/program baseline. The repository neither grants waiver authority nor assumes a customer decision changes every other applicable obligation.

### Is a Git commit an acceptance signature? Does the auditor verify the approver?

No. A commit records a repository change; it does not establish contractual authority. Final acceptance records require an authority, date, rationale and existing decision artifact or local record of an external decision. The auditor checks the declared structure and file existence, while reviewers confirm the decision's authenticity, scope and authority.

## Chief architect and systems engineering

### Is this a complete Zero Trust Architecture, or mainly a MACsec project?

It is a seven-pillar architecture scaffold whose MACsec branch is the most developed example. Other pillars still need detailed requirements, flows, integrations and verification. MACsec is Ethernet link protection; implementing it does not establish identity, application or data authorization or demonstrate complete ZTA.

### Why organize around seven pillars if security decisions cross those boundaries?

The pillars provide responsibility and navigation. A control has one authoritative parent, while other pillars can reference it. Cross-pillar resource-access scenarios, enforcement points, dependencies and failure behavior still require explicit architectural analysis; a single-parent documentation hierarchy is not a claim that the operational system is a tree.

### How can I see how the tables connect without reading every document?

Use the [decomposition tree](zta-decomposition-tree.md). It shows the selected pillar cell becoming the parent of a control table, then a requirement becoming the parent of its tests and evidence. Implementation and acceptance records attach to the control and reference the engineering definitions, preserving the existing test/evidence ancestry.

### What if one requirement supports several SOW clauses or needs several stories?

Those are many-to-many associations. Record the applicable SOW references and actual Jira links without duplicating the requirement or changing its engineering parent. The current SOW association is human-reviewed text; the auditor does not parse the contract or prove complete contractual coverage.

### How do we prevent a carefully documented but incomplete design?

Review actual access scenarios, assets, trust decisions, enforcement paths, failure modes and operational constraints with the responsible disciplines. Compare the adopted obligations with the decomposed requirements and tests. The auditor can find a broken declared relationship; it cannot identify a requirement that nobody wrote or a missing threat scenario.

### What happens when hardware, requirements or configurations change after testing?

Review the impact on affected implementation records, tests, evidence and customer decisions. Evidence identifies the implementation and exact baseline it supports; it should not be silently reused as proof of a changed configuration. Preserve historical executions and decisions, and record a new baseline, retest or disposition as appropriate.

### Are the vendor compatibility findings verified for the program's equipment?

Not yet. The [compatibility findings](procurement/hardware-compatibility.md) identify imported research and limits; they are not proof of a supported installation. Engineering must verify the actual SKU, port, module, software, media, license and adjacent peer and retain the reviewed source and inventory. The hypothetical use-case outcomes do not constitute hardware research or execution evidence.

## Scrum Masters and delivery teams

### Who creates stories and who owns the engineering content?

The proposed working model has the Scrum Master coordinating story creation and dependencies, the Product Owner prioritizing, and engineering owners maintaining definitions and reciprocal links. Reviewers assess criteria and evidence; the designated authority records acceptance. Actual assignments still need to be recorded in the [adoption checklist](HOW-TO-USE.md#program-adoption-checklist).

### Do we need software-factory access or a Jira integration to start?

No integration is needed for manual links. After an issue is created through the program's existing Jira process, enter its direct key link in the relevant engineering row and reference the engineering IDs and baseline in Jira. Live issue checks or automated updates would require later coordination and access; neither is implemented now.

### Will we have to maintain every fact in three places?

That is a risk to avoid. The proposed authoritative split keeps engineering definitions and technical records in the repository, delivery status in Jira, and program summaries in Confluence with links to the source baseline. The [manual Jira standard](standards/manual-jira-traceability.md) describes which references are entered manually; it does not require copying assignees, sprint details or story status into Markdown.

### Do we need one story or one record for every port?

Not necessarily. Split work and records where scope, capability, baseline, outcome or limitations differ. A clearly identified group with the same outcome can share an implementation record, provided its inventory and evidence justify the group-level claim. Do not generalize a result from one port/peer combination to untested equipment without an engineering basis.

### How do research, implementation and verification stories finish differently?

Research can finish with a reviewed unsupported-capability finding. Implementation can finish with the agreed configuration and change artifacts while verification remains outstanding. Verification requires the agreed execution results and review. None of those story closures automatically creates a customer acceptance decision.

### How are stale links, split stories and superseded work handled?

Review links in both directions during the agreed review cycle and retain the relationship to work already performed. Explain splits/replacements in Jira and update the engineering links without deleting evidence history. The local auditor detects specified format/conflict problems; it cannot tell whether an external issue still exists or still has the intended scope.

## Governance and practical objections

### What if engineers or reviewers do not normally use Git or Markdown?

Start with the program's actual skills and tool constraints. Confluence can provide a readable entry point, while designated maintainers handle repository edits through the approved process. That support has a real cost; the pilot should test whether it is workable. The engineering model can be adapted to existing approved tools if the repository workflow becomes an obstacle.

### Where will sensitive configurations, evidence and customer decisions live?

Use program-approved hosting, access controls, artifact storage and retention. Repository artifacts may be local records pointing to externally stored proof; the current auditor checks that local record exists, not the external system or its permissions. This project's configured remote is not evidence that any particular program data is approved for storage there. Record the actual handling agreement in the existing adoption checklist.

### How much administration is this, and who maintains it after the initial author leaves?

No measured maintenance cost is available yet. Assign accepted owners and reviewers, use shared conventions and keep the index generated so the process is not dependent on one person's memory. Start with a bounded pilot and assess whether finding and reviewing evidence becomes easier than under the existing process. Remove duplication that does not help a reviewer assess a claim.

### Could AI-generated documents make the project look more complete than it is?

Yes, if generated text is mistaken for reviewed engineering or actual results. Treat generated requirements and procedures as drafts needing domain review. Keep illustrative SOW wording, fictional issues and hypothetical outcomes labeled; populate authoritative evidence and decision records only from actual work. Document volume is not a measure of implementation or assurance.

### What are the strongest reasons to decline or defer this approach?

An equivalent, maintained traceability process may already exist; owners may be unavailable; approved tooling may not support the proposed workflow; or a pilot may show more maintenance than benefit. Those are valid reasons to adapt or defer it. The decision should turn on whether the approach improves engineering delivery and review in this program, not whether the repository is impressive in isolation.

### What decision is being requested now?

Consider a bounded pilot using an actual obligation and existing program authorities, with engineers and reviewers exercising the workflow end to end. Use the [adoption checklist](HOW-TO-USE.md#program-adoption-checklist) to record applicable agreements and approvals. Program adoption, architectural approval, procurement and acceptance of deployed work remain distinct decisions.
