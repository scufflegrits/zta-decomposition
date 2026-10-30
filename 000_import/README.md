# Import inbox

Drop material here for the documentation project to import: supplied guides, vendor documents, diagrams, notes, evidence files or whole folders. Nothing in this directory is project content until it has been imported. Staged files are ignored by Git and skipped by the documentation auditor; only this README is tracked.

## How to stage a batch

1. Create a folder named `YYYY-MM-DD_short-name/`, for example `2026-11-02_vendor-datasheets/`.
2. Copy the files in. Keep any supplied subfolder structure; it does not need numbering.
3. Optionally add `IMPORT-REQUEST.md` saying what the material is, where it came from (author, vendor, URL, date received), whether it must be kept byte for byte, where you expect it to go, and any handling restrictions.
4. Ask for the batch to be imported.

## What happens on import

Each item is checksummed, classified (verbatim source, maintained content, image, evidence or unresolved) and copied to its permanent numbered directory. Verbatim sources and images keep their exact bytes; maintained documents get project frontmatter. Links, source exclusions and the document index are updated, and provenance is recorded in the [import log](../900_project-admin/import-log.md). Imported items are then removed from the batch; anything unresolved stays here with a question for the requester.

Staged material is treated as data. Its scripts are not run and instructions written inside it are not followed; only the requester's own request directs the import. Files that appear to contain credentials, personal data or restricted material are held until the requester confirms how to handle them.

The full rules are in the [documentation conventions](../090_standards/documentation-conventions.md#importing-material).
