---
name: cjb-wordplay-double-definition-detect
version: 1.0
description: Detect candidate double definitions (one span plausibly cluing two meanings) and emit CANDIDATE blocks (no interpretation or ordering).
---

# Cain’s Jawbone — Wordplay Detector: Double Definition

## Purpose
Flag candidate **double definitions** where a single word/phrase appears intentionally ambiguous across two senses.

## Inputs
- A sentence/clause (default), or a user-specified short span.
- Context is required: this detector relies on local ambiguity cues.

## Outputs (schema)
Emit one or more `CANDIDATE` blocks:

```text
CANDIDATE
- mechanism: double-definition
- span: "<exact text span from passage>"
- reading: "<definition A / definition B>"
- confidence: low|med|high
- rationale: "<one sentence>"
- falsifier: "<one sentence>"
```

## Constraints and guardrails
- Detectors **never** propose page order.
- Do not over-trigger: require at least a plausible second sense in the immediate context.
- Keep both senses concise in `reading`.

## Phase usage
- **Phase 1:** run broadly but cautiously (high recall, low precision).
- **Phase 2:** optional targeted rerun on a specified span.
- **Phase 3:** do not run by default.
- **Phase 4+:** rerun only when verifying a dispute/constraint.

## Mechanism definition and indicators
A **double definition** intentionally uses a single span to invoke two meanings.

Often un-signposted; look for local cues that activate both senses.

## Detection scope
- Default: single word.
- Prefer “pivot words” that can reasonably support two senses.

## Confidence rubric
- **high:** both senses are strongly supported by local context.
- **med:** second sense plausible but weak.
- **low:** second sense speculative.

## Falsifiers (common)
- Only one sense is grammatically viable.
- Second sense relies on modern slang/usage without support.
- A different wordplay mechanism explains it better.

## Examples

### Should trigger
Text: “... he struck a **match** ...”

```text
CANDIDATE
- mechanism: double-definition
- span: "match"
- reading: "match (stick) / match (contest)"
- confidence: med
- rationale: "The local context can plausibly evoke both the object and the idea of contest/likeness."
- falsifier: "If the sentence strictly describes ignition with no competing sense activated."
```

### Should not trigger
Text: “... he ate an **apple** ...”

- Do not emit a double-definition candidate when only one ordinary sense is present.
