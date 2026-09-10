import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
HEADER = 'date,agent,phase,task,start,end,minutes,branch,commit,notes\n'


def corpus(root):
    root = Path(root)
    for folder in ('Archive', 'Pages', 'Worklog', 'State', 'Sources'):
        (root / folder).mkdir(parents=True, exist_ok=True)
    bodies = [f'Synthetic page {i}. Amber cobalt ivory.\n' for i in range(1, 101)]
    source = '\n____\n'.join(bodies)
    (root / 'Archive' / "Cain's Jawbone Unformatted.txt").write_text(source)
    (root / 'Archive/hash.txt').write_text(hashlib.sha256(source.encode()).hexdigest() + '\n')
    for i, body in enumerate(bodies, 1):
        (root / 'Pages' / f'cains_jawbone_page_{i}.md').write_text(body + '\n## Notes\n')
    (root / 'Worklog/worklog.csv').write_text(HEADER)
    (root / 'Worklog/current_run.txt').write_text('')
    (root / 'Sources/catalog.json').write_text('[]\n')
    for name in ('evidence', 'claims', 'research', 'tests', 'events'):
        (root / 'State' / f'{name}.jsonl').write_text('')
    write_json(root, 'State/order.json', dict(pages=[], complete=False, accepted_claims=[]))
    write_json(root, 'State/coverage.json', dict(read_pages=[]))
    write_json(root, 'State/readiness.json', dict(ready=False, reviewer='', summary='', unresolved_structural=[]))
    return root


def write_json(root, name, value):
    (Path(root) / name).write_text(json.dumps(value) + '\n')


def records(root, name, values):
    (Path(root) / 'State' / f'{name}.jsonl').write_text(''.join(json.dumps(x) + '\n' for x in values))


def evidence():
    return dict(id='V001', page=1, span='Amber', offset=18, layer='narration',
                observation='A colour word occurs.', status='active')


def claim(**changes):
    value = dict(id='C001', revision=1, relation='precedes', pages=[1, 2],
                 statement='Synthetic first page precedes the second.', evidence=['V001'],
                 dependencies={}, status='supported', alternatives=['Unrelated scenes'],
                 falsifier='An explicit reversed date.', next_test='Read the time cues.')
    value.update(changes)
    return value


def run(name, *args):
    return subprocess.run([sys.executable, str(REPO / 'Scripts' / name), *map(str, args)],
                          text=True, capture_output=True)
