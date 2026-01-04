# Cast ledger

Track people as candidates with evolving roles. This file is deliberately probabilistic and reversible.

## Principles

- Use stable `Pxx` IDs from `Indexes/people.md` (do not invent new IDs here).
- Do not assume murder: only promote roles when supported by page-cited textual evidence.
- Always include falsifiers (what would disprove the role claim).
- Prefer **downgrading** over deleting so we keep an audit trail.

## Confidence conventions

- Confidence is numeric `0.0–1.0`; use `Skills/core/cjb-phase-playbook/SKILL.md` for shared mapping to `MAYBE/LIKELY/CERTAIN`.
- Adjust conservatively (usually ±0.05 per new anchor) unless the text is explicit.

## Template

- `Pxx`
  - **Aliases / names used:**  
  - **Role candidate:** `murderer` / `victim` / `witness` / `unknown`
  - **Confidence (0.0–1.0):**  
  - **Supporting pages:**  
  - **Evidence summary:**  
  - **Falsifiers:**  
  - **Status:** `active` / `downgraded` / `rejected`

## Entries

- `P01`
  - **Aliases / names used:** Henry
  - **Role candidate:** `murderer`
  - **Confidence (0.0–1.0):** 0.55
  - **Supporting pages:** Pages/cains_jawbone_page_21.md, Pages/cains_jawbone_page_35.md, Pages/cains_jawbone_page_36.md, Pages/cains_jawbone_page_45.md, Pages/cains_jawbone_page_58.md
  - **Evidence summary:** Strongest in-world kill evidence is within the Pages/cains_jawbone_page_21.md / Pages/cains_jawbone_page_35.md / Pages/cains_jawbone_page_36.md strand (blood + corpse burial + pursuit); treat Pages/cains_jawbone_page_58.md as low-weight corroboration only (possible embedded/genre register) and Pages/cains_jawbone_page_45.md as a low-weight echo given the overloaded “Henry” label.
  - **Falsifiers:** “Victim/corpse” language resolves as non-lethal (e.g., stage/medical metaphor), or `P01` conflates multiple distinct “Henrys” (including object-coded/assistant uses) and the murderous Henry is a different person from other Henry appearances.
  - **Status:** `active`

- `P41`
  - **Aliases / names used:** Alexander; “Ecky”
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.30
  - **Supporting pages:** Pages/cains_jawbone_page_1.md, Pages/cains_jawbone_page_17.md, Pages/cains_jawbone_page_43.md, Pages/cains_jawbone_page_100.md
  - **Evidence summary:** Treated as the likely `N01` Aquarius-handwriting narrator cluster (identity inferred via cross-page anchors), with Page 100 describing an in-world collapse/possible death (cannot rise; heart distress; valediction + “drops awa” beat). Phase 6 cross-check: Page 1’s pen is explicitly treated as having “work” for the dead old man, strengthening the reading that Page 100’s “Henry… getting out of hand”/“drops awa” beat refers to an object (pen/tool) slipping during incapacity rather than to `P01` Henry.
  - **Falsifiers:** Pages/cains_jawbone_page_100.md is purely quoted/metaphorical with no in-world collapse, Pages/cains_jawbone_page_100.md is shown to be a different narrator from the Aquarius/Moon+Dawn bundle, or later context shows this narrator survives and continues after Page 100.
  - **Status:** `active`

- `P90`
  - **Aliases / names used:** gloating woman; “wicked”/“beastly woman” (unnamed)
  - **Role candidate:** `murderer`
  - **Confidence (0.0–1.0):** 0.15
  - **Supporting pages:** Pages/cains_jawbone_page_100.md
  - **Evidence summary:** Present in the Page 100 collapse scene, physically looming and “gloating” as the narrator cannot rise; may be implicated, but the page does not explicitly state agency or outcome, and the “Good-bye, Henry… drops awa” beat reads more cleanly as object-coded (pen/tool) than as a human Henry death.
  - **Falsifiers:** The collapse resolves as natural illness/fainting with no external agency, or the woman is shown to be uninvolved/bystander (or purely a quotation-layer figure) in later linked context.
  - **Status:** `downgraded`

