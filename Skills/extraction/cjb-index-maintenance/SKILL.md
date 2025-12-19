---
name: cjb-index-maintenance
version: 1.0
description: Keep Cain’s Jawbone global indices consistent (people, places, quotes, motifs, research queue) and cross-linked to pages with confidence and minimal quoting.
---

# Cain’s Jawbone — Index Maintenance

## Non-negotiables

- Do not modify page body text in `Pages/cains_jawbone_page_*.md` (Notes only).
- Keep citations minimal; never paste long page passages into index files.
- Prefer stable IDs and consistent formatting.

## Phase gating
- **Allowed phases:** `phase-1` … `phase-6`

## When to use (triggers)
- After extracting notes from any page (Phase 1).
- After resolving a research item and writing results back into notes (Phase 2).
- When you notice duplicate IDs, inconsistent spellings, or stale/conflicting entries.
- Before phase changes and before merging a run branch to `main`.

## Files covered

- `Indexes/people.md`
- `Indexes/places.md`
- `Indexes/quotes.md`
- `Indexes/objects_motifs.md`
- `Indexes/narrators.md`
- `Indexes/wordplay.md`
- `Indexes/research_queue.md`

## Rules

### People (`Indexes/people.md`)

- Assign stable IDs `P01`, `P02`, … once and never reuse.
- Record aliases, consistent tells, and page links.
- If an “entity” is non-human or unclear, say so explicitly (e.g., “Jasmine (cat)”, “(animal?)”, “(uncertain)”) rather than silently mixing it with people.
- If two IDs might be the same person, record as a hypothesis with falsifiers (don’t merge prematurely).

### Places (`Indexes/places.md`)

- Record explicit and implied locations.
- Always include a confidence tag and the pages where it appears.

### Quotes (`Indexes/quotes.md`)

- Store only a short snippet (enough to identify).
- Capture:
  - likely source/author
  - why it matters (date anchor, voice tell, continuity hook)
  - pages + confidence
  - whether research is needed

### Motifs (`Indexes/objects_motifs.md`)

- Track recurring items (foods, drinks, injuries, pills/poisons, animals, weather, tools).
- Note variants and pages; suggest clustering implications if any.

### Wordplay (`Indexes/wordplay.md`)

- This is a cross-page catalogue of **synthesis outputs** only:
  - include only `LIKELY WORDPLAY` blocks (do not copy raw detector `CANDIDATE` blocks here).
- Always include the page path and keep entries in page-number order.
- Keep `span` exact and short; do not paste long page text.
- Every entry must include `confidence` and `falsifiers` (per `Skills/wordplay/cjb-wordplay-synthesis/SKILL.md`).

### Research queue (`Indexes/research_queue.md`)

- Each item should be a small lookup task, linked to pages.
- Track status:
  - `open` (not started)
  - `in-progress` (actively working)
  - `stalled` (tried; no match yet or conflicting sources)
  - `resolved` (answer recorded with citation)
- When resolved, write the result succinctly and keep the original question for auditability.

## Formatting conventions

- **Page references:** always use full paths like `Pages/cains_jawbone_page_42.md` and keep page lists in numeric order.
- **Confidence tags:** use only `CERTAIN`, `LIKELY`, `MAYBE` (see `Skills/core/cjb-phase-playbook/SKILL.md` for shared conventions).

## After any batch update

Run `python3 Scripts/verify_pages.py`.
