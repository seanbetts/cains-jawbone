---
name: cjb-wordplay-charade-detect
version: 1.0
description: Detect candidate charades/segmentations (building a word from parts) and emit CANDIDATE blocks (no interpretation or ordering).
---

# Cain’s Jawbone — Wordplay Detector: Charade / Segmentation

## Purpose
Flag candidate **charade/segmentation** readings where a span can be plausibly split into parts that build a meaningful whole.

## Inputs
- A sentence/clause (default), or a user-specified short span.
- Optional: segmentation indicators (“made of”, “part”, “bit”, “piece”, “compound”) — may be absent.

## Outputs (schema)
Emit one or more `CANDIDATE` blocks:

```text
CANDIDATE
- mechanism: charade
- span: "<exact text span from passage>"
- reading: "<original -> part1 + part2 (+ ...) -> whole>"
- confidence: low|med|high
- rationale: "<one sentence>"
- falsifier: "<one sentence>"
```

## Constraints and guardrails
- Detectors **never** propose page order.
- Keep segmentations minimal (usually 2–3 parts).
- Do not invent parts that aren’t present in the text span.

## Phase usage
- **Phase 1:** run broadly (high recall).
- **Phase 2:** optional targeted rerun on a specified span.
- **Phase 3:** do not run by default.
- **Phase 4+:** rerun only when verifying a dispute/constraint.

## Mechanism definition and indicators
A **charade** builds a solution from smaller pieces (prefix/suffix/word parts) placed side-by-side.

Typical indicators (when signposted): “made of”, “composed of”, “bits of”, “in parts”.

## Detection scope
- Default: a short compound-like token or adjacent pair.
- Prefer spans that look deliberately assembled (hyphenations, odd compounds).

## Confidence rubric
- **high:** parts and whole are clean and context-fitting.
- **med:** plausible build but weak anchoring.
- **low:** segmentation feels arbitrary or yields marginal output.

## Falsifiers (common)
- Requires parts that aren’t in the span.
- Built word/proper noun doesn’t fit grammar/period usage.
- Competing reading is simpler and stronger.

## Examples

### Should trigger
Text: “... the **sun-day** routine ...”

```text
CANDIDATE
- mechanism: charade
- span: "sun-day"
- reading: "sun + day -> Sunday"
- confidence: high
- rationale: "A clean two-part build yields a standard compound with potential calendar relevance."
- falsifier: "If the hyphenation is clearly just line-break punctuation with no other calendar cues."
```

### Should not trigger
Text: “... the **window** was open ...”

- Do not emit a charade candidate by forcing arbitrary splits (“win + dow”).
