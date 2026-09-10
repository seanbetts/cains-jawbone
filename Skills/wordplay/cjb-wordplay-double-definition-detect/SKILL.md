---
name: cjb-wordplay-double-definition-detect
version: 2.0
description: Use when local context appears to activate two senses of the same word.
---

# Targeted detector: double-definition

Use only after the extraction anomaly scan identifies a motivated span. The phase playbook owns permissions: detectors flag candidates and never order pages. Read `Templates/wordplay.md` for the shared output contract. Zero candidates is a valid result.

## Mechanism check

State both meanings and the distinct context that activates each. Check grammar and historically appropriate usage; definitions alone are insufficient.

## Trigger discipline

Both senses need a role in the passage. “He struck a match” by itself does not activate a contest merely because the dictionary lists that sense.

Keep the exact short span and its V ID, literal reading, transformation and contextual reason. Mechanical validity is separate from interpretive support; output begins tentative. Do not call a clean operation “high confidence” merely because it produces a word or name. Synthesis assesses consequences later.

## Disconfirming check

Only one sense is grammatically/contextually viable, or the second requires unsupported modern slang.

Record the falsifier and a concrete next test in the candidate block. If source research is needed, queue an R item and respect extraction-first and source-admission policy. Do not normalize or correct the protected page body.
