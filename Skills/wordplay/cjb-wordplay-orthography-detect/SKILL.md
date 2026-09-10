---
name: cjb-wordplay-orthography-detect
version: 2.0
description: Use when spelling, punctuation, capitalization or typography differs from the expected local form.
---

# Targeted detector: orthography

Use only after the extraction anomaly scan identifies a motivated span. The phase playbook owns permissions: detectors flag candidates and never order pages. Read `Templates/wordplay.md` for the shared output contract. Zero candidates is a valid result.

## Mechanism check

Record the exact form and literal possibilities. Compare page to archive for local divergence. If needed, queue comparison with an admitted authoritative edition/image, without altering protected text.

## Trigger discipline

A marked feature may be deliberate, ordinary historical usage, or an archived transcription/OCR error. Archive agreement only proves consistency with this archive, not authenticity.

Keep the exact short span and its V ID, literal reading, transformation and contextual reason. Mechanical validity is separate from interpretive support; output begins tentative. Do not call a clean operation “high confidence” merely because it produces a word or name. Synthesis assesses consequences later.

## Disconfirming check

An authoritative image disagrees, period typography explains the form, or the proposed alternate parsing adds no supported meaning.

Record the falsifier and a concrete next test in the candidate block. If source research is needed, queue an R item and respect extraction-first and source-admission policy. Do not normalize or correct the protected page body.
