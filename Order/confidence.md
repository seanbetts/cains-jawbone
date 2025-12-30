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

- `E01` (confidence: `0.10`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_62.md
  - **Victim candidate(s):** `P59` (dead man; identity unknown)
  - **Murderer candidate(s):** `UNKNOWN`
  - **Means/method:** `UNKNOWN` (death already occurred by the time of narration)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** `UNKNOWN` (only timing detail: he spoke to narrator ~1 hour before “they came to take him away”)
  - **Narrative tells:** Framing stresses deceit (“heart… deceitful”) and a story told by a now-dead speaker; “take him away” hints at custody/institution.
  - **Evidence summary:** IN-WORLD death signal is present but agency/cause is not established on this page.
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
  - **Falsifiers:** Later context shows the “old man” survives, the death is metaphorical, or the scene is revealed as purely recollected/hypothetical rather than witnessed.

- `E03` (confidence: `0.35`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_76.md
  - **Victim candidate(s):** `P72` (Green; named as “the victim”)
  - **Murderer candidate(s):** `P106` (narrator; identity unknown)
  - **Means/method:** `UNKNOWN` (the narrator frames intent/duty, but does not name a method on this page)
  - **Motive:** `UNKNOWN` (moralising “duty” register; possible personal grievance)
  - **Opportunity:** Narrator frames the need to “do the thing” personally, implying direct access to the victim.
  - **Narrative tells:** Heavy self-justification; de Quincey murder-aesthetics reference; explicit victim naming (“Green”).
  - **Evidence summary:** An in-world victim is explicitly named as “the victim” (Green), but the page does not (by itself) prove the killing has already occurred.
  - **Falsifiers:** “Green” is not an in-world person, or the “victim” framing is hypothetical/metaphorical with no in-world harm.

- `E04` (confidence: `0.30`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_78.md
  - **Victim candidate(s):** `UNKNOWN` (soon-to-be dead woman; will/document subject)
  - **Murderer candidate(s):** `UNKNOWN`
  - **Means/method:** `UNKNOWN` (death is implied/anticipated; not described)
  - **Motive:** MAYBE inheritance/document control (forgery context)
  - **Opportunity:** Document is being guided by a “falser hand” before the woman’s death.
  - **Narrative tells:** “Mimic artistry” + “falser hand” strongly echoes will-forgery framing used elsewhere.
  - **Evidence summary:** The page explicitly anticipates a woman’s near-future death while describing document manipulation.
  - **Falsifiers:** The “soon to be dead” phrasing is metaphorical, or the document is unrelated to any death plot.

- `E05` (confidence: `0.35`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_80.md
  - **Victim candidate(s):** `P50` (Sir Paul Trinder)
  - **Murderer candidate(s):** `P107` (host narrator; identity unknown)
  - **Means/method:** aconite (aconitum) / Fleming’s tincture (as referenced) in the context of sherry
  - **Motive:** MAYBE connected to May (host wants to “do my best for May”)
  - **Opportunity:** Visitor arrives before lunch and is served drink while poisonous plant/preparation is foregrounded.
  - **Narrative tells:** “I am not incautious” + immediate move to exhibit aconitum reads like deliberate staging.
  - **Evidence summary:** A likely in-world poisoning setup involving a named target (Sir Paul) is described; Pages/cains_jawbone_page_59.md–Pages/cains_jawbone_page_60.md (see `E14`) contain a later “success” + “figurehead beard… no more” outcome claim consistent with a Trinder kill, which strengthens this as a true setup rather than mere didactic display.
  - **Falsifiers:** Later context shows no administration/ingestion, or the “figurehead beard” killed on Pages/cains_jawbone_page_60.md is clearly not Trinder.

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

- `E07` (confidence: `0.20`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_89.md
  - **Victim candidate(s):** `P82` (signature-man; identity unknown)
  - **Murderer candidate(s):** `UNKNOWN` (narrator implies intent)
  - **Means/method:** `UNKNOWN`
  - **Motive:** MAYBE fear of exposure/blackmail (“good memory” + “signatures were his business”)
  - **Opportunity:** Narrator is in conversation immediately after being introduced to the target.
  - **Narrative tells:** Wordplay that reads like a literal threat (“That signed his death warrant. Well, signatures were his business.”).
  - **Evidence summary:** The page implies a decision to kill a newly introduced man, but no act or outcome is narrated.
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

- `E09` (confidence: `0.35`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_100.md
  - **Victim candidate(s):** `UNKNOWN` (narrator collapse/possible death); MAYBE `P01` (Henry)
  - **Murderer candidate(s):** `UNKNOWN` (woman present; role unclear)
  - **Means/method:** `UNKNOWN` (MAYBE heart failure; MAYBE poisoning/violence)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Antagonistic woman is physically present and “gloating” as narrator cannot rise; Henry is “getting out of hand.”
  - **Narrative tells:** Valedictory framing (“Good-bye, Henry”); quoted lines about withdrawing and heart-illness; Scotland Yard invoked.
  - **Evidence summary:** Strong in-world crisis/death signal at the end of a segment, but agency and the exact victim(s) are not confirmed.
  - **Falsifiers:** Later pages show the narrator (and Henry) intact and the scene is revealed as rhetorical rather than an in-world death event.

- `E10` (confidence: `0.85`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_58.md
  - **Victim candidate(s):** `P92` (old family lawyer; Henry’s “third”)
  - **Murderer candidate(s):** `P01` (Henry)
  - **Means/method:** `UNKNOWN` (graphic bodily aftermath implies physical violence, but no method named)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Henry is described in direct proximity to the aftermath and is framed as the agent by the “third… victim” tally.
  - **Narrative tells:** Explicit victim counting (“his third”) + grotesque detail (“viscera”) suggest an in-world killing rather than a mere threat.
  - **Evidence summary:** Page 58 asserts a specific in-world victim as Henry’s “third” with physical remains described.
  - **Falsifiers:** The “third… victim” and “viscera” are shown to be metaphor/genre exaggeration, or refer to non-lethal “victim” usage (stage/medical/etc.).

- `E11` (confidence: `0.85`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_58.md
  - **Victim candidate(s):** `P93` (intruding charlady; Henry’s “fourth”)
  - **Murderer candidate(s):** `P01` (Henry)
  - **Means/method:** `UNKNOWN`
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Henry is described stooping over “cooling remains” and is framed as the agent by the “fourth… victim” tally.
  - **Narrative tells:** Immediate physical proximity to a body (“cooling remains”) makes a non-literal reading harder, though still possible.
  - **Evidence summary:** Page 58 asserts a second specific in-world victim as Henry’s “fourth,” with the body still present.
  - **Falsifiers:** The scene is revealed as embedded fiction/metaphor, or later pages show the “chardlady” alive/unrelated.

- `E12` (confidence: `0.45`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_21.md, Pages/cains_jawbone_page_45.md
  - **Victim candidate(s):** `UNKNOWN` (Henry’s “latest victim” / “corpse of his own making”)
  - **Murderer candidate(s):** `P01` (Henry)
  - **Means/method:** `UNKNOWN`
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Henry is seen directly over a body, with blood present, and later again over a corpse framed as his own doing.
  - **Narrative tells:** Repeated corpse/victim framing across pages suggests continuity in Henry’s role as killer (even if the specific victim is not named).
  - **Evidence summary:** Multiple pages depict Henry in immediate contact with a corpse/victim with blood, supporting an in-world death event tied to him.
  - **Falsifiers:** “Victim/corpse” language is consistently metaphorical (medical/stage), or these pages are shown to belong to different “Henry” identities.

- `E13` (confidence: `0.35`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_26.md, Pages/cains_jawbone_page_35.md, Pages/cains_jawbone_page_36.md
  - **Victim candidate(s):** `UNKNOWN` (at least two prior “killings” implied)
  - **Murderer candidate(s):** `P01` (Henry)
  - **Means/method:** `UNKNOWN`
  - **Motive:** `UNKNOWN`
  - **Opportunity:** The narration treats Henry’s killings as established history and links them to active pursuit (police “flying squad”) and corpse disposal (“buried the corpse; only the eyes showed”).
  - **Narrative tells:** “First two killings” + “crimson list” + police manhunt reads like serial killing rather than idle metaphor, but remains unconfirmed without named victims.
  - **Evidence summary:** These pages collectively strengthen the hypothesis that Henry has multiple in-world victims beyond those explicitly named on Page 58.
  - **Falsifiers:** The “killings” are shown to refer to performances/figures of speech, or the pages are not in the same narrative strand/“Henry”.

- `E14` (confidence: `0.65`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_59.md, Pages/cains_jawbone_page_60.md
  - **Victim candidate(s):** `P50` (Sir Paul Trinder; “figurehead beard”)
  - **Murderer candidate(s):** `P107` (narrator; identity unknown)
  - **Means/method:** LIKELY poison (wolfsbane/aconite/gelsemium register across Pages/cains_jawbone_page_59.md + Pages/cains_jawbone_page_80.md)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** Narrator is positioned to recount/influence events around a strange death investigation; later frames a specific “success” and a man “more dead”.
  - **Narrative tells:** Self-congratulatory “I had succeeded” + explicit death outcome language; suspicious pulpit “did the trick” phrasing.
  - **Evidence summary:** Pages/cains_jawbone_page_59.md explicitly has Trinder “about,” and Pages/cains_jawbone_page_60.md claims a successful operation that leaves a “figurehead beard” to “plough the pseudo-scientific seas no more,” strongly matching the introduced Sir Paul Trinder beard persona (Pages/cains_jawbone_page_53.md) and supporting an in-world death.
  - **Falsifiers:** “Figurehead beard” is later clearly identified as someone other than Trinder, or the Pages/cains_jawbone_page_60.md “more dead” language is shown to be a quotation/metaphor with no in-world death.

- `E15` (confidence: `0.20`; status: `active`)
  - **Pages:** Pages/cains_jawbone_page_1.md
  - **Victim candidate(s):** `P91` (dead old man; identity unknown)
  - **Murderer candidate(s):** `UNKNOWN`
  - **Means/method:** `UNKNOWN` (death pre-dates the narrated “to-day” scene)
  - **Motive:** `UNKNOWN`
  - **Opportunity:** `UNKNOWN`
  - **Narrative tells:** Offhand reference to prior work done “for the dead old man” suggests a real past death rather than a hypothetical.
  - **Evidence summary:** Page 1 establishes an in-world dead man in the narrator’s recent past, but gives no cause or agency.
  - **Falsifiers:** Later context shows the “dead old man” is purely allusive/quoted, or is explicitly unrelated to the in-world murders.

- `E16` (confidence: `0.10`; status: `active`)
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
  - **Means/method:** “Compact” (a named tool used by the narrator; likely a weapon/implement)
  - **Motive:** `UNKNOWN` (narrator distinguishes a “political” killing from “my own” as “understandable”)
  - **Opportunity:** Narrator is “alone again” immediately after the act and frames tactile contact with the victim.
  - **Narrative tells:** Self-positioning (“Don’t think me squeamish ; it was my first.”) + concrete bodily aftermath strongly signals an in-world killing, while the Spencer Perceval references read as a historical/allusive layer rather than the in-world victim’s identity.
  - **Evidence summary:** Page 77 contains a strong in-world first-murder confession with a named implement (“Compact”), but victim identity and linkage to other deaths remain unclear.
  - **Falsifiers:** “my first” is shown to refer to something non-lethal (or purely figurative), “Compact” is shown not to be a weapon/means of harm, or later pages explicitly identify the victim in a way that collapses this into a different event record.
