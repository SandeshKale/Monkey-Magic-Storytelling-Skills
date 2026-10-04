# AWAAZ Episode 1, v2 rebuild: 15-second clips at 480p

Rebuild approved under `11-audit-ep01-final.md` and all ten of its rules, plus the standing realism, physics and subtle-acting rules. The old 12-clip plan (`04-ep01-clip-prompts.md`) is retired. The story, the 60-second length and the lines are the same, trimmed to the lines that earn their place.

## What changed and why

| Audit finding | Rule applied here |
|---|---|
| Mouths moved with no line (3.0-4.75 s, 36.0 s) | Every ANIMATE prompt says `MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE`, with timed speaking windows. Every line sits mid-shot. |
| Early or late lips (0.4 s) | Windows are planned, then checked at 4 fps against the audio (see `00-review-checklist.md`, item 9). |
| Phone voice over a moving mouth (50.2-52.2 s) | The phone voice is only placed while the listener's mouth is closed. It is never generated in the shot. |
| Mouth covered during a line (44.25 s) | No line is spoken with a hand on the mouth. The old line 17 is dropped. |
| Three different Kabirs, a necklace | One canonical face frame per character, an identical face-lock block in every prompt, medium close-up only, 'no necklace' in every Sushma prompt. |
| Handling failures | A handling budget per shot: one object per hand, no ear-to-hand transitions, screens toward the actor, glasses never moved. |
| Walk instead of run | The run is a rear tracking shot. His face is never needed. |
| Silent stage cutaway | The stage cutaway is its own shot with its own spoken audio (INS-A). |
| Metronomic 5 s cuts | Shots run 4.5-12 s with planned J and L audio overlaps. |

## The plan: 60 seconds in 7 shots (plus 2 short inserts)

Format: Grok Imagine, 15-second clips, 480p, 9:16. Generate every shot at 15 s; the beats are spread over the whole 15 s; the edit uses only the KEEP window and the rest is a safe hold. Upscale to 1080x1920 in post (Lanczos, light sharpening, film grain).

| Shot | Edit time | Length | Place | Speaker (visible mouth) | Lines | KEEP from the 15 s clip |
|---|---|---|---|---|---|---|
| S1 | 0.0-12.0 | 12.0 | Pune kitchen | Sushma | 2 own + 2 phone | 0.0-12.0 |
| S2 | 12.0-19.0 | 7.0 | Bengaluru desk | Kabir | 1 | 1.0-8.0 |
| S3 | 19.0-29.0 | 10.0 | Pune table | Sushma | 2 own + 1 phone | 1.0-11.0 |
| S4 | 29.0-39.0 | 10.0 | Bengaluru desk | Riya | 2 own + 1 off-screen Kabir | 1.0-11.0 |
| S5 | 39.0-47.5 | 8.5 (4.5 + INS-A 4.0) | Bengaluru desk | none (reaction) | stage audio plays | 0.0-1.5 and 4.5-7.5 |
| INS-A | 40.5-44.5 | 4.0 | Conference stage | Kabir (recorded) | 1 | 0.0-4.0 |
| S6 | 47.5-52.0 | 4.5 | Aisle, rear tracking | none (rear view) | 1 dubbed shout | 2.0-6.5 |
| S7 | 52.0-56.5 | 4.5 | Pune table | Sushma | 1 own + 1 phone | 0.0-4.5 |
| INS-B | 56.5-60.0 | 3.5 | Top-down thumb | none | ringtone + muffled voice | 0.0-3.5 |

Seven main shots (S1-S7); INS-A is cut inside S5 and INS-B closes S7. Total: 12.0 + 7.0 + 10.0 + 10.0 + 8.5 + 4.5 + 4.5 + 3.5 = 60.0 s. Generations: 9 video clips (S1-S7, INS-A, INS-B), 3 voice sessions, plus the keyframe stills and 3 canonical crops.

**Lines kept (15 of 20):** 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 15, 16, 18, 19, 20. **Dropped (5):** 9 ('Jaldi karo'), 12 and 13 (the 'two Kabirs' banner beat, now carried by the final insert), 14 ('busy ja raha hai', replaced by dial-and-busy SFX), 17 ('Meri apni aawaaz', dropped to avoid a covered-mouth line). **Moved:** line 16 ('Teen second ki aawaaz kaafi hoti hai') is now the recorded stage talk, spoken by Kabir himself, which is the story's irony.

### The edit at a glance (J and L overlaps)

| Edit time | Overlap | What |
|---|---|---|
| 11.5 s | J-cut S1 to S2 | Office room tone fades in under Sushma's last word. |
| 12.0-12.6 s | L-cut | Kitchen fan hum continues over the first frames of S2. |
| 18.7 s | J-cut S2 to S3 | The scam voice (line 6) starts 0.3 s before the cut, over Kabir's last frames. |
| 28.7 s | J-cut S3 to S4 | Kabir's phone buzzing on a desk starts under the end of S3. |
| 40.1 s | J-cut S5 to INS-A | The recorded talk starts through a laptop speaker over Kabir's face, 0.4 s before the stage picture. |
| 47.0-47.4 s | J-cut S5 to S6 | Chair bang and footsteps begin before the run shot. |
| 51.5 s | J-cut S6 to S7 | The scam voice (line 19) begins 0.5 s before the cut, over the run. |
| 56.5 s | Hard cut S7 to INS-B | Room tone drops to nothing; ringtone and muffled voice take over. |

## Canonical faces and the face-lock method

1. Open the approved contact sheets `CS-SUSHMA`, `CS-KABIR`, `CS-RIYA`. Crop **row 1, column 1** (neutral, facing the camera) of each to a square head-and-shoulders image. Save as `CANON-S`, `CANON-K`, `CANON-R`. These three images are the only face references, ever.
2. Attach the matching `CANON-` file to **every** keyframe of that character, together with the location panel named in the shot. Paste the FACE LOCK block exactly as written; do not reword it between prompts.
3. Keep every shot a medium close-up (head to mid-chest), at most 30 degrees off straight-on. No wide shots of a face, no profile. The only exceptions are the rear run shot (face never visible) and the hands-only insert.
4. Accept a keyframe only if hair, jaw, glasses and (for Sushma) the absence of any necklace match `CANON-` side by side. Reject and regenerate otherwise. Do not animate a keyframe that is not an exact match.
5. The wardrobe lines are not part of the face lock; they differ only for the stage insert (INS-A), which is an older recorded talk.

**Jewellery note:** you asked for 'no necklace, no jewellery except the stated bangles and nose stud'. Sushma's canonical sheet also has small gold stud earrings, so the stated list in the block is bangles, nose stud and stud earrings. If you prefer none, delete 'and small gold stud earrings' in `FACE LOCK, SUSHMA RAO` and in `CS-SUSHMA`.

### FACE LOCK blocks (paste verbatim)

**Sushma**
```
FACE LOCK, SUSHMA RAO (same words in every prompt): Indian woman, 58 years old, round-oval face, wheatish skin with deep smile lines and a few age spots, heavy-lidded dark brown eyes, softly lined forehead, a small round red bindi, a small gold nose stud, greying black hair in a loose low bun with silver streaks. Jewellery: a thin gold bangle on each wrist, the nose stud and small gold stud earrings, NOTHING else. NO necklace, no chain, no pendant, no mangalsutra, no other jewellery.
```

**Kabir**
```
FACE LOCK, KABIR RAO (same words in every prompt): Indian man, 32 years old, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses.
```

**Riya**
```
FACE LOCK, RIYA MENON (same words in every prompt): Indian woman, 24 years old, round friendly face with soft cheeks, large dark expressive eyes, shoulder-length straight black hair tied in a low ponytail with a few loose strands, small silver stud earrings, no glasses.
```

