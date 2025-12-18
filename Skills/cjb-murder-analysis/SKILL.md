---
name: cjb-murder-analysis
version: 1.0
description: Conservatively analyse likely in-world deaths/violence using motive/means/opportunity and update the cast + murder-confidence ledgers with confidence and falsifiers.
---

# Cain’s Jawbone — Murder Analysis

## Non-negotiables

- Do not assume a murder unless the text supports it.
- Do not edit page body text (only write under `## Notes`).
- Default sequencing is extraction-first: do **not** resolve research items mid-pass; add `open` items to `Indexes/research_queue.md`.

## Phase gating
- **Allowed phases:** `phase-5` … `phase-6` (primary), `phase-4` (as needed)
- **Exception:** In `phase-1`, use only if harm/death is unmistakable and explicitly in-world.

## Goal

Analyse a page (or a tight cluster) for *in-world* death/violence using classic detective dimensions mapped to textual evidence, then keep our murder/victim/murderer hypotheses explicit, probabilistic, and falsifiable.

## When to use (conservative triggers)

Use this skill when a page likely contains **in-world**:

- a corpse/death (“dead”, “corpse”, “murder committed”, “killed”, burial, “remains”)
- poisoning/illness framed as a planned or suspicious “ending”
- narrator reflection implying an outcome for a character (especially with blame/agency)

If a page only references a **historical/allusive** death (e.g., Francis Ferdinand), do *not* treat it as an in-world murder; route it to quotes/date queues instead.

## Procedure

### 1) Classify the “death” signal

Label as one of:

- `IN-WORLD` — the story-world has a death/attempted killing.
- `HISTORICAL/ALLUSION` — used as a date/reading anchor; not a story-world death.
- `METAPHOR/IDIOM` — “dead” language but no actual death.
- `UNCLEAR` — not enough context yet.

### Quick decision tree (fast triage)

Text mentions death/kill/dead →
- Named historical figure/event? → `HISTORICAL/ALLUSION`
- Idiom/metaphor (“dead tired”, “dead silence”)? → `METAPHOR/IDIOM`
- Story-world person/animal/character affected? →
  - Explicit corpse/burial/killing/attempt? → `IN-WORLD`
  - Only implied/feared/foreshadowed? → `UNCLEAR`

### 2) Extract the murder dimensions (text-evidence only)

Fill what you can; leave unknowns explicit.

- **Victim candidate + profile:** who/what is harmed, why them, vulnerabilities.
- **Motive:** explicit or implied (money, jealousy, obligation, irritation, hierarchy).
- **Means:** objects/substances/access implied by prose (poisons, food/drink, tools, staging).
- **Opportunity:** who is present/absent; time cues; continuity of place.
- **Narrative tells:** self-incrimination, irony, over-precision, slips, misdirection.
- **Confidence + falsifiers:** numeric `0.0–1.0` plus what would disprove it.

If substances/food/drink/medicine are central, run `Skills/cjb-means-and-methods/SKILL.md` first, then return here.

### 3) Update ledgers (required for `IN-WORLD` or `UNCLEAR`)

#### Event ID rules (`Order/confidence.md`)

- `E##` IDs are never reused.
- Create a new event when you believe the text supports a distinct in-world death/attempted killing (even if victim/murderer are `UNKNOWN`).
- Update an existing event when adding pages that clearly describe the *same* death/attempt.

#### `Order/cast.md`

For each implicated person (`Pxx`):

- set/update `role candidate` (`murderer` / `victim` / `witness` / `unknown`)
- adjust `confidence` conservatively (small increments/decrements)
- add supporting pages + 1–2 sentence evidence summary
- add falsifiers and set status (`active` / `downgraded` / `rejected`)
  
Confidence hygiene (recommended):
- Adjust in small steps (usually ±0.05) unless the text is explicit.
- Avoid jumping from low confidence to `CERTAIN` without running falsification checks.

#### `Order/confidence.md`

Create or update an event (`E##`) with:

- pages involved
- victim/murderer candidates (or `UNKNOWN`)
- motive/means/opportunity summary
- confidence + falsifiers + status

### 4) Cross-check indices (only if needed)

- Update `Indexes/people.md` if relationships/aliases/tells become clearer.
- Update `Indexes/objects_motifs.md` for any key means/substances.
- Add any lookups to `Indexes/research_queue.md` as `open` (no resolution yet).

### 5) End with explicit uncertainty

Conclude your write-up with an explicit uncertainty statement, e.g.:

- `UNCERTAIN: in-world death vs allusion`
- `UNCERTAIN: victim identity (unnamed vs Pxx)`
- `UNCERTAIN: means implied vs explicit`

## If classification is not in-world

If you classify the signal as `HISTORICAL/ALLUSION` or `METAPHOR/IDIOM`:
- Do not update `Order/cast.md` or `Order/confidence.md`.
- Record the interpretation under the page’s `## Notes` and/or in `Indexes/quotes.md` / `Indexes/research_queue.md` as appropriate.

## Output checklist

- Cast ledger updated (or explicitly “no cast change” if purely allusive)
- Murder confidence ledger updated (or explicitly “no event recorded” if purely allusive)
- Every claim has confidence + falsifiers
