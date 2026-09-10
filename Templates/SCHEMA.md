# Canonical state schema (v2)

This schema is authoritative for new runs. UTF-8 JSON Lines files contain one JSON object per nonblank line. JSON files contain one object, except the source catalog (an array). No template/example rows belong in live records. IDs are stable and never reused; v2 V/C/R/S/T/E/P IDs use at least three digits (for example V001); page numbers are integers 1–100. Unknowns remain explicit. Legacy Markdown is not automatically migrated, verified or assigned these statuses.

## Evidence: `State/evidence.jsonl`

Required fields: `id` (`V` plus digits), `page` (integer), `span` (minimal exact body text), `offset` (zero-based character offset into the body), `layer` (`narration|dialogue|quotation|unclear`), `observation` (literal description), `status` (`active|withdrawn`). Preserve Unicode and punctuation; count characters, not bytes. The body is the entire prefix returned by `md_body_before_notes`, before the Notes heading, including any leading whitespace or page heading present. Compute offsets into that returned string; do not strip or otherwise normalize it afterward. If the span repeats, the offset identifies the occurrence. Do not guess offsets or normalize the quoted span. Evidence describes what is printed, not the inferred authorial intention. Once a V ID is used, its page/span/offset/layer/observation content is immutable: withdraw it and create a new V ID for corrections. Withdrawal invalidates live consumers; never edit content under an existing evidence ID.

## Claims: `State/claims.jsonl`

Required fields:

- `id` (`C` plus digits), `revision` (positive integer).
- `relation`: `same_narrator|same_entity|same_scene|shared_reference|precedes|adjacent|incompatible|entity_identity|death|intentional_killing|victim_identity|perpetrator_identity|narrator_assignment|wordplay|source_interpretation|date_interpretation|place_interpretation`.
- `pages`: unique integer page list. `precedes` and `adjacent` require exactly two pages in directional order A, B; `incompatible` also requires exactly two pages, without direction; other page lists identify claim scope, never imply sequence.
- `statement`: one explicit proposition, including assumptions and why the cited evidence supports it.
- `evidence`: list of V IDs. `dependencies`: object mapping each premise C, R or S ID to the positive revision used. Include every source/research result on which the interpretation relies; prose mentions do not replace typed dependencies.
- `status`: `tentative|supported|strongly_constrained|rejected|suspended`.
- `alternatives`: list of serious alternative readings, including a literal reading when relevant.
- `falsifier`: observable evidence that would defeat the proposition. `next_test`: specific discriminating test or, for suspended claims, reopening condition.

Each current ID occurs once. Increase revision whenever meaning, evidence, support status or dependencies change. Update existing record, preserving history in Git; do not append duplicate current IDs. A changed dependency revision, rejected/suspended premise, or withdrawn evidence makes dependent claims stale: suspend them and review recursively before accepting them again. Do not silently update dependency revision numbers without reassessing the inference. Tests refer to the claim ID and explicit `claim_revision`; historical tests remain, but a test of an older revision cannot support a revised claim or satisfy final gates.

Same narrator, shared reference, same scene, precedence and adjacency are distinct. Never promote between these relations implicitly. A single source identification reused across several indices remains one premise. Source-dependent interpretations name the exact supporting result in `statement` and include its R and S revisions in `dependencies`. Research and source records carry revisions too: a changed source edition/metadata or research result requires a revision increment and consumer review. A supported or strongly constrained claim may depend only on supported/strongly constrained C premises and verified R premises; tentative interpretations may retain weaker research candidates. A stale reference blocks live claims until they are suspended or actually reassessed. `incompatible` names two page assignments whose incompatibility is explained in the statement; it does not automatically forbid those two pages from both appearing in a global order.

### Support standards

- **tentative:** plausible reading with unresolved competing interpretations.
- **supported:** specific evidence favors it over stated alternatives; substantial uncertainty may remain.
- **strongly_constrained:** distinctive evidence and discriminating tests exclude serious alternatives, with no unresolved contradiction or stale premise.
- **rejected:** contradicted; retain reason and evidence.
- **suspended:** insufficient discriminating evidence or stale premises; record reopening condition.

These are reasons to assess, not numerical probabilities or automatic evidence-count thresholds. “Verified” applies to source matches or directly checked observations, not narrator or murder confidence. Absence of contradiction and repeated rereading do not promote a claim. One decisive continuation can outweigh several generic similarities; explain specificity and independence.

## Research: `State/research.jsonl`

Required fields: `id` (`R` plus digits), `revision` (positive integer), `pages`, `question`, `status`, `result` (string), `sources` (array), `searched` (list of query/source/variant strings), `next_step` (string).

Each source usage has `id` (S ID), `revision` (positive integer pinning the catalog source revision), `location` (edition volume/page, act/scene/line or equivalent), `match_type` (`exact|variant|context`), `verification` (`passage_read|snippet_only`), `supports` (the particular part of the question the passage supports).

