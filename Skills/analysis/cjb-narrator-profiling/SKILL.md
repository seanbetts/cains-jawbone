---
name: cjb-narrator-profiling
version: 1.1
description: Systematically catalogue narrator “signatures” (voice tells) across pages to support clustering without imposing page order.
---

# Cain’s Jawbone — Narrator Profiling

## Non-negotiables

- Do not edit page body text (only write under `## Notes`).
- Do not impose page order (this skill is for clustering by voice, not sequencing).
- Keep claims reversible and falsifiable; allow overlap early.
- Separate **VOICE** tells from **QUOTE-LAYER** tells (quotes/allusions are often detachable and should not be the only basis for merging narrators).

## Phase gating

- **Allowed phases:** `phase-3` … `phase-6`
- **Not allowed phases:** `phase-1`, `phase-2`

## Where to write

- Per-page: under `## Notes` → **Voice/tells** bullets in `Pages/cains_jawbone_page_*.md`
- Global index: `Indexes/narrators.md` (stable IDs `N01`, `N02`, …)
- Optional: use narrator IDs as anchors in `Order/hypotheses.md` cluster rationales

## Procedure

1. Extract tells from the page into two buckets:
   - **VOICE tells** (preferred for clustering): diction, punctuation habits, profession knowledge, social register/class tells, recurring obsessions (food/drink, plants, pets, etc.).
   - **QUOTE-LAYER tells** (record, but treat as detachable): quotations/allusions inserted for flavour, including long/identifiable source snippets that do not imply scene continuity.
2. Compare against existing narrator entries in `Indexes/narrators.md`.
3. If it matches an existing narrator:
   - append the page to that `Nxx` entry
   - add any new VOICE signature tells (and QUOTE-LAYER tells only as secondary support)
   - adjust confidence conservatively
4. If it does not match:
   - create a new `Nxx` entry with a short label and the initial signature tells
5. If uncertain:
   - record multiple candidate narrator IDs (e.g. `MAYBE N03 / N07`) and add a falsifier to break the tie later.
6. Add 1–2 **exclusion tells** (anti-anchors) for the narrator hypothesis (what would rule this voice out if seen on another page).

## Template (recommended)

- `Nxx` — Label:
  - **Signature tells (VOICE):**  
  - **Recurring quote-layer tells (optional):**  
  - **Exclusion tells (anti-anchors):**  
  - **Likely identity (if any):**  
  - **Pages:**  
  - **Confidence:** `MAYBE` / `LIKELY` / `CERTAIN`  
  - **Disconfirming evidence:**  
  - **Notes:**  

## Output checklist

- Narrator index updated (`Indexes/narrators.md`)
- Page notes updated under **Voice/tells** where relevant
