---
name: cjb-run-management
version: 2.0
description: Use when starting, resuming, closing, or preparing an independent solving run.
---

# Run management

Capture start time, then read `Worklog/current_run.txt` and `git status --short --branch`. A run spans sessions; batches do not create new runs. If metadata names a branch, remain on it. If checkout differs, inspect dirty work before switching; preserve it and never force checkout. Keep `branch=` stable; update authorized `phase=` transitions and record reasons under the phase playbook.

If metadata is empty and a new end-to-end run is authorized, create `run/YYYYMMDD-agent-focus` and record `branch`, `agent`, `task`, `phase`, `start`, `notes`, and `phase_loop=authorized` when that scope was authorized. Do not begin solving on `main`. Administrative review keeps existing run metadata and logs `admin`; it does not start another puzzle run.

Commit coherent scoped work after verification and hook inspection; do not merge other branches into an active run. Rejected claims remain identified as rejected with their tests; Git preserves prior revisions. Never rewrite history or delete run branches without instruction.

To close: verify state and bodies; commit the substantive run summary; append the final session log identifying that work HEAD; clear current-run metadata only when the run is actually complete; commit log/closure metadata explicitly. Integration is a separate authorized action under `cjb-merge-to-main`. A speculative run may remain unmerged indefinitely.

## Independent baseline

Use `python3 Scripts/prepare_fresh_run.py --destination PATH` (optional `--source PATH`). Choose a new destination; never overlay a populated folder. Inspect the manifest and validation output. The export allowlists archive, page bodies with empty Notes, reviewed skills/scripts, empty templates/state, source-admission policy and the approved neutral discovery guide. It resets `Sources/catalog.json` to an empty array: source selections from the old run could reveal earlier clue research and are not copied. The fresh solver may admit individual eligible editions within the approved discovery corpus after checking publication metadata. It excludes old notes, claims, indices, worklogs, reviews, solution content and `.git` history.

The export is deliberately not a Git repository. Before solving, initialize a new repository, commit the clean baseline after validation, create the run branch and metadata as above. Preserve provenance separately from puzzle claims. Start the solver in a new task/context with access only to the clean baseline; do not relay old conclusions in its prompt. Baseline preparation is not authorization to start solving or create a new task. A new branch in the old repository does not provide independence, and clean context cannot guarantee a model has never encountered the puzzle in training.
