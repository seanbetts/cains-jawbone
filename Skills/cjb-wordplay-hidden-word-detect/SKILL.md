---
name: cjb-wordplay-hidden-word-detect
version: 1.0
description: Detect candidate hidden words (contiguous substrings across word boundaries) and emit CANDIDATE blocks (no interpretation or ordering).
---

# Cain’s Jawbone — Wordplay Detector: Hidden Word

## Purpose
Flag candidate **hidden-word** extractions (contiguous letter runs inside a short span) for later synthesis.

## Inputs
- A sentence/clause from a page (default), or a user-specified short span.
- Optional: hidden-word indicators (“in”, “within”, “some of”, “concealed”) — may be absent.

## Outputs (schema)
Emit one or more `CANDIDATE` blocks:

```text
CANDIDATE
- mechanism: hidden-word
- span: "<exact text span from passage>"
- reading: "<original -> extracted hidden word>"
- confidence: low|med|high
- rationale: "<one sentence>"
- falsifier: "<one sentence>"
```

## Constraints and guardrails
- Detectors **never** propose page order.
- Prefer minimal spans; do not fabricate letters or skip characters.
- Keep the extracted hidden word contiguous (no acrostics or alternates here).

## Phase usage
- **Phase 1:** run broadly (high recall).
- **Phase 2:** optional targeted rerun on a specified span.
- **Phase 3:** do not run by default.
- **Phase 4+:** rerun only when verifying a specific constraint.

## Mechanism definition and indicators
A **hidden word** is a contiguous sequence of letters that appears *inside* a short span (sometimes across word boundaries).

Typical indicators (when signposted): “in”, “within”, “some of”, “part of”, “concealed”.

## Detection scope
- Default: a short phrase (usually ≤ 3–6 words).
- Prefer spans with unusual breaks/hyphenation that may mask the run.

## Confidence rubric
- **high:** extracted word is a clear dictionary word/proper noun and fits context.
- **med:** plausible extraction but unclear relevance.
- **low:** extraction yields a weak/non-anchoring word.

## Falsifiers (common)
- Requires skipping letters or wrapping around.
- Extracted word is trivial/common and doesn’t fit local grammar/meaning.
- Conflicts with stronger anchors on the page.

## Examples

### Should trigger
Text: “... the t**HE ART**ist ...”

```text
CANDIDATE
- mechanism: hidden-word
- span: "tHE ARTist"
- reading: "tHE ARTist -> HEART"
- confidence: high
- rationale: "Contiguous letters across the boundary form a clean, meaningful word."
- falsifier: "If capitalization is normalised elsewhere and no other hidden-word signals recur."
```

### Should not trigger
Text: “... the **artist** arrived ...”

- Do not emit a candidate just because a short common span happens to contain small substrings.
