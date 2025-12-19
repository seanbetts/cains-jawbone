---
name: cjb-merge-to-main
version: 1.0
description: Selectively merge infrastructure files (Skills, Scripts, AGENTS.md, README.md) from the current run branch to main without merging puzzle-state files.
---

# Cain's Jawbone — Merge to Main

## Purpose
Allow infrastructure improvements (skills, scripts, documentation) to be shared to `main` without merging puzzle-state files (Pages, Indexes, Order, Worklog).

## Phase gating
- **Allowed phases:** `phase-1` … `phase-6`

## When to use
- After updating skills, scripts, or project documentation on a run branch.
- When infrastructure changes should be available to other runs/branches.
- Before starting a new run that should inherit updated tooling.

## Files to merge (whitelist)

Only these paths are merged:

- `Skills/` (entire folder)
- `Scripts/` (entire folder)
- `AGENTS.md`
- `README.md`

## Files NOT merged (protected)

These are never merged by this skill:

- `Pages/`
- `Indexes/`
- `Order/`
- `Worklog/`
- `Archive/`
- `FINAL_SOLUTION.md`

## Prerequisites

1. You are on a run branch (not `main`).
2. All changes are committed (clean working tree).
3. The files to merge have no uncommitted changes.

## Procedure

### 1) Verify prerequisites

```bash
# Confirm current branch is not main
git rev-parse --abbrev-ref HEAD

# Confirm working tree is clean
git status --porcelain
```

If on `main` or working tree is dirty, stop and ask the user to resolve.

### 2) Checkout main and pull latest

```bash
git checkout main
git pull origin main
```

### 3) Selectively merge files from run branch

Use `git checkout <branch> -- <path>` to bring specific files from the run branch:

```bash
# Replace <run-branch> with the actual branch name
git checkout <run-branch> -- Skills/
git checkout <run-branch> -- Scripts/
git checkout <run-branch> -- AGENTS.md
git checkout <run-branch> -- README.md
```

### 4) Commit the merge

```bash
git add Skills/ Scripts/ AGENTS.md README.md
git commit -m "$(cat <<'EOF'
Merge infrastructure from <run-branch>

Selectively merged:
- Skills/
- Scripts/
- AGENTS.md
- README.md

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

### 5) Return to run branch

```bash
git checkout <run-branch>
```

### 6) Optionally push main

Only if the user explicitly requests:

```bash
git push origin main
```

## Output checklist

- Infrastructure files merged to `main`
- Puzzle-state files remain untouched on `main`
- Returned to original run branch
- Commit message describes what was merged

## Common mistakes (pitfalls)

- Merging the entire branch (use selective checkout, not `git merge`).
- Forgetting to return to the run branch after merging.
- Pushing to main without user confirmation.
- Merging with uncommitted changes (leads to conflicts or lost work).
