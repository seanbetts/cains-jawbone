# Cain’s Jawbone workspace instructions (for the AI agent)

This folder is a **literary puzzle workspace**, not a software project. The goal is to help the user **extract clues, build indices, cluster pages, and iteratively form ordering hypotheses** to identify the **six murderers and six victims**.

## Golden rules (must-follow)

1. **Log time before/after work.**  
   Follow `Skills/core/cjb-time-logging/SKILL.md`: capture `start` (UTC) before opening files and append to `Worklog/worklog.csv` with `end`/`minutes` before finishing.
2. **Use the active run branch.**  
   Follow `Skills/core/cjb-run-management/SKILL.md`: read `Worklog/current_run.txt`, stay on the recorded branch if present, or create a new `run/YYYYMMDD-agent-focus` branch only when the file is empty **and** you are starting a new end-to-end run (not a new page batch / session). Do not work on `main` directly.
3. **Never change page body text.**  
   For any file in `Pages/cains_jawbone_page_*.md`, only edit content **under** the `## Notes` heading. Do not alter, reflow, wrap, or “fix” punctuation in the page text above `## Notes`.
4. **Keep the archive immutable.**  
   Do not modify anything in `Archive/` (including `Archive/Cain's Jawbone Unformatted.txt` and `Archive/hash.txt`).
5. **Verify after edits.**  
   After any batch of note edits, run: `python3 Scripts/verify_pages.py` and ensure it prints `OK` (this checks page-body immutability, not whether notes/hypotheses are correct).
6. **No brute force.**  
   Do not attempt permutation/brute-force ordering; progress comes from clue extraction, indexing, clustering, and evidence-based hypotheses.

## Phase declaration (mandatory)

Agents must explicitly declare the phase they are operating in before starting work.

- Valid phases are:
  - Phase 1: Page extraction
  - Phase 2: External research resolution
  - Phase 3: Pattern detection and clustering
  - Phase 4: Internal ordering within clusters
  - Phase 5: Cross-cluster stitching
  - Phase 6: Convergence and falsification

For phase-specific procedures, required Skills, file updates, forbidden actions, and exit conditions, follow `Skills/core/cjb-phase-playbook/SKILL.md`.

- The active phase must be recorded:
  - in `Worklog/current_run.txt`, and
  - in the `phase` field of `Worklog/worklog.csv` for each session.

Actions outside the declared phase require explicit instruction from the user.

## Working loop (default)

- Extract clues from a page into `## Notes` (per `Skills/extraction/cjb-page-extraction/SKILL.md`).
- Update relevant `Indexes/*` entries (per `Skills/extraction/cjb-index-maintenance/SKILL.md`).
- If proposing a linkage/sequence, record it (plus falsifier) in `Order/hypotheses.md` (per `Skills/analysis/cjb-order-hypotheses/SKILL.md`).
- When a page likely involves in-world harm/death, use the murder-analysis skills (below) and keep `Order/cast.md` + `Order/confidence.md` updated.
- **Default sequencing:** complete a full page-extraction pass (all 100 pages) before doing any external research; capture research needs as `open` items in `Indexes/research_queue.md`.

Phase constraints apply:

- Phase 1: Do not propose ordering, clustering, or murderer/victim conclusions.
- Phase 2: Do not order pages; research only items recorded in `Indexes/research_queue.md`.
- Phase 3: Do not impose sequence order; clusters only.
- Phase 4+: Ordering and murder analysis may proceed, with confidence and falsifiers.

## Skills (authoritative procedures live here)

Keep all detailed procedures, templates, and rules in the Skill files to avoid drift. If guidance conflicts, treat the relevant `SKILL.md` as authoritative.

- **Phase playbook:** `Skills/core/cjb-phase-playbook/SKILL.md` — use at the start of a run and whenever the phase changes to determine allowed actions, required Skills, file updates, and exit conditions.
- **Page extraction:** `Skills/extraction/cjb-page-extraction/SKILL.md` — use when reviewing a page and updating `## Notes` + indices.
- **Index maintenance:** `Skills/extraction/cjb-index-maintenance/SKILL.md` — use when curating `Indexes/*` consistency and cross-links.
- **Order hypotheses:** `Skills/analysis/cjb-order-hypotheses/SKILL.md` — use when clustering pages and proposing sequences (with falsifiers).
- **Murder analysis:** `Skills/analysis/cjb-murder-analysis/SKILL.md` — use when pages imply in-world death/violence; updates cast + murder-confidence ledgers.
- **Means & methods:** `Skills/analysis/cjb-means-and-methods/SKILL.md` — use to catalogue substances/methods conservatively without committing to murder.
- **Motive & relationships:** `Skills/analysis/cjb-motive-and-relationships/SKILL.md` — use to extract relationship/power dynamics that support motive hypotheses.
- **Narrator profiling:** `Skills/analysis/cjb-narrator-profiling/SKILL.md` — use in Phase 3+ to catalogue narrator “signatures” (voice tells) without imposing page order.
- **Quote research:** `Skills/research/cjb-quote-research/SKILL.md` — use when capturing/identifying allusions and managing the research queue.
- **Falsification:** `Skills/analysis/cjb-falsification/SKILL.md` — use in Phase 6 to systematically try to break ordering/murder hypotheses and record outcomes.
- **Progress check:** `Skills/core/cjb-progress-check/SKILL.md` — use to decide “what next” and whether phase exit conditions are met.
- **Verification:** `Skills/core/cjb-verification/SKILL.md` — use when running integrity checks and interpreting failures.
- **Time logging:** `Skills/core/cjb-time-logging/SKILL.md` — use at the start and end of every working session to keep `Worklog/worklog.csv` accurate.
- **Run management:** `Skills/core/cjb-run-management/SKILL.md` — use to create/close run branches and maintain `Worklog/current_run.txt`.
- **Merge to main:** `Skills/core/cjb-merge-to-main/SKILL.md` — use to selectively merge infrastructure (Skills, Scripts, docs) to `main` without merging puzzle state.
- **Date research:** `Skills/research/cjb-date-research/SKILL.md` — use Chambers' Book of Days to interpret calendar clues.
- **Location research:** `Skills/research/cjb-location-research/SKILL.md` — use Highways & Byways guides to ground geographic clues.

