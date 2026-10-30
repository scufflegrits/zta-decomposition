---
schema_version: 1
id: DOC-ZTA-TODO
title: Documentation TODO
document_type: backlog
parent: ROOT
lineage:
- ROOT
owner: Documentation Engineering
owner_status: proposed
document_status: draft
implementation_status: not-applicable
baseline_date: '2026-10-25'
---

# Documentation TODO

This backlog tracks document maintenance. Engineering design inputs remain in [open questions](../020_architecture/open-questions.md) and implementation sequencing remains in the [roadmap](../020_architecture/roadmap.md). Remove items when they are completed; Git history keeps the record.

## Governance

- [ ] Review and record program adoption decisions in the single [adoption checklist](../HOW-TO-USE.md#program-adoption-checklist). Maintain outcomes and approval references there.
- [ ] Coordinate any future Jira synchronization with the software factory. Manual linking is available now; live issue checks and updates are not implemented.

## Tooling

- [ ] **Deferred:** MkDocs documentation site. Do not start this work until a trigger below is met.
  - **What it is.** MkDocs turns the existing Markdown into a static website with a navigation sidebar, full-text search and in-page Mermaid rendering. It would be a reading convenience layered over the repository, not a replacement for it.
  - **Why it is deferred.** The current workflow is already complete. The generated [document index](../index.md) provides navigation, the auditor checks links, IDs and ancestry, and readers who use Git or an editor can already find and read everything. A site adds a build, a dependency set and a hosting decision without adding capability the project needs today.
  - **Trigger to revisit.** Revisit only when people outside Git (for example management, customer or program stakeholders) need to read this documentation regularly and the index plus GitHub rendering is no longer adequate for them.
  - **Constraint if adopted: no hand-maintained navigation.** Adding a document must stay exactly the current steps: create the file in its numbered directory with valid frontmatter, link it from its parent, regenerate the index, run the audit and commit. Do not introduce a hand-written `nav:` list in `mkdocs.yml`; it adds an unchecked step, and a forgotten entry silently hides a page. Use navigation derived from the directory structure, with the generated index as the entry point.
  - **Other constraints if adopted.** Keep the change reversible: add configuration only, with no edits to existing Markdown for the site's sake, so removing the site means deleting its configuration. Install Python dependencies in an isolated virtual environment. Exclude `000_import/` and the superseded planning snapshots in `900_project-admin/`. Decide hosting deliberately and record who the intended audience is; publishing a site makes the content easier to find than the repository alone, so confirm that is acceptable for the program before choosing a public host such as GitHub Pages.
  - **Known issues to check in any trial.** Frontmatter display on rendered pages, links to non-Markdown files such as `.py` and `.json`, the numeric directory prefixes appearing in derived navigation, and Mermaid and wide-table readability.
  - **Stop condition.** Time-box any trial to a single branch and a short session. If it needs plugins, custom scripts or auditor changes to be usable, record the findings here and drop it rather than expanding scope.

## Diagrams

- [ ] Refine the known title/edge crossings in network diagrams and rerender every edited block; see the [diagram verification record](../090_standards/diagram-verification.md).
- [ ] Verify maintained diagrams in the intended presentation viewer and record the viewer and findings.

## Records

- [ ] Populate actual implementation and customer disposition records as work occurs, following the [record standard](../090_standards/implementation-acceptance.md). The registers currently contain no deployment or acceptance claims.