- `P104`
  - **Aliases / names used:** window-throw narrator (“no detective” voice; unknown)
  - **Role candidate:** `murderer`
  - **Confidence (0.0–1.0):** 0.70
  - **Supporting pages:** Pages/cains_jawbone_page_81.md
  - **Evidence summary:** Narrates a direct killing act (heaving a “victim” out of a window into water) with explicit intent and black-humour self-exculpation.
  - **Falsifiers:** The scene is later shown to be an embedded quotation/story rather than an in-world act, or later pages show the window victim survived.
  - **Status:** `active`

- `P105`
  - **Aliases / names used:** “Compact” murderer narrator (first murder; unknown)
  - **Role candidate:** `murderer`
  - **Confidence (0.0–1.0):** 0.55
  - **Supporting pages:** Pages/cains_jawbone_page_77.md
  - **Evidence summary:** Confesses a first killing (“it was my first”) and describes immediate bodily aftermath (warm→cold ankles), naming the implement “Compact” (LIKELY a portable hypodermic syringe model; see `Indexes/objects_motifs.md`).
  - **Falsifiers:** “my first” is shown to be non-lethal/metaphorical, “Compact” is not a means of harm, or this narrator is later identified as the same person as `P107` (making the murder count/identity model need revision).
  - **Status:** `active`

- `P106`
  - **Aliases / names used:** Green-target narrator (De Quincey “tooling” moral-calculus voice; unknown)
  - **Role candidate:** `murderer`
  - **Confidence (0.0–1.0):** 0.20
  - **Supporting pages:** Pages/cains_jawbone_page_76.md
  - **Evidence summary:** Frames an intended killing as a personal “duty” and explicitly names “Green” as “the victim,” but no outcome is established yet; treat as intent until a later page confirms an in-world death.
  - **Falsifiers:** “Green” is shown not to be an in-world person/victim, or the “victim” framing is purely hypothetical/metaphorical.
  - **Status:** `downgraded`

- `P107`
  - **Aliases / names used:** poison-logistics host narrator (aconite/digitalis/gelsemium; unknown)
  - **Role candidate:** `murderer`
  - **Confidence (0.0–1.0):** 0.45
  - **Supporting pages:** Pages/cains_jawbone_page_6.md, Pages/cains_jawbone_page_21.md, Pages/cains_jawbone_page_29.md, Pages/cains_jawbone_page_35.md, Pages/cains_jawbone_page_36.md, Pages/cains_jawbone_page_59.md, Pages/cains_jawbone_page_60.md, Pages/cains_jawbone_page_80.md
  - **Evidence summary:** Repeated poison-means staging (digitalis/gelsemium/aconite) and a claimed death-success register (Pages 59–60), now with a strengthened read that the “figurehead beard” death is Sir Paul Trinder (Pages 53, 59–60), plus a hosted aconite setup aimed at Sir Paul (Page 80).
  - **Falsifiers:** The poison scenes are later shown to be non-administrative (no ingestion/outcome), the “success” language resolves as figurative/quoted, or the pages are shown not to belong to a single narrator/person.
  - **Status:** `active`

- `P92`
  - **Aliases / names used:** “old family lawyer” (unnamed)
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.35
  - **Supporting pages:** Pages/cains_jawbone_page_58.md
  - **Evidence summary:** Referred to as Henry’s “third” victim with explicit bodily aftermath (“viscera”), but the claim appears only on a single page inside a strongly allusive/genre register; treat as a provisional in-world victim pending corroboration.
  - **Falsifiers:** The passage is revealed as metaphor/embedded fiction (or non-lethal “victim” usage), or later pages show the lawyer alive/unrelated.
  - **Status:** `downgraded`

- `P93`
  - **Aliases / names used:** “rash intruding charlady” (unnamed)
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.35
  - **Supporting pages:** Pages/cains_jawbone_page_58.md
  - **Evidence summary:** Referred to as Henry’s “fourth” victim with “cooling remains” present, but asserted only on a single page and not corroborated elsewhere; treat as a provisional in-world victim pending confirmation.
  - **Falsifiers:** The “fourth… victim” framing is metaphorical/embedded-fiction (or non-lethal “victim” usage), or later pages show the charlady alive/unrelated.
  - **Status:** `downgraded`