**Wardrobe and glasses blocks**
```
WARDROBE: sage-green cotton saree with a thin printed border over a deep teal blouse; a little flour on her forearm and knuckles.
WARDROBE: mid-grey bomber jacket over a muted-blue crew-neck T-shirt, black smartwatch on his left wrist.
WARDROBE (older recorded talk, a different day): black blazer over a muted-blue crew-neck T-shirt, a headset microphone at his cheek, a conference lanyard, black smartwatch on his left wrist.
WARDROBE: olive-green cotton kurta over blue jeans, a company lanyard with a plain white card.
SUSHMA'S GLASSES: round tortoiseshell reading glasses pushed up on top of her head, resting above her forehead. They stay there for the whole shot; nothing touches them.
SUSHMA'S GLASSES: round tortoiseshell reading glasses sitting on the bridge of her nose. They stay there for the whole shot; nothing touches them.
```

**Sushma's glasses continuity:** on her head in S1, on her nose in S3, S7 and the insert. Nothing in any shot moves them; the switch happens between shots, off camera.

## Voice sessions for Kabir (15 s each)

Why: Grok gives a phone voice to the person on screen, or none, so the scam voice and Kabir's off-screen lines are made here and placed in post. Make them **before** the shots so the voice is fixed first, and make **INS-A** early: Kabir speaks in it on camera, so it is the reference timbre. Pick the VS take closest to INS-A's voice. Use the audio only; throw the picture away. Start image: the `CANON-K` crop. Video mode, 15 s, 9:16, 480p. The voice is a deep, low CHEST voice, never thin or high.

Post for the cloned voice (VS-1 and VS-2): band-limit to 300-3400 Hz, mild distortion and compression, slightly too smooth; no pitch shift unless the take is above a man's normal range, then lower it by up to 3 semitones. VS-3 is not phone-filtered.

### VS-1: Cloned voice, session 1 (lines 1, 3, 6)

```
Animate the start image as ONE continuous 15-second shot, no cuts. Medium close-up of KABIR RAO, an Indian man, 32, oval face, thick tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, sitting in the dark driver's seat of a parked car at night, his face lit only by a phone held close to his mouth. He speaks the lines below, one after another, in natural conversational Hindi. He is crying and panicked, out of breath, his voice cracking, a short ragged sob between lines. VOICE: his deep, low CHEST voice, a grown man's baritone with weight in the chest, steady in pitch around the low range of a man's speaking voice. NOT high-pitched, NOT falsetto, NOT thin, NOT a boy's voice, NOT a whisper. It may crack and shake, but it always comes back down to the low chest register. Lips match every word exactly. Between lines his mouth stays closed and still. Nobody else speaks. No music, no text, no ambience.

DIALOGUE (each line fully and clearly inside its time window, with at least 1.5 seconds of silence between lines):
1. at about 0.3 s: "मम्मी! मम्मी, मुझे बचा लो!" (pronounced: Mummy! Mummy, mujhe bacha lo!)
2. at about 3.6 s: "एक्सीडेंट हो गया। पुलिस ने पकड़ लिया।" (pronounced: Accident ho gaya. Police ne pakad liya.)
3. at about 8.0 s: "चालीस हज़ार यूपीआई करो। अभी। किसी को मत बताना।" (pronounced: Chaalis hazaar UPI karo. Abhi. Kisi ko mat batana.)

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p.
```

### VS-2: Cloned voice, session 2 (line 19, three deliveries)

```
Animate the start image as ONE continuous 15-second shot, no cuts. Medium close-up of KABIR RAO, an Indian man, 32, oval face, thick tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, sitting in the dark driver's seat of a parked car at night, his face lit only by a phone held close to his mouth. He speaks the lines below, one after another, in natural conversational Hindi. He is crying and begging, his voice cracking, a ragged sob between the deliveries. Delivery 1 is desperate and shaky, delivery 2 is quieter and broken, delivery 3 is pleading through tears. VOICE: his deep, low CHEST voice, a grown man's baritone with weight in the chest, steady in pitch around the low range of a man's speaking voice. NOT high-pitched, NOT falsetto, NOT thin, NOT a boy's voice, NOT a whisper. It may crack and shake, but it always comes back down to the low chest register. Lips match every word exactly. Between lines his mouth stays closed and still. Nobody else speaks. No music, no text, no ambience.

DIALOGUE (each line fully and clearly inside its time window, with at least 1.5 seconds of silence between lines):
1. at about 0.3 s: "मम्मी, मुझसे प्यार है तो भेजो!" (pronounced: Mummy, mujhse pyaar hai toh bhejo!)
2. at about 5.2 s: "मम्मी, मुझसे प्यार है तो भेजो!" (pronounced: Mummy, mujhse pyaar hai toh bhejo!)
3. at about 10.2 s: "मम्मी, मुझसे प्यार है तो भेजो!" (pronounced: Mummy, mujhse pyaar hai toh bhejo!)

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p.
```

### VS-3: Kabir's real voice, session 3 (lines 11 and 18)

```
Animate the start image as ONE continuous 15-second shot, no cuts. Medium close-up of KABIR RAO, an Indian man, 32, oval face, thick tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, sitting in the dark driver's seat of a parked car at night, his face lit only by a phone held close to his mouth. He speaks the lines below, one after another, in natural conversational Hindi. He is NOT crying. Line 1 is muttered low and quietly to himself, shocked and flat. Lines 2 and 3 are shouted while running, out of breath, urgent, a hard exhale after each word group (line 3 is a second delivery with a little more fear). VOICE: his deep, low CHEST voice, a grown man's baritone with weight in the chest, steady in pitch around the low range of a man's speaking voice. NOT high-pitched, NOT falsetto, NOT thin, NOT a boy's voice, NOT a whisper. It may crack and shake, but it always comes back down to the low chest register. Lips match every word exactly. Between lines his mouth stays closed and still. Nobody else speaks. No music, no text, no ambience.

DIALOGUE (each line fully and clearly inside its time window, with at least 1.5 seconds of silence between lines):
1. at about 0.5 s: "मम्मी कभी तीन बार नहीं करतीं।" (pronounced: Mummy kabhi teen baar nahin kartin.)
2. at about 5.0 s: "मम्मी, मत भेजना!" (pronounced: Mummy, mat bhejna!)
3. at about 9.5 s: "मम्मी, मत भेजना!" (pronounced: Mummy, mat bhejna!)

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p.
```

## Method for every shot

1. Image mode: attach the listed references, paste the KEYFRAME prompt. Pass the side-by-side face check against `CANON-`.
2. Video mode: start image = the approved keyframe, **15 s, 9:16, 480p**, paste the ANIMATE prompt.
3. Send the clip back to me. I check it at 4 fps against the speech windows before you spend another generation.
4. Order: `CANON` crops, VS-1, VS-2, VS-3, INS-A (reference voice), then S1 to S7 and INS-B.

---

## S1: HOOK: the call

**Edit window:** 0.0-12.0 s (12.0 s). **Generate:** 15 s, 9:16, 480p. **KEEP clip time:** 0.0-12.0 s.
**Attach for the keyframe:** CANON-S, LOC-PUNE (panels 1 and 2)

### KEYFRAME (image mode)
```
Medium close-up of SUSHMA in the kitchen of a small middle-class Indian flat in Pune at night: warm tungsten ceiling light, a yellow bulb over the stove, steel containers, a wooden dining table with a plastic table runner. Her RIGHT hand holds a phone against her right ear with a correct grip, thumb behind the phone, fingers wrapped around the back, the microphone end near her cheek. Her LEFT hand rests flat on the steel counter beside a steel plate of dough. A little flour on her left cheek. She looks just slightly ahead, ordinary and calm, mouth closed. Steel containers and the stove softly out of focus behind her. FACE LOCK, SUSHMA RAO (same words in every prompt): Indian woman, 58 years old, round-oval face, wheatish skin with deep smile lines and a few age spots, heavy-lidded dark brown eyes, softly lined forehead, a small round red bindi, a small gold nose stud, greying black hair in a loose low bun with silver streaks. Jewellery: a thin gold bangle on each wrist, the nose stud and small gold stud earrings, NOTHING else. NO necklace, no chain, no pendant, no mangalsutra, no other jewellery. WARDROBE: sage-green cotton saree with a thin printed border over a deep teal blouse; a little flour on her forearm and knuckles. SUSHMA'S GLASSES: round tortoiseshell reading glasses pushed up on top of her head, resting above her forehead. They stay there for the whole shot; nothing touches them. Medium close-up (head to mid-chest), at most 30 degrees off straight-on, never wider. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints). Expression subtle and naturalistic, not exaggerated. Any screen is a plain dark glass rectangle with no readable content; real screen content is added in post. Photorealistic cinematic still, vertical 9:16, 85mm lens, shallow depth of field, natural skin with pores and fine detail, real fabric texture, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 15 s)
```
Animate the supplied start image as ONE continuous 15-second shot, no cuts. Keep the person, the place, the clothes, the glasses and the light EXACTLY as in the start image; do not change the face at any point.

