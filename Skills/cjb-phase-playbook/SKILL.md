---
name: cjb-phase-playbook
version: 1.0
description: Phase-by-phase playbook for Cain’s Jawbone. Use at the start of a run and whenever the phase changes to decide allowed actions, required Skills, required outputs, and exit conditions.
---

# Phase playbook

## Purpose
Provide a single authoritative, phase-specific guide for what to do next, what not to do, which Skills to use, what files to update, and what “done” looks like for each phase.

## When to use
- At the start of any run (after run metadata is set in `Worklog/current_run.txt`).
- Whenever the declared phase changes.
- Whenever there is ambiguity about whether an action is allowed in the current phase.

## Phase declaration requirements
- The active phase must be recorded:
  - in `Worklog/current_run.txt`, and
  - in the `phase` field in `Worklog/worklog.csv` for each session.
- Actions outside the declared phase require explicit instruction from the user.

## Global rules (apply in all phases)
- Never edit page body text in `Pages/cains_jawbone_page_*.md` (only under `## Notes`).
- Never modify anything in `Archive/`.
- Run `python3 Scripts/verify_pages.py` after edits and before commits (integrity only).
- Log start/end (UTC) for every session per `Skills/cjb-time-logging/SKILL.md`.
- Do not brute force ordering.

## Skill priority (when multiple apply)
1. `Skills/cjb-time-logging/SKILL.md` (always first/last)
2. `Skills/cjb-verification/SKILL.md` (before commits; after any page-note edits)
3. `Skills/cjb-index-maintenance/SKILL.md` (after any extraction/research writes)
4. Phase-specific skill(s) for the current work

## Confidence conventions (shared)
- Use tags `MAYBE`, `LIKELY`, `CERTAIN` in indices/hypotheses.
- When using numeric confidence (`0.0–1.0`) in ledgers:
  - `0.00–0.19` = weak signal only
  - `0.20–0.49` ≈ `MAYBE`
  - `0.50–0.79` ≈ `LIKELY`
  - `0.80–1.00` ≈ `CERTAIN`

## Progress checks (optional)
- During Phase 2, run `python3 Scripts/calculate_research_progress.py` to summarise research-queue status and index confidence distribution.

---

## Phase 1: Page extraction

### Goal
Extract signals, not meaning.

### Use
- `Skills/cjb-page-extraction/SKILL.md`
- `Skills/cjb-index-maintenance/SKILL.md`
- `Skills/cjb-verification/SKILL.md`
Optional (only when relevant):
- `Skills/cjb-means-and-methods/SKILL.md`

### Allowed actions
- Read each page once and populate `## Notes` only.
- Extract and index:
  - explicit entities (people, places)
  - quotations/allusions (short fragments only)
  - objects/motifs/substances
  - time markers (dates, days, seasons, “before/after” language)
  - research-needed flags (add to `Indexes/research_queue.md`)

### Update files
- `Pages/cains_jawbone_page_*.md` (notes only)
- `Indexes/people.md`
- `Indexes/places.md`
- `Indexes/quotes.md`
- `Indexes/objects_motifs.md`
- `Indexes/research_queue.md`

### Forbidden actions
- Do not propose ordering or clustering.
- Do not do external research.
- Do not attempt narrator synthesis.
- Do not do murder analysis unless harm/death is unmistakable and explicitly supported by text.

### Exit condition
- All 100 pages have been read once and every page has a meaningful `## Notes` section.
- Nothing feels “unknown because unseen”, only “unclear because unresolved”.

---

## Phase 2: External research resolution

### Goal
Collapse ambiguity caused by external references while keeping scope bounded.

### Use
- `Skills/cjb-quote-research/SKILL.md`
- `Skills/cjb-date-research/SKILL.md`
- `Skills/cjb-location-research/SKILL.md`
- `Skills/cjb-index-maintenance/SKILL.md`
Optional:
- `Skills/cjb-verification/SKILL.md`

### Allowed actions
Research only items that meet at least one criterion:
- Appears on multiple pages
- Seems temporally anchoring (dates, days, historical references)
- Feels like deliberate quotation/wordplay
- Marks transitions (arrivals, departures, deaths)

Resolve by:
- identifying likely sources for quotes/allusions
- grounding place references (when plausibly geographic)
- interpreting calendar/saint/day references

### Update files
- `Indexes/quotes.md` (source + why it matters + page refs)
- `Indexes/places.md`
- `Indexes/research_queue.md` (close items or mark `stalled` with reason)
- `Indexes/people.md` (only if research clarifies identity/alias)

### Forbidden actions
- Do not order pages.
- Do not build sequences.
- Do not cluster pages/narrators yet (keep this for Phase 3).
- Avoid deep research on one-off metaphors or isolated symbolism.