- `P91`
  - **Aliases / names used:** “dead old man”
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.10
  - **Supporting pages:** Pages/cains_jawbone_page_1.md
  - **Evidence summary:** Mentioned as already dead (“the dead old man”) in a context implying prior narrative work done for him; treat as background-context death unless later pages connect it to a concrete murder method/agent.
  - **Falsifiers:** Later context shows this is a purely allusive/quoted “dead old man” rather than an in-world person, or the death is unrelated to the book’s six in-world murders.
  - **Status:** `downgraded`

- `P48`
  - **Aliases / names used:** Hal
  - **Role candidate:** `unknown`
  - **Confidence (0.0–1.0):** 0.05
  - **Supporting pages:** Pages/cains_jawbone_page_46.md
  - **Evidence summary:** Appears inside a strongly dog-coded POV segment; the “not the one I killed in the matter of Jasmine” phrasing most likely refers to an animal (“Tom”/tomcat) rather than a human murder.
  - **Falsifiers:** A later page shows “Hal” committing/ordering a clearly in-world human killing, or explicitly links “the matter of Jasmine” to one of the six human murders rather than an animal/idiom.
  - **Status:** `downgraded`

- `P59`
  - **Aliases / names used:** “dead man”
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.05
  - **Supporting pages:** Pages/cains_jawbone_page_62.md
  - **Evidence summary:** Referred to explicitly as “the dead man”; treat as background-context death unless later pages connect it to a concrete murder method/agent.
  - **Falsifiers:** Later context shows “dead man” is metaphorical, purely quoted, or refers to a historical/fictional figure rather than an in-world person.
  - **Status:** `downgraded`

- `P61`
  - **Aliases / names used:** “poor old man”; “old man”
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.35
  - **Supporting pages:** Pages/cains_jawbone_page_68.md, Pages/cains_jawbone_page_69.md, Pages/cains_jawbone_page_70.md
  - **Evidence summary:** Narrator claims to have seen him “done slowly to death”; later pages suggest a connected retaliation/blackmail dynamic.
  - **Falsifiers:** “Done slowly to death” resolves as figurative or the “old man” in these pages is shown to be multiple different people.
  - **Status:** `active`

- `P72`
  - **Aliases / names used:** Green
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.25
  - **Supporting pages:** Pages/cains_jawbone_page_76.md
  - **Evidence summary:** Explicitly named as “the victim” (Green) in a murder-planning register, but no in-world death outcome is established yet.
  - **Falsifiers:** “Green” is revealed as a non-personal epithet/joke (not an in-world person), or the page’s “victim” framing is shown to be hypothetical/metaphorical with no in-world death.
  - **Status:** `downgraded`

- `P50`
  - **Aliases / names used:** Sir Paul Trinder
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.65
  - **Supporting pages:** Pages/cains_jawbone_page_53.md, Pages/cains_jawbone_page_59.md, Pages/cains_jawbone_page_60.md, Pages/cains_jawbone_page_80.md
  - **Evidence summary:** Introduced with a distinctive beard; later Trinder is explicitly “about” during poison-register staging, and the narrator claims a “success” leaving a “figurehead beard” to “plough… no more,” strongly consistent with an in-world Trinder death.
  - **Falsifiers:** “Figurehead beard” is confirmed as someone else, or Trinder is later shown alive/unharmed and the death language resolves as allusive/figurative.
  - **Status:** `active`

- `P75`
  - **Aliases / names used:** window victim (unnamed)
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.85
  - **Supporting pages:** Pages/cains_jawbone_page_81.md
  - **Evidence summary:** Referred to explicitly as “the victim” and then physically “heaved outward” from a window with drowning intent (“Go find the bottom!”).
  - **Falsifiers:** Later pages show the scene is metaphorical/quoted, or the victim is shown alive/otherwise unharmed after the window incident.
  - **Status:** `active`

- `P82`
  - **Aliases / names used:** signature-man (unnamed “ancient”)
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.10
  - **Supporting pages:** Pages/cains_jawbone_page_89.md
  - **Evidence summary:** Narrator frames a newly introduced man as doomed (“That signed his death warrant”) with punning emphasis on his signature business, but no in-world death is established yet.
  - **Falsifiers:** “Death warrant” resolves as a purely idiomatic joke, or the man is later shown to be unharmed and unrelated to in-world murders.
  - **Status:** `downgraded`
