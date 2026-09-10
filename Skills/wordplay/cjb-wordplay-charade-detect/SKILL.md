---
name: cjb-wordplay-charade-detect
version: 2.0
description: Use when marked segmentation or a composite phrase may combine meaningful parts.
---

# Targeted detector: charade

Use only after the extraction anomaly scan identifies a motivated span. The phase playbook owns permissions: detectors flag candidates and never order pages. Read `Templates/wordplay.md` for the shared output contract. Zero candidates is a valid result.

## Mechanism check

Show the exact segmentation and reading of each part, then their ordered combination. Explain each phonetic or semantic step separately.

## Trigger discipline

A local compositional cue or meaningful alternate parsing must motivate the split; do not search every possible segmentation.

Keep the exact short span and its V ID, literal reading, transformation and contextual reason. Mechanical validity is separate from interpretive support; output begins tentative. Do not call a clean operation “high confidence” merely because it produces a word or name. Synthesis assesses consequences later.

## Disconfirming check

Any part lacks contextual support, the split is arbitrary, or the final meaning requires unexplained transformations.

Record the falsifier and a concrete next test in the candidate block. If source research is needed, queue an R item and respect extraction-first and source-admission policy. Do not normalize or correct the protected page body.