PERSON: FACE LOCK, SUSHMA RAO (same words in every prompt): Indian woman, 58 years old, round-oval face, wheatish skin with deep smile lines and a few age spots, heavy-lidded dark brown eyes, softly lined forehead, a small round red bindi, a small gold nose stud, greying black hair in a loose low bun with silver streaks. Jewellery: a thin gold bangle on each wrist, the nose stud and small gold stud earrings, NOTHING else. NO necklace, no chain, no pendant, no mangalsutra, no other jewellery. WARDROBE: sage-green cotton saree with a thin printed border over a deep teal blouse; a little flour on her forearm and knuckles. SUSHMA'S GLASSES: round tortoiseshell reading glasses pushed up on top of her head, resting above her forehead. They stay there for the whole shot; nothing touches them.

TIMED BEATS (the whole 15 seconds):
- 0.0 to 1.0 s: She is already on the call: the phone stays at her right ear. Calm, mouth closed and still, eyes forward.
- 1.0 to 4.2 s: She listens. Mouth closed and still. Her face tightens slowly: brow draws together, breath catches at about 2.5 s, eyes begin to glisten. Left hand presses lightly on the counter edge. Nothing else moves.
- 4.5 to 5.3 s: She says one soft word, lips matching, then the mouth closes again.
- 5.3 to 9.6 s: She listens. Mouth closed and still. The fear deepens in small steps: a swallow, a tremble in the lower lip, her eyes filling. No wide eyes.
- 9.6 to 11.6 s: She says one short line, soft and shaking, lips matching, then the mouth closes.
- 11.6 to 15.0 s: She holds still, eyes glistening, mouth closed, phone still at her ear. (Not used in the edit; keep it perfectly calm.)

HANDLING BUDGET: RIGHT hand: the phone, at the right ear from the first frame to the last; it never leaves the ear. LEFT hand: flat on the counter. Nothing else is touched. No ear-to-hand transition. The screen is never seen.

CAMERA: Medium close-up, her face and shoulders fill the frame, eye level, locked-off with a very slow push-in (about 5 percent over 15 s).

PHYSICS: The phone is held steadily against the ear. Flour on her knuckles stays on the hand. Cloth of the saree moves only with her breathing.

STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), screens facing the person who reads them, strict physics for weight, contact and motion. (2) Performance is subtle, restrained and naturalistic: feeling shown through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE. Only the person speaking moves their lips, only inside the time windows listed under DIALOGUE, and every word matches their lips exactly. Outside those windows the mouth does not move at all: no mouthing, no muttering, no smiling with the lips parted.

VOICE: SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear. Soft, never loud.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. SUSHMA at 4.6 to 5.2 s: "कबीर?" (pronounced: Kabir?)
2. SUSHMA at 9.8 to 11.4 s: "हे भगवान! तू ठीक है?" (pronounced: Hey Bhagwan! Tu theek hai?)
Each line must be clearly audible.

AUDIO: Only Sushma's two lines are spoken. The caller on the phone is completely silent in this clip. No music. Quiet room only.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p. Large faces and hands, simple background, no tiny details.
```

**Handling budget:** RIGHT hand: the phone, at the right ear from the first frame to the last; it never leaves the ear. LEFT hand: flat on the counter. Nothing else is touched. No ear-to-hand transition. The screen is never seen.

**Dialogue timings** (clip time, then edit time)

- Sushma (Grok lip-sync, mouth open only here): clip 4.6-5.2 s, edit 4.6-5.2 s: कबीर? / Kabir? / Kabir?
- Sushma (Grok lip-sync, mouth open only here): clip 9.8-11.4 s, edit 9.8-11.4 s: हे भगवान! तू ठीक है? / Hey Bhagwan! Tu theek hai? / Oh God! Are you okay?
- Phone voice from VS-1 (post; listener's mouth closed): clip 1.5-3.8 s, edit 1.5-3.8 s: मम्मी! मम्मी, मुझे बचा लो! / Mummy! Mummy, mujhe bacha lo!
- Phone voice from VS-1 (post; listener's mouth closed): clip 6.3-9.0 s, edit 6.3-9.0 s: एक्सीडेंट हो गया। पुलिस ने पकड़ लिया। / Accident ho gaya. Police ne pakad liya.

**Post note (overlays, SFX, room tone, ringtone, J/L overlaps):** OVERLAY: title card 'AWAAZ · EP 1' at 0.0-1.0 s over the first frames; super 'PUNE' at 0.6-2.4 s, lower left. ROOM TONE: kitchen bed from 0.0 s (exhaust-fan hum, a distant pressure cooker, faint street) at about -30 dB. PHONE VOICE (VS-1, phone-filtered) at the times above. J-CUT: office room tone fades in at 11.5 s under her last word. L-CUT: kitchen fan hum continues 0.6 s into S2.

---

## S2: Kabir declines

**Edit window:** 12.0-19.0 s (7.0 s). **Generate:** 15 s, 9:16, 480p. **KEEP clip time:** 1.0-8.0 s.
**Attach for the keyframe:** CANON-K, LOC-BLR (panels 2 and 5)

### KEYFRAME (image mode)
```
Medium close-up of KABIR at a lit desk in an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors. He sits facing a laptop whose lid back is toward the camera and whose screen faces him. In his RIGHT hand he holds the yellow-and-black mechanical pencil in a normal writing grip, its tip resting on the desk. His LEFT hand rests beside a phone lying face-up on the desk in front of him; the phone's screen is angled up toward him and shows only a faint glow to the camera. A white mug and headphones around his neck. He is tired and focused, mouth closed. FACE LOCK, KABIR RAO (same words in every prompt): Indian man, 32 years old, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses. WARDROBE: mid-grey bomber jacket over a muted-blue crew-neck T-shirt, black smartwatch on his left wrist. Medium close-up (head to mid-chest), at most 30 degrees off straight-on, never wider. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints). Expression subtle and naturalistic, not exaggerated. Any screen is a plain dark glass rectangle with no readable content; real screen content is added in post. Photorealistic cinematic still, vertical 9:16, 85mm lens, shallow depth of field, natural skin with pores and fine detail, real fabric texture, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 15 s)
```
Animate the supplied start image as ONE continuous 15-second shot, no cuts. Keep the person, the place, the clothes, the glasses and the light EXACTLY as in the start image; do not change the face at any point.

PERSON: FACE LOCK, KABIR RAO (same words in every prompt): Indian man, 32 years old, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses. WARDROBE: mid-grey bomber jacket over a muted-blue crew-neck T-shirt, black smartwatch on his left wrist.

TIMED BEATS (the whole 15 seconds):
- 0.0 to 2.0 s: He looks at the laptop screen, tired and focused, mouth closed and still. The right-hand pencil taps the desk slowly, three soft taps.
- 2.0 to 3.0 s: The phone lights up on the desk: a faint glow on his face. His eyes drop to it. His jaw tightens a little. Mouth closed and still.
- 3.0 to 3.8 s: His LEFT thumb touches the phone screen once and the glow dims. The phone stays face-up where it is.
- 4.0 to 5.3 s: He says one short line, low and flat, eyes on the laptop, lips matching, then the mouth closes.
- 5.3 to 8.0 s: He goes back to the work, mouth closed and still. The pencil taps the desk.
- 8.0 to 15.0 s: He keeps working, almost still. (Not used in the edit.)

HANDLING BUDGET: RIGHT hand: the pencil, writing grip, taps the desk and never lets go. LEFT hand: only the thumb touches the phone, once; the phone never leaves the desk and is not flipped or lifted. The laptop and phone screens face Kabir, never the camera.

CAMERA: Medium close-up from slightly left of centre, eye level, locked-off with a slow push-in.

PHYSICS: The pencil taps lightly and bounces back; the phone is still. Blue screen glow on his face and glasses, no lens tint.

STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), screens facing the person who reads them, strict physics for weight, contact and motion. (2) Performance is subtle, restrained and naturalistic: feeling shown through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE. Only the person speaking moves their lips, only inside the time windows listed under DIALOGUE, and every word matches their lips exactly. Outside those windows the mouth does not move at all: no mouthing, no muttering, no smiling with the lips parted.

VOICE: KABIR: a young man's deep, low chest-voice baritone, warm, quick, dry, quieter when he avoids something. NOT high, NOT thin.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. KABIR at 4.0 to 5.3 s: "बाद में, मम्मी।" (pronounced: Baad mein, Mummy.)
Each line must be clearly audible.

AUDIO: Only Kabir's one line is spoken. No other voice. Quiet office hum.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p. Large faces and hands, simple background, no tiny details.
```

