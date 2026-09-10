---
name: cjb-time-logging
version: 2.0
description: Use when starting or ending any workspace session, including administrative review.
---

# Time logging

Capture UTC start before opening files (`date -u +%Y-%m-%dT%H:%M:%SZ`). Retain it in working context with agent, task and phase. Use the phase playbook for `phase-1` through `phase-6`, or `admin` for infrastructure-only work.

At the end, after the work commit if any, run:

```sh
python3 Scripts/log_session.py --start START_ISO --agent AGENT --phase PHASE --task TASK --notes NOTES
```

Use actual argument values with shell-safe quoting. `--root PATH` targets an explicit workspace; `--end ISO` records a captured end. The helper validates timestamps, calculates elapsed minutes, uses a CSV writer and records current branch/HEAD. Never hand-concatenate CSV, estimate missing past timings, or invent a commit. Run structural validation after logging.

The `commit` field means **work HEAD preceding this log**, not the commit containing the row. If work is uncommitted, say so in notes; the recorded HEAD is context, not proof those changes are committed. New session logging requires an initialized Git repository, a non-main work branch and a valid HEAD. Initialize and commit a fresh baseline, then create its work branch before starting solving work. A genuinely unknown historical commit may remain blank under legacy validation; do not invent a hash or use that exception for a new session. Commit the log afterward when appropriate; do not attempt a self-referential hash.

One row covers one meaningful time segment. For an actual phase transition, end that segment and start the next at the same timestamp; total elapsed time must not be counted twice. A coordinating agent may log one integrated session for delegated work, naming that fact in notes. Do not manufacture separate agent durations. Preserve historical malformed rows during normal logging; repair only from unambiguous evidence in a separately reviewed change.
