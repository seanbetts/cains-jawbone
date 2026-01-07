---
name: cjb-order-hypotheses
version: 1.1
description: Build and critique Cain’s Jawbone page clusters and candidate sequences using evidence, confidence, and explicit disconfirming tests (no brute force).
---

# Cain’s Jawbone — Order Hypotheses

## Non-negotiables

- No brute force ordering attempts.
- Every proposed linkage must include disconfirming evidence.
- Prefer clusters first; do not try to force a single global order early.

## Phase gating
- **Allowed phases:** `phase-3` … `phase-6`
- **Phase-3 constraint:** clusters only (no within-cluster sequencing).

## When to use (triggers)
- You see recurring voice/people/place/motif anchors across pages (Phase 3).
- You have a coherent cluster and want to propose an internal order (Phase 4).
- You have multiple clusters with potential joins (Phase 5).
- You are trying to break a near-final ordering (Phase 6; prefer `Skills/analysis/cjb-falsification/SKILL.md`).

## Primary file

- `Order/hypotheses.md`

## Method

### Pass 1: Clusters

Create clusters based on:

- voice/tells (diction, punctuation habits, obsessions, profession knowledge)
- recurring motifs/objects
- recurring named entities
- shared quote/allusion anchors
- time/place constraints

For each cluster, record:

- **Pages**
- **Rationale**
- **Key anchors**
- **Disconfirming evidence** (what would break the cluster)
- **Next falsification check** (the next concrete test you will run)

If a page fits multiple clusters, record it in each cluster as **pending disambiguation** (do not force a merge early).

#### Cluster card (recommended format; Phase 3-safe)

In addition to the bullets above, add a short “cluster card” to make later stitching cheaper:

- **Strong anchors (non-quote):** 2–3 anchors that are not just detachable quotations (voice tells, shared cast/props, place/time constraints).
- **Quote-layer anchors (optional):** record, but do not let these be the only glue.
- **Bridge endpoints (candidates):** pages that *look like* good predecessor/successor attachment points (scene openings/closings, handoffs, explicit “next day”, arrivals/departures). This is not a sequencing claim.
- **Pending disambiguation:** pages that fit multiple clusters and the tie-break test that would decide (a specific re-read, an index cross-check, or a research item).

### Pass 2: Intra-cluster ordering

Order within a cluster using:

- time markers (yesterday/tomorrow, meals, holidays, editions)
- place continuity (routes, venues, travel constraints)
- object continuity (letters, tools, injuries, pills/poisons)
- quote anchors (same source used in a progressive/echoing way)

For each candidate sequence, record:

- **Why** (1–3 bullets)
- **Confidence** (`CERTAIN/LIKELY/MAYBE`)
- **Disconfirming evidence** (specific tests)
- **Next falsification check** (the next concrete test you will run)

### Pass 3: Cross-cluster joins (later)

Only attempt when there are strong anchors (time/place/explicit references), and keep alternatives alive.

- **Promotion criteria:** prefer joins where continuity holds across 2+ independent dimensions (e.g., time + place, character + object, voice + quote anchor).
- **Conflict handling:** if a page fits multiple clusters equally well, keep it in both and explicitly mark “pending disambiguation” until later evidence breaks the tie.
- **Merge signals:** consider merging clusters only when they share multiple pages, share a narrator signature, or share multiple independent anchors; otherwise keep them separate with explicit alternative joins.

#### Join ledger (recommended; Phase 5+)

Maintain a join ledger in `Order/hypotheses.md` so weak boundaries are explicit and testable:

- Tag each cross-cluster boundary as:
  - `strong` — 2+ independent anchors across dimensions (time/place/cast/object/voice/quote continuation + something else).
  - `placeholder` — lexical-only (single token/ngram) or quote-only; usable for a full draft, but must be targeted for replacement/falsification.
- Every `placeholder` join must include:
  - **Next falsification check** (what you will do next to upgrade/break it),
  - 1–3 **replacement leads** (alternative predecessor/successor candidates) to prevent “circling”.
