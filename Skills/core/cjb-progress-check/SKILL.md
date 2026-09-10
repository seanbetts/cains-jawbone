---
name: cjb-progress-check
version: 2.0
description: Use when choosing the next uncertainty, reviewing phase coverage, or assessing readiness to finish.
---

# Progress check

Read current phase and canonical state. Run structural validation and `calculate_research_progress.py --root PATH` (`--legacy` for historical Markdown). Compare the phase playbook gate against all pages and outstanding claims, not a single successful cluster.

Record a short status: coverage; verified/candidate/partial/no-match/deferred research separately; assigned/overlapping/unassigned pages; accepted and contested relations; stale dependencies; unresolved structural alternatives. Never combine these into “percent solved.” Queue size may grow as understanding improves.

Select the smallest discriminating next test: state which alternatives its possible results would distinguish, what source or passage is needed, and the likely consequence. If two distinct tests have been inconclusive, suspend the claim with its reopening condition and work elsewhere. A repeated lexical scan or reread does not upgrade support. Use the authorized phase loop for a return to research or clustering and record the transition; do not fill ordering gaps to make a progress metric improve.
