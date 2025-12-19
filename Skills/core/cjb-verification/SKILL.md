---
name: cjb-verification
version: 1.0
description: Verify Cain’s Jawbone integrity: archive hash check + ensure page body text is unchanged (Notes ignored) using the local verify script.
---

# Cain’s Jawbone — Verification

## What “verified” means here

- `Archive/Cain's Jawbone Unformatted.txt` matches `Archive/hash.txt` (integrity of source).
- For every `Pages/cains_jawbone_page_*.md`, the content *above* `## Notes` matches the corresponding archive page exactly (Notes are ignored).

## Command

Run:

- `python3 Scripts/verify_pages.py`

Useful flags:

- `--show-diff` to print unified diffs for mismatches
- `--strict-whitespace` to also treat trailing whitespace as changes

## Phase gating
- **Allowed phases:** `phase-1` … `phase-6`

## When to use

- After any edits to page notes
- After bulk refactors of index/hypothesis files (sanity check)
- Before sharing/exporting pages
