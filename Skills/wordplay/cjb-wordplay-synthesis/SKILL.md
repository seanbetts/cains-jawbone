---
name: cjb-wordplay-synthesis
version: 1.0
description: Rank and interpret detector candidates in context; emit 1–3 LIKELY WORDPLAY blocks and route researchable items into the research queue (no final ordering).
---

# Cain’s Jawbone — Wordplay Synthesis

## Purpose
Take high-recall detector candidates and produce low-noise, context-aware `LIKELY WORDPLAY` findings that explain **why they matter** (without asserting final ordering).

## Inputs
- One page’s set of `CANDIDATE` blocks (from detector skills) under that page’s `## Notes`.
- Optional: a specific span to re-run a detector tightly (Phase 2 only).
- Nearby context from the same page: entity/time/place/quote/motif notes.

## Outputs (schema)
Emit the best **1 to 3** `LIKELY WORDPLAY` blocks:

```text
LIKELY WORDPLAY
- mechanism(s): <one or more>
- span: "<exact text span>"
- best reading: "<best interpretation>"
- confidence: low|med|high
- why it matters: <ordering|narrator|place|date|motif> -> <one sentence>
- falsifiers:
  - "<one>"
  - "<optional second>"
```

## Constraints and guardrails
- Must reference detector candidates explicitly (e.g., “From CANDIDATE(spoonerism): ...”) in `best reading`.
- Must not invent citations or sources. If it suggests a quotation, label it “candidate quote” until verified.
- May say “this might be useful for ordering”, but must not claim final ordering.
- Prefer 1–3 high-signal items over many weak ones.

## Phase usage
- **Phase 1:** do not run (detectors only).
- **Phase 2:** primary (interpret locally + create targeted research tasks).
- **Phase 3:** primary (use as clustering/linkage feature; low noise).
- **Phase 4+:** rerun only when resolving a dispute or verifying a constraint.

## Procedure

1. Collect all detector `CANDIDATE` blocks for the page.
2. De-duplicate overlapping spans and collapse near-identical readings.
3. Rank candidates:
   - prefer clean transformations producing valid words/proper nouns
   - prefer candidates that align with other page anchors (people/place/date/motif/voice)
   - deprioritise candidates that require forced pronunciation or long spans
4. Select the best 1–3 and emit `LIKELY WORDPLAY` blocks under the page’s `## Notes` (Wordplay section).
5. Copy the same `LIKELY WORDPLAY` blocks into `Indexes/wordplay.md` under the page entry.
6. If the best reading implies a **candidate quote/place/date**, create (or update) a targeted item in `Indexes/research_queue.md` (Phase 2) and/or the relevant index once verified.

## Examples

### Should trigger (synthesis selects best)
Inputs on a page (detectors already ran):

```text
CANDIDATE
- mechanism: spoonerism
- span: "queer old dean"
- reading: "queer old dean -> dear old queen"
- confidence: high
- rationale: "Clean initial-sound swap yields a fluent phrase."
- falsifier: "Local context requires a clergyman, not a monarch."

CANDIDATE
- mechanism: reversal
- span: "table"
- reading: "table -> elbat"
- confidence: low
- rationale: "Reversal is mechanically possible."
- falsifier: "Produces a non-word."
```

Output:

```text
LIKELY WORDPLAY
- mechanism(s): spoonerism
- span: "queer old dean"
- best reading: "From CANDIDATE(spoonerism): queer old dean -> dear old queen"
- confidence: high
- why it matters: narrator -> "A distinctive, playful transposition may be a stable voice tell if it recurs across pages."
- falsifiers:
  - "No recurrence of similar spoonerism behaviour in other pages by this narrator candidate."
  - "Context makes the literal reading unavoidable."
```

### Should not trigger (synthesis declines weak candidates)
If all detector candidates are low-confidence and unanchored, emit no `LIKELY WORDPLAY` blocks and leave the page’s wordplay section empty (or explicitly note “no high-signal wordplay after synthesis”).
