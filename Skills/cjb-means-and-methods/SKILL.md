---
name: cjb-means-and-methods
version: 1.0
description: Catalogue possible killing methods (poisons, food/drink, plants, smells, medicine) without committing to murder; update motifs and flag pages for later murder analysis.
---

# Cain’s Jawbone — Means & Methods

## Non-negotiables

- Don’t assume murder: record possibilities, not conclusions.
- Default sequencing is extraction-first: do **not** resolve research items mid-pass; add `open` items to `Indexes/research_queue.md`.

## Phase gating
- **Allowed phases:** `phase-1` … `phase-6`
- **Phase-1 constraint:** do not promote murderer/victim conclusions; prefer flags over ledgers unless death is unmistakable.

## When to use

Trigger this skill when a page foregrounds:

- food/drink/medicine/pills
- plants, scents, fumes, animal exposure
- illness, weakness, heart symptoms, “natural causes” framing
- delayed timing (“another day”, “give it time”, “after”)

## Procedure

1. Identify candidate **substances/objects** and record them in the page’s `## Notes`:
   - what it is (as written)
   - how it’s administered (if implied)
   - who controls access/preparation
   - any timing/delay cues
2. Extract **symptoms** (onset, progression, recovery, suddenness).
3. Extract **environmental access** (rooms, gardens, meals, servants, tools).
4. Update `Indexes/objects_motifs.md`:
   - add a new motif entry or append the page to an existing entry
   - keep variants/snippets minimal
5. If any term/source needs lookup, add an `open` item to `Indexes/research_queue.md`.
6. Flag the page for later murder analysis by adding a single bullet under the page’s `## Notes`, e.g.:
   - `- **Murder analysis flag:** possible poison/means via <X> (confidence: MAYBE)`
7. If the page also strongly implies an in-world death/attempt, run `Skills/cjb-murder-analysis/SKILL.md`.

## Output checklist

- Motif/substance captured under page `## Notes`
- `Indexes/objects_motifs.md` updated
- Page flagged for later murder analysis (when appropriate)
