# Cain’s Jawbone research workspace

A literary notebook for extracting clues, resolving historical references, and testing reversible ordering and identity claims. Read [AGENTS.md](AGENTS.md) before working.

## Workflow

Complete a factual pass through all 100 pages first. Then use focused research, provisional clustering, partial ordering, and discriminating tests in an iterative loop. Every relationship says exactly what it asserts; shared wording is a retrieval aid, and earlier-than does not mean immediately-before. Progress means reduced uncertainty supported by evidence, not more matches or a complete-looking draft.

[The phase playbook](Skills/core/cjb-phase-playbook/SKILL.md) owns permissions, research admission and final gates. [The schema](Templates/SCHEMA.md) owns record fields and support standards. Skills under `Skills/` describe specific techniques, including targeted wordplay detection, narrator profiling and murder analysis.

## Files

| Path | Purpose |
|---|---|
| `Archive/` | Immutable archived text and hash |
| `Pages/` | 100 page bodies, with editable Notes below each body |
| `State/` | Canonical evidence, claims, research, tests, coverage and partial order for new runs |
| `Sources/catalog.json` | Admitted historical sources with publication metadata |
| `Templates/` | Empty readable views and canonical v2 schema |
| `Indexes/`, `Order/` | Readable views linking canonical IDs; existing populated files are legacy state |
| `Worklog/` | Active run metadata and UTC session log |
| `Skills/`, `Scripts/` | Procedures and small integrity/analysis tools |
| `FINAL_SOLUTION.md` | Answers only after final checks |

The existing Markdown progress remains historical evidence. It has not been automatically converted into verified v2 claims. `--legacy` validation checks legacy structure only; it never promotes past conclusions.

## Tools

Run each tool with `--help` for options.

- `verify_pages.py`: archive hash, exact page inventory, Notes headings and page bodies.
- `validate_state.py --root PATH`: structured records, exact evidence spans, dependencies and constraint consistency; `--final` adds final structural gates, including uniqueness from accepted constraints; `--legacy` checks old records and logging without conversion.
- `calculate_research_progress.py --root PATH`: separate coverage and research dispositions, not a percent solved. `--legacy` reads historical Markdown.
- `scan_df2_boundaries.py --pair A B` or `--query TEXT`: lexical concordance independent of a complete draft. It cannot establish adjacency, direction or narrator identity.
- `log_session.py --start ISO --agent NAME --phase PHASE --task TEXT --notes TEXT`: CSV-safe session logging; see time-logging skill.
- `prepare_fresh_run.py --destination PATH`: isolated allowlisted baseline with blank solving state, no old Git history and source/tooling provenance.

Validation checks structure and internal consistency. Human/agent reasoning still has to establish what the passages mean. The body verifier does not authenticate the original transcription.

A fresh solving run needs the isolated baseline and a new context. Review the generated manifest and checks before solving; keep previous notes, hypotheses, reviews, worklogs and solution content inaccessible to that solver.