**Handling budget:** RIGHT hand: the pencil, writing grip, taps the desk and never lets go. LEFT hand: only the thumb touches the phone, once; the phone never leaves the desk and is not flipped or lifted. The laptop and phone screens face Kabir, never the camera.

**Dialogue timings** (clip time, then edit time)

- Kabir (Grok lip-sync, mouth open only here): clip 4.0-5.3 s, edit 15.0-16.3 s: बाद में, मम्मी। / Baad mein, Mummy. / Later, Mummy.

**Post note (overlays, SFX, room tone, ringtone, J/L overlaps):** OVERLAY: super 'BENGALURU' at 12.3-14.0 s; incoming-call banner 'MUMMY' slides in at the top at 13.0 s and slides out at 14.2 s (the phone screen is never visible, so the banner carries it). SFX: phone vibration buzz at 13.0-14.0 s on wood; pencil taps (add layered taps to cover any soft ones). ROOM TONE: office bed (HVAC hum, rain on glass) from 11.5 s to 19.3 s at about -28 dB. J-CUT: the scam voice (S3 line 1) starts at 18.7 s, 0.3 s before the cut, over Kabir's last frames.

---

## S3: The demand

**Edit window:** 19.0-29.0 s (10.0 s). **Generate:** 15 s, 9:16, 480p. **KEEP clip time:** 1.0-11.0 s.
**Attach for the keyframe:** CANON-S, LOC-PUNE (panels 3 and 4)

### KEYFRAME (image mode)
```
Medium close-up of SUSHMA sitting at the small wooden dining table in a small middle-class Indian flat in Pune at night: warm tungsten ceiling light, a yellow bulb over the stove, steel containers, a wooden dining table with a plastic table runner, a steel thali with unfinished dinner pushed aside, a water jug behind. A phone lies face-up on the table in front of her, its screen angled toward her (the camera sees it only at the bottom edge of the frame, from behind). Her RIGHT hand rests flat on the table beside the phone, her LEFT hand rests on the table edge. She looks at the phone, worried, mouth closed. Slight three-quarter angle. FACE LOCK, SUSHMA RAO (same words in every prompt): Indian woman, 58 years old, round-oval face, wheatish skin with deep smile lines and a few age spots, heavy-lidded dark brown eyes, softly lined forehead, a small round red bindi, a small gold nose stud, greying black hair in a loose low bun with silver streaks. Jewellery: a thin gold bangle on each wrist, the nose stud and small gold stud earrings, NOTHING else. NO necklace, no chain, no pendant, no mangalsutra, no other jewellery. WARDROBE: sage-green cotton saree with a thin printed border over a deep teal blouse; a little flour on her forearm and knuckles. SUSHMA'S GLASSES: round tortoiseshell reading glasses sitting on the bridge of her nose. They stay there for the whole shot; nothing touches them. Medium close-up (head to mid-chest), at most 30 degrees off straight-on, never wider. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints). Expression subtle and naturalistic, not exaggerated. Any screen is a plain dark glass rectangle with no readable content; real screen content is added in post. Photorealistic cinematic still, vertical 9:16, 85mm lens, shallow depth of field, natural skin with pores and fine detail, real fabric texture, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 15 s)
```
Animate the supplied start image as ONE continuous 15-second shot, no cuts. Keep the person, the place, the clothes, the glasses and the light EXACTLY as in the start image; do not change the face at any point.

PERSON: FACE LOCK, SUSHMA RAO (same words in every prompt): Indian woman, 58 years old, round-oval face, wheatish skin with deep smile lines and a few age spots, heavy-lidded dark brown eyes, softly lined forehead, a small round red bindi, a small gold nose stud, greying black hair in a loose low bun with silver streaks. Jewellery: a thin gold bangle on each wrist, the nose stud and small gold stud earrings, NOTHING else. NO necklace, no chain, no pendant, no mangalsutra, no other jewellery. WARDROBE: sage-green cotton saree with a thin printed border over a deep teal blouse; a little flour on her forearm and knuckles. SUSHMA'S GLASSES: round tortoiseshell reading glasses sitting on the bridge of her nose. They stay there for the whole shot; nothing touches them.

TIMED BEATS (the whole 15 seconds):
- 0.0 to 1.0 s: She listens to the phone. Mouth closed and still. Hands resting on the table.
- 1.0 to 5.2 s: She keeps listening: mouth closed and still. Slow tightening of the brow, a swallow, a small nod of understanding. Eyes glisten.
- 5.9 to 7.3 s: She says one line softly, lips matching, eyes on the phone, then the mouth closes.
- 7.3 to 8.6 s: She leans a few degrees forward and reads the phone, eyes narrowing as if squinting. Mouth closed and still. Hands stay on the table.
- 8.7 to 10.5 s: She says one line, puzzled, lips matching, then the mouth closes.
- 10.5 to 15.0 s: She stays frozen, eyes on the phone, mouth closed. (Not used in the edit.)

HANDLING BUDGET: BOTH hands rest on the table; she never touches the phone. The phone lies flat, screen toward her. Her glasses are already on her nose and nothing touches them. No tapping, no lifting.

CAMERA: Medium close-up, slight three-quarter, eye level, locked-off with a slow push-in.

PHYSICS: The phone lies still on the table. Her breath moves the saree slightly.

STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), screens facing the person who reads them, strict physics for weight, contact and motion. (2) Performance is subtle, restrained and naturalistic: feeling shown through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE. Only the person speaking moves their lips, only inside the time windows listed under DIALOGUE, and every word matches their lips exactly. Outside those windows the mouth does not move at all: no mouthing, no muttering, no smiling with the lips parted.

VOICE: SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear. Soft, never loud.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. SUSHMA at 5.9 to 7.3 s: "भेज रही हूँ, बेटा।" (pronounced: Bhej rahi hoon, beta.)
2. SUSHMA at 8.7 to 10.5 s: "ये नाम तो राहुल का है?" (pronounced: Ye naam toh Rahul ka hai?)
Each line must be clearly audible.

