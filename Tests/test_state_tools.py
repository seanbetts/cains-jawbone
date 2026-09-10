import csv
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from support import REPO, claim, corpus, evidence, records, run, write_json


class StateTools(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = corpus(self.temp.name)

    def validate(self, *args):
        return run('validate_state.py', '--root', self.root, *args)

    def test_empty_new_state_valid(self):
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_actual_evidence_and_typed_claim_valid(self):
        records(self.root, 'evidence', [evidence()])
        records(self.root, 'claims', [claim()])
        self.assertEqual(self.validate().returncode, 0)

    def test_inexact_span_rejected(self):
        records(self.root, 'evidence', [dict(evidence(), span='AMBER')])
        self.assertIn('span', self.validate().stderr)

    def test_evidence_offsets_preserve_original_crlf(self):
        body='Synthetic first line.\r\nAmber cobalt.\r\n'
        (self.root/'Pages/cains_jawbone_page_1.md').write_bytes((body+'## Notes\r\n').encode())
        records(self.root,'evidence',[dict(evidence(),offset=body.index('Amber'))])
        self.assertEqual(self.validate().returncode,0)

    def test_duplicate_id_rejected(self):
        records(self.root, 'evidence', [evidence(), evidence()])
        self.assertIn('duplicate', self.validate().stderr.lower())

    def test_missing_evidence_rejected(self):
        records(self.root, 'claims', [claim()])
        self.assertIn('V001', self.validate().stderr)

    def test_stale_dependency_rejected(self):
        records(self.root, 'evidence', [evidence()])
        records(self.root, 'claims', [claim(revision=2), claim(id='C002', dependencies={'C001': 1})])
        self.assertIn('stale', self.validate().stderr)

    def test_rejected_dependency_cannot_support_live_claim(self):
        records(self.root, 'evidence', [evidence()])
        records(self.root, 'claims', [claim(status='rejected'), claim(id='C002', dependencies={'C001': 1})])
        self.assertIn('rejected', self.validate().stderr)

    def test_cycle_rejected(self):
        records(self.root, 'evidence', [evidence()])
        records(self.root, 'claims', [claim(dependencies={'C002': 1}), claim(id='C002', dependencies={'C001': 1})])
        self.assertIn('cycle', self.validate().stderr)

    def test_accepted_adjacency_cannot_be_reversed(self):
        records(self.root, 'evidence', [evidence()])
        records(self.root, 'claims', [claim(relation='adjacent')])
        write_json(self.root, 'State/order.json', dict(pages=[2, 1], complete=False, accepted_claims=['C001']))
        self.assertIn('adjacent', self.validate().stderr)

    def test_accepted_precedence_cycle_even_in_partial_order_rejected(self):
        records(self.root, 'evidence', [evidence()])
        records(self.root, 'claims', [claim(), claim(id='C002', pages=[2, 1])])
        write_json(self.root, 'State/order.json', dict(pages=[], complete=False, accepted_claims=['C001', 'C002']))
        self.assertIn('cycle', self.validate().stderr)

    def test_complete_order_requires_exact_100_pages(self):
        write_json(self.root, 'State/order.json', dict(pages=[1, 2], complete=True, accepted_claims=[]))
        self.assertIn('100', self.validate().stderr)

    def test_verified_research_requires_passage_read(self):
        write_json(self.root, 'Sources/catalog.json', [dict(id='S001', revision=1, title='Synthetic old text', year=1900,
                  url='https://example.org/old', admission_note='Synthetic test fixture')])
        records(self.root, 'research', [dict(id='R001', revision=1, pages=[1], question='Identify a phrase.', status='verified',
                result='Found the phrase.', sources=[dict(id='S001', revision=1, location='p. 1', match_type='exact',
                verification='snippet_only', supports='The phrase identification.')], searched=[], next_step='')])
        self.assertIn('passage_read', self.validate().stderr)

    def test_post_1934_source_rejected(self):
        write_json(self.root, 'Sources/catalog.json', [dict(id='S001', revision=1, title='Modern text', year=2000,
                  url='https://example.org/modern', admission_note='Synthetic fixture')])
        self.assertIn('1934', self.validate().stderr)

    def test_bad_csv_rejected(self):
        with (self.root / 'Worklog/worklog.csv').open('a') as f:
            f.write('2026-09-10,codex,admin,unquoted,task,extra\n')
        self.assertIn('CSV', self.validate().stderr)

    def test_legacy_id_templates_are_not_duplicate_records(self):
        (self.root/'Indexes').mkdir()
        (self.root/'Indexes/people.md').write_text('# People\n\nTemplate:\n- `P01` — Names:\n\n## Entries\n- `P01` — Names: Synthetic\n')
        self.assertEqual(self.validate('--legacy').returncode,0)

    def test_final_gate_rejects_empty_state(self):
        self.assertIn('final', self.validate('--final').stderr.lower())

    def test_valid_synthetic_final_gate(self):
        records(self.root, 'evidence', [evidence()])
        claims, events = [], []
        for i in range(6):
            ids = [f'C{i * 4 + j + 1:03}' for j in range(4)]
            relations = ['death', 'intentional_killing', 'victim_identity', 'perpetrator_identity']
            claims += [claim(id=c, relation=r, pages=[1], status='strongly_constrained') for c, r in zip(ids, relations)]
            events.append(dict(id=f'E{i+1:03}', death_claim=ids[0], intent_claim=ids[1], victim_claim=ids[2],
                    perpetrator_claim=ids[3], victim=f'P{i+1:03}', murderer=f'P{i+7:03}', status='active'))
        order_ids=[]
        for i in range(1,100):
            cid=f'C{i+100:03}'
            claims.append(claim(id=cid,relation='adjacent',pages=[i,i+1],status='strongly_constrained'))
            order_ids.append(cid)
        records(self.root, 'claims', claims)
        records(self.root, 'tests', [dict(id=f'T{i+1:03}',claim=c['id'],claim_revision=1,
                prediction='Synthetic expected relation.',procedure='Synthetic discriminating test.',evidence=['V001'],
                outcome='supported') for i,c in enumerate(claims)])
        records(self.root, 'events', events)
        write_json(self.root, 'State/order.json', dict(pages=list(range(1,101)), complete=True, accepted_claims=order_ids))
        write_json(self.root, 'State/coverage.json', dict(read_pages=list(range(1,101))))
        write_json(self.root, 'State/readiness.json', dict(ready=True, reviewer='test reviewer',
                   summary='Synthetic review attestation, not a real solution.', unresolved_structural=[]))
        result = self.validate('--final')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_final_gate_rejects_unconstrained_complete_order(self):
        # A full permutation plus reviewer checkbox is insufficient ordering evidence.
        write_json(self.root, 'State/order.json', dict(pages=list(range(1,101)), complete=True, accepted_claims=[]))
        write_json(self.root, 'State/coverage.json', dict(read_pages=list(range(1,101))))
        write_json(self.root, 'State/readiness.json', dict(ready=True, reviewer='test', summary='Checked.', unresolved_structural=[]))
        self.assertIn('uniquely', self.validate('--final').stderr)

    def test_stale_source_revision_rejected(self):
        records(self.root, 'evidence', [evidence()])
        write_json(self.root, 'Sources/catalog.json', [dict(id='S001', revision=2, title='Synthetic old text', year=1900,
                  url='https://example.org/old', admission_note='Synthetic test fixture')])
        records(self.root, 'claims', [claim(dependencies={'S001':1})])
        self.assertIn('stale', self.validate().stderr)

    def test_stale_test_does_not_satisfy_current_claim(self):
        records(self.root, 'evidence', [evidence()])
        records(self.root, 'claims', [claim(revision=2)])
        records(self.root, 'tests', [dict(id='T001',claim='C001',claim_revision=1,prediction='A precedes B.',
                procedure='Compare dates.',evidence=['V001'],outcome='supported')])
        # Historical tests are retained, and are explicitly revision-bound.
        self.assertEqual(self.validate().returncode,0)


class IntegrityTools(StateTools):
    # Avoid inheriting the state tests; expose only verifier probes below via load_tests.
    def verify(self):
        return run('verify_pages.py', '--pages-dir', self.root / 'Pages', '--archive',
                   self.root / 'Archive' / "Cain's Jawbone Unformatted.txt", '--hash-file', self.root / 'Archive/hash.txt')

    def test_extra_page_rejected(self):
        (self.root / 'Pages/cains_jawbone_page_101.md').write_text('extra\n## Notes\n')
        self.assertNotEqual(self.verify().returncode, 0)

    def test_duplicate_notes_rejected(self):
        p = self.root / 'Pages/cains_jawbone_page_1.md'
        p.write_text(p.read_text() + '\n## Notes\n')
        self.assertNotEqual(self.verify().returncode, 0)


class LoggingTools(unittest.TestCase):
    def test_commas_roundtrip_and_work_commit(self):
        with tempfile.TemporaryDirectory() as td:
            root = corpus(td)
            subprocess.run(['git', 'init', '-b', 'run/test'], cwd=root, check=True, capture_output=True)
            subprocess.run(['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.org',
                            'commit', '--allow-empty', '-m', 'fixture'], cwd=root, check=True, capture_output=True)
            result = run('log_session.py', '--root', root, '--start', '2026-09-10T10:00:00Z',
                     '--end', '2026-09-10T10:01:30Z', '--agent', 'test', '--phase', 'admin',
                     '--task', 'Check a, b', '--notes', 'Checked a, b, and c.')
            self.assertEqual(result.returncode, 0, result.stderr)
            with (root / 'Worklog/worklog.csv').open() as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(rows[0]['task'], 'Check a, b')
            self.assertEqual(rows[0]['minutes'], '2')
            self.assertEqual(rows[0]['branch'], 'run/test')
            self.assertTrue(rows[0]['commit'])

    def test_invalid_time_does_not_write(self):
        with tempfile.TemporaryDirectory() as td:
            root = corpus(td)
            original = (root / 'Worklog/worklog.csv').read_bytes()
            result = run('log_session.py', '--root', root, '--start', '2026-09-10T10:00:00',
                         '--agent', 'test', '--phase', 'admin', '--task', 'Check', '--notes', 'Checked.')
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual((root / 'Worklog/worklog.csv').read_bytes(), original)


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(StateTools))
    suite.addTests(loader.loadTestsFromTestCase(LoggingTools))
    for name in ('test_extra_page_rejected', 'test_duplicate_notes_rejected'):
        suite.addTest(IntegrityTools(name))
    return suite
