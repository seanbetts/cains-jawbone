---
name: cjb-wordplay-deletion-detect
version: 2.0
description: Use when an explicit loss/removal cue may license subtracting letters or words.
---

# Targeted detector: deletion

Use only after the extraction anomaly scan identifies a motivated span. The phase playbook owns permissions: detectors flag candidates and never order pages. Read `Templates/wordplay.md` for the shared output contract. Zero candidates is a valid result.

## Mechanism check

Name the source span, removed material and positions, and exact remainder. The deletion indicator must justify the operation; never silently repair spelling afterward.

## Trigger discipline

Context should motivate both what is removed and what the remainder means. Arbitrarily deleting letters until a name appears is not detection.

Keep the exact short span and its V ID, literal reading, transformation and contextual reason. Mechanical validity is separate from interpretive support; output begins tentative. Do not call a clean operation “high confidence” merely because it produces a word or name. Synthesis assesses consequences later.

## Disconfirming check

Removal is unlicensed, consumes letters not present, changes order without support, or requires additional substitutions.

Record the falsifier and a concrete next test in the candidate block. If source research is needed, queue an R item and respect extraction-first and source-admission policy. Do not normalize or correct the protected page body.
