# Index schema

This file describes the **stable structure** (minimal schema) for the files under `Indexes/`.

## Global conventions

- **Page references:** always use full paths like `Pages/cains_jawbone_page_42.md` and keep page lists in numeric order.
- **Confidence tags:** use only `CERTAIN`, `LIKELY`, `MAYBE` (unless a specific Skill defines a different scale).
- **Quoting:** keep snippets short (often 5–15 words), enough to identify.
- **Stable IDs:** people use `P01`, `P02`, …; narrators use `N01`, `N02`, … (never reuse an ID).

## `Indexes/people.md`

Entry header:
- `- `Pxx` — Names/aliases: …`

Recommended fields (bullets under the entry):
- **Tells:** voice/behaviour/role signals
- **Pronouns/relationships:** how they connect to others
- **Pages:** list of `Pages/...` paths
- **Notes:** uncertainty, merge/split hypotheses + falsifiers

## `Indexes/places.md`

Entry header:
- `- **Place**`

Required fields:
- **Type:** (city/room/venue/landmark/route/region/landform/other)
- **Confidence:** `CERTAIN` / `LIKELY` / `MAYBE`
- **Pages:** list of `Pages/...` paths
- **Notes:** citations, ambiguity, why it matters

## `Indexes/quotes.md`

Entry header:
- `- **Snippet:** “…”`

Required fields:
- **Likely source/author:** (include citation/URL when known)
- **Why it matters:** (date anchor, voice tell, motif, etc.)
- **Pages:** list of `Pages/...` paths
- **Confidence:** `CERTAIN` / `LIKELY` / `MAYBE`
- **Research needed:** `yes/no` + what (when not fully resolved)

## `Indexes/objects_motifs.md`

Entry header:
- `- **Motif/Object:** …`

Recommended fields:
- **Type:** (food/drink/animal/weather/weapon/medicine/letter/tool/other)
- **Pages:** list of `Pages/...` paths
- **Notes:** variants, continuity hooks, cautious implications

## `Indexes/narrators.md`

Entry header:
- `- `Nxx` — Label: …`

Recommended fields:
- **Signature tells:** stable voice markers
- **Likely identity (if any):** keep tentative
- **Pages:** list of `Pages/...` paths
- **Confidence:** `MAYBE` / `LIKELY` / `CERTAIN`
- **Disconfirming evidence:** what would break this profile
- **Notes:** links to clusters without implying sequence

## `Indexes/wordplay.md`

Only include **synthesis outputs** (not raw detector output).

Entry header:
- `- `Pages/cains_jawbone_page_N.md``

Required block:

```text
LIKELY WORDPLAY
- mechanism(s): <one or more>
- span: "<exact text span>"
- best reading: "<best interpretation>"
- confidence: low|med|high
- why it matters: <ordering|narrator|place|date|motif> -> <one sentence>
- falsifiers:
  - "<one>"
  - "<optional second>"
```

## `Indexes/research_queue.md`

Entry header:
- `- **Item:** …`

Required fields:
- **Type:** (quote/name/place/term/other)
- **Pages:** list of `Pages/...` paths
- **Why it matters:** one sentence
- **Status:** `open` / `in-progress` / `stalled` / `resolved`
- **Result:** fill when `resolved`; if `stalled`, include what was checked + why it may still matter
