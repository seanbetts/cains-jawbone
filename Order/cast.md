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
  - **Confidence (0.0–1.0):** 0.60
  - **Supporting pages:** Pages/cains_jawbone_page_21.md, Pages/cains_jawbone_page_35.md, Pages/cains_jawbone_page_36.md, Pages/cains_jawbone_page_45.md, Pages/cains_jawbone_page_58.md
  - **Evidence summary:** Repeatedly framed with victims/corpses and a numbered victim list: seen over “the body of his latest victim” with blood; linked to corpse-burial; described with an ongoing “crimson list”; explicitly tallied “third” and “fourth” victims.
  - **Falsifiers:** “Victim/corpse” language resolves as non-lethal (e.g., stage/medical metaphor), or `P01` conflates multiple distinct “Henrys” and the murderous Henry is a different person from other Henry appearances.
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
  - **Confidence (0.0–1.0):** 0.15
  - **Supporting pages:** Pages/cains_jawbone_page_1.md
  - **Evidence summary:** Mentioned as already dead (“the dead old man”) in a context implying prior narrative work done for him.
  - **Falsifiers:** Later context shows this is a purely allusive/quoted “dead old man” rather than an in-world person, or the death is unrelated to the book’s six in-world murders.
  - **Status:** `active`

- `P48`
  - **Aliases / names used:** Hal
  - **Role candidate:** `murderer`
  - **Confidence (0.0–1.0):** 0.10
  - **Supporting pages:** Pages/cains_jawbone_page_46.md
  - **Evidence summary:** States “not the one I killed in the matter of Jasmine”, implying a prior killing of “Tom” connected to “Jasmine”.
  - **Falsifiers:** The passage is confirmed as animal POV and “Tom” is an animal (or the line is idiomatic/metaphorical), making it irrelevant to the six human murders.
  - **Status:** `active`

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
  - **Supporting pages:** Pages/cains_jawbone_page_76.md, Pages/cains_jawbone_page_77.md
  - **Evidence summary:** Explicitly named as “the victim” (Green); adjacent page reflects on a “first” killing, plausibly tied to that victim.
  - **Falsifiers:** “Green” is revealed as a non-personal epithet/joke, or Page 77’s “my first” is unrelated to the named victim.
  - **Status:** `active`

- `P50`
  - **Aliases / names used:** Sir Paul Trinder
  - **Role candidate:** `victim`
  - **Confidence (0.0–1.0):** 0.40
  - **Supporting pages:** Pages/cains_jawbone_page_53.md, Pages/cains_jawbone_page_59.md, Pages/cains_jawbone_page_60.md, Pages/cains_jawbone_page_80.md
  - **Evidence summary:** Introduced with a distinctive beard; later a detective-sergeant is investigating a strange death while Trinder is “about”; a subsequent “success” claim suggests a “figurehead beard” will “plough… no more” (possibly Trinder); separately, aconitum/Fleming’s tincture is foregrounded in a hosted sherry scene.
  - **Falsifiers:** “Figurehead beard” is confirmed as someone else, or Trinder is later shown alive/unharmed and the poison framing resolves as non-lethal or unrelated.
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
  - **Confidence (0.0–1.0):** 0.20
  - **Supporting pages:** Pages/cains_jawbone_page_89.md
  - **Evidence summary:** Narrator frames a newly introduced man as doomed (“That signed his death warrant”) with punning emphasis on his signature business.
  - **Falsifiers:** “Death warrant” resolves as a purely idiomatic joke, or the man is later shown to be unharmed and unrelated to in-world murders.
  - **Status:** `active`
