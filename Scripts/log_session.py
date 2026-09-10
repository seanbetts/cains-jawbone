#!/usr/bin/env python3
"""Append one validated UTC session, recording the work commit before the log commit."""
import argparse
import csv
import fcntl
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from state_io import FIELDS, PHASES, text, utc, worklog


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    for field in ('start', 'agent', 'phase', 'task', 'notes'):
        p.add_argument('--' + field, required=True)
    p.add_argument('--end', default=None)
    a = p.parse_args()
    try:
        start = utc(a.start)
        end = utc(a.end) if a.end else datetime.now(timezone.utc).replace(microsecond=0)
        if end < start:
            raise ValueError('end must not precede start')
        if a.phase not in PHASES:
            raise ValueError('invalid phase')
        for field in ('agent', 'task', 'notes'):
            text(getattr(a, field), field)
        branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=a.root, text=True).strip()
        commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=a.root, text=True).strip()
        if not branch or branch == 'main':
            raise ValueError('log on an active run or infrastructure branch, not main/detached HEAD')
        path = a.root / 'Worklog/worklog.csv'
        # Serialize appends and validate before writing; no sidecar files are needed.
        with path.open('r+', encoding='utf-8', newline='') as stream:
            fcntl.flock(stream, fcntl.LOCK_EX)
            worklog(path, legacy=not (a.root / 'State').exists())
            stream.seek(0, 2)
            if stream.tell():
                stream.seek(stream.tell() - 1)
                if stream.read(1) != '\n':
                    raise ValueError('worklog must end with a newline')
            stream.seek(0, 2)
            minutes = int((end - start).total_seconds() / 60 + 0.5)
            csv.writer(stream, lineterminator='\n').writerow([
                start.date().isoformat(), a.agent, a.phase, a.task, a.start,
                end.strftime('%Y-%m-%dT%H:%M:%SZ'), minutes, branch, commit, a.notes])
        print(f'Logged {minutes} minutes against work commit {commit[:12]}. Commit the log separately.')
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
