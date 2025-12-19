---
name: cjb-wordplay-anagram-detect
version: 1.0
description: Detect candidate anagrams in minimal spans and emit CANDIDATE blocks (no interpretation or ordering).
---

# Cain’s Jawbone — Wordplay Detector: Anagram

## Purpose
Flag candidate **anagram** transformations so synthesis can judge whether they matter (and where).

## Inputs
- A sentence/clause from a page (default), or a user-specified short span.
- Optional: anagram indicators (“mixed”, “oddly”, “rearranged”) — note Cain’s Jawbone may be un-signposted.

## Outputs (schema)
Emit one or more `CANDIDATE` blocks:

```text
CANDIDATE
- mechanism: anagram
- span: "<exact text span from passage>"
- reading: "<original -> transformed candidate>"
- confidence: low|med|high
- rationale: "<one sentence>"
- falsifier: "<one sentence>"
```

## Constraints and guardrails
- Detectors **never** propose page order.
- Keep `span` verbatim and short; do not reflow or “correct” page text.
- `reading` must show the transformation clearly (no hidden steps).
- Do not assert identities/sources; produce candidates only.

## Phase usage
- **Phase 1:** run broadly (high recall); accept false positives.
- **Phase 2:** optional, only on a specific span when synthesis needs more candidates.
- **Phase 3:** do not run by default (prefer synthesis outputs only).
- **Phase 4+:** rerun only to resolve a specific dispute/constraint.

## Mechanism definition and indicators
An **anagram** rearranges the letters of a word/phrase to form another word/phrase.

Typical indicators (when signposted): “mixed”, “oddly”, “confused”, “in disorder”, “rearranged”.

## Detection scope
- Default: a single word or a 2–3 word chunk (avoid very long spans).
- Prefer spans that look “name-like” (capitalised, title-like) or oddly chosen.

## Confidence rubric
- **high:** rearrangement yields a clearly valid word/proper noun and fits local context.
- **med:** yields something plausible but not clearly anchored.
- **low:** technically possible but weak plausibility (or requires forcing spelling).

## Falsifiers (common)
- Result needs added/dropped letters, or produces non-words.
- Requires modern spelling/meaning without support.
- Conflicts with established anchors on the page.

## Examples

### Should trigger
Text: “... a **silent** pause ...”

```text
CANDIDATE
- mechanism: anagram
- span: "silent"
- reading: "silent -> listen"
- confidence: high
- rationale: "Simple rearrangement yields a clean word that matches a listening/hearing context."
- falsifier: "If surrounding context makes 'silent' purely literal and no other wordplay signals recur."
```

### Should not trigger
Text: “... the **garden gate** ...”

- Do not emit a candidate if no span is unusually chosen and transformations would be arbitrary.
