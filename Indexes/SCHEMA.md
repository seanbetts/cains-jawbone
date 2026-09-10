# Legacy index schema

The populated Markdown indices in this checkout predate canonical v2 state. Historical conventions included `Pxx` and `Nxx` identifiers, `CERTAIN/LIKELY/MAYBE` tags, and research labels `open/in-progress/stalled/resolved`. Those labels are historical assertions, not verified v2 results.

For new runs, use [Templates/SCHEMA.md](../Templates/SCHEMA.md), which owns evidence, typed claims, research outcomes, dependencies and readable-view conventions. Link canonical IDs from indices rather than copying claims as corroboration. Do not bulk-convert old “resolved” or confidence labels into new statuses without rereading their actual evidence.

`validate_state.py --legacy` and `calculate_research_progress.py --legacy` read the old Markdown format for structural checks and honest summaries. They do not migrate, substantiate or improve the existing puzzle conclusions.
