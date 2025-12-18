---
name: cjb-wordplay-deletion-detect
version: 1.0
description: Detect candidate deletions/subtractions (headless/tailless/heartless, etc.) and emit CANDIDATE blocks (no interpretation or ordering).
---

# Cain’s Jawbone — Wordplay Detector: Deletion / Subtraction

## Purpose
Flag candidate **deletions/subtractions** (headless/tailless/heartless, etc.) where removing letters yields a meaningful result.

## Inputs
- A sentence/clause (default), or a user-specified short span.
- Optional indicators (“headless”, “heartless”, “endless”, “without”, “lacking”) — may be absent.

## Outputs (schema)
Emit one or more `CANDIDATE` blocks:

```text
CANDIDATE
- mechanism: deletion
- span: "<exact text span from passage>"
- reading: "<original -> after deletion/subtraction>"
- confidence: low|med|high
- rationale: "<one sentence>"
- falsifier: "<one sentence>"
```

## Constraints and guardrails
- Detectors **never** propose page order.
- Prefer explicit/nearby indicators; if un-signposted, keep confidence low unless result is very strong.
- Specify the deletion in `reading` (e.g., “headless”, “heartless”).

## Phase usage
- **Phase 1:** run broadly (high recall).
- **Phase 2:** optional targeted rerun on a specified span.
- **Phase 3:** do not run by default.
- **Phase 4+:** rerun only when verifying a dispute/constraint.

## Mechanism definition and indicators
**Deletion/subtraction** removes letters (front/back/middle) from a span to reveal another word.

Typical indicators (when signposted): “headless”, “tailless”, “endless”, “heartless”, “without”.

## Detection scope
- Default: a single token.
- Keep the rule simple (drop first letter, last letter, middle letter(s)).

## Confidence rubric
- **high:** deletion yields a clean word/proper noun and the deletion rule is plausible in-context.
- **med:** plausible output but weak anchoring.
- **low:** output is marginal or rule feels arbitrary.

## Falsifiers (common)
- Requires an ad-hoc deletion rule not supported by indicators.
- Produces non-words or anachronistic slang/usage.
- Local context strongly supports literal reading only.

## Examples

### Should trigger
Text: “... **headless plane** ...”

```text
CANDIDATE
- mechanism: deletion
- span: "plane"
- reading: "plane (headless) -> lane"
- confidence: med
- rationale: "A simple headless deletion yields a valid word that could shift meaning."
- falsifier: "If there is no deletion indicator nearby and 'plane' is clearly literal (aviation/woodworking)."
```

### Should not trigger
Text: “... **green** ...”

- Do not emit a deletion candidate just because removing letters yields a shorter fragment (“reen”) that is not meaningful.
