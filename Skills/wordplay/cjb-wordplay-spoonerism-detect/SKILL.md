---
name: cjb-wordplay-spoonerism-detect
version: 2.0
description: Use when locally odd phrasing motivates a swap of initial sounds.
---

# Targeted detector: spoonerism

Use only after the extraction anomaly scan identifies a motivated span. The phase playbook owns permissions: detectors flag candidates and never order pages. Read `Templates/wordplay.md` for the shared output contract. Zero candidates is a valid result.

## Mechanism check

Identify the two sound onsets being swapped, retain the remaining sounds and show the output. Prefer short adjacent spans; explain any separated-word operation explicitly.

## Trigger discipline

Strained phrasing or an activated alternative may justify the swap. Fluent output alone is not evidence of deliberate wordplay.

Keep the exact short span and its V ID, literal reading, transformation and contextual reason. Mechanical validity is separate from interpretive support; output begins tentative. Do not call a clean operation “high confidence” merely because it produces a word or name. Synthesis assesses consequences later.

## Disconfirming check

The swap needs additional unsupported changes, forced pronunciation, or an alternative with no contextual role.

Record the falsifier and a concrete next test in the candidate block. If source research is needed, queue an R item and respect extraction-first and source-admission policy. Do not normalize or correct the protected page body.