AUDIO: Only Sushma's two lines are spoken. The phone is completely silent in this clip. Quiet room only.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p. Large faces and hands, simple background, no tiny details.
```

**Handling budget:** BOTH hands rest on the table; she never touches the phone. The phone lies flat, screen toward her. Her glasses are already on her nose and nothing touches them. No tapping, no lifting.

**Dialogue timings** (clip time, then edit time)

- Sushma (Grok lip-sync, mouth open only here): clip 5.9-7.3 s, edit 23.9-25.3 s: भेज रही हूँ, बेटा। / Bhej rahi hoon, beta. / I'm sending it, son.
- Sushma (Grok lip-sync, mouth open only here): clip 8.7-10.5 s, edit 26.7-28.5 s: ये नाम तो राहुल का है? / Ye naam toh Rahul ka hai? / This name is Rahul's?
- Phone voice from VS-1 (post; listener's mouth closed): clip 0.7-4.6 s, edit 18.7-22.6 s: चालीस हज़ार यूपीआई करो। अभी। किसी को मत बताना। / Chaalis hazaar UPI karo. Abhi. Kisi ko mat batana.

**Post note (overlays, SFX, room tone, ringtone, J/L overlaps):** PHONE VOICE (VS-1, phone-filtered) plays at edit 18.7-22.6 s (it begins in the last 0.3 s of S2). OVERLAY: UPI card 'RAHUL VERMA  ₹40,000' (lower third, white card, green button) fades in at edit 26.2 s and holds to 29.0 s and into the cut. ROOM TONE: kitchen/dining bed (fan hum, distant street) from 19.0 s at about -30 dB. J-CUT into S4: Kabir's phone buzzing on a desk at 28.7 s.

---

## S4: Riya notices

**Edit window:** 29.0-39.0 s (10.0 s). **Generate:** 15 s, 9:16, 480p. **KEEP clip time:** 1.0-11.0 s.
**Attach for the keyframe:** CANON-R, LOC-BLR (panels 2 and 5)

### KEYFRAME (image mode)
```
Medium close-up of RIYA standing at a desk in an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors. An open laptop sits on the desk in front of her with its lid back toward the camera and its screen facing her. Her fingertips rest lightly on the desk edge on both sides. She looks off to the right (toward Kabir, who is off camera), concerned, mouth closed. No mug, no bag, nothing in her hands. Slight three-quarter angle. FACE LOCK, RIYA MENON (same words in every prompt): Indian woman, 24 years old, round friendly face with soft cheeks, large dark expressive eyes, shoulder-length straight black hair tied in a low ponytail with a few loose strands, small silver stud earrings, no glasses. WARDROBE: olive-green cotton kurta over blue jeans, a company lanyard with a plain white card. Medium close-up (head to mid-chest), at most 30 degrees off straight-on, never wider. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints). Expression subtle and naturalistic, not exaggerated. Any screen is a plain dark glass rectangle with no readable content; real screen content is added in post. Photorealistic cinematic still, vertical 9:16, 85mm lens, shallow depth of field, natural skin with pores and fine detail, real fabric texture, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 15 s)
```
Animate the supplied start image as ONE continuous 15-second shot, no cuts. Keep the person, the place, the clothes, the glasses and the light EXACTLY as in the start image; do not change the face at any point.

PERSON: FACE LOCK, RIYA MENON (same words in every prompt): Indian woman, 24 years old, round friendly face with soft cheeks, large dark expressive eyes, shoulder-length straight black hair tied in a low ponytail with a few loose strands, small silver stud earrings, no glasses. WARDROBE: olive-green cotton kurta over blue jeans, a company lanyard with a plain white card.

TIMED BEATS (the whole 15 seconds):
- 0.0 to 1.0 s: She looks down at the laptop, then lifts her eyes to the right. Mouth closed and still.
- 1.5 to 4.4 s: She says one line to Kabir off camera, steady, lips matching, then the mouth closes.
- 4.4 to 6.9 s: She watches him. Mouth closed and still. Her brow draws slightly, her expression moves from teasing to unease in small steps.
- 6.9 to 7.4 s: She glances down at the laptop, a small breath in. Mouth closed.
- 7.4 to 9.6 s: She says one line, quieter, thinking aloud, lips matching, then the mouth closes.
- 9.6 to 15.0 s: She keeps looking at him, eyes narrowing slightly, mouth closed. (Not used in the edit.)

HANDLING BUDGET: BOTH hands: fingertips rest on the desk edge for the whole shot. The laptop is open on the desk with its screen toward her, lid back to camera, and is never touched or moved. No mug, no laptop under her arm.

CAMERA: Medium close-up, slight three-quarter, eye level, locked-off.

PHYSICS: Nothing moves except Riya's face, breath and eyes.

STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), screens facing the person who reads them, strict physics for weight, contact and motion. (2) Performance is subtle, restrained and naturalistic: feeling shown through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE. Only the person speaking moves their lips, only inside the time windows listed under DIALOGUE, and every word matches their lips exactly. Outside those windows the mouth does not move at all: no mouthing, no muttering, no smiling with the lips parted.

VOICE: RIYA: a young woman's voice, clear mid-high pitch, quick and steady.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. RIYA at 1.5 to 4.4 s: "कबीर, तुम्हारी मम्मी तीसरी बार कर रही हैं।" (pronounced: Kabir, tumhaari Mummy teesri baar kar rahi hain.)
2. RIYA at 7.4 to 9.6 s: "तुमने क्लोनिंग का डेमो दिया था ना?" (pronounced: Tumne cloning ka demo diya tha na?)
Each line must be clearly audible.

AUDIO: Only Riya's two lines are spoken. Kabir is off camera and silent in this clip. Quiet office hum.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p. Large faces and hands, simple background, no tiny details.
```

**Handling budget:** BOTH hands: fingertips rest on the desk edge for the whole shot. The laptop is open on the desk with its screen toward her, lid back to camera, and is never touched or moved. No mug, no laptop under her arm.

**Dialogue timings** (clip time, then edit time)

- Riya (Grok lip-sync, mouth open only here): clip 1.5-4.4 s, edit 29.5-32.4 s: कबीर, तुम्हारी मम्मी तीसरी बार कर रही हैं। / Kabir, tumhaari Mummy teesri baar kar rahi hain. / Kabir, your mother is calling a third time.
- Riya (Grok lip-sync, mouth open only here): clip 7.4-9.6 s, edit 35.4-37.6 s: तुमने क्लोनिंग का डेमो दिया था ना? / Tumne cloning ka demo diya tha na? / You gave that cloning demo, didn't you?
- Off-screen Kabir (VS-3, post; Riya's mouth closed): clip 4.9-6.6 s, edit 32.9-34.6 s: मम्मी कभी तीन बार नहीं करतीं। / Mummy kabhi teen baar nahin kartin.

**Post note (overlays, SFX, room tone, ringtone, J/L overlaps):** OFF-SCREEN KABIR (VS-3 take, clean, not phone-filtered): 'मम्मी कभी तीन बार नहीं करतीं।' ('Mummy kabhi teen baar nahin kartin.') at edit 32.9-34.6 s, over Riya's listening face (her mouth is closed). SFX: phone buzz on wood 28.7-29.6 s; at 34.7-35.3 s a muffled dial ring-ring-ring and then the fast busy beeps of a failed call from off camera (J into her second line). ROOM TONE: office bed -28 dB. J-CUT into S5: stage-talk audio from a laptop speaker starts at 40.1 s.

---

## S5: The spike: his own voice

**Edit window:** 39.0-47.5 s (8.5 s). **Generate:** 15 s, 9:16, 480p. **KEEP clip time:** 0.0-7.5 s.
**Attach for the keyframe:** CANON-K, LOC-BLR (panel 2), INS-A (cut in from the stage insert)

### KEYFRAME (image mode)
```
Medium close-up of KABIR leaning forward over an open laptop on a desk in an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors. The laptop's lid back is toward the camera and its screen faces him; a cold blue glow from the screen lights his face and shows faintly in his clear glasses. His LEFT hand rests flat on the desk. His RIGHT arm hangs relaxed at his side. A single yellow-and-black pencil lies on the desk at the left edge of the frame. He stares at the screen, mouth closed, concentrating. FACE LOCK, KABIR RAO (same words in every prompt): Indian man, 32 years old, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses. WARDROBE: mid-grey bomber jacket over a muted-blue crew-neck T-shirt, black smartwatch on his left wrist. Medium close-up (head to mid-chest), at most 30 degrees off straight-on, never wider. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints). Expression subtle and naturalistic, not exaggerated. Any screen is a plain dark glass rectangle with no readable content; real screen content is added in post. Photorealistic cinematic still, vertical 9:16, 85mm lens, shallow depth of field, natural skin with pores and fine detail, real fabric texture, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 15 s)
```
Animate the supplied start image as ONE continuous 15-second shot, no cuts. Keep the person, the place, the clothes, the glasses and the light EXACTLY as in the start image; do not change the face at any point.

PERSON: FACE LOCK, KABIR RAO (same words in every prompt): Indian man, 32 years old, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses. WARDROBE: mid-grey bomber jacket over a muted-blue crew-neck T-shirt, black smartwatch on his left wrist.

TIMED BEATS (the whole 15 seconds):
- 0.0 to 1.5 s: He stares at the screen, mouth closed and still. Blue glow on his face.
- 1.5 to 4.5 s: He keeps staring. (This part is replaced in the edit by the stage insert INS-A. Stay very still, mouth closed.)
- 4.5 to 5.2 s: His breath stops. His eyes widen only slightly and his face goes still.
- 5.2 to 6.2 s: His RIGHT hand rises slowly and settles over his mouth, fingers together. One deliberate movement, no jerking.
- 6.2 to 7.5 s: He holds: hand over his mouth, eyes fixed on the screen, absolutely still, breathing very shallowly.
- 7.5 to 15.0 s: He holds still. (Not used in the edit.)

HANDLING BUDGET: LEFT hand: flat on the desk the whole time. RIGHT hand: one slow movement from his side to his mouth, then stays there. The pencil is only lying on the desk, never held. The laptop screen faces Kabir; the camera sees only the lid.

CAMERA: Medium close-up from the front, eye level, locked-off with a very slow push-in.

PHYSICS: The laptop and desk are still. Blue light flickers softly on his face.

STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), screens facing the person who reads them, strict physics for weight, contact and motion. (2) Performance is subtle, restrained and naturalistic: feeling shown through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: nobody speaks. MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE. (The mouth never moves.)

