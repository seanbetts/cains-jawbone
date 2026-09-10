---
name: cjb-index-maintenance
version: 2.0
description: Use when updating indices after extraction, research, tests, or claim revisions.
---

# Index maintenance

Canonical records live in State under `Templates/SCHEMA.md`; indices are concise readable views. Store each observation and claim once, then link IDs from page Notes, people, places, quotes, motifs, narrators, wordplay and research views. Copying a claim into three files never supplies three sources of support.

Use stable entity IDs with explicit referents and uncertainty; distinguish people, animals, fictional/allusive figures and unknown mentions. Possible aliases require a same-entity or entity-identity claim before consolidation. Preserve original IDs as traceable aliases after a supported merge. Page references use `Pages/cains_jawbone_page_N.md`; sort nondirectional page lists numerically.

Keep literal observations separate from inferred place, narrator or source identities. Wordplay views link synthesis claims; detector candidates remain in Notes. Research views preserve exact question, truthful status, source location and next step. Never promote candidate/no-match/partial to verified merely to close a queue.

On claim, research or source revision, update its canonical record and recursively suspend/reassess consumers of an older C/R/S revision. Correct evidence by withdrawing its V ID and issuing a new one; evidence content under an existing ID stays immutable. Remove stale “accepted” displays; rejected records remain available with reasons. Keep current hypotheses and pending tests compact; Git or History preserves superseded discussion outside Archive. Existing legacy state stays legacy unless an explicitly scoped evidence-based migration is requested.

Run `validate_state.py --root PATH` and body verification after edits. Structural validation cannot detect copied reasoning posing as independent evidence; review provenance directly.
