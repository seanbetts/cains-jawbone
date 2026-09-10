---
name: cjb-wordplay-anagram-detect
version: 2.0
description: Use when a locally motivated rearrangement of letters may explain marked wording.
---

# Targeted detector: anagram

Use only after the extraction anomaly scan identifies a motivated span. The phase playbook owns permissions: detectors flag candidates and never order pages. Read `Templates/wordplay.md` for the shared output contract. Zero candidates is a valid result.

## Mechanism check

Compare the complete letter multiset of the short source span and proposed output, stating treatment of spaces/punctuation and case. Every letter must be accounted for; do not silently add, remove or substitute characters.

## Trigger discipline

A rearrangement cue, strained phrase or contextual ambiguity motivates the span. Ordinary words often have anagrams; mechanical possibility alone is not a clue.

Keep the exact short span and its V ID, literal reading, transformation and contextual reason. Mechanical validity is separate from interpretive support; output begins tentative. Do not call a clean operation “high confidence” merely because it produces a word or name. Synthesis assesses consequences later.

## Disconfirming check

The transformation has unmatched letters, or the literal reading explains the marked context without the proposed rearrangement.

Record the falsifier and a concrete next test in the candidate block. If source research is needed, queue an R item and respect extraction-first and source-admission policy. Do not normalize or correct the protected page body.
