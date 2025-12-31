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
  - **Evidence summary:** Strongest in-world kill evidence is within the Pages/cains_jawbone_page_21.md / Pages/cains_jawbone_page_35.md / Pages/cains_jawbone_page_36.md strand (blood + corpse burial + pursuit), with additional murder-counting corroboration on Pages/cains_jawbone_page_58.md; treat Pages/cains_jawbone_page_45.md as a low-weight echo given the overloaded “Henry” label.
  - **Falsifiers:** “Victim/corpse” language resolves as non-lethal (e.g., stage/medical metaphor), or `P01` conflates multiple distinct “Henrys” (including object-coded/assistant uses) and the murderous Henry is a different person from other Henry appearances.
  - **Status:** `active`

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
  - **Evidence summary:** Confesses a first killing (“it was my first”) and describes immediate bodily aftermath, while naming the implement “Compact”.
  - **Falsifiers:** “my first” is shown to be non-lethal/metaphorical, “Compact” is not a means of harm, or this narrator is later identified as the same person as `P107` (making the murder count/identity model need revision).
  - **Status:** `active`

- `P106`
  - **Aliases / names used:** Green-target narrator (De Quincey “tooling” moral-calculus voice; unknown)
  - **Role candidate:** `murderer`
  - **Confidence (0.0–1.0):** 0.30
  - **Supporting pages:** Pages/cains_jawbone_page_76.md
  - **Evidence summary:** Frames an intended killing as a personal “duty” and explicitly names “Green” as “the victim,” but the page does not (alone) prove the act is completed.
  - **Falsifiers:** “Green” is shown not to be an in-world person/victim, or the “victim” framing is purely hypothetical/metaphorical.
  - **Status:** `active`

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
  - **Confidence (0.0–1.0):** 0.90
  - **Supporting pages:** Pages/cains_jawbone_page_58.md
  - **Evidence summary:** Referred to as Henry’s “third” victim with explicit bodily aftermath (“viscera”).
  - **Falsifiers:** The passage is revealed as metaphor/genre exaggeration, or “third… victim” is shown to refer to something other than an in-world death.
  - **Status:** `active`

- `P93`
  - **Aliases / names used:** “rash intruding charlady” (unnamed)
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.90
  - **Supporting pages:** Pages/cains_jawbone_page_58.md
  - **Evidence summary:** Referred to as Henry’s “fourth” victim with “cooling remains” immediately present.
  - **Falsifiers:** The “fourth… victim” framing is metaphorical/embedded-fiction, or later pages show the charlady is alive and the scene is non-literal.
  - **Status:** `active`

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
  - **Confidence (0.0–1.0):** 0.10
  - **Supporting pages:** Pages/cains_jawbone_page_62.md
  - **Evidence summary:** Referred to explicitly as “the dead man”; told narrator a story shortly before being “taken away”.
  - **Falsifiers:** Later context shows “dead man” is metaphorical, purely quoted, or refers to a historical/fictional figure rather than an in-world person.
  - **Status:** `active`

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
  - **Confidence (0.0–1.0):** 0.45
  - **Supporting pages:** Pages/cains_jawbone_page_76.md
  - **Evidence summary:** Explicitly named as “the victim” (Green) in a self-justifying murder-planning register.
  - **Falsifiers:** “Green” is revealed as a non-personal epithet/joke (not an in-world person), or the page’s “victim” framing is shown to be hypothetical/metaphorical with no in-world death.
  - **Status:** `active`

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
