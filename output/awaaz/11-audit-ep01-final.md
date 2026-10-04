# AWAAZ Ep1 final cut: stringent frame-level audit

Source: `AWAAZ-EP01.m4v` (1080x1920, 24 fps, 60.0 s, -16 LUFS). Reviewed at 4 fps (240 frames, timestamped) plus the audio speech-activity windows from `tools/frame_audit.py`. The video was not changed. Method: `10-stringent-audit-protocol.md`.

Verdict: **FAIL on all four complaints** (sync, identity, handling, phone screens). Only the hook, the 5 s cut rhythm and the final freeze/overlay work.

## Hard cuts found
5, 10, 15, 20, 25, 30, 35, 42.25, 43.75, 45, 50, 55, 59.5 s. Every cut lands exactly on a 5 s grid: the edit is metronomic and no sound crosses a cut.

## Findings by clip (FAIL > 0.4 s or visible defect, SOFT = noticeable, OK)

| Clip / time | Category | Finding | Grade |
|---|---|---|---|
| C01 0-5 | Sync | Sushma's mouth moves 3.0-4.75 s; her only line ("Kabir?") is at 2.4-2.9 s. Mouth keeps going in silence. | FAIL |
| C01 | Restraint | Wide eyes, raised brows: more than the rule allows. | SOFT |
| C02 5-10 | Identity | A necklace appears (locked to none). Grade and background change at the cut. | FAIL |
| C02 | Restraint | Open-mouth crying 8.75-9.5 s. | FAIL |
| C03 10-15 | Handling | Phone lifted and rotated so the screen faces camera 13.75-14.0 s. Pencil and phone share the hand awkwardly. | FAIL |
| C03 | Sync | Kabir's mouth starts about 0.25-0.5 s before his line (13.0-13.8 s). | SOFT |
| C04 15-20 | Sync | Mouth starts about 0.4 s before the line at 18.4-19.5 s; moves with no audio 17.2-18.3 s. | FAIL |
| C04 | Object | Glasses go from head to nose 16.75-17.5 s (intended). | OK |
| C05 20-25 | Identity | Necklace visible again. | FAIL |
| C05 | Restraint | Mouth wide open in distress 21.75-22.5 s. | FAIL |
| C05 | Screen | UPI card overlay "RAHUL VERMA 40,000" 20.25-23.25 s is readable and correct. | OK |
| C06 25-30 | Handling | Kabir's arms: a third arm/forearm enters from the right at about 26.0 s while one hand is on the keyboard. Phone "creep" on the desk is not visible; phone is simply pushed. Riya's mug steams but is never tilted or sipped (static prop). | FAIL |
| C06 | Identity | Kabir here has rounder face and shorter hair than in C03. | SOFT |
| C06 | Sync | Riya 25.5-27.4 s and Kabir 27.7-28.8 s line up with mouths within 0.2 s. | OK |
| C06 | Restraint | Palm-open gesturing at 27.75-28.5 s is theatrical. | SOFT |
| C07 30-35 | Screen | Phone held with back/camera lenses toward the viewer (screen to her). Correct. Green reflection in her glasses is a good touch. | OK |
| C07 | Sync | Her line at 31.6-32.7 s matches the open mouth at 32.0-32.5 s. The phone voice at 33.1-34.7 s has a closed mouth. Correct. | OK |
| C07 | Physics | Phone at ear 30.0-30.75 s, then lowered at 31.0 s, though the script has the call on speaker. | SOFT |
| C07 | Overlay | Call banner 31.0-32.75 s works; "कॉल वेटिंग" text is tiny. | OK |
| C08 35-40 | Identity | Kabir's face is narrower than C06 (different jaw and hair). | FAIL |
| C08 | Sync | Kabir talks into the phone 36.0-36.5 s with no audio; his line is at 37.0-37.7 s. | FAIL |
| C08 | Handling | Phone goes from ear to hand to off-frame in 1 s (36.5-37.5 s). Riya's laptop rotates and the hands clasp over it in an unclear way (38.0-38.5 s). | FAIL |
| C09 40-45 | Screen | Laptop shows its lid, screen faces them; blue reflection on glasses. Correct. | OK |
| C09 | Sync | Riya 40.4-42.1 s: lips match. | OK |
| C09 42.25-43.75 | Assembly | Stage cutaway has no audio (silent gap 42.1-43.9 s). Man on stage talks and gestures in silence. Pencil sits in jacket pocket, jacket and face differ from desk Kabir. | FAIL |
| C09 43.75-45 | Sync | "Meri apni aawaaz" (43.9-44.9 s) is spoken while his hand covers his mouth 44.25-44.75 s. | FAIL |
| C10 45-50 | Identity | Corridor Kabir has curly hair, a rounder young face and stubble. Different person from the desk. | FAIL |
| C10 | Motion | He walks; script says sprint with jacket flying. No chair spin, no pencil drop. Mouth sync at 46.4-47.1 s is acceptable. | FAIL |
| C11 50-55 | Sync | Sushma's lips move 50.2-52.2 s while the voice playing is the scam call; it reads as her speaking in Kabir's voice. Her own line 53.0-54.0 s lines up well. | FAIL |
| C11 | Restraint | Wide open mouth 52.75-53.5 s. Tears: good. | SOFT |
| C12 55-59.5 | Screen | Phone screen is the focus (deliberate POV). Grok drew an incoming-call UI with tiny glyphs; fine under overlays. Thumb enters from a second hand at 55.75 s. | SOFT |
| C12 | Overlay | UPI card, call banner, caption and "EP 2" all read well; the freeze from 57 s works. The card sits on Sushma's left hand. | OK |
| Whole | Audio | Digital silence 3%, no room tone, no ringtone under C12. Loudness -16 LUFS is fine. | SOFT |

