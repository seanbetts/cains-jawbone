---
name: cjb-time-logging
version: 1.0
description: Log start/end times and session duration for every work session in Worklog/worklog.csv.
---

# Time logging

## Purpose
Ensure every session is time-stamped and attributable.

## Phase gating
- **Allowed phases:** `phase-1` … `phase-6` (always required)

## When to use
- Always at the start of a session, before reading or editing project files.
- Always at the end of a session, after the final commit (if any) is made.

## Procedure

### Start of session
1. Determine current time in UTC in `YYYY-MM-DDTHH:MM:SSZ` (ISO 8601), e.g. `date -u +"%Y-%m-%dT%H:%M:%SZ"`.
2. Create an in-progress session note (in working memory for this run) with:
   - date (YYYY-MM-DD)
   - agent name
   - phase (e.g. `phase-1`; use `Worklog/current_run.txt` as source of truth)
   - intended task
   - branch (if known)
   - start time (UTC)

Do not write to the CSV yet unless you are creating a placeholder row.

### End of session
1. Determine current time in UTC in `YYYY-MM-DDTHH:MM:SSZ`.
2. Compute `minutes = round((end - start) / 60)` (nearest whole minute).
3. Ensure a commit exists for the session if files changed.
4. Set the `commit` field:
   - If files changed: the last commit hash you made for this session.
   - If no files changed: the current `HEAD` hash (still log the session).
5. Append a single row to `Worklog/worklog.csv`:

Columns:
`date,agent,phase,task,start,end,minutes,branch,commit,notes`

Constraints:
- `minutes` must be numeric.
- `notes` must be one sentence.
- `phase` must be present (use `phase-1` … `phase-6`).
- Use UTC consistently.

## Example row

```csv
2025-12-14,codex-cli,phase-1,extract pages 21-30,2025-12-14T20:10:00Z,2025-12-14T20:37:00Z,27,run/20251214-codex-extraction-pass1,abc1234,"Added notes and updated quotes index."
```
