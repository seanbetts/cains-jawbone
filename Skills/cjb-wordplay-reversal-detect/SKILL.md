---
name: cjb-wordplay-reversal-detect
version: 1.0
description: Detect candidate reversals (backwards readings) and emit CANDIDATE blocks (no interpretation or ordering).
---

# Cain’s Jawbone — Wordplay Detector: Reversal

## Purpose
Flag candidate **reversals** where a word/phrase may be intended to be read backwards.

## Inputs
- A sentence/clause (default), or a user-specified short span.
- Optional reversal indicators (“back”, “returned”, “reversed”, “from the end”) — may be absent.

## Outputs (schema)
Emit one or more `CANDIDATE` blocks:

```text
CANDIDATE
- mechanism: reversal
- span: "<exact text span from passage>"
- reading: "<original -> reversed reading>"
- confidence: low|med|high
- rationale: "<one sentence>"
- falsifier: "<one sentence>"
```

## Constraints and guardrails
- Detectors **never** propose page order.
- Prefer minimal spans (single words or short tokens).
- Do not “fix” spelling; the reversal itself is the candidate.

## Phase usage
- **Phase 1:** run broadly (high recall).
- **Phase 2:** optional targeted rerun on a specified span.
- **Phase 3:** do not run by default.
- **Phase 4+:** rerun only when verifying a dispute/constraint.

## Mechanism definition and indicators
A **reversal** reads a span backwards (letters, sometimes words).

Typical indicators (when signposted): “back”, “returned”, “reversed”, “from the end”.

## Detection scope
- Default: single word.
- Optional: short hyphenated tokens if they look deliberate.

## Confidence rubric
- **high:** reversal yields a clean, meaningful word/proper noun and plausibly fits.
- **med:** yields something plausible but unclear.
- **low:** yields weak/non-anchoring output.

## Falsifiers (common)
- Output is non-word or only coincidentally “looks like” something.
- Conflicts with local grammar/meaning.

## Examples

### Should trigger
Text: “... **stressed** ...”

```text
CANDIDATE
- mechanism: reversal
- span: "stressed"
- reading: "stressed -> desserts"
- confidence: high
- rationale: "Full reversal yields a clean word with a plausible food/dessert hook."
- falsifier: "If the context is clearly emotional/psychological with no food register at all."
```

### Should not trigger
Text: “... **table** ...”

- Do not emit a candidate if reversal yields a non-word (“elbat”) with no plausible interpretive path.