## Root causes
1. **Sync:** a clip is generated for 6 s with action spread across it, then cut to 5 s. Mouths run on with no line, because Grok animates the mouth for the entire clip. Dialogue sits in only 1-1.5 s of each clip.
2. **Identity:** each clip starts from a different keyframe; the contact sheet is not strong enough to hold a face when angle and lighting change. Kabir exists as three different men (C03/C06, C08/C09, C10/C11).
3. **Handling:** any two-hand or two-object action (phone + pencil, laptop + clasped hands, phone from ear to desk) fails in Grok. One object in one hand survives.
4. **Screens:** worked in clips where the screen faces the actor and the content was overlaid in post (C05, C07, C12). Failed wherever the screen was turned to camera.
5. **Edit:** hard cuts on a rigid 5 s grid and no audio bridges.

## Rules for the next video
1. Mouth discipline: say in every prompt "mouth closed and still except while speaking the line". Put the line in the middle second only (about 1.5-3.0 s). Trim clips tight around the line.
2. One speaker, one visible mouth, one line per clip. Never cover the mouth during a line.
3. Face lock: generate every keyframe from the same character sheet frame at the same angle family; use the same hair, glasses and stubble words in every prompt and reject any take where hair, jaw or glasses differ. Never use a corridor wide shot for a face you need to match; keep a medium close-up.
4. Add "no necklace, no jewellery except the stated bangles and nose stud" to every Sushma clip.
5. Handling budget: one object per hand per clip; no hand-offs, no ear-to-hand transitions, no clasped-over objects. Cut away between phone states (ear, lowered) instead of animating them.
6. Phones: screen toward the actor, lenses toward camera; screens carry overlays added in post. POV screen inserts only once per episode.
7. Motion: when the script says run, generate a rear or side tracking shot, not a frontal walk; add a hard SFX in post (chair, pencil) to sell the action.
8. Restraint: never "wide open mouth", "eyes wide"; use "slight tremble of the lip", "eyes glisten".
9. Edit: overlap audio across cuts by 0.2-0.3 s (J/L cuts), add room tone and ringtone beds in post, and score the stage cutaway with the recorded stage audio.
10. Review at 4 fps with `tools/frame_audit.py`; for each line, find the audio window, then check the lip start/stop frame against it before accepting the take.
