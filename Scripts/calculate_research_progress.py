#!/usr/bin/env python3
"""Report coverage and recorded dispositions separately; never percent solved.

Default input is State/{research,claims}.jsonl and State/coverage.json.
This report checks IDs/statuses and coverage; run validate_state.py for full
record schemas, evidence, dependencies and constraints. --legacy reads actual
Markdown research records, excluding the labelled template, and counts their
historical labels without treating 'resolved' as verified.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[1]
RESEARCH_STATUSES = ('open', 'in_progress', 'verified', 'candidate', 'partial', 'no_match', 'deferred')
CLAIM_STATUSES = ('tentative', 'supported', 'strongly_constrained', 'rejected', 'suspended')
LEGACY_STATUSES = ('open', 'in-progress', 'stalled', 'resolved')
LEGACY_FIELDS = {'Type', 'Pages', 'Why it matters', 'Status', 'Result'}
FIELD_RE = re.compile(r'^\s*- \*\*([^*]+):\*\*\s*(.*?)\s*$')


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON field: {key}')
        result[key] = value
    return result


def counts(statuses, allowed):
    counted = Counter(statuses)
    return {'total': len(statuses), 'statuses': {status: counted[status] for status in allowed}}


def disposition_file(path: Path, allowed: tuple) -> dict:
    seen = set()
    statuses = []
    for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            continue
        label = f'{path.name}:{line_number}'
        try:
            record = json.loads(line, object_pairs_hook=unique_keys)
        except ValueError as error:
            raise ValueError(f'{label}: {error}') from error
        if not isinstance(record, dict):
            raise ValueError(f'{label}: expected a JSON object')
        identifier, status = record.get('id'), record.get('status')
        if not isinstance(identifier, str) or not identifier.strip():
            raise ValueError(f'{label}: missing or invalid id')
        if identifier in seen:
            raise ValueError(f'{label}: duplicate id {identifier}')
        if status not in allowed:
            raise ValueError(f'{label}: missing or unknown status {status!r}')
        seen.add(identifier)
        statuses.append(status)
    return counts(statuses, allowed)


def coverage_file(path: Path) -> dict:
    data = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_keys)
    if not isinstance(data, dict) or set(data) != {'read_pages'}:
        raise ValueError('coverage.json: expected only the read_pages field')
    pages = data['read_pages']
    if not isinstance(pages, list) or any(type(p) is not int or not 1 <= p <= 100 for p in pages):
        raise ValueError('coverage.json: read_pages must contain integer page IDs in 1..100')
    if len(set(pages)) != len(pages):
        raise ValueError('coverage.json: duplicate page IDs')
    return {'read_count': len(pages), 'total_pages': 100, 'unread_pages': [p for p in range(1, 101) if p not in pages]}


def legacy_research(path: Path) -> dict:
    """Parse field records, never loose occurrences of a Status label."""
    records = []
    current = None
    template = False
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if re.match(r'^(?:#+\s*)?Template\s*:', line, re.IGNORECASE):
            if current:
                records.append(current)
                current = None
            template = True
            continue
        if line.startswith('#'):
            if current:
                records.append(current)
                current = None
            template = bool(re.match(r'^#+\s+Template\b', line, re.IGNORECASE))
            continue
        if template:
            continue
        match = FIELD_RE.match(line)
        if not match:
            continue
        field, value = match.groups()
        if field == 'Item':
            if current:
                records.append(current)
            if not value:
                raise ValueError(f'{path.name}:{number}: empty Item outside template')
            current = {'Item': value, '_line': number}
        elif current is not None:
            if field not in LEGACY_FIELDS:
                raise ValueError(f'{path.name}:{number}: unknown field {field}')
            if field in current:
                raise ValueError(f'{path.name}:{number}: duplicate field {field}')
            current[field] = value
        else:
            raise ValueError(f'{path.name}:{number}: field {field} outside an Item')
    if current:
        records.append(current)
    statuses = []
    for record in records:
        label = f"{path.name}:{record['_line']}"
        missing = LEGACY_FIELDS - set(record)
        if missing:
            raise ValueError(f'{label}: missing fields {sorted(missing)}')
        for field in ('Type', 'Pages', 'Why it matters'):
            if not record[field]:
                raise ValueError(f'{label}: empty {field}')
        match = re.fullmatch(r'`(open|in-progress|stalled|resolved)`', record['Status'])
        if not match:
            raise ValueError(f'{label}: unknown or ambiguous Status {record["Status"]!r}')
        if match[1] == 'resolved' and not record['Result']:
            raise ValueError(f'{label}: resolved label without Result')
        page_ids = re.findall(r'Pages/cains_jawbone_page_(\d+)\.md', record['Pages'])
        if not page_ids or any(not 1 <= int(p) <= 100 for p in page_ids):
            raise ValueError(f'{label}: missing or invalid page references')
        statuses.append(match[1])
    return counts(statuses, LEGACY_STATUSES)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=REPO_ROOT)
    parser.add_argument('--legacy', action='store_true', help='Report historical Markdown labels instead of structured State data.')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    try:
        if args.legacy:
            report = {'limitation': 'Historical labels only; resolved does not mean source-verified.',
                      'legacy_research': legacy_research(args.root / 'Indexes' / 'research_queue.md')}
        else:
            state = args.root / 'State'
            report = {'limitation': 'Coverage and recorded dispositions only; full structural validation is separate and interpretation truth is not measured.',
                      'coverage': coverage_file(state / 'coverage.json'),
                      'research': disposition_file(state / 'research.jsonl', RESEARCH_STATUSES),
                      'claims': disposition_file(state / 'claims.jsonl', CLAIM_STATUSES)}
    except (OSError, ValueError) as error:
        parser.error(str(error))
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(report['limitation'])
        if 'coverage' in report:
            print(f"Pages read: {report['coverage']['read_count']}/100")
            print('Unread pages: ' + ', '.join(map(str, report['coverage']['unread_pages'])))
        for name in ('research', 'claims', 'legacy_research'):
            if name in report:
                group = report[name]
                print(f"\n{name.replace('_', ' ').capitalize()}: {group['total']} records")
                for status, count in group['statuses'].items():
                    print(f'  {status}: {count}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
