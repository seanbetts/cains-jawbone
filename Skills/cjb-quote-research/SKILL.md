---
name: cjb-quote-research
version: 1.0
description: Identify, record, and (optionally) research Cain’s Jawbone quotations and allusions; update quote index and research queue with minimal snippets and clear anchors.
---

# Cain’s Jawbone — Quote Research

## Non-negotiables

- Quote only the minimum fragment needed to identify a reference.
- Do not paste large page text blocks into indices.
- Record uncertainty explicitly; do not “lock in” a source without evidence.

## Where to write

- Per-page: `Pages/cains_jawbone_page_N.md` under `## Notes`
- Global index: `Indexes/quotes.md`
- Open questions: `Indexes/research_queue.md`

## Phase gating
- **Allowed phases:** `phase-1` (capture only), `phase-2` (resolve), `phase-3` … `phase-6` (as needed)

## Sources policy
- Use only historically appropriate sources (≤1934), preferring items listed in `Indexes/reference_sources.md`.
- Avoid solved guides/modern analyses unless the user explicitly requests spoilers.

## Workflow

If you start from wordplay outputs:
- Treat `CANDIDATE` blocks from `Skills/cjb-wordplay-allusion-detect/SKILL.md` as **candidate quotes** only (no attribution until verified).
- Treat any synthesis “candidate quote” as a cue to create a targeted lookup in `Indexes/research_queue.md`.

1. Extract the smallest identifying snippet (often 5–15 words).
2. In the page’s `## Notes`, record:
   - snippet
   - suspected source/author (if any)
   - why it might matter (date anchor, thematic marker, voice tell)
   - confidence
3. Add/update an entry in `Indexes/quotes.md` with the same information and page links.
4. If identification is uncertain, add an `open` item to `Indexes/research_queue.md`.

## Citation format (recommended)

- `Author, *Work* (Year/Edition), location (act/scene/line or p. X), URL (if applicable)`

## Default sequencing (extraction-first)

During the first full extraction pass, prefer capturing quotes + adding `open` research items over doing lookups. Resolve the research queue after the full-page pass unless the user explicitly asks to research earlier.

## If browsing is enabled by the user

Do targeted lookups (quotes, proper nouns, locations) and record results in:

- `Indexes/quotes.md` (for quotes)
- `Indexes/places.md` (for locations)
- `Indexes/research_queue.md` (mark resolved + result)

## If research yields no match (or conflicts)

1. Keep the research queue item small and specific.
2. Mark the item `stalled` (not `resolved`) and record:
   - which sources you checked (e.g., Chambers 1908, Book of Days, Gutenberg)
   - any variant spellings tried
   - why it might still matter
3. Record multiple plausible candidates (if any) with confidence and a brief disambiguation note; keep status `stalled` until a single best match is justified.
