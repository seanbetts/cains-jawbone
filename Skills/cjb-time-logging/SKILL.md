---
name: time-logging
description: Log start/end times and session duration for every work session in Worklog/worklog.csv. Use at the beginning and end of any session that edits files or proposes hypotheses.
---

# Time logging

## Purpose
Ensure every session is time-stamped and attributable.

## When to use
- Always at the start of a session, before reading or editing project files.
- Always at the end of a session, after the final commit is made.

## Procedure

### Start of session
1. Determine current time in UTC (ISO 8601).
2. Create an in-progress session note (in working memory for this run) with:
   - date (YYYY-MM-DD)
   - agent name
   - phase (e.g. `phase-1`)
   - intended task
   - branch (if known)
   - start time (UTC)

Do not write to the CSV yet unless you are creating a placeholder row.

### End of session
1. Determine current time in UTC (ISO 8601).
2. Compute `minutes` as the rounded difference between start and end.
3. Ensure a commit exists for the session if files changed.
4. Append a single row to `Worklog/worklog.csv`:

Columns:
`date,agent,phase,task,start,end,minutes,branch,commit,notes`

Constraints:
- `minutes` must be numeric.
- `notes` must be one sentence.
- `phase` must be present (use `phase-1` … `phase-6`).
- Use UTC consistently.

## Example row

```csv
2025-12-14,codex-cli,phase-1,extract pages 21-30,2025-12-14T20:10Z,2025-12-14T20:37Z,27,run/20251214-codex-extraction-pass1,abc1234,"Added notes and updated quotes index."
```