## Wordplay skills

- **Detectors:** `Skills/wordplay/cjb-wordplay-*-detect/SKILL.md` (anagram, hidden-word, homophone, spoonerism, reversal, deletion, charade, double-definition, orthography, allusion)
- **Synthesis:** `Skills/wordplay/cjb-wordplay-synthesis/SKILL.md`
- **Phase policy:** Phase 1 detectors only; Phase 2–3 synthesis; Phase 4+ rerun only to verify disputes/constraints.
- **Hard rule:** detectors never order pages; synthesis may say “useful for ordering” but must not claim final ordering.
- **Output contract:** every block includes `confidence` + `falsifier(s)` and uses exact short spans; synthesis outputs are copied to `Indexes/wordplay.md`.

## Global artefacts (files we maintain)

Maintain these central files to turn page-by-page extraction into a searchable “index of clues”:

- `Indexes/people.md` (stable IDs like `P01`, aliases, pronouns/tells, pages seen)
- `Indexes/places.md` (place names, implied geography, pages, confidence)
- `Indexes/quotes.md` (exact snippet, likely source/author, why it matters, pages)
- `Indexes/objects_motifs.md` (recurring items/injuries/food/drink/animals/weather, pages)
- `Indexes/narrators.md` (narrator “signatures” / voice tells, pages, confidence)
- `Indexes/wordplay.md` (synthesised wordplay findings, pages, why-it-matters tag, falsifiers)
- `Indexes/SCHEMA.md` (schemas/templates for all `Indexes/*`)
- `Indexes/research_queue.md` (rolling queue of lookups to do; link items back to pages)
- `Order/hypotheses.md` (candidate sequences/clusters with reasons, confidence, falsifiers)
- `Order/cast.md` (people tracked as murderer/victim/witness/unknown candidates)
- `Order/confidence.md` (in-world death/murder event hypotheses with confidence + falsifiers)

## Murder analysis skills

Use murder-analysis skills conservatively:

- Do not assume murder unless textual evidence supports it.
- Prefer means/motive extraction before accusation (use `cjb-means-and-methods` and `cjb-motive-and-relationships`).
- All conclusions must include confidence and falsifiers, and stay reversible (`active`/`downgraded`/`rejected`).

## Notes quick reference (non-authoritative)

This is a convenience summary only. The authoritative procedure/template is `Skills/extraction/cjb-page-extraction/SKILL.md`.

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
3. Append a row to `Worklog/worklog.csv` (`date,agent,phase,task,start,end,minutes,branch,commit,notes`).
4. Include `branch` and `commit` if available.

See `Skills/core/cjb-time-logging/SKILL.md` for the full procedure and formatting requirements.

## Agent runs and branching

Runs are **end-to-end workstreams** (e.g., “full extraction pass”, “clustering pass”, “ordering pass”) that may span multiple sessions/days. Runs use dedicated git branches and `Worklog/current_run.txt` to keep track of the active branch.

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
- Do **not** create new run branches for page “batches”; keep committing batches on the same run branch until the run’s end goal is reached.

### Closing a run
1. Run `python3 Scripts/verify_pages.py`.
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
- Run `python3 Scripts/verify_pages.py` before committing. If it fails, fix and re-run. (`OK` means page-body integrity only, not that notes/hypotheses are correct.)
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

## Final solution output

- The final answer must be written only to `FINAL_SOLUTION.md`.
- Do not create alternative solution files or drafts.
- Do not include reasoning, commentary, or confidence in the final output.
- Populate `FINAL_SOLUTION.md` only when the ordering and murders are considered stable.
- Treat `FINAL_SOLUTION.md` as write-once unless explicitly instructed to revise.
- Commits that modify `FINAL_SOLUTION.md` must not modify any other files.

## Safety & scope

- **No spoilers:** do not import or reproduce known solved page orders, murderer/victim lists, or solution summaries from the internet unless the user explicitly requests spoilers.
- **Mandatory research policy:** when research is needed, use only historically appropriate sources (≤1934). Default sequencing is extraction-first: finish the full page pass before resolving research queue items unless the user explicitly asks to research earlier.
- When conducting research, use only sources listed in `Indexes/reference_sources.md` unless explicitly instructed otherwise.
- Avoid reproducing large verbatim chunks of page text in outputs; quote only the minimum needed for identification.
