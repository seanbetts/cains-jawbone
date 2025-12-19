---
name: cjb-progress-check
version: 1.0
description: Quick, phase-aware progress assessment to decide what to do next and whether exit conditions are met (with lightweight scripts where available).
---

# Cain’s Jawbone — Progress Check

## Purpose
Provide a lightweight, repeatable way to answer: **“Are we done with this phase, and if not, what’s the next highest-value work?”**

## Phase gating
- **Allowed phases:** `phase-1` … `phase-6`

## When to use (triggers)
- At the start of a session (choose the next task).
- Before changing `phase=` in `Worklog/current_run.txt`.
- At the end of a session (capture a concise status note for `Worklog/worklog.csv`).

## Inputs
- Current phase from `Worklog/current_run.txt`
- Current state of `Pages/`, `Indexes/`, and `Order/`

## Outputs
- A 1–3 sentence status summary (use as the `notes` field in `Worklog/worklog.csv`).
- Optional: a short, prioritized list of next actions (kept in working memory for the run).

## Procedure

1. Confirm you’re on the active run branch (see `Skills/core/cjb-run-management/SKILL.md`).
2. If you edited any page notes, run integrity verification:
   - `python3 Scripts/verify_pages.py`
3. Run phase-specific checks (below).
4. Compare against the phase exit conditions in `Skills/core/cjb-phase-playbook/SKILL.md`.
5. Pick the smallest next step that reduces uncertainty (or closes an `open` research item).

## Phase-specific checks (quick)

### Phase 1 (page extraction)
- Coverage: all 100 pages have a meaningful `## Notes` section.
- Indices exist and have non-empty entries: `Indexes/people.md`, `Indexes/places.md`, `Indexes/quotes.md`, `Indexes/objects_motifs.md`, `Indexes/research_queue.md`.
- Wordplay (optional): detector `CANDIDATE` blocks exist on pages where wording feels mechanistic or quote-like.

### Phase 2 (external research resolution)
- Research queue is shrinking and higher-signal: recurring anchors are `resolved` or clearly `stalled`.
- Run the progress script:
  - `python3 Scripts/calculate_research_progress.py`
- Confirm that any newly resolved anchors were written back into:
  - the originating page’s `## Notes`, and
  - the relevant index (`Indexes/quotes.md`, `Indexes/places.md`, `Indexes/people.md`, `Indexes/wordplay.md`).

### Phase 3 (pattern detection and clustering)
- 4–8 provisional clusters exist in `Order/hypotheses.md`, each with:
  - rationale + key anchors
  - explicit falsifiers
- Narrator profiles exist in `Indexes/narrators.md` (Phase 3+ only).

### Phase 4 (within-cluster ordering)
- At least one cluster has an internal sequence proposal with explicit disconfirming tests.
- Conflicts/alternatives are recorded rather than overwritten.

### Phase 5 (cross-cluster stitching)
- A single end-to-end candidate ordering exists (even if confidence varies).
- Murder/cast ledgers are being updated conservatively (events/roles have falsifiers).

### Phase 6 (convergence and falsification)
- Falsification runs are being logged (what was tested + pass/fail/unclear).
- Remaining doubts are minor/local (not structural) per the phase playbook.

