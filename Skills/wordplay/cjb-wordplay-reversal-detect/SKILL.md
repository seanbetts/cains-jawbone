---
name: cjb-wordplay-reversal-detect
version: 2.0
description: Use when a backward-reading cue or marked short span suggests reversal.
---

# Targeted detector: reversal

Use only after the extraction anomaly scan identifies a motivated span. The phase playbook owns permissions: detectors flag candidates and never order pages. Read `Templates/wordplay.md` for the shared output contract. Zero candidates is a valid result.

## Mechanism check

Specify whether letters or words reverse and show the exact operation, including normalization. A reversal must account for the entire chosen span.

## Trigger discipline

A reversal cue plus relevant alternate reading motivates inspection. A familiar reversible pair in unmarked prose is not enough.

Keep the exact short span and its V ID, literal reading, transformation and contextual reason. Mechanical validity is separate from interpretive support; output begins tentative. Do not call a clean operation “high confidence” merely because it produces a word or name. Synthesis assesses consequences later.

## Disconfirming check

The output is forced, the span arbitrary, or the literal reading fully accounts for the supposed cue.

Record the falsifier and a concrete next test in the candidate block. If source research is needed, queue an R item and respect extraction-first and source-admission policy. Do not normalize or correct the protected page body.
