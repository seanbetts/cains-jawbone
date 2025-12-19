---
name: cjb-falsification
version: 1.0
description: Systematically try to break ordering/clustering/murder hypotheses; record tests performed and downgrade/reject when contradictions appear.
---

# Cain’s Jawbone — Falsification

## Non-negotiables

- No brute force ordering.
- Prefer concrete tests over story explanation.
- Record both the test and the outcome (pass/fail/unclear).

## Phase gating

- **Allowed phases:** `phase-6` (primary)
- **Not allowed phases:** `phase-1` … `phase-5` (unless the user explicitly instructs otherwise)

## Inputs (what you falsify)

- A cluster, sequence, or join in `Order/hypotheses.md`
- A murder event hypothesis in `Order/confidence.md`
- A role claim in `Order/cast.md`

## Procedure

1. Pick a single claim to test (keep scope tight).
2. Write 2–5 explicit predictions implied by the claim, e.g.:
   - time continuity (“yesterday/tomorrow”, meals, saint/day anchors)
   - place continuity (route constraints, venues, travel time)
   - narrator continuity (voice tells, recurring obsessions)
   - object continuity (letters, weapons, poisons, pets)
3. Actively search for contradictions:
   - re-read the candidate transition pages
   - cross-check indices (`Indexes/people.md`, `Indexes/places.md`, `Indexes/quotes.md`, `Indexes/objects_motifs.md`, `Indexes/narrators.md`)
4. Record outcome:
   - **Fail:** downgrade or reject the claim; record the contradiction and any revised alternative.
   - **Pass:** upgrade confidence slightly; record what was checked.
   - **Unclear:** keep confidence the same and record what evidence is missing.

## Output checklist

- `Order/hypotheses.md` updated with “Disconfirming evidence” and test outcome
- Any impacted ledger entries updated (`Order/cast.md`, `Order/confidence.md`)
