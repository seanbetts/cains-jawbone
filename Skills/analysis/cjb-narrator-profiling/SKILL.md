---
name: cjb-narrator-profiling
version: 1.0
description: Systematically catalogue narrator “signatures” (voice tells) across pages to support clustering without imposing page order.
---

# Cain’s Jawbone — Narrator Profiling

## Non-negotiables

- Do not edit page body text (only write under `## Notes`).
- Do not impose page order (this skill is for clustering by voice, not sequencing).
- Keep claims reversible and falsifiable; allow overlap early.

## Phase gating

- **Allowed phases:** `phase-3` … `phase-6`
- **Not allowed phases:** `phase-1`, `phase-2`

## Where to write

- Per-page: under `## Notes` → **Voice/tells** bullets in `Pages/cains_jawbone_page_*.md`
- Global index: `Indexes/narrators.md` (stable IDs `N01`, `N02`, …)
- Optional: use narrator IDs as anchors in `Order/hypotheses.md` cluster rationales

## Procedure

1. Extract voice tells from the page (skip anything that’s just a quotation being inserted):
   - diction (formal/informal; favourite words)
   - punctuation/typography habits (dashes, semicolons, parentheses)
   - professional knowledge (law, medicine, theatre, botany, naval terms)
   - social register/class tells (servants, clubs, schools, habits)
   - obsessive motifs (food/drink, plants, dogs/cats, citations)
2. Compare against existing narrator entries in `Indexes/narrators.md`.
3. If it matches an existing narrator:
   - append the page to that `Nxx` entry
   - add any new signature tells
   - adjust confidence conservatively
4. If it does not match:
   - create a new `Nxx` entry with a short label and the initial signature tells
5. If uncertain:
   - record multiple candidate narrator IDs (e.g. `MAYBE N03 / N07`) and add a falsifier to break the tie later.

## Template (recommended)

- `Nxx` — Label:
  - **Signature tells:**  
  - **Likely identity (if any):**  
  - **Pages:**  
  - **Confidence:** `MAYBE` / `LIKELY` / `CERTAIN`  
  - **Disconfirming evidence:**  
  - **Notes:**  

## Output checklist

- Narrator index updated (`Indexes/narrators.md`)
- Page notes updated under **Voice/tells** where relevant
