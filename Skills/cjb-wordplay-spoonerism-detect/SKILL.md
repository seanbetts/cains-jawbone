---
name: cjb-wordplay-spoonerism-detect
version: 1.0
description: Detect candidate spoonerisms (initial sound swaps, usually adjacent words) and emit CANDIDATE blocks (no interpretation or ordering).
---

# Cain’s Jawbone — Wordplay Detector: Spoonerism

## Purpose
Flag candidate **spoonerisms** (phonetic transpositions) that may conceal names/places/titles.

## Inputs
- A sentence/clause (default), or a user-specified short span.
- Spoonerisms are often un-signposted; prioritize adjacent word pairs first.

## Outputs (schema)
Emit one or more `CANDIDATE` blocks:

```text
CANDIDATE
- mechanism: spoonerism
- span: "<exact text span from passage>"
- reading: "<original -> spoonerised reading>"
- confidence: low|med|high
- rationale: "<one sentence>"
- falsifier: "<one sentence>"
```

## Constraints and guardrails
- Detectors **never** propose page order.
- Operate on **adjacent word pairs first**; avoid complex multi-word swaps.
- Deprioritise candidates that require stretching pronunciation.

## Phase usage
- **Phase 1:** run broadly (high recall).
- **Phase 2:** optional targeted rerun on a specified span.
- **Phase 3:** do not run by default.
- **Phase 4+:** rerun only when verifying a dispute/constraint.

## Mechanism definition and indicators
A **spoonerism** swaps initial consonant clusters (or initial sounds) between nearby words.

Indicators are often absent; sometimes phrasing is deliberately “off”.

## Detection scope
- Default: adjacent word pairs.
- Optional: short adjacent triples only if strongly signposted by weirdness.

## Confidence rubric
- **high:** swap yields clear words/proper nouns (especially name/place/title-like) and fits context.
- **med:** yields plausible words but weak anchoring.
- **low:** produces awkward/non-words or needs forced phonetics.

## Falsifiers (common)
- Output requires implausible pronunciation.
- Output produces non-words or breaks grammar.
- No corroboration across pages (and no other anchors on the page).

## Examples

### Should trigger
Text: “... a **queer old dean** ...”

```text
CANDIDATE
- mechanism: spoonerism
- span: "queer old dean"
- reading: "queer old dean -> dear old queen"
- confidence: high
- rationale: "Clean initial-sound swap yields a fluent, meaningful phrase."
- falsifier: "If the local context explicitly requires a clergyman (dean) and 'queen' is irrelevant."
```

### Should not trigger
Text: “... a **red old door** ...”

- Do not emit a candidate if swapping initials yields gibberish or only trivial changes.
