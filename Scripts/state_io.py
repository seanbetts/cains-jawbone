"""Strict, small record readers shared by administrative tools (standard library only)."""
from __future__ import annotations

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

FIELDS = ['date', 'agent', 'phase', 'task', 'start', 'end', 'minutes', 'branch', 'commit', 'notes']
PHASES = {'admin', *(f'phase-{i}' for i in range(1, 7))}


def utc(value: str) -> datetime:
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', value):
        raise ValueError(f'Expected UTC YYYY-MM-DDTHH:MM:SSZ: {value!r}')
    return datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(timezone.utc)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON field {key}')
        result[key] = value
    return result


def json_file(path: Path):
    try:
        return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
    except (OSError, ValueError) as exc:
        raise ValueError(f'{path}: {exc}') from exc


def json_lines(path: Path, prefix: str):
    result = {}
    try:
        lines = path.read_text(encoding='utf-8').splitlines()
    except OSError as exc:
        raise ValueError(f'{path}: {exc}') from exc
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line, object_pairs_hook=unique_object)
            if not isinstance(record, dict) or not re.fullmatch(prefix + r'\d{3,}', str(record.get('id', ''))):
                raise ValueError(f'expected {prefix} ID with at least three digits')
            if record['id'] in result:
                raise ValueError(f'duplicate ID {record["id"]}')
            result[record['id']] = record
        except (ValueError, TypeError) as exc:
            raise ValueError(f'{path}:{number}: {exc}') from exc
    return result


def keys(record, required, label):
    if not isinstance(record, dict):
        raise ValueError(f'{label}: expected an object')
    missing = set(required) - record.keys()
    unknown = record.keys() - set(required)
    if missing or unknown:
        raise ValueError(f'{label}: missing fields {sorted(missing)}; unknown fields {sorted(unknown)}')


def text(value, label, *, empty=False):
    if not isinstance(value, str) or (not empty and not value.strip()):
        raise ValueError(f'{label}: expected {"a string" if empty else "nonempty text"}')


def strings(value, label):
    if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
        raise ValueError(f'{label}: expected list of nonempty strings')


def pages(value, label):
    if not isinstance(value, list) or any(type(x) is not int or not 1 <= x <= 100 for x in value):
        raise ValueError(f'{label}: expected page numbers 1..100')
    if len(set(value)) != len(value):
        raise ValueError(f'{label}: duplicate page number')


def worklog(path: Path, *, legacy=False):
    try:
        with path.open(encoding='utf-8', newline='') as stream:
            rows = list(csv.reader(stream, strict=True))
    except (OSError, csv.Error) as exc:
        raise ValueError(f'CSV {path}: {exc}') from exc
    if not rows or rows[0] != FIELDS:
        raise ValueError(f'CSV {path}: invalid header')
    for n, row in enumerate(rows[1:], 2):
        if len(row) != len(FIELDS):
            raise ValueError(f'CSV {path}:{n}: expected 10 columns, found {len(row)}')
        r = dict(zip(FIELDS, row))
        try:
            start, end = utc(r['start']), utc(r['end'])
            if end < start or r['date'] != start.date().isoformat():
                raise ValueError('date or end precedes start')
            if not re.fullmatch(r'\d+', r['minutes']):
                raise ValueError('minutes must be a nonnegative integer')
            if not legacy and abs(int(r['minutes']) - (end - start).total_seconds()/60) > 0.5 + 1e-9:
                raise ValueError('minutes do not match elapsed time')
            if r['phase'] not in PHASES:
                raise ValueError('unknown phase')
            for field in ('agent', 'task', 'branch', 'commit', 'notes'):
                if legacy and field == 'commit' and not r[field]:
                    continue
                text(r[field], field)
        except ValueError as exc:
            raise ValueError(f'CSV {path}:{n}: {exc}') from exc
    return rows
