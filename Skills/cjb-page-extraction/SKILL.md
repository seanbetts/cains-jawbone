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
   - **Wordplay:** spoonerisms, cryptic indicators, homophones, hidden names.
   - **Motifs/continuity hooks:** objects, injuries, pills/poisons, animals, weather, letters.
   - **Voice/tells:** diction, punctuation habits, obsessions, professional knowledge.
   - **Research needed:** items to add to the global research queue.
4. Use confidence tags: `CERTAIN:`, `LIKELY:`, `MAYBE:`.
5. If you discover index-worthy items, update:
   - `Indexes/people.md`
   - `Indexes/places.md`
   - `Indexes/quotes.md`
   - `Indexes/objects_motifs.md`
   - `Indexes/research_queue.md`

## Phase-gated additions (optional)

- **Phase 1:** do not add clustering/ordering hypotheses. If harm/death is not unmistakable, add a single `Murder analysis flag` bullet and defer ledger updates.
- **Phase 3:** optionally add `Cluster candidates` notes on pages (no sequences).
- **Phase 4+:** optionally add `Ordering hypotheses` + `Disconfirming evidence` bullets (with falsifiers).
- **Phase 5+:** if an in-world death/attempt is supported by text, use `Skills/cjb-means-and-methods/SKILL.md` and `Skills/cjb-murder-analysis/SKILL.md`, and keep `Order/cast.md` + `Order/confidence.md` updated.

## Output checklist

- Notes added under `## Notes` only
- Any new entities/quotes/motifs reflected in indices
- `python3 Scripts/verify_pages.py` passes
