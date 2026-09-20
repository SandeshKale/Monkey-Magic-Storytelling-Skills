---
name: youtube-storytelling
description: Plan, script, localize, and package YouTube long-form videos and Shorts using the Monkey Magic free storytelling course. Use when the user wants a YouTube script, vlog structure, hook, title and thumbnail pack, Shorts loop, video brief for an LLM or video model, translation of a storytelling framework, retention architecture, rasa map, three-act beat sheet, or help turning a real incident into a story instead of an anecdote.
license: MIT
metadata:
  type: workflow
  version: "1.0"
  source_playlist: https://www.youtube.com/playlist?list=PLG3pPBnwP3-Y
  source_channel: Monkey Magic ((conversations))
  instructor: Raunaq Sahni
---

# YouTube Storytelling

Turn a real incident, idea, or brief into a YouTube video package an LLM or video model can shoot, voice, or animate. Encode the Monkey Magic free course as operational rules, not film-school theory.

Source course (attribute, do not plagiarize voice or claim authorship) — [references/source-and-attribution.md](references/source-and-attribution.md).

## Load order

1. This file.
2. [references/glossary.md](references/glossary.md) if terms collide.
3. The one module that matches the ask. Do not load every reference.
4. [references/script-templates.md](references/script-templates.md) before writing spoken lines.
5. [references/llm-video-pipeline.md](references/llm-video-pipeline.md) when the output is for a video model, avatar, or multilingual dub.
6. [references/translation-guide.md](references/translation-guide.md) when the user wants another language.
7. [references/audit-checklist.md](references/audit-checklist.md) before handing work back.

Module map

| Ask | File |
|---|---|
| Is this even a story | [references/01-what-is-a-story.md](references/01-what-is-a-story.md) |
| Make it dramatic | [references/02-drama.md](references/02-drama.md) |
| Goal, stakes, obstacles | [references/03-conflict.md](references/03-conflict.md) |
| Plot vs character, 70/30 | [references/04-plot-and-character.md](references/04-plot-and-character.md) |
| Daily vlog, vulnerability | [references/05-character-vlogs.md](references/05-character-vlogs.md) |
| Emotion mix, Navras | [references/06-rasa.md](references/06-rasa.md) |
| Beginning middle end | [references/07-three-act.md](references/07-three-act.md) |
| Why this video exists | [references/08-motivation-structure.md](references/08-motivation-structure.md) |
| Full long-form recipe | [references/09-perfect-recipe.md](references/09-perfect-recipe.md) |
| Dissect or clone a format | [references/10-examples-dissection.md](references/10-examples-dissection.md) |
| Shorts | [references/11-shorts.md](references/11-shorts.md) |
| Honesty pass | [references/12-truth.md](references/12-truth.md) |
| Pick a genre | [references/video-types.md](references/video-types.md) |

Copy-ready canvases live in `assets/`.

## Hard rules

- A story is change in the character's mindset. An anecdote is an incident with no change. Reject anecdote scripts.
- Drama is a character in a situation they do not belong in. Invent mismatch, do not invent events.
- Conflict is the problem between the character and the goal. Stronger antagonist, stronger hero. Multiple small conflicts beat one flat goal.
- Character beats plot. Aim 70 percent character, 30 percent idea. Viewers subscribe to a person, not a premise.
- Truth first. Structure second. Never fake tears, stakes, or a life the creator does not have.
- YouTube openings skip world-building. First 30 seconds carry the inciting incident, the why, and a promise of change.
- YouTube endings cut at the payoff. Do not walk the character home.
- Long-form needs 4 to 6 rasas. One-emotion videos bore. Mix entertainment, education, and inspiration.
- Shorts need a loop, progressive reveal, and 75 percent-plus intended retention. They must be a compressed sibling of the long-form, not a different channel.
- Titles are dramatic and idea-first. Thumbnails match the title's drama. Do not write clickbait the video cannot pay off.
- Translate meaning, not slang. Keep the framework names stable across languages so models can reuse them.

## Default intake (ask only what is missing)

Batch unknowns. Do not invent a creator's life.

1. Format — long-form, Short, series episode, daily vlog, hybrid
2. Language and market
3. Creator identity — who they are on camera, what they will not fake
4. Raw incident or idea (facts only)
5. Character goal and what is at stake if they fail
6. Antagonist — person, system, weather, object, self
7. Why this video exists beyond views
8. Intended change in the character by the last frame
9. Runtime target
10. Deliverable — script, beat sheet, shot list, title pack, video-model brief, or localized package

If the user dumps notes, extract a beat sheet yourself and confirm only the risky choices (truth, why, change, title).

## Workflow

### 1. Classify the raw material

Label it story or anecdote. If anecdote, find the real change or refuse to script a vlog of routine. See 01.

### 2. Lock the spine

Write one line in this shape

When [character] wants [goal] but [antagonist / mismatch] stands in the way, they [struggle], and leave [changed].

If you cannot fill every bracket with something true, stop and ask.

### 3. Choose video type

Idea-based, personalized vlog, or hybrid (preferred). See [references/video-types.md](references/video-types.md).

### 4. Map acts onto YouTube time

- Act 1 compressed — idle world in one sentence, then inciting incident.
- Act 2 — point of no return plus stacked conflicts.
- Climax — do-or-die, peak rasa.
- Act 3 — change visible, then cut.

See 07 and 08.

### 5. Season with rasa and EEI

Mark 4 to 6 rasas on the beat sheet. Confirm the video is not only funny or only sad. Confirm a mix of entertainment, education, inspiration. See 06.

### 6. Write the package

Produce, in order

1. Title options (3-5), idea-first and dramatic
2. Thumbnail brief (one sentence of visible drama)
3. One-line spine
4. Why (spoken in the first 30-45 seconds)
5. Beat sheet with timestamps
6. Spoken script or voiceover
7. B-roll and sound cues
8. End-screen CTA that does not kill the ending
9. If requested — video-model prompt pack and localized twin

Use templates in [references/script-templates.md](references/script-templates.md) and canvases in `assets/`.

### 7. Audit

Run [references/audit-checklist.md](references/audit-checklist.md). Fail the draft if there is no change, no mismatch, no why, no truth, or a dragged ending.

## Output shape

Default to a single markdown package the user can paste into a doc or a video model. Do not lecture the course back. Apply it.

When the user only wants a translation of the framework, output a clean glossary plus the beat-sheet labels in the target language, keeping English keys in parentheses.

## What this skill does not do

- Does not generate fake diary events or manufactured trauma.
- Does not replace visual-craft for thumbnails, posters, or motion.
- Does not publish to YouTube.
- Does not copy Monkey Magic scripts, voice, or journeys. Use the method. Invent nothing that belongs to Raunaq Sahni's life.
