# LLM and video-model pipeline

Use this when the user wants footage, an avatar, a dubbed cut, or a prompt pack another model can shoot.

This skill writes story. It does not replace visual-craft for finished frames.

## Package the model can ingest

Emit a single markdown or JSON-shaped brief with stable headings

```
meta.format
meta.runtime_seconds
meta.language
meta.aspect          # 16:9 long-form or 9:16 Short
spine
why
cast                 # who may appear, what they will not do
locations
acts[]               # clock, beat name, rasa, conflict, spoken lines, visual, sfx
titles[]
thumbnail_brief
forbidden            # events not to invent, faces not to clone
```

Keep spoken lines under 18 words per shot unless the user wants a talking-head essay.

## Shot grammar that serves the method

- Open on the mismatch, not on a bedroom alarm clock.
- Cut away from the face when the conflict is an object or a place.
- Hold long enough on the human crumb that it reads as a person.
- Do not generate a cry, a crash, or a crowd reaction the user did not authorize.
- End on a still image of the change (helmet box, zero bill, shared plate). Then black.

## Avatar / TTS

If the creator is an avatar, truth still applies to the claims. An animated host may not narrate a childhood they do not have. Write Y as a present-tense motive of the project, not a fake memoir.

## Multilingual dub

Translate the spoken lines with the translation guide. Keep shot clocks identical so one picture track serves N languages. Do not retime the climax per language.

## What to hand a human editor

Beat sheet with clocks, a select list ("use the real train audio here"), and a do-not-use list. Editors kill truth when they add stock cry or stock cheer. Say so.

## Visual skill handoff

Thumbnails, posters, and motion bumpers go through visual-craft after this skill locks the title and the mismatch sentence.
