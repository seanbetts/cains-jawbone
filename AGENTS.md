# Cain’s Jawbone workspace instructions

This is a literary puzzle notebook. Work from textual evidence to test identities and ordering; do not attempt permutation or brute-force solving.

## Entry and authority

1. Capture UTC start time before opening workspace files; use `Skills/core/cjb-time-logging/SKILL.md` at session start/end.
2. Read `Worklog/current_run.txt` and follow `Skills/core/cjb-run-management/SKILL.md`. Continue its branch; never solve on `main`.
3. Declare the active phase before puzzle work. For infrastructure-only work declare **administrative review** and retain the existing puzzle phase. Permissions, transitions, and exit gates have one authoritative home: `Skills/core/cjb-phase-playbook/SKILL.md`.
4. Read the skill relevant to the task. Schemas and evidence/status conventions have one authoritative home: `Templates/SCHEMA.md`. The older `Indexes/SCHEMA.md` documents legacy files only.

Explicit user instructions take precedence over repository guidance. Within repository guidance, this file governs protections, the phase playbook governs permissions, and the schema governs records; task skills supply procedures. Report a genuine unresolved conflict instead of silently weakening a protection.

## Protections

- Never modify `Archive/`.
- In `Pages/cains_jawbone_page_*.md`, edit only beneath the single `## Notes` heading. Preserve everything above it, including punctuation and formatting.
- Run `python3 Scripts/verify_pages.py` after note batches and before commits; `OK` establishes integrity relative to the archive, not transcription authenticity or a correct solution.
- Preserve unrelated work. Inspect hooks before committing or integrating; use small scoped commits. Merge, push, and deployment require user authorization. Run integration uses `Skills/core/cjb-merge-to-main/SKILL.md`.
- Never import or reproduce remembered or published solutions, solved page orders, or murderer/victim lists unless the user explicitly requests spoilers. Derive claims from permitted evidence.
- Research only queued questions, using admitted sources containing material published by 1934. Admission and host/transcription rules are in the phase playbook. Keep quotation fragments minimal.

## Output and restart

The answer belongs only in `FINAL_SOLUTION.md`, answers only, when the final gate passes. Working partial orders belong in the state ledgers; do not create alternative solution files or drafts. Treat the solution file as write-once unless explicitly authorized to revise. Its commit must change no other file.

For an independent restart, use `Scripts/prepare_fresh_run.py` and the run-management skill. A new branch of populated puzzle state is not an independent baseline. Keep earlier progress outside the fresh solver’s workspace and start a new task/context. Infrastructure review is not authorization to begin solving or create that task.
