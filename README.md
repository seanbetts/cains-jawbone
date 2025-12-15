# Cain’s Jawbone — Notes & Ordering Workspace

This repository is a working notebook for solving **Cain’s Jawbone** by annotating each page, building global indices of clues, clustering pages by voice/motifs, and iteratively proposing (and falsifying) ordering hypotheses.

This is not a software project; the “code” here exists only to protect text integrity and support lightweight analysis.

## Folder layout

- `Pages/` — `cains_jawbone_page_1.md` … `cains_jawbone_page_100.md` (page text + `## Notes`)
- `Archive/` — immutable source text + hash (`Cain's Jawbone Unformatted.txt`, `hash.txt`)
- `Indexes/` — global indices (`people.md`, `places.md`, `quotes.md`, `objects_motifs.md`, `research_queue.md`)
- `Order/` — ordering hypotheses and clusters (`hypotheses.md`), plus cast + murder-confidence ledgers (`cast.md`, `confidence.md`)
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

## Master plan

This project follows a phased approach. Phases should be completed in order.

**Phase 1: Page extraction**  
Read all 100 pages and extract signals without attempting to order them. Capture entities, quotations, objects, motifs, temporal hints, and uncertainties in `## Notes`, keeping global indices up to date. The goal is coverage, not understanding.

**Phase 2: External research resolution**  
Resolve shared or anchoring references (quotations, dates, places) that recur across pages or appear to structure time or movement. Research is bounded and conservative, aimed at collapsing ambiguity rather than explaining everything.

**Phase 3: Pattern detection and clustering**  
Identify recurring voices, characters, locations, tones, and motifs. Group pages into provisional narrative clusters without imposing internal order. Clusters are hypotheses and may overlap.

**Phase 4: Internal ordering within clusters**  
Propose page sequences within individual clusters using continuity cues (time, place, pronouns, quoted material). Test and refine these sequences, recording confidence and explicit falsifiers.

**Phase 5: Cross-cluster stitching**  
Connect ordered clusters into a single global sequence. Use shared characters, consequences, and deaths as linking constraints. At this stage, candidate murderers and victims begin to stabilise.

**Phase 6: Convergence and falsification**  
Stress-test the full ordering and murder list by actively seeking contradictions and alternative explanations. Resolve remaining inconsistencies until only local, non-structural uncertainty remains.

## Working loop

1. Extract clues from a page into `## Notes`.
2. Update the relevant `Indexes/*` entries.
3. If proposing a linkage/sequence, record it (plus a falsifier) in `Order/hypotheses.md`.

## Default sequencing (extraction-first)

The default approach is:

1. Do a complete extraction pass across **all 100 pages** (populate `## Notes` + keep indices current).
2. Only then start resolving `Indexes/research_queue.md` items (quotes, calendar clues, locations), since later pages often answer earlier uncertainties.

## Final output

The canonical solution is recorded in `FINAL_SOLUTION.md`.

This file contains:
1) The list of murdered persons and their murderers
2) The correct page order for all 100 pages

It contains no working or explanation.

## Skills (how we work)

The authoritative procedures/templates live in these files:

- `Skills/cjb-page-extraction/SKILL.md`
- `Skills/cjb-index-maintenance/SKILL.md`
- `Skills/cjb-order-hypotheses/SKILL.md`
- `Skills/cjb-murder-analysis/SKILL.md`
- `Skills/cjb-means-and-methods/SKILL.md`
- `Skills/cjb-motive-and-relationships/SKILL.md`
- `Skills/cjb-quote-research/SKILL.md`
- `Skills/cjb-verification/SKILL.md`
- `Skills/cjb-time-logging/SKILL.md`
- `Skills/cjb-run-management/SKILL.md`
- `Skills/cjb-date-research/SKILL.md`
- `Skills/cjb-location-research/SKILL.md`

## Integrity checking

Run:

- `python3 verify_pages.py`

What “OK” means:

- `Archive/Cain's Jawbone Unformatted.txt` matches `Archive/hash.txt`
- Page body text (above `## Notes`) in `Pages/*.md` matches the archive

It does **not** judge whether notes/hypotheses are correct.

## Git workflow

- Commit small, single-purpose changes (avoid mega-commits).
- Use branches for competing ordering approaches or discrete runs.
- Tag major milestones (e.g. `milestone-first-clustering-pass`).
- If a hypothesis collapses, prefer `git revert` over rewriting history.

## Agent runs & branching

- A run branch represents an end-to-end workstream (e.g. full extraction pass, clustering pass) and may span multiple sessions/days: `run/YYYYMMDD-<agent>-<focus>`.
- The active run metadata lives in `Worklog/current_run.txt`; leave it empty to signal no active run.
- During a run:
  - Stay on the recorded branch (no merging other branches in).
  - Log start/end times via the time-logging skill.
  - Commit frequently; final commit should be `Run summary: ...`.
- After a run:
  - Run `python3 verify_pages.py`, update `Worklog/worklog.csv`, merge to `main` only if the work is accepted, and clear `Worklog/current_run.txt`.

## Spoilers policy

- Do not import solved page orders, murderer/victim lists, or solution summaries.
- Research is limited to historically appropriate sources (≤1934). In particular:
  - Use Chambers' Book of Days to interpret date/saint/holiday references.
  - Use the Highways & Byways series to ground geographic descriptions.
  - Record findings in the indices/research queue.