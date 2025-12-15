# Cain’s Jawbone workspace instructions (for the coding agent)

This folder is a **literary puzzle workspace**, not a software project. The goal is to help the user **extract clues, build indices, cluster pages, and iteratively form ordering hypotheses** to identify the **six murderers and six victims**.

## Golden rules (must-follow)

1. **Log time before/after work.**  
   Follow `Skills/cjb-time-logging/SKILL.md`: capture `start` (UTC) before opening files and append to `Worklog/worklog.csv` with `end`/`minutes` before finishing.
2. **Use the active run branch.**  
   Follow `Skills/cjb-run-management/SKILL.md`: read `Worklog/current_run.txt`, stay on the recorded branch if present, or create a new `run/YYYYMMDD-agent-focus` branch only when the file is empty. Do not work on `main` directly.
3. **Never change page body text.**  
   For any file in `Pages/cains_jawbone_page_*.md`, only edit content **under** the `## Notes` heading. Do not alter, reflow, wrap, or “fix” punctuation in the page text above `## Notes`.
4. **Keep the archive immutable.**  
   Do not modify anything in `Archive/` (including `Archive/Cain's Jawbone Unformatted.txt` and `Archive/hash.txt`).
5. **Verify after edits.**  
   After any batch of note edits, run: `python3 verify_pages.py` and ensure it prints `OK` (this checks page-body immutability, not whether notes/hypotheses are correct).
6. **No brute force.**  
   Do not attempt permutation/brute-force ordering; progress comes from clue extraction, indexing, clustering, and evidence-based hypotheses.

## Working loop (default)

- Extract clues from a page into `## Notes` (per `Skills/cjb-page-extraction/SKILL.md`).
- Update relevant `Indexes/*` entries (per `Skills/cjb-index-maintenance/SKILL.md`).
- If proposing a linkage/sequence, record it (plus falsifier) in `Order/hypotheses.md` (per `Skills/cjb-order-hypotheses/SKILL.md`).

## Skills (authoritative procedures live here)

Keep all detailed procedures, templates, and rules in the Skill files to avoid drift. If guidance conflicts, treat the relevant `SKILL.md` as authoritative.

- **Page extraction:** `Skills/cjb-page-extraction/SKILL.md` — use when reviewing a page and updating `## Notes` + indices.
- **Index maintenance:** `Skills/cjb-index-maintenance/SKILL.md` — use when curating `Indexes/*` consistency and cross-links.
- **Order hypotheses:** `Skills/cjb-order-hypotheses/SKILL.md` — use when clustering pages and proposing sequences (with falsifiers).
- **Quote research:** `Skills/cjb-quote-research/SKILL.md` — use when capturing/identifying allusions and managing the research queue.
- **Verification:** `Skills/cjb-verification/SKILL.md` — use when running integrity checks and interpreting failures.
- **Time logging:** `Skills/cjb-time-logging/SKILL.md` — use at the start and end of every working session to keep `Worklog/worklog.csv` accurate.
- **Run management:** `Skills/cjb-run-management/SKILL.md` — use to create/close run branches and maintain `Worklog/current_run.txt`.
- **Date research:** `Skills/cjb-date-research/SKILL.md` — use Chambers' Book of Days to interpret calendar clues.
- **Location research:** `Skills/cjb-location-research/SKILL.md` — use Highways & Byways guides to ground geographic clues.

## Global artefacts (files we maintain)

Maintain these central files to turn page-by-page extraction into a searchable “index of clues”:

- `Indexes/people.md` (stable IDs like `P01`, aliases, pronouns/tells, pages seen)
- `Indexes/places.md` (place names, implied geography, pages, confidence)
- `Indexes/quotes.md` (exact snippet, likely source/author, why it matters, pages)
- `Indexes/objects_motifs.md` (recurring items/injuries/food/drink/animals/weather, pages)
- `Indexes/research_queue.md` (rolling queue of lookups to do; link items back to pages)
- `Order/hypotheses.md` (candidate sequences/clusters with reasons, confidence, falsifiers)

## Notes quick reference (non-authoritative)

This is a convenience summary only. The authoritative procedure/template is `Skills/cjb-page-extraction/SKILL.md`.

