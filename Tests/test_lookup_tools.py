"""Regression tests for retrieval and disposition reports, using synthetic text only."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LookupToolsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.pages = self.root / 'Pages'
        self.pages.mkdir()

    def run_tool(self, tool, *args):
        return subprocess.run([sys.executable, str(ROOT / 'Scripts' / tool), *map(str, args)], capture_output=True, text=True)

    def page(self, number, body):
        (self.pages / f'cains_jawbone_page_{number}.md').write_text(body + '\n\n## Notes\nsecret note only\n', encoding='utf-8')

    def scan(self, *args):
        return self.run_tool('scan_df2_boundaries.py', '--pages-dir', self.pages, '--json', *args)

    def test_one_shared_phrase_is_one_match_without_draft(self):
        self.page(1, 'before amber cobalt ivory')
        self.page(2, 'amber cobalt ivory afterwards')
        result = self.scan('--pair', 1, 2, '--edge-tokens', 3)
        self.assertEqual(result.returncode, 0, result.stderr)
        pair = json.loads(result.stdout)['pairs'][0]
        self.assertEqual(len(pair['matches']), 1)
        match = pair['matches'][0]
        self.assertEqual(match['normalized'], 'amber cobalt ivory')
        self.assertEqual(match['a']['text'], 'amber cobalt ivory')
        self.assertEqual(match['a']['start'], 7)
        self.assertEqual(match['a']['end'], 25)
        self.assertTrue(match['a']['at_end'])
        self.assertFalse(match['a']['at_start'])
        self.assertTrue(match['b']['at_start'])
        reverse = json.loads(self.scan('--pair', 2, 1).stdout)['pairs'][0]['matches']
        self.assertEqual([m['normalized'] for m in reverse], ['amber cobalt ivory'])

    def test_overlapping_repeated_words_do_not_inflate_a_single_phrase(self):
        self.page(1, 'before amber amber amber')
        self.page(2, 'amber amber amber afterwards')
        result = self.scan('--pair', 1, 2, '--min-words', 1)
        self.assertEqual(result.returncode, 0, result.stderr)
        matches = json.loads(result.stdout)['pairs'][0]['matches']
        self.assertEqual([m['normalized'] for m in matches], ['amber amber amber'])

    def test_unicode_query_preserves_original_offsets_and_ignores_notes(self):
        body = 'Here Café’s blue and cafe\u0301\'s BLUE.'
        self.page(1, body)
        result = self.scan('--query', "CAFÉ'S blue")
        self.assertEqual(result.returncode, 0, result.stderr)
        hits = json.loads(result.stdout)['queries'][0]['matches']
        self.assertEqual(len(hits), 2)
        self.assertEqual([hit['text'] for hit in hits], ['Café’s blue', "cafe\u0301's BLUE"])
        for hit in hits:
            self.assertEqual(body[hit['start']:hit['end']], hit['text'])
            self.assertIn(hit['text'], hit['context'])
        self.assertEqual(json.loads(self.scan('--query', 'secret note').stdout)['queries'][0]['matches'], [])

    def test_scanner_bad_input_is_friendly(self):
        self.page(1, 'one two')
        for args in [('--pair', 0, 1), ('--pair', 1, 101), ('--query', '   '), ('--query', '!!!'), ('--pair', 1, 2)]:
            with self.subTest(args=args):
                result = self.scan(*args)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn('Traceback', result.stderr)
        (self.pages / 'cains_jawbone_page_1.md').write_text('missing notes')
        result = self.scan('--query', 'missing')
        self.assertEqual(result.returncode, 2)
        self.assertIn('Notes', result.stderr)

    def state(self, research, claims=None, coverage=None):
        state = self.root / 'State'
        state.mkdir(exist_ok=True)
        for name, values in [('research', research), ('claims', claims or [])]:
            (state / (name + '.jsonl')).write_text(''.join(json.dumps(x) + '\n' for x in values))
        (state / 'coverage.json').write_text(json.dumps(coverage or {'read_pages': [1, 3]}))

    def progress(self, *args):
        return self.run_tool('calculate_research_progress.py', '--root', self.root, '--json', *args)

    def test_structured_dispositions_are_separate_from_coverage_and_claims(self):
        self.state([{'id': 'R001', 'status': 'no_match'}, {'id': 'R002', 'status': 'partial'}, {'id': 'R003', 'status': 'verified'}], [{'id': 'C001', 'status': 'tentative'}, {'id': 'C002', 'status': 'supported'}])
        result = self.progress()
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data['coverage']['read_count'], 2)
        self.assertEqual(data['research']['statuses']['no_match'], 1)
        self.assertEqual(data['research']['statuses']['verified'], 1)
        self.assertEqual(data['claims']['statuses']['tentative'], 1)
        self.assertNotIn('overall', data)
        self.assertNotIn('percent', result.stdout)

    def test_bad_state_is_not_silently_counted(self):
        for research in [[{'id': 'R1'}], [{'id': 'R1', 'status': 'resolved'}], [{'id': 'R1', 'status': 'open'}, {'id': 'R1', 'status': 'open'}]]:
            with self.subTest(research=research):
                self.state(research)
                result = self.progress()
                self.assertEqual(result.returncode, 2)
                self.assertNotIn('Traceback', result.stderr)
        self.state([], coverage={'read_pages': [True, 3]})
        self.assertEqual(self.progress().returncode, 2)

    def legacy(self, status='`resolved`', extra=''):
        indexes = self.root / 'Indexes'
        indexes.mkdir(exist_ok=True)
        (indexes / 'research_queue.md').write_text('''# Research queue
Template:
- **Item:**
  - **Status:** `open` / `resolved`
## Open items
- **Item:** Identify synthetic phrase
  - **Type:** quote
  - **Pages:** Pages/cains_jawbone_page_1.md
  - **Why it matters:** Distinguish source
  - **Status:** ''' + status + '''
  - **Result:** Candidate only
''' + extra)

    def test_legacy_template_is_excluded_and_resolved_remains_a_label(self):
        self.legacy()
        result = self.progress('--legacy')
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data['legacy_research']['total'], 1)
        self.assertEqual(data['legacy_research']['statuses']['resolved'], 1)
        self.assertNotIn('verified', data['legacy_research']['statuses'])

    def test_legacy_rejects_unknown_duplicate_missing_or_ambiguous_fields(self):
        for status, extra in [('`unknown`', ''), ('`open` / `resolved`', ''), ('`open`', '  - **Status:** `open`\n'), ('`open`', '  - **Mystery:** nope\n')]:
            with self.subTest(status=status, extra=extra):
                self.legacy(status, extra)
                self.assertEqual(self.progress('--legacy').returncode, 2)
        path = self.root / 'Indexes' / 'research_queue.md'
        self.legacy()
        path.write_text(path.read_text().replace('  - **Type:** quote\n', ''))
        self.assertEqual(self.progress('--legacy').returncode, 2)


if __name__ == '__main__':
    unittest.main()
