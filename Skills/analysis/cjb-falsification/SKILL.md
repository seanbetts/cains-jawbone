---
name: cjb-falsification
version: 1.1
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

## Anchor rubric (for ordering joins)

Treat a join as “real” only when it has **2+ independent anchors**. Independence means the anchors are not just the same phrase repeated.

Common anchor types:

- **Time:** day/date/saint/book-day, meal sequence, “yesterday/tomorrow”, season/weather shifts.
- **Place/route:** explicit venue, travel constraint, arrival/departure continuity.
- **Narrator signature:** stable voice tells, profession knowledge, recurring obsessions.
- **Object/prop:** letter/weapon/pills/pet/food/drink continues across the boundary.
- **Quote/allusion:** the same source used in a progressive/echoing way (best when research-resolved).
- **Lexical overlap:** rare phrase/tokens. Useful, but **not sufficient alone** unless paired with another anchor type.

## Procedure

1. Pick a single claim to test (keep scope tight; 1 join or 1 event).
2. Write 2–5 explicit predictions implied by the claim (what *must* be true if the claim holds), e.g.:
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

## Phase 6 join-work loop (to avoid “circling”)

When Phase 6 stalls on weak/zero-anchor boundaries, prefer **doing one real restitch experiment** over accumulating more lexical-only leads.

1. **Triage:** in `Order/hypotheses.md`, maintain a short list of the worst joins (especially “zero-anchor” boundaries).
2. **Upgrade or break:** for one boundary, attempt to either:
   - add a second independent anchor (upgrade from lexical-only), or
   - downgrade it to `FAIL` with a recorded contradiction (make room for replacements).
3. **Replacement leads:** if a boundary fails, record 1–3 replacement predecessor/successor leads, but only promote a lead to a tested join if it has 2+ independent anchors.
4. **Minimal trial restitch:** when testing a replacement, evaluate the *two* surrounding joins as well (don’t just move the problem one page over).
5. **Adoption rule:** only adopt a restitch if it reduces the count of zero-anchor joins without introducing a new hard contradiction elsewhere; otherwise keep it as a marked alternative.

## When to step back (with explicit user approval)

If you repeatedly can’t find second anchors (you’re collecting lexical-only leads across many boundaries), it often means the issue is **structural** (cluster/narrator mix-up or unresolved external anchor). In that case:

- Propose a short **Phase 3 micro-pass** (narrator profiling for the pages around the worst joins), or
- Propose a short **Phase 2 micro-pass** (targeted research for the specific unresolved anchor items that would decide between competing joins).

Phase changes require explicit user instruction; record any approved phase shift in `Worklog/current_run.txt` and in the session row in `Worklog/worklog.csv`.

## Output checklist

- `Order/hypotheses.md` updated with the test, outcome (`PASS/FAIL/UNCLEAR`), and explicit falsifier(s)
- Any impacted ledger entries updated (`Order/cast.md`, `Order/confidence.md`)
