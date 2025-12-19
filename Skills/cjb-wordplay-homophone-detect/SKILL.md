---
name: cjb-wordplay-homophone-detect
version: 1.0
description: Detect candidate homophones (sound-alikes) and emit CANDIDATE blocks (no interpretation or ordering).
---

# Cain’s Jawbone — Wordplay Detector: Homophone

## Purpose
Flag candidate **homophone** readings where a spoken-sound substitution may be intended.

## Inputs
- A sentence/clause (default), or a user-specified short span.
- Optional: “sound” indicators (“heard”, “said”, “sounds like”, “in my ear”) — may be absent.

## Outputs (schema)
Emit one or more `CANDIDATE` blocks:

```text
CANDIDATE
- mechanism: homophone
- span: "<exact text span from passage>"
- reading: "<original -> homophonic reading>"
- confidence: low|med|high
- rationale: "<one sentence>"
- falsifier: "<one sentence>"
```

## Constraints and guardrails
- Detectors **never** propose page order.
- Avoid stretching pronunciation; prefer period-plausible sound-alikes.
- Do not “solve” to a named person/place as fact; keep it as a candidate.

## Phase usage
- **Phase 1:** run broadly (high recall).
- **Phase 2:** optional targeted rerun on a specified span.
- **Phase 3:** do not run by default.
- **Phase 4+:** rerun only when verifying a dispute/constraint.

## Mechanism definition and indicators
A **homophone** is a sound-alike substitution (word/phrase that sounds like another).

Typical indicators (when signposted): “heard”, “said”, “by ear”, “sounds like”.

## Detection scope
- Default: single word or short phrase.
- Prefer spans that become a meaningful alternative reading when “heard aloud”.

## Confidence rubric
- **high:** the sound-alike is very close and yields a clear, context-fitting word/proper noun.
- **med:** plausible sound-alike but weak anchoring.
- **low:** requires forcing or produces an unlikely word.

## Falsifiers (common)
- Requires implausible pronunciation shifts without support.
- Produces a reading that breaks grammar/period usage.
- A literal reading fits perfectly with no other wordplay cues.

## Examples

### Should trigger
Text: “... he spoke of a **knight** ...”

```text
CANDIDATE
- mechanism: homophone
- span: "knight"
- reading: "knight -> night"
- confidence: med
- rationale: "The sound-alike produces a plausible alternate reading that could change temporal emphasis."
- falsifier: "If the surrounding clause clearly requires the chivalric sense (armour, heraldry, etc.)."
```

### Should not trigger
Text: “... a **book** on the table ...”

- Do not emit a candidate when no plausible sound-alike changes meaning in a useful way.
