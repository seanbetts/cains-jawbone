---
name: cjb-page-extraction
version: 1.0
description: Extract actionable clues from a Cain’s Jawbone page and update per-page Notes + global indices without ever changing page body text.
---

# Cain’s Jawbone — Page Extraction

## Non-negotiables

- Only edit content under `## Notes` in `Pages/cains_jawbone_page_*.md`.
- Never modify `Archive/` contents.
- Keep quotes minimal: only the smallest fragment needed to identify a reference.
- After edits, run `python3 Scripts/verify_pages.py` (must return `OK`).

## Phase gating
- **Allowed phases:** `phase-1` (primary), `phase-2` (write research results back into Notes), `phase-3` … `phase-6` (targeted rereads)
- **Phase-gated sections:** clustering/ordering and murder-ledger updates are only allowed in later phases (see below).

## Goal

Turn each page into structured, searchable clues that support clustering and ordering later.

## When to use (triggers)
- When you are reading a page for the first time in Phase 1.
- When Phase 2 research resolves an open item and you need to write the result back into the page’s notes.
- When later phases require a targeted reread to confirm/deny a specific hypothesis.

## Default sequencing (extraction-first)

During the first full extraction pass, do not pause to resolve external research questions. Instead:

- Record “source TBD” / uncertainties under the page’s `## Notes`.
- Add an `open` item to `Indexes/research_queue.md`.
- Continue to the next page (later pages often supply the missing context).

## Procedure (per page)

1. Open the page file: `Pages/cains_jawbone_page_N.md`.
2. Read the body text once, then focus on extraction (do not rewrite).
3. Under `## Notes`, add bullets in this order (skip any section that has nothing):
   - **Entities:** people/aliases, places, organizations.
   - **Time markers:** dates/holidays/seasonal cues, meals, timetable words, “yesterday/tomorrow”.
   - **Quotes & allusions:** minimal snippet + suspected source + why it’s an anchor.
   - **Wordplay:** in Phase 1, run wordplay detectors and record `CANDIDATE` blocks; in Phase 2+, run wordplay synthesis and record `LIKELY WORDPLAY` blocks (copy synthesis outputs into `Indexes/wordplay.md`).
   - **Motifs/continuity hooks:** objects, injuries, pills/poisons, animals, weather, letters.
   - **Voice/tells:** diction, punctuation habits, obsessions, professional knowledge.
   - **Research needed:** items to add to the global research queue.
4. Use confidence tags: `CERTAIN:`, `LIKELY:`, `MAYBE:`.
   - Wordplay outputs use `low|med|high` per `Skills/cjb-wordplay-synthesis/SKILL.md` and the Wordplay policy in `Skills/cjb-phase-playbook/SKILL.md`.
5. If you discover index-worthy items, update:
   - `Indexes/people.md`
   - `Indexes/places.md`
   - `Indexes/quotes.md`
   - `Indexes/objects_motifs.md`
   - `Indexes/wordplay.md` (Phase 2+; copy `LIKELY WORDPLAY` blocks)
   - `Indexes/research_queue.md`

## Phase-gated additions (optional)

- **Phase 1:** do not add clustering/ordering hypotheses. If harm/death is not unmistakable, add a single `Murder analysis flag` bullet and defer ledger updates.
- **Phase 1 (wordplay):** run all wordplay detectors (high recall) and record `CANDIDATE` blocks; do not interpret beyond `rationale` + `falsifier`.
- **Phase 2 (wordplay):** run `Skills/cjb-wordplay-synthesis/SKILL.md` to select 1–3 `LIKELY WORDPLAY` blocks and convert quote/place/date candidates into targeted research queue items.
- **Phase 3:** optionally add `Cluster candidates` notes on pages (no sequences).
- **Phase 4+:** optionally add `Ordering hypotheses` + `Disconfirming evidence` bullets (with falsifiers).
- **Phase 5+:** if an in-world death/attempt is supported by text, use `Skills/cjb-means-and-methods/SKILL.md` and `Skills/cjb-murder-analysis/SKILL.md`, and keep `Order/cast.md` + `Order/confidence.md` updated.

## Output checklist

- Notes added under `## Notes` only
- Any new entities/quotes/motifs reflected in indices
- `python3 Scripts/verify_pages.py` passes

## Recommended batching
- Extract **5–10 pages** per session for focus.
- Commit after each batch (not each page).
- Avoid pushing past ~30 pages in one sitting; quality tends to drop.

## Example extraction (style, not a real page)

Before (page snippet):
> “He thought of Johnson, dead these many years…”

After (notes):
- **Entities:** Johnson (P??) — unclear if in-world or historical.
- **Harm/death cues:** “dead these many years” — MAYBE allusion/idiom; do not record as in-world death without more.
- **Research needed:** Identify “Johnson” if the surrounding context suggests a specific historical/literary reference → add to `Indexes/research_queue.md`.

## Common mistakes (pitfalls)
- Copying long chunks of page text into indices (keep snippets minimal).
- Treating allusive/historical deaths as in-world murders.
- Recording wordplay without falsifiers (every block needs a way to be wrong).
- Merging people IDs too early (prefer “possible same as Pxx” + a falsifier).
