import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from support import REPO, corpus, run


class FreshExport(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base=Path(self.temp.name)
        self.source=corpus(base/'source')
        self.dest=base/'fresh'
        for folder in ('Scripts','Skills','Templates','Tests'):
            shutil.copytree(REPO/folder,self.source/folder,ignore=shutil.ignore_patterns('__pycache__'))
        for name in ('AGENTS.md','README.md','.gitignore'):
            shutil.copy2(REPO/name,self.source/name)
        (self.source/'Indexes').mkdir()
        (self.source/'Indexes/people.md').write_text('OLD SOLVING DATA')
        (self.source/'State/claims.jsonl').write_text('OLD SOLVING DATA')
        (self.source/'FINAL_SOLUTION.md').write_text('OLD SOLVING DATA')
        (self.source/'Reviews').mkdir()
        (self.source/'Reviews/audit.md').write_text('OLD SOLVING DATA')
        p=self.source/'Pages/cains_jawbone_page_1.md'
        p.write_text(p.read_text()+'OLD SOLVING DATA\n')

    def export(self):
        return run('prepare_fresh_run.py','--source',self.source,'--destination',self.dest)

    def test_no_old_progress_in_export_and_manifest_readback(self):
        result=self.export()
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertFalse((self.dest/'.git').exists())
        self.assertFalse((self.dest/'Reviews').exists())
        self.assertEqual((self.dest/'State/claims.jsonl').read_text(),'')
        self.assertEqual((self.dest/'Worklog/current_run.txt').read_text(),'')
        self.assertNotIn('OLD SOLVING DATA',(self.dest/'Pages/cains_jawbone_page_1.md').read_text())
        self.assertNotIn('OLD SOLVING DATA',(self.dest/'Indexes/people.md').read_text())
        self.assertNotIn('OLD SOLVING DATA',(self.dest/'FINAL_SOLUTION.md').read_text())
        manifest=json.loads((self.dest/'BASELINE_MANIFEST.json').read_text())
        self.assertIn('Archive/hash.txt',manifest['files'])
        check=run('prepare_fresh_run.py','--verify',self.dest)
        self.assertEqual(check.returncode,0,check.stderr)

    def test_existing_destination_not_changed(self):
        self.dest.mkdir()
        (self.dest/'sentinel').write_text('keep')
        self.assertNotEqual(self.export().returncode,0)
        self.assertEqual((self.dest/'sentinel').read_text(),'keep')

    def test_export_rejects_symlink_in_allowed_tree(self):
        (self.source/'Skills/unsafe.md').symlink_to(self.source/'Indexes/people.md')
        self.assertNotEqual(self.export().returncode,0)
        self.assertFalse(self.dest.exists())

    def test_manifest_detects_edit(self):
        result=self.export()
        self.assertEqual(result.returncode,0,result.stderr)
        p=self.dest/'Pages/cains_jawbone_page_1.md'
        p.write_text(p.read_text()+'unexpected note\n')
        self.assertNotEqual(run('prepare_fresh_run.py','--verify',self.dest).returncode,0)

    def test_export_rejects_mutated_source_archive(self):
        p=self.source/'Archive'/"Cain's Jawbone Unformatted.txt"
        p.write_text(p.read_text()+'mutation')
        self.assertNotEqual(self.export().returncode,0)
        self.assertFalse(self.dest.exists())
