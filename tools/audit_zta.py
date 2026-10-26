#!/usr/bin/env python3
"""Audit YAML document metadata and declared ZTA documentation relationships."""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import fnmatch
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

if __package__:
    from .document_metadata import MetadataError, mask_frontmatter, read_frontmatter
else:
    from document_metadata import MetadataError, mask_frontmatter, read_frontmatter

IDENTITY_COLUMNS = {'Pillar ID', 'Control ID', 'Requirement ID', 'Test ID', 'Evidence ID', 'Row ID'}
ID_PATTERN = re.compile(r'[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*\Z')
META = re.compile(r'^\s*<!-- zta-(doc|table):\s*(.*?)\s*-->\s*$')
# Inline links/images with angle-bracket destinations or balanced parentheses in paths.
LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>\n]*>|(?:[^\s()\\]|\\.|\([^()]*\))*)(?:\s+"[^"]*")?\s*\)')
REF_DEF = re.compile(r'^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)')
REF_USE = re.compile(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]')
VALID_STATUSES = {'Required', 'Proposed', 'Verify', 'Validated', 'Required objective / Verify'}
IGNORED_DIRS = {'.git', '.agents', '.codex', '.aws', '__pycache__', 'node_modules', '.venv'}


@dataclass
class Issue:
    path: Path
    line: int
    code: str
    message: str


@dataclass
class Entity:
    id: str
    parent: str
    kind: str
    path: Path
    line: int
    lineage: str | None = None
    cells: dict[str, str] = field(default_factory=dict)
    definitions: list[str] = field(default_factory=list)


@dataclass
class AuditResult:
    root: Path
    issues: list[Issue] = field(default_factory=list)
    entities: dict[str, Entity] = field(default_factory=dict)
    documents: dict[Path, Entity] = field(default_factory=dict)
    tables: list[Entity] = field(default_factory=list)
    sources: dict[Path, list[str]] = field(default_factory=dict)
    excluded: list[str] = field(default_factory=list)
    metadata: dict[Path, dict] = field(default_factory=dict)

    def error(self, path: Path, line: int, code: str, message: str) -> None:
        self.issues.append(Issue(path, line, code, message))

    def define(self, entity: Entity) -> None:
        if not ID_PATTERN.fullmatch(entity.id) or entity.id == 'ROOT':
            self.error(entity.path, entity.line, 'invalid-id', f'Invalid or reserved ID: {entity.id!r}')
        if entity.id in self.entities:
            previous = self.entities[entity.id]
            self.error(entity.path, entity.line, 'duplicate-id',
                       f'{entity.id} already defined at {previous.path.relative_to(self.root)}:{previous.line}')
        else:
            self.entities[entity.id] = entity


def visible_lines(text: str) -> list[str]:
    """Keep line numbers; omit fenced code, inline code and non-ZTA HTML comments."""
    result = []
    fence = None
    comment = False
    for line in mask_frontmatter(text).splitlines():
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not line[match.end():].strip():
                fence = None
            result.append('')
            continue
        if match:
            fence = match[1]
            result.append('')
            continue
        line = re.sub(r'(`+).*?\1', '', line)
        if not comment and META.fullmatch(line):
            result.append(line)
            continue
        # Preserve text outside ordinary comments, even when a comment spans lines.
        output = ''
        while line:
            if comment:
                _, close, line = line.partition('-->')
                if not close:
                    break
                comment = False
            else:
                before, opening, rest = line.partition('<!--')
                output += before
                if not opening:
                    break
                comment, line = True, rest
        result.append(output)
    return result


