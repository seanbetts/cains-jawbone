---
name: cjb-phase-playbook
version: 2.0
description: Use when starting work, changing phase, admitting a research source, or deciding whether a run can finish.
---

# Phase playbook

This is the authoritative repository policy for phase permissions, transitions, source admission and final gates. `Templates/SCHEMA.md` owns record fields and support levels; AGENTS owns source-text protection. No task skill overrides this matrix.

## Modes and authorization

Declare `Phase N: <name>` before puzzle work and record `phase-N` in current-run metadata and session logs. **Administrative review** covers tooling, skills, logging repairs and baseline preparation: do not infer puzzle claims or change the recorded puzzle phase. Log `admin` for administrative sessions. This mode is not a seventh solving phase.

A fresh end-to-end solving instruction authorizes the iterative Phase 2–6 loop after the Phase 1 coverage gate. Record `phase_loop=authorized` in that run's metadata with the authorizing request summarized in `notes`. Existing runs do not inherit this authority retroactively; consult their user instructions. Record each transition and its reason before dependent work; run branch identity remains stable. If a phase changes during a session, log separate contiguous time segments, never overlapping duration twice. A return to research does not erase established claims, but suspends promotion pending the relevant test.

## Phase matrix

| Phase | Allowed work and primary skills | Forbidden inference | Exit/review gate |
|---|---|---|---|
| 1: Page extraction | Read all pages; exact observations, literal relationships, voices as page signatures, candidate references and motivated wordplay. Page extraction, index maintenance, means/methods, motive/relationships as factual extraction only. | External lookups; cross-page clustering, ordering or murder/identity conclusions. | All 100 pages read and marked in coverage; each has meaningful Notes or explicit no-observation result; uncertainties queued. |
| 2: External research resolution | Research recorded questions; quote/date/location skills, targeted wordplay synthesis; test source identifications. | New clustering or ordering claims. | Important questions have truthful dispositions, source locations and next steps; review unresolved questions and what each blocks. No quota of “resolved” items. |
| 3: Pattern detection and clustering | Narrator profiling and clusters through typed same-narrator/entity/scene/reference or incompatibility claims; overlapping or unassigned pages allowed. | Sequence order or final murderer/victim conclusions. | Review all pages as assigned, overlapping or unassigned; each proposed cluster has evidence, alternatives, exclusion tells and a test; no prescribed cluster count. |
| 4: Internal ordering within clusters | Typed precedence/adjacency constraints and partial orders; conservative murder analysis as needed; test each claim. | Global stitching; forcing unassigned pages into a sequence. | Review internal constraints for every proposed cluster, unresolved pages, competing orders and contradictions. One solved cluster is insufficient; identify which uncertainties must be resolved before global work. |
| 5: Cross-cluster stitching | Cross-cluster constraints, consequences and event/identity claims; keep gaps and competing possibilities explicit. | Filling gaps just to produce 100 positions or six roles. | Whole-task coverage and uncertainty review: each proposed boundary has a claim or remains explicitly unresolved; competing structures and their decisive tests recorded. A complete draft alone does not pass. |
| 6: Convergence and falsification | Integrated challenge of accepted constraints and distinct event/identity claims; targeted returns through the authorized loop. | Final output while structural alternatives remain. | Final gate below. |

Falsification is allowed for every observation or claim the current phase permits. Phase 1 checks extraction; Phase 2 checks source matches; Phase 3 challenges clusters; Phase 4 tests internal order. Phase 6 integrates these tests. Testing does not authorize an otherwise forbidden new claim.

At each review, name unresolved contradictions, unassigned pages and stale dependencies. Choose the next question by the alternative it can discriminate. After two distinct inconclusive tests, suspend that claim and record the evidence that would reopen it; work on another uncertainty. Repeating a search or reread is not new corroboration. This is a practical effort limit, not a confidence formula.

## Source admission

In v2, research uses only sources admitted in `Sources/catalog.json`. Admission requires title, verifiable publication year at or before 1934, URL/location, and an admission note identifying the edition and evidence for the date. Verify metadata from the title/imprint page or reliable bibliographic record before admission. A listed work with unknown date remains excluded. An explicitly authorized corpus can be populated with eligible editions under that authorization; expanding beyond it requires user instruction. An empty catalog permits bibliographic eligibility checks and admission within the approved discovery corpus in `Templates/reference_sources.md`; it permits no evidentiary reliance on a source until that edition is admitted. This approved workflow authorizes within-corpus eligibility checking and admission without another permission request.

A modern scan or faithful transcription can host eligible historical text. Distinguish its historical passage from modern editorial commentary, search snippets, OCR errors and later annotations. These modern additions are not puzzle evidence. Consult only the admitted historical text for interpretation. Metadata verification can establish eligibility without admitting the site's modern analysis. Do not follow solution leads encountered accidentally.

Legacy runs use `Indexes/reference_sources.md` as their approved candidate list, but still verify edition/date before relying on a passage. Listing alone does not establish eligibility. A source match requires its exact location and reading the passage; record snippets as candidates. Research failure cannot prove original authorship, fictionality or absence from the literature.

## Wordplay and evidence

Make one local anomaly scan; call a detector only for a motivated span. Detectors never order pages. Their mechanically valid transformations remain candidates. Allow no convincing wordplay. Synthesis may propose a typed wordplay interpretation when this phase allows it; a date/place/narrator/order consequence requires its own claim and dependencies. Recurrence alone does not prove intention. Preserve literal readings and quoted-speaker versus narrator distinctions.

## Final gate

Before filling `FINAL_SOLUTION.md`:

1. Pass body integrity and ordinary `validate_state.py --root PATH` before integrated review. Keep readiness false while that review is incomplete.
2. Read the complete candidate once in order. All 100 pages must appear once; all accepted precedence and immediate-adjacency constraints must hold and jointly determine a unique sequence. The validator checks constraint-graph uniqueness without permutation search; merely listing a complete order does not qualify. Inspect narrator changes, quotation boundaries, time/place continuity and consequences, including joins without repeated wording.
3. Accepted claims must have current dependency revisions, active evidence, discriminating tests and no unresolved contradictions. Document why remaining alternatives do not change order, narrator partition or event/participant identities. Structural uncertainty blocks final output even if the validator passes.
4. Separately support death, intentional killing, victim identity and perpetrator identity for each distinct event. Deduplicate event descriptions and aliases. The stated six-murderer/six-victim target is a consistency check against supported distinct identities, never a reason to invent participants. One person can occupy both roles; attempts and allusive deaths do not count as completed murders.
5. Keep unknowns until evidence resolves them. If the target count and supported events disagree, return to testing. No arbitrary support score or lexical-match total can satisfy this gate.
6. Record the actual integrated review in readiness, with reviewer, summary and any structural issues. Set ready=true only when those issues are resolved, then pass `validate_state.py --root PATH --final`. This final check follows the review attestation; it is not a precondition to starting review. Commit the supporting state first. Write answers only in `FINAL_SOLUTION.md` and commit that file alone; log/closure commits remain separate.