DIALOGUE in natural conversational Hindi, in this order, no overlap:
none (nobody speaks in this clip)
Each line must be clearly audible.

AUDIO: Nobody speaks in this clip. His breath only. Quiet office hum.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p. Large faces and hands, simple background, no tiny details.
```

**Handling budget:** LEFT hand: flat on the desk the whole time. RIGHT hand: one slow movement from his side to his mouth, then stays there. The pencil is only lying on the desk, never held. The laptop screen faces Kabir; the camera sees only the lid.

**Dialogue timings** (clip time, then edit time)

- None in this clip.

**Post note (overlays, SFX, room tone, ringtone, J/L overlaps):** EDIT: use clip 0.0-1.5 s at edit 39.0-40.5 s, then cut to INS-A (stage insert) for edit 40.5-44.5 s, then clip 4.5-7.5 s at edit 44.5-47.5 s. GRADE: colour drains from his face by about 15 percent from edit 45.0 to 47.5 s. AUDIO: INS-A's audio (the recorded talk) starts at 40.1 s through a laptop-speaker filter over Kabir's face and ends at 43.8 s. SFX: a low heartbeat-like sub tone from 44.8 s. No speech from Kabir: the line 'मेरी अपनी आवाज़' from the old script is dropped (his covered mouth would repeat last time's sync fault). J-CUT into S6: footsteps and a chair bang at 47.0-47.4 s.

---

## INS-A: Stage insert (recorded talk, own audio)

**Edit window:** 40.5-44.5 s (4.0 s). **Generate:** 15 s, 9:16, 480p. **KEEP clip time:** 0.0-4.0 s.
**Attach for the keyframe:** CANON-K, PROP-STAGE

### KEYFRAME (image mode)
```
Medium close-up of KABIR RAO on a modern tech conference stage at a lectern, a large screen behind him showing only an abstract audio waveform with no text, an audience of blurred shapes in the dark foreground, stage lighting. A headset microphone at his cheek. His LEFT hand rests on the lectern. His RIGHT hand is relaxed at his side. He looks slightly out toward the audience, confident, mouth closed. Slight three-quarter angle. FACE LOCK, KABIR RAO (same words in every prompt): Indian man, 32 years old, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses. WARDROBE (older recorded talk, a different day): black blazer over a muted-blue crew-neck T-shirt, a headset microphone at his cheek, a conference lanyard, black smartwatch on his left wrist. Medium close-up (head to mid-chest), at most 30 degrees off straight-on, never wider. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints). Expression subtle and naturalistic, not exaggerated. Any screen is a plain dark glass rectangle with no readable content; real screen content is added in post. Photorealistic cinematic still, vertical 9:16, 85mm lens, shallow depth of field, natural skin with pores and fine detail, real fabric texture, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 15 s)
```
Animate the supplied start image as ONE continuous 15-second shot, no cuts. Keep the person, the place, the clothes, the glasses and the light EXACTLY as in the start image; do not change the face at any point.

PERSON: FACE LOCK, KABIR RAO (same words in every prompt): Indian man, 32 years old, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses. WARDROBE (older recorded talk, a different day): black blazer over a muted-blue crew-neck T-shirt, a headset microphone at his cheek, a conference lanyard, black smartwatch on his left wrist.

TIMED BEATS (the whole 15 seconds):
- 0.0 to 0.6 s: He looks out at the audience, confident, mouth closed and still.
- 0.7 to 3.3 s: He says one line to the audience, clear and easy, a small open-palm gesture of his RIGHT hand at the middle of the line, lips matching, then the mouth closes with a half-smile.
- 3.3 to 4.0 s: He holds the half-smile, mouth closed and still.
- 4.0 to 15.0 s: He stays calm and nearly still. (Not used in the edit.)

HANDLING BUDGET: LEFT hand: rests on the lectern. RIGHT hand: one small open-palm gesture, then back to his side. Nothing held.

CAMERA: Medium close-up, slight three-quarter, eye level, locked-off.

PHYSICS: Stage light and the screen glow are steady; the headset mic stays at his cheek.

STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), screens facing the person who reads them, strict physics for weight, contact and motion. (2) Performance is subtle, restrained and naturalistic: feeling shown through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE. Only the person speaking moves their lips, only inside the time windows listed under DIALOGUE, and every word matches their lips exactly. Outside those windows the mouth does not move at all: no mouthing, no muttering, no smiling with the lips parted.

VOICE: KABIR: a young man's deep, low chest-voice baritone, warm, quick, dry, quieter when he avoids something. NOT high, NOT thin.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. KABIR at 0.7 to 3.3 s: "तीन सेकंड की आवाज़ काफ़ी होती है।" (pronounced: Teen second ki aawaaz kaafi hoti hai.)
Each line must be clearly audible.

AUDIO: Only Kabir's one line is spoken, as if recorded on a stage mic. Faint hall reverb. No applause.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p. Large faces and hands, simple background, no tiny details.
```

**Handling budget:** LEFT hand: rests on the lectern. RIGHT hand: one small open-palm gesture, then back to his side. Nothing held.

**Dialogue timings** (clip time, then edit time)

- Kabir (Grok lip-sync, mouth open only here): clip 0.7-3.3 s, edit 41.2-43.8 s: तीन सेकंड की आवाज़ काफ़ी होती है। / Teen second ki aawaaz kaafi hoti hai. / Three seconds of voice is enough.

**Post note (overlays, SFX, room tone, ringtone, J/L overlaps):** This is the 'recorded talk' on Riya's laptop. Treat it as footage: desaturate by about 15 percent, slight vignette, subtle softening. AUDIO: keep Grok's own spoken audio (he lip-syncs it), laptop-speaker filter (band-limited 200 Hz-6 kHz). Pitch-match this voice to Kabir's other lines (S2, VS-1, VS-3): choose the VS-1 and VS-3 takes closest to this timbre, then shift +/-2 semitones if needed. Generate this one early; it is the reference for the cloned voice.