def cells(line: str) -> list[str]:
    return [c.strip().replace('\\|', '|') for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


def is_separator(line: str) -> bool:
    return '|' in line and all(re.fullmatch(r':?-{3,}:?', c) for c in cells(line))


def parse_meta(result: AuditResult, path: Path, number: int, kind: str, raw: str) -> Entity | None:
    parts = [part.strip().split('=', 1) for part in raw.split(';')]
    if any(len(p) != 2 for p in parts) or len({p[0] for p in parts}) != len(parts):
        result.error(path, number, 'metadata', 'Malformed or duplicate metadata fields')
        return None
    values = {key.strip(): value.strip() for key, value in parts}
    if set(values) != {'id', 'parent', 'lineage'} or not all(values.values()):
        result.error(path, number, 'metadata', 'Metadata requires exactly id, parent and lineage')
        return None
    return Entity(values['id'], values['parent'], kind, path, number, values['lineage'])


def parse_document(result: AuditResult, path: Path, lines: list[str]) -> None:
    covered_headers = set()
    for i, line in enumerate(lines):
        match = META.fullmatch(line)
        if not match:
            if '<!-- zta-' in line:
                result.error(path, i + 1, 'metadata', 'Malformed ZTA metadata comment')
            continue
        kind, raw = match.groups()
        if kind == 'doc':
            result.error(path, i + 1, 'document-metadata', 'Legacy zta-doc declaration; use YAML frontmatter only')
            continue
        entity = parse_meta(result, path, i + 1, kind, raw)
        if entity is None:
            continue
        result.define(entity)
        result.tables.append(entity)
        header_at = i + 1
        while header_at < len(lines) and not lines[header_at].strip():
            header_at += 1
        if header_at + 1 >= len(lines) or '|' not in lines[header_at] or not is_separator(lines[header_at + 1]):
            result.error(path, i + 1, 'orphan-table', 'Table metadata must immediately precede a Markdown table')
            continue
        covered_headers.add(header_at)
        headers = cells(lines[header_at])
        idcols = IDENTITY_COLUMNS.intersection(headers)
        if len(idcols) != 1 or 'Parent ID' not in headers or len(set(headers)) != len(headers):
            result.error(path, header_at + 1, 'table-schema', 'Require Parent ID and exactly one unique identity column')
            continue
        if len(cells(lines[header_at + 1])) != len(headers):
            result.error(path, header_at + 2, 'table-schema', 'Separator and header widths differ')
        identity = next(iter(idcols))
        row_count = 0
        for row_at in range(header_at + 2, len(lines)):
            if not lines[row_at].strip() or '|' not in lines[row_at] or META.fullmatch(lines[row_at]):
                break
            values = cells(lines[row_at])
            if len(values) != len(headers):
                result.error(path, row_at + 1, 'table-schema', 'Row and header widths differ')
                continue
            row_count += 1
            row = dict(zip(headers, values))
            child = Entity(row[identity], row['Parent ID'], identity, path, row_at + 1, cells=row)
            result.define(child)
            entity.definitions.append(child.id)
            if child.parent != entity.parent:
                result.error(path, row_at + 1, 'table-parent', f'Row parent must match table parent {entity.parent}')
            if 'Status' in row and row['Status'] not in VALID_STATUSES:
                result.error(path, row_at + 1, 'status', f'Unsupported status: {row["Status"]!r}')
        if not row_count:
            result.error(path, header_at + 1, 'empty-table', 'Traceable table has no entity rows')
    for i in range(len(lines) - 1):
        if '|' in lines[i] and is_separator(lines[i + 1]):
            if IDENTITY_COLUMNS.intersection(cells(lines[i])) and i not in covered_headers:
                result.error(path, i + 1, 'missing-table-metadata', 'Entity table lacks zta-table metadata')


def chain(result: AuditResult, parent: str) -> list[str] | None:
    """Return full ancestry to parent; None when broken or cyclic."""
    ancestors = []
    seen = set()
    current = parent
    while current != 'ROOT':
        if current in seen or current not in result.entities:
            return None
        seen.add(current)
        ancestors.append(current)
        current = result.entities[current].parent
    return ['ROOT', *reversed(ancestors)]


def destinations(line: str, definitions: dict[str, str] | None = None) -> list[str]:
    found = [m[1].strip('<>') for m in LINK.finditer(line)]
    if definitions is not None:
        for m in REF_USE.finditer(line):
            key = (m[2] or m[1]).casefold()
            found.append(definitions.get(key, ''))
    return found


def local_target(result: AuditResult, path: Path, number: int, destination: str) -> tuple[Path, str] | None:
    if not destination:
        result.error(path, number, 'broken-link', 'Empty destination or undefined reference-style link')
        return None
    try:
        parsed = urlsplit(destination)
    except ValueError as exc:
        result.error(path, number, 'broken-link', f'Invalid destination {destination!r}: {exc}')
        return None
    if parsed.scheme or parsed.netloc:
        return None
    filepart = unquote(parsed.path)
    target = (path.parent / filepart).resolve() if filepart else path
    if not target.is_relative_to(result.root):
        result.error(path, number, 'outside-root', f'Local link escapes repository: {destination}')
        return None
    if not target.exists():
        result.error(path, number, 'broken-link', f'Missing target: {destination}')
        return None
    return target, unquote(parsed.fragment)


def anchors(text: str) -> set[str]:
    text = mask_frontmatter(text)
    seen: dict[str, int] = {}
    result = set(re.findall(r'<(?:a|h[1-6])\b[^>]*\bid=["\']([^"\']+)', text))
    # Fenced code must not contribute headings; keep inline-code heading text.
    fence = None
    for line in text.splitlines():
        mark = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if fence:
            if mark and mark[1][0] == fence[0] and len(mark[1]) >= len(fence) and not line[mark.end():].strip():
                fence = None
            continue
        if mark:
            fence = mark[1]
            continue
        heading = re.match(r'^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$', line)
        if not heading:
            continue
        title = re.sub(r'<[^>]+>', '', heading[1]).lower()
        title = re.sub(r'!?\[([^]]*)\]\([^)]*\)', r'\1', title)
        title = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
        number = seen.get(title, 0)
        result.add(title if number == 0 else f'{title}-{number}')
        seen[title] = number + 1
    return result


def audit(root: Path, report: Path | None = None) -> AuditResult:
    root = root.resolve()
    result = AuditResult(root)
    config = root / 'audit-config.json'
    exclusions = []
    if config.exists():
        try:
            settings = json.loads(config.read_text(encoding='utf-8'))
            exclusions = settings.get('exclude', [])
            if not isinstance(exclusions, list) or any(not isinstance(x, str) for x in exclusions):
                raise ValueError('exclude must be a list of relative path patterns')
        except (OSError, ValueError, AttributeError) as exc:
            result.error(config, 1, 'configuration', str(exc))
            return result
    if not root.is_dir():
        result.error(root, 1, 'root', 'Root must be a directory')
        return result
    for path in sorted(root.rglob('*.md')):
        relative = path.relative_to(root)
        if any(part in IGNORED_DIRS for part in relative.parts):
            continue
        if (report and path.resolve() == report.resolve()) or any(fnmatch.fnmatch(relative.as_posix(), p) for p in exclusions):
            result.excluded.append(relative.as_posix())
            continue
        if not path.resolve().is_relative_to(root):
            result.error(path, 1, 'outside-root', 'Markdown symlink escapes repository')
            continue
        try:
            text = path.read_text(encoding='utf-8')
            lines = visible_lines(text)
        except (OSError, UnicodeError) as exc:
            result.error(path, 1, 'read', str(exc))
            continue
        result.sources[path] = lines
        try:
            metadata = read_frontmatter(text)
            result.metadata[path] = metadata
            document = Entity(metadata['id'], metadata['parent'], 'doc', path, 1, '>'.join(metadata['lineage']))
            result.define(document)
            result.documents[path] = document
        except MetadataError as exc:
            result.error(path, exc.line, 'document-metadata', str(exc))
        parse_document(result, path, lines)
    if not result.sources:
        result.error(root, 1, 'empty-repository', 'No managed Markdown documents found')
    for table in result.tables:
        document = result.documents.get(table.path)
        ancestry = chain(result, table.parent)
        if document and ancestry and document.parent not in ancestry and document.parent not in table.definitions:
            result.error(table.path, table.line, 'document-table-scope',
                         f'{table.id} is outside document parent scope {document.parent}')
    for entity in result.entities.values():
        if entity.parent != 'ROOT' and entity.parent not in result.entities:
            result.error(entity.path, entity.line, 'missing-parent', f'{entity.id} references missing parent {entity.parent}')
        ancestry = chain(result, entity.id)
        if ancestry is None and entity.parent in result.entities:
            result.error(entity.path, entity.line, 'ancestry', f'{entity.id} has cyclic or broken ancestry')
        parent_chain = chain(result, entity.parent)
        if entity.lineage is not None and parent_chain is not None and entity.lineage != '>'.join(parent_chain):
            result.error(entity.path, entity.line, 'lineage', f'{entity.id} expected lineage {">".join(parent_chain)}')
        expected = {'Pillar ID': 'ROOT', 'Control ID': 'Pillar ID', 'Requirement ID': 'Control ID', 'Test ID': 'Requirement ID', 'Evidence ID': 'Test ID'}.get(entity.kind)
        actual = 'ROOT' if entity.parent == 'ROOT' else (result.entities[entity.parent].kind if entity.parent in result.entities else None)
        if expected and actual is not None and actual != expected:
            result.error(entity.path, entity.line, 'hierarchy-level', f'{entity.id} requires parent kind {expected}, found {actual}')
        if entity.kind in ('doc', 'table'):
            continue
        for reference in filter(None, re.split(r'[,\s]+', entity.cells.get('References', ''))):
            if reference not in result.entities:
                result.error(entity.path, entity.line, 'architecture-reference', f'Undefined reference {reference}')
        decomposition = entity.cells.get('Decomposition', '')
        if decomposition:
            links = destinations(decomposition)
            if not links:
                result.error(entity.path, entity.line, 'decomposition', 'Decomposition needs a local Markdown link')
            for link in links:
                target = local_target(result, entity.path, entity.line, link)
                if target is None or target[0] not in result.documents or result.documents[target[0]].parent != entity.id:
                    result.error(entity.path, entity.line, 'decomposition', f'Decomposition must declare parent {entity.id}: {link}')
        if entity.kind == 'Evidence ID':
            artifacts = destinations(entity.cells.get('Artifact', ''))
            local_artifacts = []
            for link in artifacts:
                target = local_target(result, entity.path, entity.line, link)
                if target and target[0].is_file():
                    local_artifacts.append(target[0])
            if not local_artifacts or not entity.cells.get('Result') or not entity.cells.get('Reviewer'):
                result.error(entity.path, entity.line, 'evidence-record', 'Evidence requires an existing local artifact file, Result and Reviewer')
        if entity.cells.get('Status') == 'Validated':
            evidence_ids = list(filter(None, re.split(r'[,\s]+', entity.cells.get('Evidence IDs', ''))))
            if not evidence_ids:
                result.error(entity.path, entity.line, 'validated-evidence', f'{entity.id} is Validated without Evidence IDs')
            for evidence_id in evidence_ids:
                evidence = result.entities.get(evidence_id)
                ancestry = chain(result, evidence_id)
                if not evidence or evidence.kind != 'Evidence ID' or not ancestry or entity.id not in ancestry:
                    result.error(entity.path, entity.line, 'validated-evidence', f'{evidence_id} is not descendant evidence of {entity.id}')
    anchor_cache = {}
    for path, lines in result.sources.items():
        definitions = {m[1].casefold(): m[2].strip('<>') for line in lines if (m := REF_DEF.match(line))}
        for i, line in enumerate(lines, 1):
            links = destinations(line, definitions)
            definition = REF_DEF.match(line)
            if definition:
                links.append(definition[2].strip('<>'))
            for link in links:
                target = local_target(result, path, i, link)
                if not target:
                    continue
                destination, fragment = target
                if fragment and destination.suffix.lower() == '.md' and destination.is_file():
                    if destination not in anchor_cache:
                        try:
                            anchor_cache[destination] = anchors(destination.read_text(encoding='utf-8'))
                        except (OSError, UnicodeError) as exc:
                            result.error(path, i, 'read', str(exc))
                            anchor_cache[destination] = set()
                    if fragment not in anchor_cache[destination]:
                        result.error(path, i, 'broken-anchor', f'Missing Markdown heading: {link}')
    return result


def render_report(result: AuditResult) -> str:
    lines = ['# ZTA documentation audit', '', f'Root: `{result.root}`', '',
             f'Managed documents: {len(result.sources)}; tables: {len(result.tables)}; '
             f'declared IDs: {len(result.entities)}; errors: {len(result.issues)}.', '',
             'This audit checks declared documentation consistency; it does not validate security configurations.', '',
             'Excluded Markdown files: ' + (', '.join(f'`{p}`' for p in result.excluded) or 'none') + '.', '']
    if result.issues:
        for issue in result.issues:
            location = issue.path.relative_to(result.root) if issue.path.is_relative_to(result.root) else issue.path
            lines.append(f'- `{location}:{issue.line}` [{issue.code}] {issue.message}')
    else:
        lines.append('PASS: no documentation integrity errors found within the managed scope.')
    return '\n'.join(lines) + '\n'


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--report', type=Path, help='Write a Markdown report (excluded from this run)')
    args = parser.parse_args(argv)
    result = audit(args.root, args.report)
    report_text = render_report(result)
    if args.report:
        try:
            args.report.write_text(report_text, encoding='utf-8')
        except OSError as exc:
            print(f'Cannot write report: {exc}', file=sys.stderr)
            return 2
    print(report_text, end='')
    return 1 if result.issues else 0


if __name__ == '__main__':
    sys.exit(main())