| Status | Meaning |
|---|---|
| `open` | Question recorded, not investigated |
| `in_progress` | Investigation under way |
| `verified` | The whole stated question is answered with admitted source passages actually read, precise locations, and a reasoned match |
| `candidate` | Plausible identification, including snippet-only evidence, needing verification |
| `partial` | Only part of the question answered; name the unresolved part or split into separate questions |
| `no_match` | Bounded searches performed without a match; record corpus, variants and limits |
| `deferred` | Deliberately postponed; record reason and reopening condition |

A thematic/context passage can verify a contextual question, not exact authorship or wording. A variant match explains differences. `no_match` cannot establish that something is original, fictional, or absent everywhere. A `verified` source match does not verify its proposed narrator, date-in-story or ordering consequence. Verified research must pin the current catalog revision in every source usage. When a source changes, reassess its cited passages and increment the affected research revision; stale verified citations block live consumers. Never update source pins merely to silence validation.

## Sources: `Sources/catalog.json`

Array of objects with `id` (`S` plus digits), `revision` (positive integer), `title`, `year` (integer 1–1934), `url` (HTTP(S)), `admission_note`. Record edition and date-verification basis in admission_note. The catalog is the admitted corpus, not a list of search websites. Modern host metadata and modern commentary are distinct from historical source content. `Templates/reference_sources.md` is a discovery guide, not evidence or automatic admission. Follow the phase playbook before adding sources. An empty array means none admitted for evidentiary use yet. Eligibility checks and edition admission within the approved discovery corpus can proceed under the phase playbook; an empty catalog does not prevent admission.

## Tests: `State/tests.jsonl`

Required fields: `id` (`T` plus digits), `claim` (C ID), `claim_revision` (positive integer), `prediction`, `procedure`, `evidence` (V ID list), `outcome` (`supported|contradicted|inconclusive`). State the competing reading and what result distinguishes it. A test can support one consequence without proving every part of a claim. Repeating the same test is not independent corroboration.

## Coverage and partial order

`State/coverage.json`: `{ "read_pages": [] }`. Mark a page read only after the extraction pass and note review.

`State/order.json`: `{ "pages": [], "complete": false, "accepted_claims": [] }`. List only an explicitly proposed sequence; unplaced pages remain absent while incomplete. Keep disconnected partial constraints in claims instead of pretending all fragments form one sequence. `accepted_claims` lists C IDs accepted for this proposal. At final review it must include every supported or strongly_constrained ordering constraint; do not omit an inconvenient supported constraint without explicitly rejecting or suspending it and recording why. Complete means all 100 pages once, not proven correctness.

## Events and readiness

`State/events.jsonl`: objects with `id` (`E` plus digits), `death_claim`, `intent_claim`, `victim_claim`, `perpetrator_claim` (C IDs), `victim`, `murderer` (stable entity-ID strings), `status` (`active|rejected|unresolved`). Use P IDs with at least three digits for participant referents. An unresolved event may leave missing claim/participant fields as empty strings. Keep event occurrence, intentional killing and the two participant identities separate. Unknown participant IDs do not become valid merely to meet a count. Deduplicate multiple descriptions of the same event and aliases; attempts and quoted deaths are not completed in-world murders.

`State/readiness.json`: `{ "reviewer": "", "summary": "", "unresolved_structural": [], "ready": false }`. The named reviewer writes an actual integrated-review summary and lists structural issues. `ready: true` is an attestation after review, never a way to suppress validation errors.

Final structural validation requires complete order uniquely determined by the accepted precedence/adjacency constraints, with each constraint satisfied; current evidence/dependencies; qualifying tests of current claim revisions with nonempty active evidence and no unresolved contradicted test; six active distinct death claims, six unique victim IDs and six unique murderer IDs; correctly typed, strongly constrained event claims; and ready=true with reviewer/summary and no unresolved structural issues. Overlap between murderer and victim sets is allowed. Metadata validation cannot determine whether two IDs actually refer to the same person or whether prose proves a murder; the phase playbook requires that semantic review.

## Readable views and logs

Use `Pages/...` Notes and `Indexes/*.md` as short observation/claim-ID views, not independent copies of evidence. `Order/hypotheses.md` is a compact current-claims and next-tests view. `Order/cast.md` and `Order/confidence.md` link entity/event claims. Use stable P IDs for entity referents and N IDs only for supported narrator hypotheses; page signatures may remain unassigned. A changed label never silently merges IDs. Keep history in Git or `History/` outside immutable Archive; history is excluded from fresh exports.

`Worklog/worklog.csv` columns: `date,agent,phase,task,start,end,minutes,branch,commit,notes`. UTC ISO start/end; numeric elapsed minutes; `phase-1`…`phase-6` or `admin`. CSV quoting is handled by the logging script. `commit` identifies work HEAD preceding the log, not its own log commit. New sessions require initialized Git, a non-main work branch and a valid HEAD. A genuinely unknown historical commit may remain blank under legacy validation; never invent it. See time-logging skill.
