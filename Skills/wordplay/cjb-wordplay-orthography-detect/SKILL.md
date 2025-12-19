---
name: cjb-wordplay-orthography-detect
version: 1.0
description: Detect orthographic/typographic oddities (spelling, hyphenation, capitalization, punctuation) and emit CANDIDATE blocks (no interpretation or ordering).
---

# Cain’s Jawbone — Wordplay Detector: Orthography / Typography

## Purpose
Flag **orthographic/typographic** anomalies that may be deliberate (or may be transcription artifacts) so they can be evaluated carefully.

## Inputs
- A sentence/clause (default), or a user-specified short span.

## Outputs (schema)
Emit one or more `CANDIDATE` blocks:

```text
CANDIDATE
- mechanism: orthography
- span: "<exact text span from passage>"
- reading: "<original -> candidate normalisation or alternate parsing>"
- confidence: low|med|high
- rationale: "<one sentence>"
- falsifier: "<one sentence>"
```

## Constraints and guardrails
- Detectors **never** propose page order.
- Never change page body text; only record candidates in Notes.
- Treat “corrections” as hypotheses: some oddities may be intentional.

## Phase usage
- **Phase 1:** flag broadly (high recall) but keep confidence conservative.
- **Phase 2:** optional targeted rerun to support a specific research/interpretation question.
- **Phase 3:** do not run by default.
- **Phase 4+:** rerun only when verifying a dispute/constraint.

## Mechanism definition and indicators
**Orthography/typography** covers anomalies like:
- unusual hyphenation or line-break joins
- archaic spellings
- odd capitalization
- suspicious punctuation breaks

These may signal hidden-word boundaries, segmentation, or deliberate emphasis.

## Detection scope
- Default: the smallest span that contains the anomaly.
- Prefer minimal, exact spans (don’t quote a full sentence).

## Confidence rubric
- **high:** anomaly is strongly suggestive (repeats across pages, or directly enables another clean mechanism).
- **med:** anomaly plausibly meaningful but unconfirmed.
- **low:** could be incidental or purely stylistic.

## Falsifiers (common)
- The same “oddity” appears as a normal stylistic habit across many pages (voice tell, not puzzle).
- Normalising it removes a known anchor elsewhere.
- Archive verification confirms the “oddity” is part of the source text (so not a transcription error).

## Examples

### Should trigger
Text: “... **re-search** ...”

```text
CANDIDATE
- mechanism: orthography
- span: "re-search"
- reading: "re-search -> research (alternate parsing)"
- confidence: med
- rationale: "Hyphenation may be a deliberate segmentation cue that changes how the token is read."
- falsifier: "If hyphenation is consistent typographic style on this page/voice with no other wordplay reinforcement."
```

### Should not trigger
Text: “... **Mr. Smith** ...”

- Do not emit a candidate for ordinary punctuation that does not change parsing or meaning.
