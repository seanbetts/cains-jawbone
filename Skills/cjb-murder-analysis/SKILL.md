---
name: cjb-murder-analysis
description: Conservatively analyse likely in-world deaths/violence using motive/means/opportunity and update the cast + murder-confidence ledgers with confidence and falsifiers.
---

# Cain’s Jawbone — Murder Analysis

## Non-negotiables

- Do not assume a murder unless the text supports it.
- Do not edit page body text (only write under `## Notes`).
- Default sequencing is extraction-first: do **not** resolve research items mid-pass; add `open` items to `Indexes/research_queue.md`.

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

#### `Order/cast.md`

For each implicated person (`Pxx`):

- set/update `role candidate` (`murderer` / `victim` / `witness` / `unknown`)
- adjust `confidence` conservatively (small increments/decrements)
- add supporting pages + 1–2 sentence evidence summary
- add falsifiers and set status (`active` / `downgraded` / `rejected`)

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

## Output checklist

- Cast ledger updated (or explicitly “no cast change” if purely allusive)
- Murder confidence ledger updated (or explicitly “no event recorded” if purely allusive)
- Every claim has confidence + falsifiers

