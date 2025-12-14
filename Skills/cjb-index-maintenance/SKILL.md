---
name: cjb-index-maintenance
description: Keep Cain’s Jawbone global indices consistent (people, places, quotes, motifs, research queue) and cross-linked to pages with confidence and minimal quoting.
---

# Cain’s Jawbone — Index Maintenance

## Non-negotiables

- Do not modify page body text in `Pages/cains_jawbone_page_*.md` (Notes only).
- Keep citations minimal; never paste long page passages into index files.
- Prefer stable IDs and consistent formatting.

## Files covered

- `Indexes/people.md`
- `Indexes/places.md`
- `Indexes/quotes.md`
- `Indexes/objects_motifs.md`
- `Indexes/research_queue.md`

## Rules

### People (`Indexes/people.md`)

- Assign stable IDs `P01`, `P02`, … once and never reuse.
- Record aliases, consistent tells, and page links.
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

### Research queue (`Indexes/research_queue.md`)

- Each item should be a small lookup task, linked to pages.
- Track status: `open` → `in-progress` → `resolved`.
- When resolved, write the result succinctly and keep the original question for auditability.

## After any batch update

Run `python3 verify_pages.py`.

