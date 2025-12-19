---
name: cjb-wordplay-allusion-detect
version: 1.0
description: Detect candidate allusions/quotations (quote-like spans) and emit CANDIDATE blocks labelled as candidates (no attribution or ordering).
---

# Cain’s Jawbone — Wordplay Detector: Allusion / Quotation Candidate

## Purpose
Flag short spans that look like **candidate quotations/allusions** for later verification via `Skills/research/cjb-quote-research/SKILL.md`.

## Inputs
- A sentence/clause (default), or a user-specified short span.

## Outputs (schema)
Emit one or more `CANDIDATE` blocks:

```text
CANDIDATE
- mechanism: allusion
- span: "<exact text span from passage>"
- reading: "<span -> candidate allusion/quotation (source TBD)>"
- confidence: low|med|high
- rationale: "<one sentence>"
- falsifier: "<one sentence>"
```

## Constraints and guardrails
- Detectors **never** propose page order.
- Output must be **candidate allusion** only (no definitive attribution unless verified elsewhere).
- Keep spans very short (minimum needed to identify).
- Must not invent citations or sources.

## Phase usage
- **Phase 1:** run broadly (high recall) to capture candidates.
- **Phase 2:** optional targeted rerun on a specified span; then hand off to `Skills/research/cjb-quote-research/SKILL.md`.
- **Phase 3:** do not run by default.
- **Phase 4+:** rerun only when verifying a dispute/constraint.

## Mechanism definition and indicators
An **allusion/quotation candidate** is a span that feels “quoted” or externally sourced (unusual phrasing, archaic diction, distinctive rhythm).

Indicators may be absent; look for:
- quotation marks (if present)
- sudden register shifts
- oddly specific phrasing
- biblical/Shakespearean cadence

## Detection scope
- Default: 5–15 words (or the smallest unique fragment).
- Prefer minimal spans that can be searched/verified.

## Confidence rubric
- **high:** span is highly distinctive/quote-like and likely traceable.
- **med:** plausible allusion but could be idiomatic prose.
- **low:** weak signal; capture only if it feels unusually “borrowed”.

## Falsifiers (common)
- Phrase is common idiom/proverb with no specific source.
- Context shows it is plainly the narrator’s own phrasing with no quotation register.
- No match found after targeted research (then mark research item `stalled`, not `resolved`).

## Examples

### Should trigger
Text: “... **the quality of mercy** ...”

```text
CANDIDATE
- mechanism: allusion
- span: "the quality of mercy"
- reading: "the quality of mercy -> candidate allusion/quotation (source TBD)"
- confidence: high
- rationale: "Highly distinctive phrase strongly suggests an external quotation."
- falsifier: "If the phrase recurs as a purely literal descriptor with no traceable source in period texts."
```

### Should not trigger
Text: “... **in the morning** ...”

- Do not emit an allusion candidate for ordinary, non-distinctive prose.
