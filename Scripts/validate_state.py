#!/usr/bin/env python3
"""Validate record structure and explicit constraints; never certify literary truth."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from state_io import json_file, json_lines, keys, pages, strings, text, worklog
from verify_pages import md_body_before_notes

RELATIONS = {'same_narrator', 'same_entity', 'same_scene', 'shared_reference', 'precedes', 'adjacent',
             'incompatible', 'entity_identity', 'death', 'intentional_killing', 'victim_identity',
             'perpetrator_identity', 'narrator_assignment', 'wordplay', 'source_interpretation',
             'date_interpretation', 'place_interpretation'}
CLAIM_STATES = {'tentative', 'supported', 'strongly_constrained', 'rejected', 'suspended'}
RESEARCH_STATES = {'open', 'in_progress', 'verified', 'candidate', 'partial', 'no_match', 'deferred'}
LIVE = {'tentative', 'supported', 'strongly_constrained'}


def choice(value, allowed, label):
    if not isinstance(value, str) or value not in allowed:
        raise ValueError(f'{label}: expected one of {sorted(allowed)}')


def acyclic(graph, label):
    active, done = set(), set()
    def visit(node):
        if node in active:
            raise ValueError(f'{label}: cycle at {node}')
        if node in done:
            return
        active.add(node)
        for other in graph.get(node, []):
            visit(other)
        active.remove(node)
        done.add(node)
    for node in graph:
        visit(node)


def revision(value, label):
    if type(value) is not int or value < 1:
        raise ValueError(f'{label}: revision must be a positive integer')


def uniquely_constrained(graph, order, next_page, prev_page):
    """Check uniqueness of a declared order by DAG elimination; no permutation search."""
    # Adjacency forces whole chains to stay contiguous; collapse these first.
    blocks, owner = {}, {}
    for start in range(1, 101):
        if start in prev_page:
            continue
        chain, node = [], start
        while True:
            chain.append(node)
            owner[node] = start
            if node not in next_page:
                break
            node = next_page[node]
        blocks[start] = chain
    edges = {b: set() for b in blocks}
    for a, targets in graph.items():
        for b in targets:
            if owner[a] != owner[b]:
                edges[owner[a]].add(owner[b])
    indegree = dict.fromkeys(blocks, 0)
    for targets in edges.values():
        for b in targets:
            indegree[b] += 1
    result = []
    while indegree:
        available = [p for p, degree in indegree.items() if degree == 0]
        if len(available) != 1:
            raise ValueError('final order is not uniquely determined by accepted ordering constraints')
        node = available[0]
        result.extend(blocks[node])
        del indegree[node]
        for b in edges[node]:
            indegree[b] -= 1
    if result != order:
        raise ValueError('final order differs from the uniquely constrained order')


def validate(root: Path, final=False):
    worklog(root / 'Worklog/worklog.csv')
    evidence = json_lines(root / 'State/evidence.jsonl', 'V')
    claims = json_lines(root / 'State/claims.jsonl', 'C')
    research = json_lines(root / 'State/research.jsonl', 'R')
    tests = json_lines(root / 'State/tests.jsonl', 'T')
    events = json_lines(root / 'State/events.jsonl', 'E')
    catalog = json_file(root / 'Sources/catalog.json')
    if not isinstance(catalog, list):
        raise ValueError('Sources/catalog.json must be a list')
    sources = {}
    for source in catalog:
        keys(source, {'id', 'revision', 'title', 'year', 'url', 'admission_note'}, 'source')
        revision(source['revision'], 'source')
        for field in ('id', 'title', 'url', 'admission_note'):
            text(source[field], f'source {field}')
        if not re.fullmatch(r'S\d{3,}', source['id']) or source['id'] in sources:
            raise ValueError(f'duplicate or invalid source ID {source["id"]}')
        if type(source['year']) is not int or not 1 <= source['year'] <= 1934:
            raise ValueError(f'{source["id"]}: admitted edition must be dated <=1934')
        if not source['url'].startswith(('https://', 'http://')):
            raise ValueError(f'{source["id"]}: source URL must be HTTP(S)')
        sources[source['id']] = source
    bodies = {}
    for eid, e in evidence.items():
        keys(e, {'id', 'page', 'span', 'offset', 'layer', 'observation', 'status'}, eid)
        pages([e['page']], eid)
        for field in ('span', 'observation'):
            text(e[field], f'{eid} {field}')
        if type(e['offset']) is not int or e['offset'] < 0:
            raise ValueError(f'{eid}: offset must be a nonnegative integer')
        choice(e['layer'], {'narration', 'dialogue', 'quotation', 'unclear'}, eid)
        choice(e['status'], {'active', 'withdrawn'}, eid)
        p = e['page']
        if p not in bodies:
            with (root / 'Pages' / f'cains_jawbone_page_{p}.md').open(encoding='utf-8', newline='') as stream:
                bodies[p] = md_body_before_notes(stream.read())
        if bodies[p][e['offset']:e['offset'] + len(e['span'])] != e['span']:
            raise ValueError(f'{eid}: span does not match page {p} at offset {e["offset"]}')
    for cid, c in claims.items():
        keys(c, {'id', 'revision', 'relation', 'pages', 'statement', 'evidence', 'dependencies', 'status',
                 'alternatives', 'falsifier', 'next_test'}, cid)
        revision(c['revision'], cid)
        choice(c['relation'], RELATIONS, cid)
        choice(c['status'], CLAIM_STATES, cid)
        pages(c['pages'], cid)
        if not c['pages']:
            raise ValueError(f'{cid}: at least one page is required')
        if c['relation'] in {'precedes', 'adjacent', 'incompatible'} and len(c['pages']) != 2:
            raise ValueError(f'{cid}: relation requires two distinct pages')
        for field in ('statement', 'falsifier', 'next_test'):
            text(c[field], f'{cid} {field}')
        strings(c['alternatives'], cid)
        strings(c['evidence'], cid)
        if not c['evidence']:
            raise ValueError(f'{cid}: evidence cannot be empty')
        for eid in c['evidence']:
            if eid not in evidence:
                raise ValueError(f'{cid}: missing evidence {eid}')
            if c['status'] in LIVE and evidence[eid]['status'] != 'active':
                raise ValueError(f'{cid}: withdrawn evidence {eid}')
        if not isinstance(c['dependencies'], dict):
            raise ValueError(f'{cid}: dependencies must map claim IDs to revisions')
        premises = {**claims, **research, **sources}
        for dep, rev in c['dependencies'].items():
            if dep not in premises:
                raise ValueError(f'{cid}: dangling dependency {dep}')
            revision(rev, f'{cid} dependency')
            if c['status'] in LIVE:
                if premises[dep]['revision'] != rev:
                    raise ValueError(f'{cid}: stale dependency {dep} revision {rev}')
                if dep in claims and claims[dep]['status'] not in LIVE:
                    raise ValueError(f'{cid}: dependency {dep} is {claims[dep]["status"]}')
                if c['status'] in {'supported', 'strongly_constrained'}:
                    if dep in research and research[dep]['status'] != 'verified':
                        raise ValueError(f'{cid}: supported claim depends on unverified research {dep}')
                    if dep in claims and claims[dep]['status'] == 'tentative':
                        raise ValueError(f'{cid}: supported claim depends on tentative claim {dep}')
    acyclic({cid: [dep for dep in c['dependencies'] if dep in claims] for cid, c in claims.items()}, 'claim dependencies')
    for rid, r in research.items():
        keys(r, {'id', 'revision', 'pages', 'question', 'status', 'result', 'sources', 'searched', 'next_step'}, rid)
        revision(r['revision'], rid)
        pages(r['pages'], rid)
        if not r['pages']:
            raise ValueError(f'{rid}: pages required')
        choice(r['status'], RESEARCH_STATES, rid)
        text(r['question'], rid)
        text(r['result'], rid, empty=r['status'] in {'open', 'in_progress'})
        text(r['next_step'], rid, empty=r['status'] == 'verified')
        strings(r['searched'], rid)
        if r['status'] == 'no_match' and not r['searched']:
            raise ValueError(f'{rid}: no_match requires searched sources/variants')
        if not isinstance(r['sources'], list):
            raise ValueError(f'{rid}: sources must be a list')
        for citation in r['sources']:
            keys(citation, {'id', 'revision', 'location', 'match_type', 'verification', 'supports'}, rid)
            revision(citation['revision'], f'{rid} citation')
            if citation['id'] not in sources:
                raise ValueError(f'{rid}: unknown source {citation["id"]}')
            if r['status'] == 'verified' and citation['revision'] != sources[citation['id']]['revision']:
                raise ValueError(f'{rid}: stale source citation {citation["id"]} revision {citation["revision"]}')
            for field in ('location', 'supports'):
                text(citation[field], rid)
            choice(citation['match_type'], {'exact', 'variant', 'context'}, rid)
            choice(citation['verification'], {'passage_read', 'snippet_only'}, rid)
        if r['status'] == 'verified' and (not r['sources'] or
                any(c['verification'] != 'passage_read' for c in r['sources'])):
            raise ValueError(f'{rid}: verified identification requires passage_read citations')
    for tid, t in tests.items():
        keys(t, {'id', 'claim', 'claim_revision', 'prediction', 'procedure', 'evidence', 'outcome'}, tid)
        if t['claim'] not in claims:
            raise ValueError(f'{tid}: unknown claim {t["claim"]}')
        revision(t['claim_revision'], tid)
        if t['claim_revision'] > claims[t['claim']]['revision']:
            raise ValueError(f'{tid}: test revision exceeds current claim revision')
        for field in ('prediction', 'procedure'):
            text(t[field], tid)
        strings(t['evidence'], tid)
        if any(e not in evidence for e in t['evidence']):
            raise ValueError(f'{tid}: missing test evidence')
        choice(t['outcome'], {'supported', 'contradicted', 'inconclusive'}, tid)
    for eid, event in events.items():
        keys(event, {'id', 'death_claim', 'intent_claim', 'victim_claim', 'perpetrator_claim',
                     'victim', 'murderer', 'status'}, eid)
        choice(event['status'], {'active', 'rejected', 'unresolved'}, eid)
        for field, relation in [('death_claim', 'death'), ('intent_claim', 'intentional_killing'),
                                ('victim_claim', 'victim_identity'), ('perpetrator_claim', 'perpetrator_identity')]:
            cid = event[field]
            text(cid, eid, empty=event['status'] == 'unresolved')
            if cid and (cid not in claims or claims[cid]['relation'] != relation):
                raise ValueError(f'{eid}: {field} must reference a {relation} claim')
        for field in ('victim', 'murderer'):
            text(event[field], eid, empty=event['status'] == 'unresolved')
            if event[field] and not re.fullmatch(r'P\d{3,}', event[field]):
                raise ValueError(f'{eid}: {field} must be a stable P ID')
    coverage = json_file(root / 'State/coverage.json')
    keys(coverage, {'read_pages'}, 'coverage')
    pages(coverage['read_pages'], 'coverage')
    order = json_file(root / 'State/order.json')
    keys(order, {'pages', 'complete', 'accepted_claims'}, 'order')
    pages(order['pages'], 'order')
    if type(order['complete']) is not bool:
        raise ValueError('order complete must be boolean')
    if order['complete'] and set(order['pages']) != set(range(1, 101)):
        raise ValueError('complete order must contain all 100 pages exactly once')
    strings(order['accepted_claims'], 'accepted claims')
    if len(set(order['accepted_claims'])) != len(order['accepted_claims']):
        raise ValueError('duplicate accepted claim')
    positions = {p: i for i, p in enumerate(order['pages'])}
    graph, next_page, prev_page = {}, {}, {}
    for cid in order['accepted_claims']:
        if cid not in claims or claims[cid]['status'] not in {'supported', 'strongly_constrained'}:
            raise ValueError(f'accepted claim {cid} must be supported or strongly_constrained')
        c = claims[cid]
        if c['relation'] not in {'precedes', 'adjacent'}:
            continue
        a, b = c['pages']
        graph.setdefault(a, set()).add(b)
        if a in positions and b in positions:
            gap = positions[b] - positions[a]
            if gap <= 0 or (c['relation'] == 'adjacent' and gap != 1):
                raise ValueError(f'{cid}: order violates {c["relation"]} constraint')
        if c['relation'] == 'adjacent':
            if a in next_page and next_page[a] != b or b in prev_page and prev_page[b] != a:
                raise ValueError(f'{cid}: conflicting adjacent constraints')
            next_page[a], prev_page[b] = b, a
    acyclic(graph, 'accepted precedence constraints')
    readiness = json_file(root / 'State/readiness.json')
    keys(readiness, {'ready', 'reviewer', 'summary', 'unresolved_structural'}, 'readiness')
    if type(readiness['ready']) is not bool:
        raise ValueError('readiness ready must be boolean')
    text(readiness['reviewer'], 'reviewer', empty=not readiness['ready'])
    text(readiness['summary'], 'review summary', empty=not readiness['ready'])
    strings(readiness['unresolved_structural'], 'structural uncertainties')
    if final:
        if not order['complete'] or len(coverage['read_pages']) != 100 or not readiness['ready'] or readiness['unresolved_structural']:
            raise ValueError('final gate requires full coverage, complete order and explicit structural review')
        for cid, c in claims.items():
            if c['status'] in {'supported', 'strongly_constrained'} and c['relation'] in {'precedes', 'adjacent'} and cid not in order['accepted_claims']:
                raise ValueError(f'final order omitted supported ordering constraint {cid}')
        uniquely_constrained(graph, order['pages'], next_page, prev_page)
        active = [e for e in events.values() if e['status'] == 'active']
        if len(active) != 6 or any(len({e[f] for e in active}) != 6 for f in ('death_claim', 'victim', 'murderer')):
            raise ValueError('final gate requires six distinct active deaths, victim IDs and murderer IDs')
        for e in active:
            for field in ('death_claim', 'intent_claim', 'victim_claim', 'perpetrator_claim'):
                if claims[e[field]]['status'] != 'strongly_constrained':
                    raise ValueError('final event claims must be strongly_constrained')
        final_claims = set(order['accepted_claims']) | {e[f] for e in active for f in
                        ('death_claim', 'intent_claim', 'victim_claim', 'perpetrator_claim')}
        for cid in final_claims:
            current_tests = [t for t in tests.values() if t['claim'] == cid and t['claim_revision'] == claims[cid]['revision']]
            qualified = [t for t in current_tests if t['evidence'] and
                         all(evidence[e]['status'] == 'active' for e in t['evidence'])]
            if not any(t['outcome'] == 'supported' for t in qualified) or any(t['outcome'] == 'contradicted' for t in current_tests):
                raise ValueError(f'final claim {cid} needs a current discriminating test without unresolved contradiction')
        integrity = subprocess.run([sys.executable, str(Path(__file__).with_name('verify_pages.py')),
                    '--pages-dir', str(root / 'Pages'), '--archive', str(root / 'Archive' / "Cain's Jawbone Unformatted.txt"),
                    '--hash-file', str(root / 'Archive/hash.txt')], capture_output=True, text=True)
        if integrity.returncode:
            raise ValueError(f'final integrity check failed: {integrity.stderr.strip()}')
    return dict(evidence=len(evidence), claims=len(claims), research=len(research), tests=len(tests), events=len(events))


def legacy(root):
    rows = worklog(root / 'Worklog/worklog.csv', legacy=True)
    count = 0
    for folder in ('Pages', 'Indexes', 'Order'):
        for path in (root / folder).glob('*.md'):
            content = path.read_text(encoding='utf-8')
            for page in re.findall(r'Pages/cains_jawbone_page_(\d+)\.md', content):
                if not (root / 'Pages' / f'cains_jawbone_page_{page}.md').is_file():
                    raise ValueError(f'{path}: invalid page reference {page}')
            # Historical ID examples precede the explicit Entries/Events section.
            section = re.split(r'(?m)^## (?:Entries|Events)\s*$', content, maxsplit=1)
            ids = re.findall(r'^- `(P\d+|N\d+|E\d+)`', section[1], re.M) if len(section) == 2 else []
            if len(ids) != len(set(ids)):
                raise ValueError(f'{path}: duplicate entry IDs')
            count += 1
    return {'legacy_files': count, 'historical_missing_commit_rows': [i for i, r in enumerate(rows[1:], 2) if not r[8]]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--legacy', action='store_true', help='Check historical Markdown references/IDs and worklog only')
    parser.add_argument('--final', action='store_true', help='Require complete structured order, event and review metadata')
    args = parser.parse_args()
    try:
        if args.legacy and args.final:
            raise ValueError('--final requires structured State records, not --legacy')
        counts = legacy(args.root) if args.legacy else validate(args.root, args.final)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f'INVALID: {exc}', file=sys.stderr)
        return 1
    print(f'OK: {counts}; structure/explicit constraints only, not literary correctness.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
