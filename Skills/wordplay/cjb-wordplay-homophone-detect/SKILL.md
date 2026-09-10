---
name: cjb-wordplay-homophone-detect
version: 2.0
description: Use when a sound cue or local ambiguity motivates a sound-alike reading.
---

# Targeted detector: homophone

Use only after the extraction anomaly scan identifies a motivated span. The phase playbook owns permissions: detectors flag candidates and never order pages. Read `Templates/wordplay.md` for the shared output contract. Zero candidates is a valid result.

## Mechanism check

Write the spoken forms and the candidate substitution. State period-plausible pronunciation or accent assumptions; do not stretch sounds silently.

## Trigger discipline

A hearing/speaking cue or simultaneous sound-based ambiguity is relevant. The mere existence of a homophone is insufficient.

Keep the exact short span and its V ID, literal reading, transformation and contextual reason. Mechanical validity is separate from interpretive support; output begins tentative. Do not call a clean operation “high confidence” merely because it produces a word or name. Synthesis assesses consequences later.

## Disconfirming check

Required pronunciation is implausible for the period/context, or grammar and context support only the ordinary sense.

Record the falsifier and a concrete next test in the candidate block. If source research is needed, queue an R item and respect extraction-first and source-admission policy. Do not normalize or correct the protected page body.
