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

## Golden rules

- Never edit the page body text in `Pages/*.md` (only write under `## Notes`).
- Never modify anything in `Archive/`.
- Run `python3 verify_pages.py` after edits and before commits.
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

## Spoilers policy

- Do not import solved page orders, murderer/victim lists, or solution summaries.
- Research is allowed only for quotation/place/reference resolution; record results in the indices.

