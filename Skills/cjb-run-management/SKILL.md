---
name: cjb-run-management
description: Manage long-lived run branches via Worklog/current_run.txt so end-to-end workstreams are isolated, logged, and mergeable.
---

# Run management

## Purpose
Keep exploratory work isolated per end-to-end workstream (“run”), with clear provenance and easy rollback.

## Definitions

- **Session:** a single working block that gets a `start/end/minutes` row in `Worklog/worklog.csv`.
- **Run:** a long-lived branch for a coherent goal (e.g., first full extraction pass) that may span multiple sessions/days.

## Files/tools
- `Worklog/current_run.txt` — stores the currently active run metadata (blank means no active run)
- `Worklog/worklog.csv` — overall time log (see `Skills/cjb-time-logging/SKILL.md`)

## Run metadata format

`Worklog/current_run.txt` should contain simple key/value pairs:

```
branch=run/20251215-codex-clustering-pass1
agent=codex-cli
task=clustering pass 1
start=2025-12-15T10:05Z
notes=initial narrator clustering
```

An empty file (or missing `branch=` line) means no active run.

## Start a run

1. Read `Worklog/current_run.txt`.
2. If it already has a `branch=` entry, stay on that branch and continue the run.
3. If it is empty:
   - Determine the new branch name: `run/YYYYMMDD-<agent>-<focus>` (lowercase, hyphen-separated).
   - Create and checkout the branch: `git checkout -b <branch>`.
   - Write run metadata to `Worklog/current_run.txt` (branch, agent, task, start, notes).
   - Log start time per `Skills/cjb-time-logging/SKILL.md`.

## When to start a new run (and when not to)

- Start a new run only when starting a new end-to-end approach (e.g., “full extraction pass 1”, “clustering pass 1”, “ordering hypothesis pass 2”).
- Do **not** start a new run for each batch of pages; batches belong to commits within the same run.

## During a run

- Commit frequently with descriptive messages.
- Do **not** merge other branches into the run branch.
- Keep `Worklog/current_run.txt` untouched until the run ends (so restarts continue on the same branch).

## End a run

1. Ensure `python3 verify_pages.py` passes.
2. Make a final commit summarising the run: `Run summary: <one sentence>`.
3. Log the session end time (with final commit hash) in `Worklog/worklog.csv`.
4. If merging to `main`, do so after the summary commit; otherwise leave the branch as-is for review.
5. Clear `Worklog/current_run.txt` (leave empty) to signal no active run.

## After a run

- Merge into `main` only if the run produced coherent progress.
- Leave rejected experiments unmerged (branch stays as record).
- Never delete run branches unless explicitly instructed.
