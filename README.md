# Cain’s Jawbone — Notes & Ordering Workspace

This repository is a working notebook for solving **Cain’s Jawbone** by annotating each page, building global indices of clues, clustering pages by voice/motifs, and iteratively proposing (and falsifying) ordering hypotheses.

This is not a software project; the “code” here exists only to protect text integrity and support lightweight analysis.

## Folder layout

- `Pages/` — `cains_jawbone_page_1.md` … `cains_jawbone_page_100.md` (page text + `## Notes`)
- `Archive/` — immutable source text + hash (`Cain's Jawbone Unformatted.txt`, `hash.txt`)
- `Indexes/` — global indices (`people.md`, `places.md`, `quotes.md`, `objects_motifs.md`, `research_queue.md`)
- `Order/` — ordering hypotheses and clusters (`hypotheses.md`)
- `Skills/` — modular workflows (authoritative procedures in each `SKILL.md`)
- `verify_pages.py` — integrity verifier (archive hash + page-body immutability)
- `Worklog/worklog.csv` — mandatory session log (see `Skills/cjb-time-logging/SKILL.md`)
- `Worklog/current_run.txt` — active run metadata (empty means no active run)

## Golden rules

- Never edit the page body text in `Pages/*.md` (only write under `## Notes`).
- Never modify anything in `Archive/`.
- Run `python3 verify_pages.py` after edits and before commits.
- Log session start/end (UTC) and append to `Worklog/worklog.csv` per the time-logging skill.
- Don’t brute-force ordering (100! is not a strategy).

## Working loop

1. Extract clues from a page into `## Notes`.
2. Update the relevant `Indexes/*` entries.
3. If proposing a linkage/sequence, record it (plus a falsifier) in `Order/hypotheses.md`.

## Skills (how we work)

The authoritative procedures/templates live in these files:

- `Skills/cjb-page-extraction/SKILL.md`
- `Skills/cjb-index-maintenance/SKILL.md`
- `Skills/cjb-order-hypotheses/SKILL.md`
- `Skills/cjb-quote-research/SKILL.md`
- `Skills/cjb-verification/SKILL.md`
- `Skills/cjb-time-logging/SKILL.md`
- `Skills/cjb-run-management/SKILL.md`

## Integrity checking

Run:

- `python3 verify_pages.py`

What “OK” means:

- `Archive/Cain's Jawbone Unformatted.txt` matches `Archive/hash.txt`
- Page body text (above `## Notes`) in `Pages/*.md` matches the archive

It does **not** judge whether notes/hypotheses are correct.

## Git workflow

- Commit small, single-purpose changes (avoid mega-commits).
- Use branches for competing ordering approaches.
- Tag major milestones (e.g. `milestone-first-clustering-pass`).
- If a hypothesis collapses, prefer `git revert` over rewriting history.

## Agent runs & branching

- Each AI session runs on its own branch: `run/YYYYMMDD-<agent>-<focus>`.
- The active run metadata lives in `Worklog/current_run.txt`; leave it empty to signal no active run.
- During a run:
  - Stay on the recorded branch (no merging other branches in).
  - Log start/end times via the time-logging skill.
  - Commit frequently; final commit should be `Run summary: ...`.
- After a run:
  - Run `python3 verify_pages.py`, update `Worklog/worklog.csv`, merge to `main` only if the work is accepted, and clear `Worklog/current_run.txt`.

## Spoilers policy

- Do not import solved page orders, murderer/victim lists, or solution summaries.
- Research is allowed only for quotation/place/reference resolution; record results in the indices.