### Exit condition
- Most recurring/anchoring references are resolved, or explicitly marked `stalled` with a reason and confidence.
- `Indexes/research_queue.md` is materially smaller and higher-signal.

---

## Phase 3: Pattern detection and clustering

### Goal
Identify groups before order.

### Use
- `Skills/cjb-order-hypotheses/SKILL.md` (clusters-only mode)
- `Skills/cjb-index-maintenance/SKILL.md`
- `Skills/cjb-narrator-profiling/SKILL.md`

### Allowed actions
- Identify patterns across pages:
  - stylistic voice tells
  - recurring people
  - recurring locations
  - same dates
  - repeated objects/substances
  - similar emotional tone
- Propose clusters as narrative strands (not sequences).
- Allow overlap: pages may belong to multiple clusters early.

### Update files
- `Order/hypotheses.md` (clusters only; reasons + falsifiers)
- Optional: add “cluster candidates” notes on pages under `## Notes`
- `Indexes/narrators.md` (narrator signatures + page lists)
- Keep indices consistent as clusters reveal duplicates/aliases

### Forbidden actions
- Do not impose page order within clusters.
- Do not attempt global ordering.
- Avoid final murderer/victim conclusions.

### Exit condition
- 4–8 rough clusters exist with defensible rationales and falsifiers.
- You can describe what makes each cluster coherent (voice/motif/people/place).

---

## Phase 4: Internal ordering within clusters

### Goal
Turn clusters into sequences.

### Use
- `Skills/cjb-order-hypotheses/SKILL.md`
- `Skills/cjb-verification/SKILL.md`
Optional:
- `Skills/cjb-narrator-profiling/SKILL.md`

### Allowed actions
Within a single cluster at a time, propose internal page sequences using:
- temporal cues (day/time/before-after language)
- physical continuity (movement, locations)
- pronoun resolution and conversational continuity
- quote continuation logic
- entry/exit logic (how scenes begin/end)

Record:
- proposed local orderings
- confidence and falsifiers

### Update files
- `Order/hypotheses.md` (cluster orderings + evidence + falsifiers)
- `Order/confidence.md` (confidence tracking for ordering hypotheses as needed)

### Forbidden actions
- Do not merge clusters yet.
- Do not force unclustered pages into sequences.
- Do not write the final solution.

### Exit condition
- At least one cluster has a high-confidence internal order that survives falsification attempts.

---

## Phase 5: Cross-cluster stitching

### Goal
Build the full 100-page sequence.

### Use
- `Skills/cjb-order-hypotheses/SKILL.md`
- `Skills/cjb-murder-analysis/SKILL.md`
- `Skills/cjb-means-and-methods/SKILL.md`
- `Skills/cjb-motive-and-relationships/SKILL.md`
Optional:
- `Skills/cjb-narrator-profiling/SKILL.md`

### Allowed actions
- Align cluster endings to other cluster beginnings.
- Use shared characters and consequences as constraints.
- Use deaths as connectors, not endpoints.
- Start stabilising murderer/victim candidate tracking as ordering firms up.

### Update files
- `Order/hypotheses.md` (cross-cluster joins + alternatives + falsifiers)
- `Order/cast.md` (candidate roles with confidence + falsifiers)
- `Order/confidence.md` (event-level murder hypotheses as needed)
- Indices as newly revealed links require deduplication

### Forbidden actions
- Do not “finalise” if major ordering uncertainty remains.
- Do not write `FINAL_SOLUTION.md` until the ordering and murders are stable.

### Exit condition
- A single proposed full ordering exists (even if confidence varies across segments).
- Murderer/victim candidates have narrowed and are becoming consistent with the ordering.

---

## Phase 6: Convergence and falsification

### Goal
Break the solution, then earn confidence back.

### Use
- `Skills/cjb-verification/SKILL.md`
- `Skills/cjb-order-hypotheses/SKILL.md`
- `Skills/cjb-murder-analysis/SKILL.md`
- `Skills/cjb-falsification/SKILL.md`

### Allowed actions
- Actively falsify:
  - ordering joins
  - murder counts
  - murderer identities
  - victim identities
- Re-read transitions where joins occur.
- Resolve contradictions in tone, continuity, and reference alignment.

### Update files
- `Order/hypotheses.md` (final refinements + explicit rejected alternatives)
- `Order/cast.md` and `Order/confidence.md` (stabilise and prune)
- Indices as needed for final consistency

### Forbidden actions
- Do not write `FINAL_SOLUTION.md` until remaining doubts are minor and local.

### Exit condition
- Remaining doubts are minor and local, not structural.
- Ordering and murders are stable enough to justify populating `FINAL_SOLUTION.md`.

---

## Final output gating
Only once Phase 6 exit conditions are satisfied:
- Populate `FINAL_SOLUTION.md` (answers only, no commentary).
- Do not create alternative solution files or drafts.
