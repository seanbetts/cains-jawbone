"""Independent review regressions; all fixtures are synthetic and temporary."""
import json
from pathlib import Path
import tempfile
import unittest

from support import claim, corpus, evidence, records, run, write_json
from test_fresh_export import FreshExport
from test_state_tools import StateTools


class ReviewRegressions(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = corpus(self.temp.name)

    def validate(self, *args):
        return run('validate_state.py', '--root', self.root, *args)

    def final_fixture(self):
        # Reuse the complete synthetic scenario, not production solving state.
        fixture = StateTools()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        fixture.test_valid_synthetic_final_gate()
        self.root = fixture.root

    def read_records(self, name):
        return [json.loads(line) for line in (self.root / 'State' / f'{name}.jsonl').read_text().splitlines() if line.strip()]

    def test_revised_source_invalidates_verified_research_citation(self):
        source = dict(id='S001', revision=1, title='Synthetic edition', year=1900,
                      url='https://example.org/text', admission_note='Synthetic metadata fixture')
        write_json(self.root, 'Sources/catalog.json', [source])
        records(self.root, 'research', [dict(id='R001', revision=1, pages=[1], question='Identify phrase',
                    status='verified', result='The phrase occurs in the cited passage.',
                    sources=[dict(id='S001', revision=1, location='p. 1', match_type='exact',
                                  verification='passage_read', supports='Phrase identification')],
                    searched=[], next_step='')])
        # Revision-pinned current citations must first be accepted.
        current = self.validate()
        self.assertEqual(current.returncode, 0, current.stderr)
        write_json(self.root, 'Sources/catalog.json', [dict(source, revision=2, title='Corrected edition')])
        changed = self.validate()
        self.assertNotEqual(changed.returncode, 0, changed.stdout)
        self.assertIn('revision', changed.stderr.lower())

    def test_final_uniqueness_respects_forced_adjacency(self):
        self.final_fixture()
        claims = self.read_records('claims')
        # 1 must immediately precede 2; 1 precedes 3; 3..100 form a chain.
        # Only 1,2,3,...,100 satisfies both precedence and adjacency.
        for item in claims:
            if item['id'] == 'C102':
                item['relation'] = 'precedes'
                item['pages'] = [1, 3]
        records(self.root, 'claims', claims)
        result = self.validate('--final')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_final_cannot_omit_supported_contradictory_constraint(self):
        self.final_fixture()
        claims = self.read_records('claims')
        claims.append(claim(id='C999', relation='precedes', pages=[2, 1], status='supported'))
        records(self.root, 'claims', claims)
        result = self.validate('--final')
        self.assertNotEqual(result.returncode, 0, result.stdout)

    def test_final_test_support_cannot_use_withdrawn_evidence(self):
        self.final_fixture()
        records(self.root, 'evidence', [evidence(), dict(evidence(), id='V002', status='withdrawn')])
        records(self.root, 'tests', [dict(test, evidence=['V002']) for test in self.read_records('tests')])
        result = self.validate('--final')
        self.assertNotEqual(result.returncode, 0, result.stdout)

    def test_export_parent_symlink_cannot_route_inside_old_workspace(self):
        fixture = FreshExport()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        alias = fixture.source.parent / 'alias'
        alias.symlink_to(fixture.source, target_is_directory=True)
        fixture.dest = alias / 'fresh-inside-old'
        result = fixture.export()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertFalse((fixture.source / 'fresh-inside-old').exists())

    def test_worklog_elapsed_minutes_must_match_timestamps(self):
        with (self.root / 'Worklog/worklog.csv').open('a') as stream:
            stream.write('2026-09-10,test,admin,test,2026-09-10T10:00:00Z,2026-09-10T10:01:00Z,999,run/test,abc,test\n')
        result = self.validate()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('minute', result.stderr.lower())


def load_tests(loader, tests, pattern):
    # Imported fixture classes must not duplicate their suites in discovery.
    return loader.loadTestsFromTestCase(ReviewRegressions)


if __name__ == '__main__':
    unittest.main()
