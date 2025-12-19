---
name: cjb-date-research
version: 1.0
description: Use Chambers' Book of Days (1890s edition) to interpret date/month clues from Cain's Jawbone pages and log findings in Indexes.
---

# Date research (Chambers' Book of Days)

## Purpose
Anchor any explicit or implied dates using the historical reference that would have been available in 1934.

## When to use
- Whenever a page mentions a specific day/month, saint’s day, holiday, festival, or almanac-style reference.
- When a clue implies “the day when …” that might map to a Book of Days entry.

## Phase gating
- **Allowed phases:** `phase-2` (primary), `phase-3` … `phase-6` (as needed)

## Procedure
1. Extract the minimal quote referencing the date and add it to the page’s Notes.
2. Log the lookup in `Indexes/research_queue.md` if unresolved.
3. Consult Chambers' Book of Days (use a public-domain scan; limit to content published before 1934).
4. Record findings:
   - Add entry to `Indexes/quotes.md` or `Indexes/objects_motifs.md` as appropriate.
   - Note any associations (events, historical figures, traditions) plus why it matters for ordering or narrator ID.
5. Cross-reference with other pages mentioning the same date or saint.

## Output format
- Page notes: `CERTAIN: Date reference → [Book of Days entry summary] (Chambers' Book of Days)`
- Index entry: include page(s), Book of Days page/volume if available, and confidence.

## If no match is found

- Mark the research queue item as `stalled`, record what you checked, and keep the smallest plausible interpretations alive (variant spellings, fictional name-days, etc.).
