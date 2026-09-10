---
name: cjb-verification
version: 2.0
description: Use when checking source integrity, edited records, exports, or final structural consistency.
---

# Verification

After note edits and before commits, run `python3 Scripts/verify_pages.py`. It checks the archive hash, exactly pages 1–100, one Notes heading per page, and correspondence of each protected page body to the archive. Consult `--help` for diff and whitespace flags. Default comparison may normalize whitespace as documented by the tool; use strict whitespace for the stronger comparison. Neither mode authenticates the original transcription or establishes a correct interpretation. Never change the archive/hash to make a check pass.

Run `python3 Scripts/validate_state.py --root PATH` after structured state changes and before phase reviews. This checks IDs, fields, page references, exact evidence offsets/spans, source metadata, dependencies, worklog shape and accepted constraints. Use `--legacy` for old Markdown state; it does not migrate or semantically certify historical claims. Use `--final` only alongside the playbook's human/agent final review.

On failure, identify the specific invariant and fix only the responsible editable record. Preserve evidence content under each V ID; corrections withdraw it and create a new ID. Suspend dependent claims when evidence is withdrawn or a C/R/S premise is revised. Historical tests remain but cannot validate a changed claim revision. An integrity failure must be resolved before committing, never “fixed” by editing protected text. Validate an export from its own root. Record commands and outcomes within their actual scope; passing checks is not a percent solved.