---

## S6: The run (rear tracking)

**Edit window:** 47.5-52.0 s (4.5 s). **Generate:** 15 s, 9:16, 480p. **KEEP clip time:** 2.0-6.5 s.
**Attach for the keyframe:** CANON-K (for hair and jacket only), LOC-BLR (panel 3, the long aisle)

### KEYFRAME (image mode)
```
Medium shot from directly behind KABIR RAO, who is running down a long aisle between desks in an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors, glass walls and strip lights ahead. The back of his head, his shoulders and his torso fill the frame. His RIGHT hand holds a phone against his right ear. His LEFT arm swings with his stride. His mid-grey bomber jacket flaps behind him. His face is never visible. Slightly low camera, behind him. FACE LOCK, KABIR RAO (same words in every prompt): Indian man, 32 years old, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses. WARDROBE: mid-grey bomber jacket over a muted-blue crew-neck T-shirt, black smartwatch on his left wrist. The face is never visible in this shot. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints). Expression subtle and naturalistic, not exaggerated. Any screen is a plain dark glass rectangle with no readable content; real screen content is added in post. Photorealistic cinematic still, vertical 9:16, 85mm lens, shallow depth of field, natural skin with pores and fine detail, real fabric texture, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 15 s)
```
Animate the supplied start image as ONE continuous 15-second shot, no cuts. Keep the person, the place, the clothes, the glasses and the light EXACTLY as in the start image; do not change the face at any point.

PERSON: FACE LOCK, KABIR RAO (same words in every prompt): Indian man, 32 years old, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses. WARDROBE: mid-grey bomber jacket over a muted-blue crew-neck T-shirt, black smartwatch on his left wrist.

TIMED BEATS (the whole 15 seconds):
- 0.0 to 2.0 s: He is already running: a firm, fast stride, jacket flapping, the camera tracking from directly behind at the same speed. (Not used in the edit.)
- 2.0 to 6.5 s: He keeps running at the same pace; the camera stays behind him. His head turns slightly left and right once as he passes desks. The phone stays at his right ear.
- 6.5 to 15.0 s: He keeps running, receding slightly. (Not used in the edit.)

HANDLING BUDGET: RIGHT hand: the phone at the right ear for the whole shot (never moves from the ear; no transition). LEFT arm: swings naturally with the stride. Nothing else is held. His face is never visible.

CAMERA: REAR TRACKING shot: camera directly behind him, waist to head height, moving at the same speed as the runner, steady, slight handheld sway.

PHYSICS: Real running mechanics: heel-toe stride, arm swing opposite to the leg, jacket and hair trailing, weight shifting with each step.

STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), screens facing the person who reads them, strict physics for weight, contact and motion. (2) Performance is subtle, restrained and naturalistic: feeling shown through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: nobody speaks. MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE. (The mouth never moves.)

DIALOGUE in natural conversational Hindi, in this order, no overlap:
none (nobody speaks in this clip)
Each line must be clearly audible.

AUDIO: Nobody speaks in this clip. Footsteps and breath only.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p. Large faces and hands, simple background, no tiny details.
```

**Handling budget:** RIGHT hand: the phone at the right ear for the whole shot (never moves from the ear; no transition). LEFT arm: swings naturally with the stride. Nothing else is held. His face is never visible.

**Dialogue timings** (clip time, then edit time)

- None in this clip.
- Kabir shout (VS-3, post; face not visible): edit 47.7-49.1 s: मम्मी, मत भेजना! / Mummy, mat bhejna!

**Post note (overlays, SFX, room tone, ringtone, J/L overlaps):** No speech is generated; his mouth is not visible. VOICE: Kabir shouting 'मम्मी, मत भेजना!' ('Mummy, mat bhejna!') from VS-3 (clean, not phone-filtered; breathless) at edit 47.7-49.1 s. SFX: running footsteps on polished floor, jacket cloth, breath; ringback tone from the phone, faint, at 49.5-51.8 s; a chair spinning and hitting a desk at 47.0-47.4 s (before the shot). ROOM TONE: office bed. J-CUT into S7: the scam voice (L19) starts at 51.5 s over the last 0.5 s of the run.

---

## S7: BUTTON: the thumb

**Edit window:** 52.0-56.5 s (4.5 s). **Generate:** 15 s, 9:16, 480p. **KEEP clip time:** 0.0-4.5 s.
**Attach for the keyframe:** CANON-S, LOC-PUNE (panels 3 and 4)

### KEYFRAME (image mode)
```
Medium close-up of SUSHMA sitting at the small wooden dining table in a small middle-class Indian flat in Pune at night: warm tungsten ceiling light, a yellow bulb over the stove, steel containers, a wooden dining table with a plastic table runner. A phone lies face-up on the table in front of her, screen toward her, seen only at the bottom edge of the frame from behind. Her RIGHT hand rests flat on the table beside it, her LEFT hand rests on the table edge. Her eyes are lowered to the phone, glistening, tears just starting. Mouth closed. Slight three-quarter angle. FACE LOCK, SUSHMA RAO (same words in every prompt): Indian woman, 58 years old, round-oval face, wheatish skin with deep smile lines and a few age spots, heavy-lidded dark brown eyes, softly lined forehead, a small round red bindi, a small gold nose stud, greying black hair in a loose low bun with silver streaks. Jewellery: a thin gold bangle on each wrist, the nose stud and small gold stud earrings, NOTHING else. NO necklace, no chain, no pendant, no mangalsutra, no other jewellery. WARDROBE: sage-green cotton saree with a thin printed border over a deep teal blouse; a little flour on her forearm and knuckles. SUSHMA'S GLASSES: round tortoiseshell reading glasses sitting on the bridge of her nose. They stay there for the whole shot; nothing touches them. Medium close-up (head to mid-chest), at most 30 degrees off straight-on, never wider. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints). Expression subtle and naturalistic, not exaggerated. Any screen is a plain dark glass rectangle with no readable content; real screen content is added in post. Photorealistic cinematic still, vertical 9:16, 85mm lens, shallow depth of field, natural skin with pores and fine detail, real fabric texture, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 15 s)
```
Animate the supplied start image as ONE continuous 15-second shot, no cuts. Keep the person, the place, the clothes, the glasses and the light EXACTLY as in the start image; do not change the face at any point.

PERSON: FACE LOCK, SUSHMA RAO (same words in every prompt): Indian woman, 58 years old, round-oval face, wheatish skin with deep smile lines and a few age spots, heavy-lidded dark brown eyes, softly lined forehead, a small round red bindi, a small gold nose stud, greying black hair in a loose low bun with silver streaks. Jewellery: a thin gold bangle on each wrist, the nose stud and small gold stud earrings, NOTHING else. NO necklace, no chain, no pendant, no mangalsutra, no other jewellery. WARDROBE: sage-green cotton saree with a thin printed border over a deep teal blouse; a little flour on her forearm and knuckles. SUSHMA'S GLASSES: round tortoiseshell reading glasses sitting on the bridge of her nose. They stay there for the whole shot; nothing touches them.

TIMED BEATS (the whole 15 seconds):
- 0.0 to 2.4 s: She listens to the phone. Mouth closed and still. Tears run slowly down her cheeks; her lower lip trembles very slightly. Eyes on the phone.
- 2.4 to 2.8 s: She raises her eyes a few degrees, as if looking at something far away. Mouth closed.
- 2.9 to 3.9 s: She whispers one line, barely audible, lips matching, then the mouth closes.
- 3.9 to 4.5 s: She stares at the phone, tears falling, mouth closed and still.
- 4.5 to 15.0 s: She holds still. (Not used in the edit.)

HANDLING BUDGET: BOTH hands rest on the table; she does not touch the phone in this shot. The phone lies flat, screen toward her. Glasses on her nose, untouched.

CAMERA: Medium close-up, slight three-quarter, eye level, locked-off with a very slow push-in.

PHYSICS: Tears follow the contour of her cheek and fall; the phone lies still.

STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), screens facing the person who reads them, strict physics for weight, contact and motion. (2) Performance is subtle, restrained and naturalistic: feeling shown through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE. Only the person speaking moves their lips, only inside the time windows listed under DIALOGUE, and every word matches their lips exactly. Outside those windows the mouth does not move at all: no mouthing, no muttering, no smiling with the lips parted.

VOICE: SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear. Soft, never loud.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. SUSHMA at 2.9 to 3.9 s: "कौन-सा कबीर?" (pronounced: Kaun-sa Kabir?)
Each line must be clearly audible.

AUDIO: Only Sushma's one whispered line is spoken. The phone is completely silent in this clip. Quiet room only.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p. Large faces and hands, simple background, no tiny details.
```

