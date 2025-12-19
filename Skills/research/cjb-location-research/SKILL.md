---
name: cjb-location-research
version: 1.0
description: Use the Highways & Byways guidebook series to ground geographic/location references from Cain's Jawbone pages and update indices.
---

# Location research (Highways & Byways)

## Purpose
Identify real English/Scottish/Irish locations described in the text using the Highways & Byways travel guides available circa 1934.

## When to use
- Any time a page references towns, roads, regions, landmarks, or descriptive travel passages.
- When imagery or diction matches known Highways & Byways descriptions (e.g., parish churches, seaside promenades).

## Phase gating
- **Allowed phases:** `phase-2` (primary), `phase-3` … `phase-6` (as needed)

## Procedure
1. Capture the minimal location quote in the page’s Notes.
2. Search the appropriate Highways & Byways volume (pre-1934 editions only).
3. Confirm whether the description matches; note page/volume if possible.
4. Update:
   - `Indexes/places.md` with place name, description, confidence, supporting Highways & Byways citation.
   - `Indexes/research_queue.md` if the lookup is pending or inconclusive.
5. Use consistent phrasing for citations: `Highways & Byways in [Region] (Year), p. X`.

## Output format
- Page notes: `LIKELY: Location resembles [Place] per Highways & Byways in [Region], p. X`.
- Index entry: include references and any ordering implications (e.g., travel route continuity).

## If no match is found

- Mark the research queue item as `stalled`, record which volumes/regions you checked, and keep alternative interpretations explicit (metaphor vs real place, variant spelling, fictional locale).
