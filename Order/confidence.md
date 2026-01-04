# Murder confidence ledger

Track *in-world* death/murder hypotheses separately from page-ordering hypotheses.

- Ordering/clustering lives in `Order/hypotheses.md`.
- Quotes/date anchors live in `Indexes/quotes.md` + `Indexes/research_queue.md`.

## Principles

- Only include **in-world** death/violence hypotheses here (not purely historical/allusive deaths).
- Use `Pxx` IDs when possible; otherwise use `UNKNOWN` plus a short descriptor.
- Keep claims reversible: include confidence + falsifiers + status.

## Confidence conventions

- Confidence is numeric `0.0–1.0`; use `Skills/core/cjb-phase-playbook/SKILL.md` for shared mapping to `MAYBE/LIKELY/CERTAIN`.
- Adjust conservatively (usually ±0.05 per new anchor) unless the text is explicit.

## Event template

- `E01` (confidence: `0.0–1.0`; status: `active` / `downgraded` / `rejected`)
  - **Pages:**  
  - **Victim candidate(s):**  
  - **Murderer candidate(s):**  
  - **Means/method:**  
  - **Motive:**  
  - **Opportunity:**  
  - **Narrative tells:**  
  - **Evidence summary:**  
  - **Falsifiers:**  

## Events

- `E01` (confidence: `0.05`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_62.md
  - **Victim candidate(s):** `P59` (dead man; identity unknown)
  - **Murderer candidate(s):** `UNKNOWN`
  - **Means/method:** `UNKNOWN` (death already occurred by the time of narration)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** `UNKNOWN` (only timing detail: he spoke to narrator ~1 hour before “they came to take him away”)
  - **Narrative tells:** Framing stresses deceit (“heart… deceitful”) and a story told by a now-dead speaker; “take him away” hints at custody/institution.
  - **Evidence summary:** Background-context in-world death signal is present but agency/cause is not established; do not count as one of the six unless later pages tie it to a concrete method/agent.
  - **Falsifiers:** Later pages clarify the “dead man” is a metaphor/allusion, or confirm a non-violent natural death unrelated to the six in-world murders.

- `E02` (confidence: `0.30`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_68.md, Pages/cains_jawbone_page_69.md, Pages/cains_jawbone_page_70.md
  - **Victim candidate(s):** `P61` (poor old man; identity unknown)
  - **Murderer candidate(s):** `UNKNOWN`
  - **Means/method:** `UNKNOWN` (described as “done slowly to death”; could imply poisoning/neglect, but not explicit)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Narrator claims direct witnessing; surrounding pages suggest a “crucial meeting” and later fear of retaliation.
  - **Narrative tells:** Emphasis on time-of-night wakefulness + self-command (“collect myself”) after witnessing the slow death; later page frames a franked warning/blackmail note and the threat of being “done in”.
  - **Evidence summary:** IN-WORLD death is asserted with slow-killing language, but agent/means are not named.
  - **Phase 6 test (2025-12-31):** re-read Pages/cains_jawbone_page_68.md, Pages/cains_jawbone_page_69.md, Pages/cains_jawbone_page_70.md; Page 69 remains an explicit witnessed slow-death claim (“done slowly to death before my eyes”), but Page 70’s retaliation fear is directed at an unnamed “he” (arthritic knee; “contact with his infancy” link via Page 95) who may be the *perpetrator/antagonist* rather than the old-man victim. Keep `P61` as victim-only and do not treat the Page 70 “he” as the victim without a second identifier.
  - **Phase 6 test (2026-01-01):** re-read Pages/cains_jawbone_page_68.md and Pages/cains_jawbone_page_69.md; “last crucial meeting with the old man” (p68) remains compatible with the late-night aftermath/witnessing posture (p69) but no shared prop/place/name anchor yet collapses the “old man” referent. Cross-check: keep `P61` (slow-death strand) separate from Pages/cains_jawbone_page_74.md’s Leningrad/OGPU “old man” (`P69`) until a second concrete identifier emerges.
  - **Phase 6 test (2026-01-02):** ran page-body df==2 token + df==2 trigram scans for Pages/cains_jawbone_page_68.md–Pages/cains_jawbone_page_70.md; found no second anchor that identifies the victim or ties the infancy/knee “he” to the slow-death scene (only scattered single-token overlaps and the isolated trigram `poor old man` with Pages/cains_jawbone_page_54.md). Keep `P61` as victim and murderer `UNKNOWN`.
  - **Falsifiers:** Later context shows the “old man” survives, the death is metaphorical, or the scene is revealed as purely recollected/hypothetical rather than witnessed.

- `E03` (confidence: `0.20`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_76.md
  - **Victim candidate(s):** `P72` (Green; named as “the victim”)
  - **Murderer candidate(s):** `P106` (narrator; identity unknown)
  - **Means/method:** `UNKNOWN` (the narrator frames intent/duty, but does not name a method on this page)
  - **Motive:** `UNKNOWN` (moralising “duty” register; possible personal grievance)
  - **Opportunity:** Narrator frames the need to “do the thing” personally, implying direct access to the victim.
  - **Narrative tells:** Heavy self-justification; de Quincey murder-aesthetics reference; explicit victim naming (“Green”).
  - **Evidence summary:** An in-world victim is explicitly named as “the victim” (Green), but the page ends with “I would have to think it over,” so treat as intent/planning until a later page establishes an in-world death outcome for Green.
  - **Falsifiers:** “Green” is not an in-world person, or the “victim” framing is hypothetical/metaphorical with no in-world harm.

- `E04` (confidence: `0.15`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_78.md
  - **Victim candidate(s):** `UNKNOWN` (soon-to-be dead woman; will/document subject)
  - **Murderer candidate(s):** `UNKNOWN`
  - **Means/method:** `UNKNOWN` (death is implied/anticipated; not described)
  - **Motive:** MAYBE inheritance/document control (forgery context)
  - **Opportunity:** Document is being guided by a “falser hand” before the woman’s death.
  - **Narrative tells:** “Mimic artistry” + “falser hand” strongly echoes will-forgery framing used elsewhere.
  - **Evidence summary:** The page anticipates a near-future death while describing document manipulation, but does not establish a killing act/outcome; treat as background-context threat setup until a later page confirms an in-world death event.
  - **Falsifiers:** The “soon to be dead” phrasing is metaphorical, or the document is unrelated to any death plot.

- `E05` (confidence: `0.10`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_80.md
  - **Victim candidate(s):** `P50` (Sir Paul Trinder)
  - **Murderer candidate(s):** `P107` (host narrator; identity unknown)
  - **Means/method:** aconite (aconitum) / Fleming’s tincture (as referenced) in the context of sherry
  - **Motive:** MAYBE connected to May (host wants to “do my best for May”)
  - **Opportunity:** Visitor arrives before lunch and is served drink while poisonous plant/preparation is foregrounded.
  - **Narrative tells:** “I am not incautious” + immediate move to exhibit aconitum reads like deliberate staging.
  - **Evidence summary:** This reads as the **setup** for the Sir Paul Trinder poisoning that culminates in the Pages/cains_jawbone_page_59.md → Pages/cains_jawbone_page_60.md “success” claim; keep the unified murder event in `E14` and treat `E05` as a supporting precursor record rather than a separate counted death event.
  - **Falsifiers:** Pages/cains_jawbone_page_80.md is shown to be a non-administrative specimen-demonstration scene unrelated to the Pages/cains_jawbone_page_59.md–Pages/cains_jawbone_page_60.md “figurehead beard” death, or Sir Paul Trinder is shown to survive unaffected by this visit.

- `E06` (confidence: `0.85`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_81.md
  - **Victim candidate(s):** `P75` (window victim; identity unknown)
  - **Murderer candidate(s):** `P104` (narrator; identity unknown)
  - **Means/method:** thrown from a window into water; LIKELY drowning
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Victim blocks the open window and is within physical reach; narrator has immediate means to push/heave the victim outward.
  - **Narrative tells:** Self-exculpation (“thank goodness, I was no detective”); black humour (“pulled up his socks… heaved outward”); deliberate death-wish framing (“He was asking for it”).
  - **Evidence summary:** The page narrates a direct killing act with intent and an explicit “victim” label; outcome is treated as likely fatal (“with any luck, was dead”).
  - **Falsifiers:** Later pages show the victim survives, or the whole incident resolves as a quoted story/metaphor rather than an in-world event.
  - **Phase 6 test (2026-01-02):** re-read Pages/cains_jawbone_page_81.md and cross-checked the only strong lexical bridge candidate (Pages/cains_jawbone_page_6.md) for any second continuity anchor; none found. Keep `E06` as an isolated in-world killing vignette until a later page identifies `P75` or `P104` by a shared cast/prop/time marker.

- `E07` (confidence: `0.10`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_89.md
  - **Victim candidate(s):** `P82` (signature-man; identity unknown)
  - **Murderer candidate(s):** `UNKNOWN` (narrator implies intent)
  - **Means/method:** `UNKNOWN`
  - **Motive:** MAYBE fear of exposure/blackmail (“good memory” + “signatures were his business”)
  - **Opportunity:** Narrator is in conversation immediately after being introduced to the target.
  - **Narrative tells:** Wordplay that reads like a literal threat (“That signed his death warrant. Well, signatures were his business.”).
  - **Evidence summary:** The page implies a decision to kill a newly introduced man, but no act or outcome is narrated; treat as a threat/intent cue until a later page establishes an in-world death for this target.
  - **Falsifiers:** “Death warrant” is purely idiomatic or comic wordplay with no subsequent in-world harm to this person.

- `E08` (confidence: `0.10`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_99.md
  - **Victim candidate(s):** `UNKNOWN` (prior “killed” referent; identity unclear; LIKELY non-human/idiomatic in the dog‑POV context)
  - **Murderer candidate(s):** `UNKNOWN` (dog‑POV narrator claims responsibility; could be metaphor/animal kill)
  - **Means/method:** `UNKNOWN`
  - **Motive:** `UNKNOWN`
  - **Opportunity:** `UNKNOWN`
  - **Narrative tells:** Casual aside (“she wasn’t the one I’d killed”) occurs inside a strongly dog-coded POV segment and is paired with four-foot/idiom pressure (“I had three more left”).
  - **Evidence summary:** The page contains a “killed” admission, but the surrounding dog‑POV register makes it more likely to be an animal-kill or idiom layer than one of the six in-world murders.
  - **Falsifiers:** Later pages explicitly identify a human victim for this “killed” admission and link it to a broader murder sequence.

- `E09` (confidence: `0.40`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_100.md
  - **Victim candidate(s):** `P41` (Alexander/Ecky narrator; identity inferred via `N01` cross-anchors)
  - **Murderer candidate(s):** MAYBE `P90` (gloating woman; role unclear)
  - **Means/method:** `UNKNOWN` (MAYBE heart failure; MAYBE poisoning/violence)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Antagonistic woman is physically present and “gloating” as narrator cannot rise; the scene ends with a valediction and a “drop” (“Good-bye, Henry. He drops awa…”).
  - **Narrative tells:** Direct incapacity (“believe me, I cannot” get up) + “how ill… about my heart” framing; Scotland Yard invoked; ambiguous “Henry” role (may be a person-name collision or an object-coded “handheld” Henry).
  - **Evidence summary:** Strong in-world collapse signal, but it is still unclear whether this is a completed death, an attempted killing, or purely rhetorical quotation-layer staging. Identity: multiple independent, non-quotation cross-anchors support treating Page 100 as part of the `P41` / `N01` Aquarius-handwriting narrator cluster (Pages/cains_jawbone_page_1.md “dead old man” ↔ Page 100 “old dead”; Pages/cains_jawbone_page_17.md ↔ Page 100 corpus-unique “Why should I think…” + `slips`). Do not assume `P01` Henry is involved: Page 100’s “Henry… getting out of hand” + “drops awa…” reads more consistently as a handheld object (LIKELY a pen) slipping from the narrator’s hand than as a coherent in-scene person.
  - **Phase 6 test (2026-01-01):** re-read Pages/cains_jawbone_page_100.md and cross-check Pages/cains_jawbone_page_1.md + Pages/cains_jawbone_page_17.md; the N01 linkage strengthens the “in-world collapse” reading, but agency remains unproven. Keep `P90` as a low-confidence candidate only.
  - **Phase 6 test (2026-01-04):** cross-checked Pages/cains_jawbone_page_1.md’s pen framing (“this little pen… has not had much work since it flew… for the dead old man”): Page 100’s parallel “Henry had worked for him” + the literalised “out of hand”/“drops awa” beat reads cleanly as **object-coded Henry** (pen/tool) rather than `P01` Henry. This supports an in-world collapse/incapacity reading but still does not establish death outcome or external agency.
  - **Falsifiers:** Later pages show the narrator remains intact/active after this moment, or clarify that the collapse language is purely figurative/quoted rather than an in-world medical crisis; or later context shows “Henry” here is a named person acting in a coherent in-world scene (disproving the object-coded reading).

- `E10` (confidence: `0.35`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_58.md
  - **Victim candidate(s):** `P92` (old family lawyer; Henry’s “third”)
  - **Murderer candidate(s):** `P01` (Henry)
  - **Means/method:** `UNKNOWN` (graphic bodily aftermath implies physical violence, but no method named)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Henry is described in direct proximity to the aftermath and is framed as the agent by the “third… victim” tally.
  - **Narrative tells:** Explicit victim counting (“his third”) + grotesque detail (“viscera”) suggest an in-world killing rather than a mere threat.
  - **Evidence summary:** Page 58 asserts a specific victim as Henry’s “third” with physical remains described, but this is a single-page claim inside a strongly allusive/genre register (Browning monologue + serial-counting) with no corroborating page naming this victim; downgrade until we can confirm this is in-world rather than embedded fiction/metaphor.
  - **Falsifiers:** A later page shows this “third… victim” framing is metaphor/genre exaggeration (or non-lethal “victim” usage), or a later page shows the lawyer alive/unrelated.

- `E11` (confidence: `0.35`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_58.md
  - **Victim candidate(s):** `P93` (intruding charlady; Henry’s “fourth”)
  - **Murderer candidate(s):** `P01` (Henry)
  - **Means/method:** `UNKNOWN`
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Henry is described stooping over “cooling remains” and is framed as the agent by the “fourth… victim” tally.
  - **Narrative tells:** Immediate physical proximity to a body (“cooling remains”) makes a non-literal reading harder, though still possible.
  - **Evidence summary:** Page 58 asserts a second victim as Henry’s “fourth,” with the body still present, but this is only asserted on one page and sits inside the same “Browning/genre” register; downgrade until corroborated as an in-world death.
  - **Falsifiers:** The scene is revealed as embedded fiction/metaphor (or non-lethal “victim” usage), or later pages show the charlady alive/unrelated.

- `E12` (confidence: `0.50`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_21.md, Pages/cains_jawbone_page_35.md, Pages/cains_jawbone_page_36.md
  - **Victim candidate(s):** `UNKNOWN` (Henry’s “latest victim” / buried corpse; additional victims implied by “crimson list”)
  - **Murderer candidate(s):** `P01` (Henry)
  - **Means/method:** `UNKNOWN`
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Henry is seen directly over a body with blood present (p21), later treated as an active manhunt target (p35), and is explicitly described as having buried a corpse (p36).
  - **Narrative tells:** “body of his latest victim”; “flying squad”; “crimson list”; “He had buried the corpse; only the eyes showed.”
  - **Evidence summary:** A coherent within-voice strand depicts Henry as a killer under police pursuit, with at least one in-world corpse explicitly present/hidden even if the victim’s identity is not yet recoverable from these pages alone.
  - **Falsifiers:** “Victim/corpse” language is consistently metaphorical (medical/stage), or the Henry on these pages is shown to be a different referent from the murderous Henry elsewhere (name collision).

- `E13` (confidence: `0.15`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_26.md, Pages/cains_jawbone_page_45.md
  - **Victim candidate(s):** `UNKNOWN` (at least two prior “killings” implied; “corpse of his own making”)
  - **Murderer candidate(s):** `P01` (Henry; identity may be overloaded)
  - **Means/method:** `UNKNOWN`
  - **Motive:** `UNKNOWN`
  - **Opportunity:** The pages assert prior killings and place Henry in proximity to a corpse, but do not establish a named victim or a full scene-mechanic continuity.
  - **Narrative tells:** “first two killings of his” (p26); “bending innocently over an innocent corpse of his own making” (p45).
  - **Evidence summary:** Treat as a low-confidence supporting echo for a murderous-Henry reading; the cross-narrator “Henry” label is heavily overloaded elsewhere, so do not count this as a distinct death event unless a later anchor ties these pages to a specific victim/method sequence.
  - **Falsifiers:** “killings/corpse” language is shown to be figurative or embedded-story content, or this Henry is proven to be a different identity from the killer-Henry strand (name collision).

- `E14` (confidence: `0.70`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_80.md, Pages/cains_jawbone_page_59.md, Pages/cains_jawbone_page_60.md
  - **Victim candidate(s):** `P50` (Sir Paul Trinder; “figurehead beard”)
  - **Murderer candidate(s):** `P107` (narrator; identity unknown)
  - **Means/method:** LIKELY poison (wolfsbane/aconite/gelsemium register across Pages/cains_jawbone_page_59.md + Pages/cains_jawbone_page_80.md)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Narrator is positioned to recount/influence events around a strange death investigation; later frames a specific “success” and a man “more dead”.
  - **Narrative tells:** Self-congratulatory “I had succeeded” + explicit death outcome language; suspicious pulpit “did the trick” phrasing.
  - **Evidence summary:** Pages/cains_jawbone_page_80.md foregrounds an aconitum/Fleming’s-tincture poisoning setup aimed at Sir Paul Trinder; Pages/cains_jawbone_page_59.md explicitly has Trinder “about,” and Pages/cains_jawbone_page_60.md claims a successful operation that leaves a “figurehead beard” to “plough the pseudo-scientific seas no more,” strongly matching Trinder’s introduced beard persona (Pages/cains_jawbone_page_53.md) and supporting an in-world death.
  - **Phase 6 test (2026-01-01):** re-read Pages/cains_jawbone_page_80.md, Pages/cains_jawbone_page_59.md, Pages/cains_jawbone_page_60.md; the poison setup (aconitum + sherry) → “bane… failed” pivot (with Trinder “about” + gelsemium) → “I had succeeded” + “figurehead beard… no more” payoff is internally consistent and reads as an in-world death outcome (no contradiction found).
  - **Falsifiers:** “Figurehead beard” is later clearly identified as someone other than Trinder, or the Pages/cains_jawbone_page_60.md “more dead” language is shown to be a quotation/metaphor with no in-world death.

- `E15` (confidence: `0.10`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_1.md
  - **Victim candidate(s):** `P91` (dead old man; identity unknown)
  - **Murderer candidate(s):** `UNKNOWN`
  - **Means/method:** `UNKNOWN` (death pre-dates the narrated “to-day” scene)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** `UNKNOWN`
  - **Narrative tells:** Offhand reference to prior work done “for the dead old man” suggests a real past death rather than a hypothetical.
  - **Evidence summary:** Page 1 establishes an in-world dead man in the narrator’s recent past, but gives no cause or agency; treat as background-context death (not yet one of the six) unless later pages tie it to a concrete murder method/agent.
  - **Falsifiers:** Later context shows the “dead old man” is purely allusive/quoted, or is explicitly unrelated to the in-world murders.

- `E16` (confidence: `0.05`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_33.md
  - **Victim candidate(s):** `UNKNOWN` (woman; “dead the same day”)
  - **Murderer candidate(s):** `UNKNOWN`
  - **Means/method:** `UNKNOWN`
  - **Motive:** `UNKNOWN`
  - **Opportunity:** `UNKNOWN`
  - **Narrative tells:** The page treats the woman as dead while the letter text plays with “dead and buried… still alive,” raising the chance of quotation/allusion rather than in-world fact.
  - **Evidence summary:** A death is asserted (“a woman, dead the same day”) but the surrounding epistolary material is ambiguous about whether this is in-world or quoted.
  - **Falsifiers:** The “dead the same day” framing is identified as an external quotation/citation rather than an in-world death.

- `E17` (confidence: `0.05`; status: `downgraded`)
  - **Pages:** Pages/cains_jawbone_page_46.md
  - **Victim candidate(s):** `UNKNOWN` (“Tom… in the matter of Jasmine”; LIKELY “tom”/tomcat, not a human victim)
  - **Murderer candidate(s):** `UNKNOWN`
  - **Means/method:** `UNKNOWN`
  - **Motive:** `UNKNOWN`
  - **Opportunity:** `UNKNOWN`
  - **Narrative tells:** The page’s dog-coded POV + De Quincey quotation layer strongly suggests “Tom… in the matter of Jasmine” is an animal/wordplay thread rather than a human murder admission.
  - **Evidence summary:** Treat as out-of-scope for the six human murders unless later pages force a human identity for “Tom” and tie the “Jasmine” matter to a broader in-world killing sequence.
  - **Falsifiers:** A later page clearly identifies “Tom” as a human victim in this strand, or explicitly links this “I killed” clause to one of the six in-world murders.

- `E18` (confidence: `0.35`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_77.md
  - **Victim candidate(s):** `UNKNOWN` (unnamed “first” victim; described via “bony ankles” warmth → cold)
  - **Murderer candidate(s):** `P105` (narrator; identity unknown)
  - **Means/method:** LIKELY hypodermic syringe (“Compact” model name); injection (substance unknown)
  - **Motive:** `UNKNOWN` (narrator distinguishes a “political” killing from “my own” as “understandable”)
  - **Opportunity:** Narrator is “alone again” immediately after the act and frames tactile contact with the victim.
  - **Narrative tells:** Self-positioning (“Don’t think me squeamish ; it was my first.”) + concrete bodily aftermath strongly signals an in-world killing, while the Spencer Perceval references read as a historical/allusive layer rather than the in-world victim’s identity.
  - **Evidence summary:** Page 77 contains a strong in-world first-murder confession with a named implement (“Compact”), but victim identity and linkage to other deaths remain unclear.
  - **Phase 6 test (2026-01-01):** re-read Pages/cains_jawbone_page_77.md; the act reads as in-world (warm→cold body aftermath + “alone again”), and `Compact` is plausibly physical (see `Indexes/objects_motifs.md` hypodermic “Compact” attestation), reducing the chance it is merely metaphorical.
  - **Phase 6 test (2026-01-02):** page-body df==2 scan found only weak lexical echoes: `ankles` + `cold` overlap with Pages/cains_jawbone_page_82.md, and `warrant` + `public` overlap with Pages/cains_jawbone_page_89.md. Re-reads suggest these are incidental (p82 is a table/dog scene; p89 is a deer/collops “signatures” threat scene). No second anchor (shared participant/prop/place/time) currently identifies the Page 77 victim or links this act to another in-world death event.
  - **Falsifiers:** “my first” is shown to refer to something non-lethal (or purely figurative), “Compact” is shown not to be a weapon/means of harm, or later pages explicitly identify the victim in a way that collapses this into a different event record.
