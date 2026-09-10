---
name: cjb-merge-to-main
version: 2.0
description: Use when integrating reviewed infrastructure or accepted puzzle work into another branch.
---

# Scoped integration

User authorization to edit does not automatically authorize merge or push. Prepare a concrete reviewed change before requesting any genuinely missing authorization; do not ask again if already granted.

1. Read status, active branch, target revision, recent infrastructure history and hooks (`core.hooksPath` and repository hooks). Preserve unrelated changes. Do not pull or update remotes automatically.
2. Identify exact infrastructure-only commits or a reviewed scoped patch against the current target. Allowlist intended files. Do not check out whole directories from the run branch: this can overwrite newer target work. Exclude Archive, Pages, populated state/indices/order, solution and run logs unless the integration explicitly includes them.
3. Apply in an isolated target checkout/worktree when necessary. Resolve changes against current target content; preserve newer work. Inspect the complete resulting diff and verify bodies, relevant script tests and state. If an intended patch cannot apply, explain the conflict with the concrete resolution.
4. Stage only intended files. Confirm hooks cannot trigger unapproved publication or deployment. Commit using truthful authorship; no hard-coded coauthor identity. A final-solution commit changes only that file.
5. Report source/target commits and checks. Merge and push remain separate actions. Keep the original run branch as a historical record; do not delete it without instruction.