**Handling budget:** BOTH hands rest on the table; she does not touch the phone in this shot. The phone lies flat, screen toward her. Glasses on her nose, untouched.

**Dialogue timings** (clip time, then edit time)

- Sushma (Grok lip-sync, mouth open only here): clip 2.9-3.9 s, edit 54.9-55.9 s: कौन-सा कबीर? / Kaun-sa Kabir? / Which Kabir?
- Phone voice from VS-2 (post; listener's mouth closed): clip -0.5-1.9 s, edit 51.5-53.9 s: मम्मी, मुझसे प्यार है तो भेजो! / Mummy, mujhse pyaar hai toh bhejo!

**Post note (overlays, SFX, room tone, ringtone, J/L overlaps):** PHONE VOICE (VS-2, phone-filtered) at edit 51.5-53.9 s (starts 0.5 s before the cut). ROOM TONE: dining bed -30 dB, which DROPS to silence at 56.5 s on the cut to INS-B. Then INS-B.

---

## INS-B: BUTTON insert: top-down thumb (the one allowed POV screen)

**Edit window:** 56.5-60.0 s (3.5 s). **Generate:** 15 s, 9:16, 480p. **KEEP clip time:** 0.0-3.5 s.
**Attach for the keyframe:** CANON-S (wrist and hand skin tone only), LOC-PUNE (panel 4)

### KEYFRAME (image mode)
```
Top-down point-of-view close-up of the wooden dining table in a small middle-class Indian flat in Pune at night: warm tungsten ceiling light, a yellow bulb over the stove, steel containers, a wooden dining table with a plastic table runner. A phone lies flat on the table, its screen facing up toward the camera, a plain dark glass rectangle with no readable content. SUSHMA'S RIGHT hand, an older woman's hand with fine wrinkles, a thin gold bangle on the wrist and flour on the knuckles, hovers just above the lower part of the screen with the thumb extended. Her LEFT hand rests flat on the table edge. A faint dusting of flour on the table. Nothing else in frame; no face. The hand is Sushma's: FACE LOCK, SUSHMA RAO (same words in every prompt): Indian woman, 58 years old, round-oval face, wheatish skin with deep smile lines and a few age spots, heavy-lidded dark brown eyes, softly lined forehead, a small round red bindi, a small gold nose stud, greying black hair in a loose low bun with silver streaks. Jewellery: a thin gold bangle on each wrist, the nose stud and small gold stud earrings, NOTHING else. NO necklace, no chain, no pendant, no mangalsutra, no other jewellery. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints). Expression subtle and naturalistic, not exaggerated. Any screen is a plain dark glass rectangle with no readable content; real screen content is added in post. Photorealistic cinematic still, vertical 9:16, 85mm lens, shallow depth of field, natural skin with pores and fine detail, real fabric texture, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 15 s)
```
Animate the supplied start image as ONE continuous 15-second shot, no cuts. Keep the person, the place, the clothes, the glasses and the light EXACTLY as in the start image; do not change the face at any point.

PERSON: only Sushma's right hand and left hand are visible. FACE LOCK, SUSHMA RAO (same words in every prompt): Indian woman, 58 years old, round-oval face, wheatish skin with deep smile lines and a few age spots, heavy-lidded dark brown eyes, softly lined forehead, a small round red bindi, a small gold nose stud, greying black hair in a loose low bun with silver streaks. Jewellery: a thin gold bangle on each wrist, the nose stud and small gold stud earrings, NOTHING else. NO necklace, no chain, no pendant, no mangalsutra, no other jewellery.

TIMED BEATS (the whole 15 seconds):
- 0.0 to 1.5 s: Her right thumb hovers above the screen and trembles very slightly, a few millimetres of shake. Her left hand stays flat.
- 1.5 to 3.5 s: The thumb drifts a little to one side, then back to the middle. It never touches the screen.
- 3.5 to 15.0 s: The thumb hangs in the air, trembling. (Not used in the edit; the freeze happens in post.)

HANDLING BUDGET: The phone lies flat and is not touched. RIGHT hand: only the thumb moves, hovering and trembling, never touching the glass. LEFT hand: flat on the table. This is the one deliberate screen-to-camera shot in the episode; the screen is plain dark glass and all content is added in post.

CAMERA: Top-down POV, locked-off, slight push-in. No face visible.

PHYSICS: The thumb's tremor is small and real. The phone stays still on the table.

STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), screens facing the person who reads them, strict physics for weight, contact and motion. (2) Performance is subtle, restrained and naturalistic: feeling shown through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: nobody speaks. MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE. (The mouth never moves.)

DIALOGUE in natural conversational Hindi, in this order, no overlap:
none (nobody speaks in this clip)
Each line must be clearly audible.

AUDIO: Nobody speaks. Faint breath only.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 15 seconds, 9:16, 480p. Large faces and hands, simple background, no tiny details.
```

**Handling budget:** The phone lies flat and is not touched. RIGHT hand: only the thumb moves, hovering and trembling, never touching the glass. LEFT hand: flat on the table. This is the one deliberate screen-to-camera shot in the episode; the screen is plain dark glass and all content is added in post.

**Dialogue timings** (clip time, then edit time)

- None in this clip.

**Post note (overlays, SFX, room tone, ringtone, J/L overlaps):** OVERLAYS (on the plain dark screen and the frame): the screen shows two round green buttons, ACCEPT and PAY, drawn in post and tracked to the phone (the top-down shot is locked-off, so no tracking is needed). A call banner 'KABIR  इनकमिंग कॉल' at the top of the frame; the UPI card 'RAHUL VERMA  ₹40,000 / भेजें ₹40,000' in the lower third; caption 'कौन-सा कबीर?' centred at 58.0 s; 'EP 2 →' bottom right at 58.4 s. FREEZE: freeze the frame at edit 58.0 s through 59.5 s; CUT TO BLACK at 59.5 s to 60.0 s. AUDIO: a ringtone bed (a generic marimba-style ring, not a branded tone) from 56.5 s to 59.5 s; under it, a muffled loop of VS-2's begging voice, low-passed, at about -18 dB, 56.6-58.5 s; room tone gone from 56.5 s, silent after the cut to black.

---

## Pre-flight checks before you generate

- Every ANIMATE prompt contains the sentence `MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE.`
- Each phone-voice window (S1 1.5-3.8 and 6.3-9.0 s; S3 edit 18.7-22.6 s; S7 edit 51.5-53.9 s) falls in a stretch where the listener's mouth is closed.
- No shot has two visible mouths. S4's Kabir reply is off-screen audio over Riya's closed mouth.
- No shot moves an object between ear and hand, flips a phone, or turns a screen to the camera, except INS-B.
- Accept a take only if it passes the lip-window check in `00-review-checklist.md` item 9.

## Hindi check
The lines are written by an AI and I cannot hear them. A native speaker should check the register before release. Disclosure: if you publish Grok-generated video and voices, apply the platform's synthetic-media label, and say so in the caption.

