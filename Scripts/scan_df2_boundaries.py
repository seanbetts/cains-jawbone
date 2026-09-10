#!/usr/bin/env python3
"""Directionless lexical concordance (historical filename retained).

No draft is read and no ordering is generated or scored. Match offsets are
zero-based Unicode character positions in the original Markdown body before
Notes; end offsets are exclusive. NFC, casefold and straight/curly apostrophe
normalization affect lookup only. Punctuation between words is ignored; inspect
exact spans and context before interpreting a result. Repeated occurrences are
locations, not independent evidence.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import unicodedata

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTES_RE = re.compile(r'(?m)^##[ \t]+Notes[ \t]*\r?$')
PAGE_RE = re.compile(r'cains_jawbone_page_([1-9][0-9]*)\.md')
APOSTROPHES = "'’‘ʼ"
LIMITATION = 'Lexical retrieval only: matches do not establish direction, adjacency, narrator identity or independent corroboration.'


@dataclass(frozen=True)
class Token:
    value: str
    start: int
    end: int


def tokens(text: str) -> list[Token]:
    """Tokenize the original text so normalization cannot move its offsets."""
    result = []
    i = 0
    while i < len(text):
        if not text[i].isalnum():
            i += 1
            continue
        start = i
        i += 1
        while i < len(text):
            char = text[i]
            if char.isalnum() or unicodedata.category(char).startswith('M'):
                i += 1
            elif char in APOSTROPHES and i + 1 < len(text) and text[i + 1].isalnum():
                i += 1
            else:
                break
        value = text[start:i].translate(str.maketrans({c: "'" for c in APOSTROPHES}))
        result.append(Token(unicodedata.normalize('NFC', value).casefold(), start, i))
    return result


def load_page(pages_dir: Path, number: int) -> tuple[str, list[Token]]:
    path = pages_dir / f'cains_jawbone_page_{number}.md'
    # Preserve original newlines as well as Unicode spelling for exact offsets.
    with path.open(encoding='utf-8', newline='') as stream:
        text = stream.read()
    headings = list(NOTES_RE.finditer(text))
    if len(headings) != 1:
        raise ValueError(f'{path.name}: expected exactly one ## Notes heading, found {len(headings)}')
    body = text[:headings[0].start()]
    return body, tokens(body)


def occurrence(number: int, body: str, words: list[Token], start: int, length: int, edge: int) -> dict:
    first, last = words[start].start, words[start + length - 1].end
    return {'page': number, 'start': first, 'end': last, 'text': body[first:last],
            'context': body[max(0, first - 60):min(len(body), last + 60)],
            'token_start': start, 'token_end': start + length,
            'at_start': start + length <= edge, 'at_end': start >= len(words) - edge}


def pair_matches(a: int, b: int, pages: dict, minimum: int, edge: int) -> list[dict]:
    body_a, words_a = pages[a]
    body_b, words_b = pages[b]
    matches = []
    # Maximal aligned runs: substrings of a longer match are not emitted again.
    # Comparing two supplied texts is retrieval, not a permutation search.
    for i, word_a in enumerate(words_a):
        for j, word_b in enumerate(words_b):
            if word_a.value != word_b.value:
                continue
            if i and j and words_a[i - 1].value == words_b[j - 1].value:
                continue
            length = 1
            while i + length < len(words_a) and j + length < len(words_b) and words_a[i + length].value == words_b[j + length].value:
                length += 1
            if length >= minimum:
                matches.append({'normalized': ' '.join(t.value for t in words_a[i:i + length]),
                                'a': occurrence(a, body_a, words_a, i, length, edge),
                                'b': occurrence(b, body_b, words_b, j, length, edge)})
    # A repeated word can form shifted runs inside the same longer occurrence
    # on both pages. Suppress these too; retain separate non-contained locations.
    return [match for match in matches if not any(
        other is not match
        and all(other[side]['start'] <= match[side]['start']
                and other[side]['end'] >= match[side]['end'] for side in ('a', 'b'))
        for other in matches
    )]


def query_matches(query: str, pages: dict, edge: int) -> list[dict]:
    needle = [t.value for t in tokens(query)]
    if not needle:
        raise ValueError('--query must contain at least one word')
    found = []
    for number, (body, words) in sorted(pages.items()):
        for i in range(len(words) - len(needle) + 1):
            if [t.value for t in words[i:i + len(needle)]] == needle:
                found.append(occurrence(number, body, words, i, len(needle), edge))
    return found


def page_id(raw: str) -> int:
    try:
        value = int(raw)
    except ValueError:
        raise argparse.ArgumentTypeError('page IDs must be integers in 1..100') from None
    if not 1 <= value <= 100:
        raise argparse.ArgumentTypeError('page IDs must be integers in 1..100')
    return value


def show_occurrence(hit: dict) -> None:
    position = '/'.join(label for label in ('start', 'end') if hit['at_' + label]) or 'interior'
    print(f"  p{hit['page']} chars {hit['start']}:{hit['end']} ({position}): {hit['text']!r}")
    print(f"    context: {hit['context']!r}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pages-dir', type=Path, default=REPO_ROOT / 'Pages')
    parser.add_argument('--pair', nargs=2, type=page_id, action='append', metavar=('A', 'B'), help='Compare two supplied pages, without implying an order; repeatable.')
    parser.add_argument('--query', action='append', help='Find a normalized word or phrase across available pages; repeatable.')
    parser.add_argument('--min-words', type=int, default=2, help='Minimum length of pair matches; use 1 to include single words.')
    parser.add_argument('--edge-tokens', type=int, default=20, help='Label spans wholly within this many tokens of start/end (default: 20).')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    try:
        if not args.pair and not args.query:
            raise ValueError('provide --pair A B and/or --query TEXT; draft scanning is no longer supported')
        if args.min_words < 1 or args.edge_tokens < 1:
            raise ValueError('--min-words and --edge-tokens must be positive')
        wanted = {p for pair in (args.pair or []) for p in pair}
        if args.query:
            for path in args.pages_dir.glob('cains_jawbone_page_*.md'):
                match = PAGE_RE.fullmatch(path.name)
                if not match or not 1 <= int(match[1]) <= 100:
                    raise ValueError(f'invalid page filename: {path.name}')
                wanted.add(int(match[1]))
        if not wanted:
            raise ValueError(f'no pages found in {args.pages_dir}')
        pages = {number: load_page(args.pages_dir, number) for number in sorted(wanted)}
        report = {'limitation': LIMITATION, 'normalization': 'NFC; Unicode casefold; curly apostrophes mapped to straight; inter-word punctuation ignored',
                  'offsets': 'original body, zero-based Unicode characters, end exclusive',
                  'edge_tokens': args.edge_tokens,
                  'pairs': [{'pages': [a, b], 'matches': pair_matches(a, b, pages, args.min_words, args.edge_tokens)} for a, b in (args.pair or [])],
                  'queries': [{'query': q, 'matches': query_matches(q, pages, args.edge_tokens)} for q in (args.query or [])]}
    except (OSError, ValueError) as error:
        parser.error(str(error))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(LIMITATION)
        print('Offsets: original body characters, zero-based, end exclusive. Edge labels are positions only.')
        for pair in report['pairs']:
            print(f"\nPages {pair['pages'][0]} and {pair['pages'][1]}: maximal whole-page lexical matches")
            if not pair['matches']:
                print('  No matches at the requested minimum length.')
            for match in pair['matches']:
                print(f"  Normalized: {match['normalized']!r}")
                show_occurrence(match['a'])
                show_occurrence(match['b'])
        for query in report['queries']:
            print(f"\nQuery {query['query']!r}")
            if not query['matches']:
                print('  No matches.')
            for hit in query['matches']:
                show_occurrence(hit)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
