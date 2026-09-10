---
name: cjb-wordplay-hidden-word-detect
version: 2.0
description: Use when marked boundaries suggest a contiguous hidden word.
---

# Targeted detector: hidden-word

Use only after the extraction anomaly scan identifies a motivated span. The phase playbook owns permissions: detectors flag candidates and never order pages. Read `Templates/wordplay.md` for the shared output contract. Zero candidates is a valid result.

## Mechanism check

Identify the exact contiguous substring and its boundaries. State any removal of spaces/punctuation; do not skip interior letters, wrap around or switch to an acrostic.

## Trigger discipline

An inclusion cue, conspicuous segmentation or locally meaningful hidden reading motivates inspection. Short common substrings in normal prose are expected coincidences.

Keep the exact short span and its V ID, literal reading, transformation and contextual reason. Mechanical validity is separate from interpretive support; output begins tentative. Do not call a clean operation “high confidence” merely because it produces a word or name. Synthesis assesses consequences later.

## Disconfirming check

The extraction skips letters, has arbitrary boundaries, or has no explanatory advantage over the literal wording.

Record the falsifier and a concrete next test in the candidate block. If source research is needed, queue an R item and respect extraction-first and source-admission policy. Do not normalize or correct the protected page body.
