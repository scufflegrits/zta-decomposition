"""Shared YAML frontmatter schema for maintained project documents."""
from datetime import date
import re

import yaml


DOCUMENT_TYPES = (
    'navigation', 'guide', 'architecture', 'decision', 'pillar', 'control',
    'requirements', 'verification', 'procurement', 'reference', 'standard',
    'tooling', 'backlog',
)
FIELDS = {
    'schema_version', 'id', 'title', 'document_type', 'parent', 'lineage',
    'owner', 'owner_status', 'document_status', 'implementation_status', 'baseline_date',
}
ID = re.compile(r'[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*\Z')


class MetadataError(ValueError):
    def __init__(self, message, line=1):
        super().__init__(message)
        self.line = line


class UniqueLoader(yaml.SafeLoader):
    """Safe YAML loading with duplicate mapping keys rejected."""


def unique_mapping(loader, node):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str) or key in mapping:
            raise MetadataError('Metadata keys must be unique strings', key_node.start_mark.line + 2)
        mapping[key] = loader.construct_object(value_node)
    return mapping


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def mask_frontmatter(text):
    """Blank the opening YAML block, preserving original body line numbers."""
    lines = text.splitlines()
    if lines and lines[0] == '---':
        end = next((i for i in range(1, len(lines)) if lines[i] == '---'), len(lines) - 1)
        lines[:end + 1] = [''] * (end + 1)
    return '\n'.join(lines)


def read_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0] != '---':
        raise MetadataError('Document must begin with YAML frontmatter')
    end = next((i for i in range(1, len(lines)) if lines[i] == '---'), None)
    if end is None:
        raise MetadataError('Unterminated YAML frontmatter')
    try:
        data = yaml.load('\n'.join(lines[1:end]), Loader=UniqueLoader)
    except yaml.YAMLError as exc:
        mark = getattr(exc, 'problem_mark', None)
        raise MetadataError('Malformed YAML frontmatter: ' + str(exc), mark.line + 2 if mark else 1) from exc
    if not isinstance(data, dict) or set(data) != FIELDS:
        raise MetadataError('Frontmatter requires exactly: ' + ', '.join(sorted(FIELDS)))
    if type(data['schema_version']) is not int or data['schema_version'] != 1:
        raise MetadataError('schema_version must be integer 1')
    for key in FIELDS - {'schema_version', 'lineage'}:
        if not isinstance(data[key], str) or not data[key].strip() or '\n' in data[key]:
            raise MetadataError(f'{key} must be a nonempty single-line string')
    for key in ('id', 'parent'):
        if not ID.fullmatch(data[key]) or (key == 'id' and data[key] == 'ROOT'):
            raise MetadataError(f'Invalid {key}: {data[key]!r}')
    lineage = data['lineage']
    if (not isinstance(lineage, list) or not lineage
            or any(not isinstance(item, str) or not ID.fullmatch(item) for item in lineage)):
        raise MetadataError('lineage must be a nonempty list of identifiers')
    choices = {
        'document_type': DOCUMENT_TYPES,
        'owner_status': ('proposed', 'accepted'),
        'document_status': ('draft', 'in-review', 'approved', 'superseded'),
        'implementation_status': ('unvalidated', 'not-applicable'),
    }
    for key, allowed in choices.items():
        if data[key] not in allowed:
            raise MetadataError(f'{key} must be one of: {", ".join(allowed)}')
    try:
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', data['baseline_date']):
            raise ValueError()
        date.fromisoformat(data['baseline_date'])
    except ValueError as exc:
        raise MetadataError('baseline_date must be a quoted YYYY-MM-DD date') from exc
    return data


def frontmatter(data):
    return '---\n' + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + '---\n\n'
