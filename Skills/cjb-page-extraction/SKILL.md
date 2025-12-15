---
name: cjb-page-extraction
description: Extract actionable clues from a Cain’s Jawbone page and update per-page Notes + global indices without ever changing page body text.
---

# Cain’s Jawbone — Page Extraction

## Non-negotiables

- Only edit content under `## Notes` in `Pages/cains_jawbone_page_*.md`.
- Never modify `Archive/` contents.
- Keep quotes minimal: only the smallest fragment needed to identify a reference.
- After edits, run `python3 verify_pages.py` (must return `OK`).

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
   - **Harm/death cues (optional):** if the page likely implies in-world violence/death, run `Skills/cjb-means-and-methods/SKILL.md` and/or `Skills/cjb-murder-analysis/SKILL.md` and keep `Order/cast.md` + `Order/confidence.md` updated.
   - **Voice/tells:** diction, punctuation habits, obsessions, professional knowledge.
   - **Ordering hypotheses:** candidate links to other pages with reasons + confidence.
   - **Disconfirming evidence:** what would falsify each linkage/cluster claim.
   - **Research needed:** items to add to the global research queue.
4. Use confidence tags: `CERTAIN:`, `LIKELY:`, `MAYBE:`.
5. If you discover index-worthy items, update:
   - `Indexes/people.md`
   - `Indexes/places.md`
   - `Indexes/quotes.md`
   - `Indexes/objects_motifs.md`
   - `Indexes/research_queue.md`

## Output checklist

- Notes added under `## Notes` only
- Any new entities/quotes/motifs reflected in indices
- `python3 verify_pages.py` passes
