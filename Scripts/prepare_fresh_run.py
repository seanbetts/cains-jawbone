#!/usr/bin/env python3
"""Export an independent empty baseline; never copy solver state or Git history."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from state_io import FIELDS
from validate_state import validate
from verify_pages import md_body_before_notes

ROOT = Path(__file__).resolve().parents[1]
TREES = ('Scripts', 'Skills', 'Templates', 'Tests')
ROOT_FILES = ('AGENTS.md', 'README.md', '.gitignore')
INDEX_TEMPLATES = ('people', 'places', 'quotes', 'objects_motifs', 'narrators', 'wordplay', 'research_queue')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root):
    return {p.relative_to(root).as_posix(): digest(p) for p in sorted(root.rglob('*'))
            if p.is_file() and p.name != 'BASELINE_MANIFEST.json' and '__pycache__' not in p.parts}


def verified_body_source(root):
    result = subprocess.run([sys.executable, str(ROOT / 'Scripts/verify_pages.py'), '--pages-dir', str(root / 'Pages'),
              '--archive', str(root / 'Archive' / "Cain's Jawbone Unformatted.txt"), '--hash-file', str(root / 'Archive/hash.txt')],
              capture_output=True, text=True)
    if result.returncode:
        raise ValueError(result.stderr.strip() or result.stdout.strip())


def safe_tree(source, target):
    if source.is_symlink() or not source.is_dir():
        raise ValueError(f'Not an ordinary source directory: {source}')
    target.mkdir()
    for path in sorted(source.rglob('*')):
        rel = path.relative_to(source)
        if '__pycache__' in rel.parts or path.suffix in {'.pyc', '.pyo'}:
            continue
        if path.is_symlink():
            raise ValueError(f'Symlink is not allowed in baseline inputs: {path}')
        dest = target / rel
        if path.is_dir():
            dest.mkdir(exist_ok=True)
        elif path.is_file():
            shutil.copy2(path, dest)
        else:
            raise ValueError(f'Unsupported source entry: {path}')


def check_manifest(root):
    if root.is_symlink() or any(p.is_symlink() for p in root.rglob('*')):
        raise ValueError('Baseline contains a symlink')
    manifest = json.loads((root / 'BASELINE_MANIFEST.json').read_text())
    actual = inventory(root)
    if actual != manifest['files']:
        differences = sorted(k for k in set(actual) | set(manifest['files']) if actual.get(k) != manifest['files'].get(k))
        raise ValueError(f'Baseline manifest mismatch: {differences}')
    if (root / '.git').exists():
        raise ValueError('This pristine baseline check is before Git initialization or solving')
    verified_body_source(root)
    validate(root)
    return manifest


def prepare(source, destination):
    source = source.resolve()
    destination = destination.absolute()
    if destination.exists() or destination.is_symlink():
        raise ValueError('Destination already exists; refusing to overlay or replace it')
    destination = destination.resolve()
    if destination.is_relative_to(source):
        raise ValueError('Destination must be outside the old workspace')
    if not destination.parent.is_dir():
        raise ValueError('Destination parent must already exist')
    for folder in ('Archive', 'Pages', *TREES):
        tree = source / folder
        if tree.is_symlink() or any(p.is_symlink() for p in tree.rglob('*')):
            raise ValueError(f'Symlink in allowed input tree {folder}')
    verified_body_source(source)
    with tempfile.TemporaryDirectory(prefix='.cjb-baseline-', dir=destination.parent) as temporary:
        stage = Path(temporary) / 'baseline'
        stage.mkdir()
        for tree in TREES:
            safe_tree(source / tree, stage / tree)
        for name in ROOT_FILES:
            path = source / name
            if path.is_symlink() or not path.is_file():
                raise ValueError(f'Invalid allowlisted root file {path}')
            shutil.copy2(path, stage / name)
        for folder in ('Archive', 'Pages', 'Indexes', 'Order', 'State', 'Sources', 'Worklog'):
            (stage / folder).mkdir()
        for name in ("Cain's Jawbone Unformatted.txt", 'hash.txt'):
            shutil.copy2(source / 'Archive' / name, stage / 'Archive' / name)
        for i in range(1, 101):
            name = f'cains_jawbone_page_{i}.md'
            with (source / 'Pages' / name).open(encoding='utf-8', newline='') as stream:
                body = md_body_before_notes(stream.read())
            (stage / 'Pages' / name).write_text(body + '## Notes\n', encoding='utf-8')
        for name in INDEX_TEMPLATES:
            shutil.copy2(stage / 'Templates' / f'{name}.md', stage / 'Indexes' / f'{name}.md')
        (stage / 'Indexes/SCHEMA.md').write_text('# Index views\n\nCanonical records: `Templates/SCHEMA.md`.\n')
        shutil.copy2(stage / 'Templates/reference_sources.md', stage / 'Indexes/reference_sources.md')
        for name in ('hypotheses', 'cast', 'confidence'):
            shutil.copy2(stage / 'Templates' / f'{name}.md', stage / 'Order' / f'{name}.md')
        for name in ('evidence', 'claims', 'research', 'tests', 'events'):
            (stage / 'State' / f'{name}.jsonl').write_text('')
        for name, value in [('order', dict(pages=[], complete=False, accepted_claims=[])),
                            ('coverage', dict(read_pages=[])),
                            ('readiness', dict(ready=False, reviewer='', summary='', unresolved_structural=[]))]:
            (stage / 'State' / f'{name}.json').write_text(json.dumps(value, indent=2) + '\n')
        (stage / 'Sources/catalog.json').write_text('[]\n')
        (stage / 'Worklog/current_run.txt').write_text('')
        (stage / 'Worklog/worklog.csv').write_text(','.join(FIELDS) + '\n')
        (stage / 'FINAL_SOLUTION.md').write_text('')
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=source, capture_output=True, text=True)
        commit = result.stdout.strip() if result.returncode == 0 else None
        manifest = dict(schema_version=2, tooling_commit=commit, source_sha256=digest(stage / 'Archive' / "Cain's Jawbone Unformatted.txt"),
                        limitation='Archive agreement is not original-edition authentication. No old solving state or Git history exported.',
                        files=inventory(stage))
        (stage / 'BASELINE_MANIFEST.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
        check_manifest(stage)
        # mkdir claims destination without overwriting; move only into our newly claimed empty folder.
        destination.mkdir()
        try:
            for path in stage.iterdir():
                shutil.move(str(path), str(destination / path.name))
        except BaseException:
            shutil.rmtree(destination)
            raise
    check_manifest(destination)
    return manifest


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source', type=Path, default=ROOT)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument('--destination', type=Path)
    group.add_argument('--verify', type=Path, help='Verify the pristine export manifest before starting work')
    a = p.parse_args()
    try:
        manifest = check_manifest(a.verify) if a.verify else prepare(a.source, a.destination)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    print(f'OK: independent baseline, {len(manifest["files"])} verified files; solving has not started.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