- Add notes only under `## Notes` in `Pages/cains_jawbone_page_*.md`.
- Prefer clue extraction over plot summary; keep quotes minimal.
- Common headings to include when relevant: Entities, Time markers, Quotes/allusions, Wordplay, Motifs/continuity hooks, Voice/tells, Ordering hypotheses, Disconfirming evidence, Research needed.
- Use confidence tags: `CERTAIN:`, `LIKELY:`, `MAYBE:`.
- Cross-reference with file paths like `Pages/cains_jawbone_page_42.md`.

## Mandatory time logging

Before doing any work:
1. Record `start` time (UTC) for this session.

Before finishing:
1. Record `end` time (UTC).
2. Calculate `minutes` between start and end.
3. Append a row to `Worklog/worklog.csv` (`date,agent,task,start,end,minutes,branch,commit,notes`).
4. Include `branch` and `commit` if available.

See `Skills/cjb-time-logging/SKILL.md` for the full procedure and formatting requirements.

## Agent runs and branching

Discrete AI agent sessions are treated as **runs**. Runs use dedicated git branches and `Worklog/current_run.txt` to keep track of the active branch.

### Creating a run
- Check `Worklog/current_run.txt`. If it already lists a `branch=…`, continue on that branch.
- If the file is empty:
  - Create a new branch: `run/YYYYMMDD-<agent>-<focus>` (e.g. `run/20251215-claude-clustering-pass1`).
  - Record branch metadata (branch/agent/task/start/notes) in `Worklog/current_run.txt`.

### During a run
- Commit frequently with small, descriptive commits.
- Log start/end times using the Time Logging Skill.
- Do not merge other branches into the run branch.
- Leave `Worklog/current_run.txt` untouched so restarts pick up the same run.

### Closing a run
1. Run `python3 verify_pages.py`.
2. Make a final commit summarising the run: `Run summary: <one sentence>`.
3. Log the session end time and final commit in `Worklog/worklog.csv`.
4. Clear `Worklog/current_run.txt` (empty file) once the run is complete.

### After a run
- Merge into `main` **only if** the run produced coherent progress.
- If a run is rejected or inconclusive, leave the branch unmerged as a record.
- Do not delete run branches unless explicitly instructed.

### Source of truth
- `main` always reflects the best current working state.
- Experimental, partial, or speculative work lives only in run branches.

## Git and versioning

This repo uses git for versioning. Keep a clean history so we can roll back hypotheses and index changes safely.

### Rules

- Never commit changes to any page-body text in `Pages/*.md`. Only edit metadata and `## Notes`.
- Run `python3 verify_pages.py` before committing. If it fails, fix and re-run. (`OK` means page-body integrity only, not that notes/hypotheses are correct.)
- Commit small, single-purpose changes. Avoid “mega commits”.
- Use branches for competing ordering approaches (clusters, narrator splits, alternative sequences). Prefer merge commits that explain what won.

### Commit conventions

Use short, descriptive messages, for example:

- `Notes: extract pages 1-10`
- `Indexes: add 4 quotes, 2 people aliases`
- `Order: propose Cluster A v2 + falsifiers`
- `Fix: normalise note headings for pages 33-40`

### Tags (milestones)

Use lightweight milestone tags without punctuation that git disallows, e.g.:

- `milestone-first-clustering-pass`
- `milestone-first-complete-ordering-pass`

### Rollback behaviour

If a hypothesis collapses, revert the commit(s) that introduced it rather than editing history. Record the reason for rollback in a new commit message or in `Order/hypotheses.md`.

## Safety & scope

- **No spoilers:** do not import or reproduce known solved page orders, murderer/victim lists, or solution summaries from the internet unless the user explicitly requests spoilers.
- **Mandatory research policy:** agents are expected to self-initiate research using only historically appropriate sources (≤1934). In particular, consult Chambers' Book of Days for calendar clues, Highways & Byways guides for geographic clues, and pre-1934 dictionaries/almanacs for terminology. Record all findings in the relevant indices and research queue.
- Avoid reproducing large verbatim chunks of page text in outputs; quote only the minimum needed for identification.
