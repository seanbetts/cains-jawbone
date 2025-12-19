---
name: cjb-run-management
version: 1.0
description: Manage long-lived run branches via Worklog/current_run.txt so end-to-end workstreams are isolated, logged, and mergeable.
---

# Run management

## Purpose
Keep exploratory work isolated per end-to-end workstream (“run”), with clear provenance and easy rollback.

## Phase gating
- **Allowed phases:** `phase-1` … `phase-6`

## Definitions

- **Session:** a single working block that gets a `start/end/minutes` row in `Worklog/worklog.csv`.
- **Run:** a long-lived branch for a coherent goal (e.g., first full extraction pass) that may span multiple sessions/days.

## Files/tools
- `Worklog/current_run.txt` — stores the currently active run metadata (blank means no active run)
- `Worklog/worklog.csv` — overall time log (see `Skills/core/cjb-time-logging/SKILL.md`)

## Run metadata format

`Worklog/current_run.txt` should contain simple key/value pairs:

```
branch=run/20251215-codex-clustering-pass1
agent=codex-cli
task=clustering pass 1
phase=phase-3
start=2025-12-15T10:05:00Z
notes=initial narrator clustering
```

An empty file (or missing `branch=` line) means no active run.

## Preflight (always)

1. Read `Worklog/current_run.txt`.
2. If it contains a `branch=...` entry, ensure it matches your current git branch:
   - `git rev-parse --abbrev-ref HEAD`
3. If you are not on the run branch, switch to it before doing any work:
   - `git checkout <branch>`

## Start a run

1. Read `Worklog/current_run.txt`.
2. If it already has a `branch=` entry, stay on that branch and continue the run.
3. If it is empty:
   - Determine the new branch name: `run/YYYYMMDD-<agent>-<focus>` (lowercase, hyphen-separated).
   - Create and checkout the branch: `git checkout -b <branch>`.
   - Decide the starting phase (usually `phase-1`) and write run metadata to `Worklog/current_run.txt` (branch, agent, task, phase, start, notes).
   - Log start time per `Skills/core/cjb-time-logging/SKILL.md`.

## When to start a new run (and when not to)

- Start a new run only when starting a new end-to-end approach (e.g., “full extraction pass 1”, “clustering pass 1”, “ordering hypothesis pass 2”).
- Do **not** start a new run for each batch of pages; batches belong to commits within the same run.

## During a run

- Commit frequently with descriptive messages.
- Do **not** merge other branches into the run branch.
- Keep `Worklog/current_run.txt` stable so restarts continue on the same branch (do not edit `branch=`); update only `phase=` when the active phase changes.

## Change phase during a run

1. Decide the new phase (`phase-1` … `phase-6`) based on `Skills/core/cjb-phase-playbook/SKILL.md`.
2. Update only the `phase=` line in `Worklog/current_run.txt`.
3. Commit the phase change (single-purpose), e.g. `Worklog: update current run to phase-3`.
4. Continue logging each session in `Worklog/worklog.csv` per `Skills/core/cjb-time-logging/SKILL.md`.

## End a run

1. Ensure `python3 Scripts/verify_pages.py` passes.
2. Make a final commit summarising the run: `Run summary: <one sentence>`.
3. Log the session end time (with final commit hash) in `Worklog/worklog.csv`.
4. If merging to `main`, do so after the summary commit; otherwise leave the branch as-is for review.
5. Clear `Worklog/current_run.txt` (leave empty) to signal no active run.

## After a run

- **Full merge:** Merge the entire branch into `main` only if the run produced coherent puzzle progress.
- **Selective merge:** If only infrastructure improved (Skills, Scripts, docs), use `Skills/core/cjb-merge-to-main/SKILL.md` to merge just those files without touching puzzle state on `main`.
- Leave rejected experiments unmerged (branch stays as record).
- Never delete run branches unless explicitly instructed.
