# Cain’s Jawbone workspace instructions (for the coding agent)

This folder is a **literary puzzle workspace**, not a software project. The goal is to help the user **extract clues, build indices, cluster pages, and iteratively form ordering hypotheses** to identify the **six murderers and six victims**.

## Golden rules (must-follow)

1. **Log time before/after work.**  
   Follow `Skills/cjb-time-logging/SKILL.md`: capture `start` (UTC) before opening files and append to `Worklog/worklog.csv` with `end`/`minutes` before finishing.
2. **Never change page body text.**  
   For any file in `Pages/cains_jawbone_page_*.md`, only edit content **under** the `## Notes` heading. Do not alter, reflow, wrap, or “fix” punctuation in the page text above `## Notes`.
3. **Keep the archive immutable.**  
   Do not modify anything in `Archive/` (including `Archive/Cain's Jawbone Unformatted.txt` and `Archive/hash.txt`).
4. **Verify after edits.**  
   After any batch of note edits, run: `python3 verify_pages.py` and ensure it prints `OK` (this checks page-body immutability, not whether notes/hypotheses are correct).
5. **No brute force.**  
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
- **Allowed research (if enabled by the user):** quotations, place names/geography, proper nouns, archaic terms, and reference resolution; record results in `Indexes/quotes.md`, `Indexes/places.md`, and/or `Indexes/research_queue.md`.
- Avoid reproducing large verbatim chunks of page text in outputs; quote only the minimum needed for identification.
