# LLM and video-model pipeline

Use this when the user wants footage, an avatar, a dubbed cut, or a prompt pack another model can shoot.

This skill writes story. It does not render finished frames, thumbnails, or motion.

## Package the model can ingest

Emit a single markdown or JSON-shaped brief with stable headings. Stable names let a downstream model and a human checker find the same field every time.

```
meta.format
meta.mode            # retrospective | prospective
meta.runtime_seconds
meta.language        # BCP-47 code, for example en-IN, hi-IN
meta.aspect          # 16:9 long-form or 9:16 Short
meta.synthetic       # none | avatar | cloned_voice | generated_footage
spine
why
ledger[]             # id, fact. Every claim below cites these ids
cast                 # who may appear, what they will not do
no_go[]              # what the creator will not show or fake
locations
acts[]               # clock, beat, src, rasa, conflict, spoken, visual, sfx, safety
titles[]
thumbnail_brief
forbidden            # events not to invent, faces and voices not to clone
open_items[]         # every GAP, unapproved STAGE, ledger conflict, disclosure
```

`src` on each act is `F#`, `STAGE`, or `GAP`. A downstream model must treat `GAP` as "do not generate" and `STAGE` as "do not generate until approved".

Keep spoken lines under 18 words per shot unless the user wants a talking-head essay.

A compact JSON example:

```json
{
  "meta": {"format": "long", "mode": "retrospective", "runtime_seconds": 600,
           "language": "en-IN", "aspect": "16:9", "synthetic": "none"},
  "spine": "When Neha wants to reach the far wall ...",
  "ledger": [{"id": "F1", "fact": "Neha has a fear of deep water"}],
  "acts": [{"clock": "0:00", "beat": "cold_open", "src": ["F1"],
            "rasa": "Bhayanaka", "spoken": "", "visual": "Feet at the pool edge",
            "sfx": "Echoing pool hall", "safety": ""}],
  "open_items": ["GAP: what the instructor actually said at 5:40"]
}
```

## Shot grammar that serves the method

- Open on the mismatch, not on a bedroom alarm clock.
- Cut away from the face when the conflict is an object or a place.
- Hold long enough on the human crumb that it reads as a person.
- Do not generate a cry, a crash, or a crowd reaction the user did not authorize. A generated one is a fabricated event.
- End on a still image of the change (helmet box, zero bill, shared plate), from real footage or a labeled reenactment. Then black.

## Prospective runs

When the shoot is ahead, `acts[]` becomes a capture list: what to film, what to record as sound, and the questions to answer on camera at the end. Every act is `STAGE` with a safety line. The lines for the change beat are a `GAP`.

## Avatar, TTS, and cloned voice

If the creator is an avatar or synthetic voice, truth still applies to the claims. An animated host may not narrate a childhood they do not have. Write Y as the project's present-tense motive, not a fake memoir. Do not clone a real person's face or voice without their consent. Set `meta.synthetic` and add the platform's synthetic-media disclosure to Open items where the content looks realistic. Policies change, so tell the creator to check the current ones.

## Multilingual dub

Translate the spoken lines with the translation guide. Keep shot clocks identical so one picture track serves N languages. Do not retime the climax per language. Provenance tags and `GAP` placeholders carry over unchanged.

## What to hand a human editor

Beat sheet with clocks, a select list ("use the real train audio here"), and a do-not-use list. Editors kill truth when they add stock cry or stock cheer. Say so. Sound cues describe the sound. They do not name a copyrighted track.

## Design handoff

After this skill locks the title and the mismatch sentence, pass those two lines to whatever draws the thumbnail, poster, or bumper (another skill, a design model, or a human editor). Do not invent pixels here.
