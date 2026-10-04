# AWAAZ Episode 1: clip prompts (6-second clips, about 400x736)

**Output limits (paid Grok account, as reported):** videos still render at 6 seconds and about 400x736. Generations are no longer rationed.

## What changed for 6-second clips
- **Every clip is generated at 6 seconds and trimmed to 5 in the edit.** The extra second absorbs timing drift (the first approved take had its spoken word about 0.3 s late).
- **Clip 12 is a separate 6-second POV insert of her thumb again** (the merged version made the screen face the camera). Episode 1 is back to **12 clips**; the freeze is still made in post.
- **The stage-talk insert (INS-9) is a still image, not a video.** I put it on the laptop screen with a slow push-in.
- **The phone voice comes from 3 six-second voice sessions** (VS-A, VS-B, VS-C), one or two lines each. The last whispered word "मम्मी..." is cut from the start of VS-A, so no fourth session is needed.
- **Low resolution:** every prompt asks for large faces and hands, simple backgrounds and no tiny details. I upscale to 1080x1920 in the edit (Lanczos with light sharpening and film grain). It will look soft on a big screen and fine on a phone.
- **Clip 10 (the sprint) is reframed** as a medium tracking shot, because a wide shot falls apart at 400 pixels.

## Order of work (14 generations, plus images)
| Step | Generations | What |
|---|---|---|
| 1 | VS-A, VS-B, VS-C | The three voice sessions (audio only is used). |
| 2 | Clip 02, clip 03, clip 04 | Clip 01 is already approved. |
| 3 | Clip 05, clip 06, clip 07 | |
| 4 | Clip 08, clip 09, clip 10 | Clip 09 needs the INS-9 still first. |
| 5 | Clip 11 | Then I assemble the episode. |

Retakes are extra. Do the contact sheets first.

## Method for every clip (2 steps)
1. **Keyframe still.** Grok image mode, attach the references listed for the clip, paste the **KEYFRAME** prompt. Keep the one where the face matches the contact sheet.
2. **Animate.** Grok video mode, start image = the approved still, **6 seconds**, **9:16**, paste the **ANIMATE** prompt.

Send each clip as soon as it is made so I can check lip-sync, voices and faces before you spend another generation.

## Standing rules from Sandesh (apply to every prompt and every review)
1. **Objects are handled as a real person would:** real hand grips, correct anatomy (five fingers, natural joints), screens facing the user, a phone held at the ear on calls, strict physics (weight, contact, motion).
2. **Performances are subtle, restrained and naturalistic, never exaggerated:** feeling shows in the eyes, brow, breath and hands. No wide-open mouths, bulging eyes, flailing or theatrical gestures.

These rules are inside every KEYFRAME and ANIMATE prompt below, and in the review checklist.

## Shared checks for every clip
Lips match the words. Objects are handled correctly (grips, anatomy, screens facing the user, phone at the ear, physics). The performance is restrained. The voices are clearly different. The face matches the contact sheet. No readable text. No cuts or ghost images. Natural motion. The phone is silent (its voice is mixed in post).

## The phone voice is made separately (new)
Grok gave the phone voice to the person on screen, or not at all, so the cloned voice is **not** generated inside the Sushma clips any more. Instead:

1. In each Sushma clip, the phone is silent and she reacts to it. Only her own lines are spoken.
2. Generate the three **voice sessions** below: Kabir crying into a phone in a parked car. We use only the **audio**; the picture is thrown away. Start from the Kabir contact sheet face crop.
3. I cut each line from the sessions, filter it to sound like a cheap phone speaker (narrow band, slight distortion), and place it at the exact time shown on each clip.

This also keeps the cloned voice close to the real Kabir's voice, which is the point of the story.


### VS-A: Cloned voice, session A (lines 1 and 3)

Start image: crop of `CS-KABIR` (face). Video mode, 6 seconds, any aspect. Keep the best take.

```
Animate the start image as ONE continuous 6-second shot, no cuts. Close-up of KABIR RAO, an Indian man, 32, oval face, thick tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, sitting in the dark driver's seat of a parked car at night, his face lit only by a phone held close to his mouth, crying and panicked, out of breath. He speaks the lines below into the phone in natural conversational Hindi, sobbing, his voice cracking, with a short ragged sob between lines. His normal LOW chest voice, a grown man's hoarse, cracking baritone, as if crying through a clenched throat: NOT high-pitched, NOT falsetto, NOT a boy's voice. The same low voice he uses in normal conversation, only broken by sobs and shaking. Lips match every word exactly. Nobody else speaks. No music, no text.

DIALOGUE:
1. at about 0.2 s: "मम्मी! मम्मी, मुझे बचा लो!" (pronounced: Mummy! Mummy, mujhe bacha lo!)
2. at about 2.9 s: "एक्सीडेंट हो गया। पुलिस ने पकड़ लिया।" (pronounced: Accident ho gaya. Police ne pakad liya.)

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds. Each line must be said fully and clearly inside its time window.
```

### VS-B: Cloned voice, session B (lines 6 and 9)

Start image: crop of `CS-KABIR` (face). Video mode, 6 seconds, any aspect. Keep the best take.

```
Animate the start image as ONE continuous 6-second shot, no cuts. Close-up of KABIR RAO, an Indian man, 32, oval face, thick tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, sitting in the dark driver's seat of a parked car at night, his face lit only by a phone held close to his mouth, crying and panicked, out of breath. He speaks the lines below into the phone in natural conversational Hindi, sobbing, his voice cracking, with a short ragged sob between lines. His normal LOW chest voice, a grown man's hoarse, cracking baritone, as if crying through a clenched throat: NOT high-pitched, NOT falsetto, NOT a boy's voice. The same low voice he uses in normal conversation, only broken by sobs and shaking. Lips match every word exactly. Nobody else speaks. No music, no text.

DIALOGUE:
1. at about 0.2 s: "चालीस हज़ार यूपीआई करो। अभी। किसी को मत बताना।" (pronounced: Chaalis hazaar UPI karo. Abhi. Kisi ko mat batana.)
2. at about 4.3 s: "जल्दी करो, मम्मी!" (pronounced: Jaldi karo, Mummy!)

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds. Each line must be said fully and clearly inside its time window.
```

### VS-C: Cloned voice, session C (lines 13 and 19)

Start image: crop of `CS-KABIR` (face). Video mode, 6 seconds, any aspect. Keep the best take.

```
Animate the start image as ONE continuous 6-second shot, no cuts. Close-up of KABIR RAO, an Indian man, 32, oval face, thick tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, sitting in the dark driver's seat of a parked car at night, his face lit only by a phone held close to his mouth, crying and panicked, out of breath. He speaks the lines below into the phone in natural conversational Hindi, sobbing, his voice cracking, with a short ragged sob between lines. His normal LOW chest voice, a grown man's hoarse, cracking baritone, as if crying through a clenched throat: NOT high-pitched, NOT falsetto, NOT a boy's voice. The same low voice he uses in normal conversation, only broken by sobs and shaking. Lips match every word exactly. Nobody else speaks. No music, no text.

DIALOGUE:
1. at about 0.2 s: "पुलिस है! मत उठाओ, मम्मी!" (pronounced: Police hai! Mat uthao, Mummy!)
2. at about 3.0 s: "मम्मी, मुझसे प्यार है तो भेजो!" (pronounced: Mummy, mujhse pyaar hai toh bhejo!)

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds. Each line must be said fully and clearly inside its time window.
```

## CLIP 01: HOOK (0:00 to 0:05)

**References to attach for the keyframe:** CS-SUSHMA, LOC-PUNE

### KEYFRAME (image mode)
```
Close-up of SUSHMA in the kitchen of a small middle-class Indian flat in Pune at night: warm tungsten light, steel kitchen counter and containers, a wooden dining table with a plastic runner. A phone is pressed to her ear in her floury right hand, a little flour dusted on her cheek, her left hand flat on the steel counter beside a steel plate of dough. Reading glasses pushed up on her head. Her expression has only just begun to change from ordinary to alarmed. SUSHMA RAO: Indian woman, 58, 155 cm, medium build, wheatish skin with deep smile lines, greying black hair in a loose low bun with silver streaks, a small round red bindi on her forehead, round tortoiseshell reading glasses (pushed up on her head unless stated), small gold nose stud, small gold earrings, a sage-green cotton saree with a thin printed border over a deep teal blouse, a thin gold bangle on each wrist, no necklace, flour on her hands. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Sushma: Indian woman, 58, greying bun, small red bindi, reading glasses on her head, gold nose stud, sage-green saree over a deep teal blouse, floury hands.

WHAT MOVES: 0.0 to 0.3 s: she is already on the call, the phone at her ear. 0.3 to 2.2 s: someone on the other end is crying and begging (you do not hear them in this clip); within about a second her face tightens, her eyes widen slightly and her breath catches, and her left hand rests firmly on the counter edge; her mouth stays closed or barely parted. 2.4 to 3.4 s: she says one soft word, lips matching. 3.4 to 5.0 s: she stares ahead, very still, her eyes glistening and filling slowly; no gasping, no wide eyes.

CAMERA: Handheld CLOSE-UP, her face fills the frame with shoulders just visible, eye level, slow push-in.

PHYSICS: Flour dust falls from her fingers. Her hand shakes with real fear. The phone rests against her cheek and presses her hair slightly.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly. IMPORTANT: the phone is completely silent in this clip. Nobody but the people listed under DIALOGUE speaks. Sushma reacts as if she is hearing a crying, panicked voice on the phone starting at about 0.3 s, and she stops her own speech while it plays.

VOICES (clearly different from each other):
- SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 2.5 s, SUSHMA: "कबीर?" (pronounced: Kabir?)
Each line must be clearly audible.

AUDIO: Kitchen ambience only: exhaust fan hum, a distant pressure-cooker whistle, a wall clock ticking, her breath. No phone ringing.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Cloned voice (phone) @ 0.3 s: मम्मी! मम्मी, मुझे बचा लो! / Mummy! Mummy, mujhe bacha lo! / Mummy! Mummy, save me!
- Sushma @ 2.5 s: कबीर? / Kabir? / Kabir?

**Phone voice (added in post, not generated in this clip):** "मम्मी! मम्मी, मुझे बचा लो!" at 0.3 s. I take it from the voice session and filter it to sound like a phone.

**Post note:** Title card AWAAZ · EP 1 and the word PUNE in the first second.

## CLIP 02: FRICTION (0:05 to 0:10)

**References to attach for the keyframe:** CS-SUSHMA, LOC-PUNE

### KEYFRAME (image mode)
```
Medium close-up of SUSHMA at the kitchen counter in a small middle-class Indian flat in Pune at night: warm tungsten light, steel kitchen counter and containers, a wooden dining table with a plastic runner, the phone pressed to her ear with her right hand, her left hand flat on the steel counter with white flour handprints around it. Her face is frozen in dawning panic. SUSHMA RAO: Indian woman, 58, 155 cm, medium build, wheatish skin with deep smile lines, greying black hair in a loose low bun with silver streaks, a small round red bindi on her forehead, round tortoiseshell reading glasses (pushed up on her head unless stated), small gold nose stud, small gold earrings, a sage-green cotton saree with a thin printed border over a deep teal blouse, a thin gold bangle on each wrist, no necklace, flour on her hands. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Sushma: Indian woman, 58, greying bun, small red bindi, reading glasses on her head, gold nose stud, sage-green saree over a deep teal blouse, floury hands.

WHAT MOVES: 0.0 to 0.4 s: she stands rigid, listening. 0.4 to 2.8 s: the tinny crying voice from the phone speaks; her face tightens, her lips tremble slightly and her eyes glisten; her left hand presses on the counter edge and leaves white floury fingerprints on the steel; no sobbing, no open-mouthed crying. 3.0 to 4.4 s: she speaks, her voice cracking, lips matching. 4.4 to 5.0 s: she closes her eyes for a moment and breathes in slowly.

CAMERA: Handheld medium close-up, a little lower than eye level, slow push-in.

PHYSICS: Flour smears naturally under her fingers. Her saree pallu slips a few centimetres off her shoulder as she grips.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly. IMPORTANT: the phone is completely silent in this clip. Nobody but the people listed under DIALOGUE speaks. Sushma reacts as if she is hearing a crying, panicked voice on the phone starting at about 0.5 s, and she stops her own speech while it plays.

VOICES (clearly different from each other):
- SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 3.0 s, SUSHMA: "हे भगवान! तू ठीक है?" (pronounced: Hey Bhagwan! Tu theek hai?)
Each line must be clearly audible.

AUDIO: The same kitchen ambience, the thin phone voice, her breath.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Cloned voice (phone) @ 0.5 s: एक्सीडेंट हो गया। पुलिस ने पकड़ लिया। / Accident ho gaya. Police ne pakad liya. / There's been an accident. The police have me.
- Sushma @ 3.0 s: हे भगवान! तू ठीक है? / Hey Bhagwan! Tu theek hai? / Oh God! Are you okay?

**Phone voice (added in post, not generated in this clip):** "एक्सीडेंट हो गया। पुलिस ने पकड़ लिया।" at 0.5 s. I take it from the voice session and filter it to sound like a phone.

## CLIP 03: FRICTION (0:10 to 0:15)

**References to attach for the keyframe:** CS-KABIR, LOC-BLR

### KEYFRAME (image mode)
```
Medium close-up of KABIR at a lit desk in an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors. Headphones around his neck, a yellow-and-black pencil in his right hand, two monitors with blurred illegible code behind him. His phone lies face-up on the desk, its screen lit with a contact photo of a smiling older woman. KABIR RAO: Indian man, 32, slim, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses, mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black smartwatch on his left wrist, ONE yellow-and-black mechanical pencil (only this one pencil exists). Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Kabir: Indian man, 32, slim, oval face, tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, mid-grey bomber over blue T-shirt, one yellow-and-black pencil.

WHAT MOVES: 0.0 to 0.8 s: the phone buzzes and lights up; he glances at it. 0.8 to 1.8 s: his jaw tightens, his thumb hovers over the screen. 1.8 to 2.5 s: he swipes it away and flips the phone face-down. 2.5 to 3.8 s: he says one quiet line without looking at it. 3.8 to 5.0 s: he goes back to typing, the pencil tapping the desk.

CAMERA: Handheld medium close-up from slightly to his left, shallow depth of field.

PHYSICS: The phone vibrates on the desk with a real buzz. The pencil taps the desk at a steady rhythm. Rain trickles down the window behind.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly.

VOICES (clearly different from each other):
- KABIR: a young man's voice, warm medium-low baritone, quick and dry, quieter when he avoids something.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 2.6 s, KABIR: "बाद में, मम्मी।" (pronounced: Baad mein, Mummy.)
Each line must be clearly audible.

AUDIO: Office night ambience: air conditioning hum, distant rain, keyboard clicks, the phone buzz, pencil taps.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Kabir @ 2.6 s: बाद में, मम्मी। / Baad mein, Mummy. / Later, Mummy.

**Post note:** Place BENGALURU super.

## CLIP 04: FRICTION (0:15 to 0:20)

**References to attach for the keyframe:** CS-SUSHMA, LOC-PUNE

### KEYFRAME (image mode)
```
Medium close-up of SUSHMA seated at the small wooden dining table in a small middle-class Indian flat in Pune at night: warm tungsten light, steel kitchen counter and containers, a wooden dining table with a plastic runner. A phone lies flat on the table in front of her. A steel thali with half-eaten dinner is pushed aside. Her reading glasses are pushed up on her head. Her hands rest on the table beside the phone, lightly floury and trembling. Her face is tense and still, her mouth closed. SUSHMA RAO: Indian woman, 58, 155 cm, medium build, wheatish skin with deep smile lines, greying black hair in a loose low bun with silver streaks, a small round red bindi on her forehead, round tortoiseshell reading glasses (pushed up on her head unless stated), small gold nose stud, small gold earrings, a sage-green cotton saree with a thin printed border over a deep teal blouse, a thin gold bangle on each wrist, no necklace, flour on her hands. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Sushma: Indian woman, 58, greying bun, small red bindi, reading glasses on her head, gold nose stud, sage-green saree over a deep teal blouse, floury hands.

WHAT MOVES: 0.0 to 3.0 s: she sits almost motionless, staring down at the phone with her mouth CLOSED. She makes no sound and says no words: only her chest rising and falling and her hands trembling slightly. There is no sobbing, no whimpering and no muttering. 2.6 to 3.1 s: with one hand she pulls her reading glasses down onto her nose. 3.3 to 4.5 s: she taps the phone screen with a shaking finger and says one short line, lips matching, voice small and shaky. 4.5 to 5.0 s: she keeps her eyes on the screen. NO large gestures: no hand to her head, no slapping the table.

CAMERA: Handheld medium close-up, slight push-in, eye level.

PHYSICS: The glasses slide down her head and land on her nose naturally. The thali rattles slightly as the table shakes under her trembling hands.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly. IMPORTANT: the phone is completely silent in this clip. Nobody but the people listed under DIALOGUE speaks. Sushma reacts as if she is hearing a crying, panicked voice on the phone starting at about 0.1 s, and she stops her own speech while it plays.

VOICES (clearly different from each other):
- SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 3.4 s, SUSHMA: "भेज रही हूँ, बेटा।" (pronounced: Bhej rahi hoon, beta.)
Each line must be clearly audible.

AUDIO: Fan hum, a clock tick, her fast breathing. She is silent until her one line.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Cloned voice (phone) @ 0.1 s: चालीस हज़ार यूपीआई करो। अभी। किसी को मत बताना। / Chaalis hazaar UPI karo. Abhi. Kisi ko mat batana. / Send forty thousand on UPI. Now. Don't tell anyone.
- Sushma @ 3.4 s: भेज रही हूँ, बेटा। / Bhej rahi hoon, beta. / I'm sending it, son.

**Phone voice (added in post, not generated in this clip):** "चालीस हज़ार यूपीआई करो। अभी। किसी को मत बताना।" at 0.1 s. I take it from the voice session and filter it to sound like a phone.

**Post note:** RETAKE of the rejected take 1, which had Sushma vocalising during the phone-voice window and slapping her head.

## CLIP 05: FRICTION (0:20 to 0:25)

**References to attach for the keyframe:** CS-SUSHMA

### KEYFRAME (image mode)
```
Close-up of SUSHMA's face at the dining table in a small middle-class Indian flat in Pune at night: warm tungsten light, steel kitchen counter and containers, a wooden dining table with a plastic runner, lit from below by the glow of a phone screen held just below frame, reading glasses on her nose, her eyes moving along the screen, lips slightly parted. SUSHMA RAO: Indian woman, 58, 155 cm, medium build, wheatish skin with deep smile lines, greying black hair in a loose low bun with silver streaks, a small round red bindi on her forehead, round tortoiseshell reading glasses (pushed up on her head unless stated), small gold nose stud, small gold earrings, a sage-green cotton saree with a thin printed border over a deep teal blouse, a thin gold bangle on each wrist, no necklace, flour on her hands. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Sushma: Indian woman, 58, greying bun, small red bindi, reading glasses on her head, gold nose stud, sage-green saree over a deep teal blouse, floury hands.

WHAT MOVES: 0.0 to 1.2 s: she reads, eyes moving, lips moving silently. 1.2 s: she stops, her brow drawing together. 1.4 to 3.0 s: she says one slow line quietly, lips matching, doubt in her voice, mouth only slightly open. 3.2 to 4.2 s: a sharp voice on the phone (not heard in this clip) makes her give a small start: her shoulders tighten and her eyes flick up; no big flinch. 4.2 to 5.0 s: she looks back at the screen, undecided.

CAMERA: Handheld close-up with a slow push-in; the phone glow lights her face.

PHYSICS: Phone light flickers on her glasses lenses. Her flinch moves her whole head a few centimetres back.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly. IMPORTANT: the phone is completely silent in this clip. Nobody but the people listed under DIALOGUE speaks. Sushma reacts as if she is hearing a crying, panicked voice on the phone starting at about 3.2 s, and she stops her own speech while it plays.

VOICES (clearly different from each other):
- SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 1.4 s, SUSHMA: "ये नाम तो राहुल का है?" (pronounced: Ye naam toh Rahul ka hai?)
Each line must be clearly audible.

AUDIO: Fan hum, a clock tick, her breathing, the phone voice.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Sushma @ 1.4 s: ये नाम तो राहुल का है? / Ye naam toh Rahul ka hai? / This name is Rahul's?
- Cloned voice (phone) @ 3.2 s: जल्दी करो, मम्मी! / Jaldi karo, Mummy! / Hurry, Mummy!

**Phone voice (added in post, not generated in this clip):** "जल्दी करो, मम्मी!" at 3.2 s. I take it from the voice session and filter it to sound like a phone.

**Post note:** Add the UPI receiver-name overlay (a made-up name) if you want the viewer to read what she reads.

## CLIP 06: FRICTION (0:25 to 0:30)

**References to attach for the keyframe:** CS-KABIR, CS-RIYA, LOC-BLR

### KEYFRAME (image mode)
```
Medium two-shot in an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors. KABIR sits at the lit desk on the right, typing. RIYA arrives from the left with a white mug, olive kurta, lanyard. Kabir's phone lies face-down on the desk between them. KABIR RAO: Indian man, 32, slim, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses, mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black smartwatch on his left wrist, ONE yellow-and-black mechanical pencil (only this one pencil exists). RIYA MENON: Indian woman, 24, slim, round friendly face, large dark eyes, shoulder-length straight black hair in a low ponytail, small silver stud earrings, olive-green cotton kurta over blue jeans, company lanyard with a plain white card, no glasses. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Kabir: Indian man, 32, slim, oval face, tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, mid-grey bomber over blue T-shirt, one yellow-and-black pencil. Riya: Indian woman, 24, black low ponytail, olive kurta, jeans, lanyard.

WHAT MOVES: 0.0 to 1.0 s: Riya walks up; the face-down phone buzzes and creeps across the desk. 1.0 to 3.0 s: Riya looks at the phone and says one line. 3.0 to 4.5 s: Kabir looks at the phone, the annoyance leaves his face, he says one quiet line. 4.5 to 5.0 s: he snatches up the phone.

CAMERA: Handheld medium two-shot at eye level, slight sway.

PHYSICS: The phone vibrates and slides on the desk. The mug steams slightly. Kabir's chair creaks as he sits up.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly.

VOICES (clearly different from each other):
- RIYA: a young woman's voice, clear mid-high pitch, quick and steady.
- KABIR: a young man's voice, warm medium-low baritone, quick and dry, quieter when he avoids something.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 1.0 s, RIYA: "कबीर, तुम्हारी मम्मी तीसरी बार कर रही हैं।" (pronounced: Kabir, tumhaari Mummy teesri baar kar rahi hain.)
2. at about 3.2 s, KABIR: "मम्मी कभी तीन बार नहीं करतीं।" (pronounced: Mummy kabhi teen baar nahin kartin.)
Each line must be clearly audible.

AUDIO: Office ambience, keyboard clicks, the phone buzz, footsteps.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Riya @ 1.0 s: कबीर, तुम्हारी मम्मी तीसरी बार कर रही हैं। / Kabir, tumhaari Mummy teesri baar kar rahi hain. / Kabir, your mother is calling a third time.
- Kabir @ 3.2 s: मम्मी कभी तीन बार नहीं करतीं। / Mummy kabhi teen baar nahin kartin. / Mummy never calls three times.

## CLIP 07: FRICTION (0:30 to 0:35)

**References to attach for the keyframe:** CS-SUSHMA, LOC-PUNE

### KEYFRAME (image mode)
```
Medium close-up of SUSHMA at the dining table in a small middle-class Indian flat in Pune at night: warm tungsten light, steel kitchen counter and containers, a wooden dining table with a plastic runner, on a phone call: the phone is held to her right ear in her right hand with a normal grip, her left hand resting on the table, reading glasses on her nose, her face tense and quiet. SUSHMA RAO: Indian woman, 58, 155 cm, medium build, wheatish skin with deep smile lines, greying black hair in a loose low bun with silver streaks, a small round red bindi on her forehead, round tortoiseshell reading glasses (pushed up on her head unless stated), small gold nose stud, small gold earrings, a sage-green cotton saree with a thin printed border over a deep teal blouse, a thin gold bangle on each wrist, no necklace, flour on her hands. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Sushma: Indian woman, 58, greying bun, small red bindi, reading glasses on her head, gold nose stud, sage-green saree over a deep teal blouse, floury hands.

WHAT MOVES: 0.0 to 0.9 s: she listens with the phone at her ear. 0.9 to 1.5 s: she hears a soft call-waiting beep, lowers the phone about 20 centimetres from her ear and looks at its screen; the BACK of the phone faces the camera and the screen glow lights her face and glasses (we never see the screen). 1.5 to 2.6 s: she says one puzzled line, looking from the phone to the table and back. 2.6 to 4.0 s: she listens to a panicked voice on the phone (not heard in this clip); her thumb rests near the edge of the phone, undecided. 4.0 to 5.0 s: she brings the phone back toward her ear slowly.

CAMERA: Handheld medium close-up, slow push-in, eye level.

PHYSICS: Normal phone grip: four fingers behind, thumb at the side. The screen glow changes on her face as she tilts the phone. Her arm moves with natural weight.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly. IMPORTANT: the phone is completely silent in this clip. Nobody but the people listed under DIALOGUE speaks. Sushma reacts as if she is hearing a crying, panicked voice on the phone starting at about 2.6 s, and she stops her own speech while it plays.

VOICES (clearly different from each other):
- SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 1.6 s, SUSHMA: "तेरा फोन भी आ रहा है।" (pronounced: Tera phone bhi aa raha hai.)
Each line must be clearly audible.

AUDIO: Fan hum, her breathing, a very soft call-waiting beep.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Sushma @ 1.6 s: तेरा फोन भी आ रहा है। / Tera phone bhi aa raha hai. / Your phone is calling too.
- Cloned voice (phone) @ 2.6 s: पुलिस है! मत उठाओ, मम्मी! / Police hai! Mat uthao, Mummy! / It's the police! Don't answer, Mummy!

**Phone voice (added in post, not generated in this clip):** "पुलिस है! मत उठाओ, मम्मी!" at 2.6 s. I take it from the voice session and filter it to sound like a phone.

**Post note:** RETAKE (batch 3 take held the phone up with its screen facing the camera). The call banner is shown in the C12 POV insert.

## CLIP 08: FRICTION (0:35 to 0:40)

**References to attach for the keyframe:** CS-KABIR, CS-RIYA, LOC-BLR

### KEYFRAME (image mode)
```
Handheld two-shot in an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors. KABIR stands at his desk with a phone pressed to his ear, tense. RIYA stands beside him with a laptop tucked under her arm, frowning. Rain on the window behind them. A yellow-and-black pencil lies on the desk. KABIR RAO: Indian man, 32, slim, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses, mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black smartwatch on his left wrist, ONE yellow-and-black mechanical pencil (only this one pencil exists). RIYA MENON: Indian woman, 24, slim, round friendly face, large dark eyes, shoulder-length straight black hair in a low ponytail, small silver stud earrings, olive-green cotton kurta over blue jeans, company lanyard with a plain white card, no glasses. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Kabir: Indian man, 32, slim, oval face, tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, mid-grey bomber over blue T-shirt, one yellow-and-black pencil. Riya: Indian woman, 24, black low ponytail, olive kurta, jeans, lanyard.

WHAT MOVES: 0.0 to 1.2 s: a ring tone is heard from his phone; he waits, tapping the desk with his free hand. 1.2 to 1.8 s: a busy beep; he lowers the phone. 1.8 to 2.6 s: he says one line. 2.6 to 4.2 s: Riya frowns, thinking, and says one line. 4.2 to 5.0 s: Kabir's eyes widen as it lands.

CAMERA: Handheld two-shot, slight push-in on Kabir at the end.

PHYSICS: The phone ring and busy beep are heard from the handset, not the room. Kabir's breathing is audible.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly.

VOICES (clearly different from each other):
- KABIR: a young man's voice, warm medium-low baritone, quick and dry, quieter when he avoids something.
- RIYA: a young woman's voice, clear mid-high pitch, quick and steady.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 1.8 s, KABIR: "बिज़ी जा रहा है।" (pronounced: Busy ja raha hai.)
2. at about 2.6 s, RIYA: "तुमने क्लोनिंग का डेमो दिया था ना?" (pronounced: Tumne cloning ka demo diya tha na?)
Each line must be clearly audible.

AUDIO: Office ambience, rain, the ring tone, a busy beep.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Kabir @ 1.8 s: बिज़ी जा रहा है। / Busy ja raha hai. / It's going busy.
- Riya @ 2.6 s: तुमने क्लोनिंग का डेमो दिया था ना? / Tumne cloning ka demo diya tha na? / You gave that cloning demo, didn't you?

## CLIP 09: SPIKE (0:40 to 0:45)

**References to attach for the keyframe:** CS-KABIR, CS-RIYA, LOC-BLR

### KEYFRAME (image mode)
```
Medium shot in an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors. The camera sits just behind an open laptop on the desk: the BACK of the laptop lid fills the lower foreground (plain silver, no logo). Above it, KABIR stands leaning toward the screen and RIYA stands beside him, both looking down at the screen, their faces lit from below by its cool glow. A yellow-and-black pencil lies on the desk. The people face the laptop screen; the camera does not see the screen. KABIR RAO: Indian man, 32, slim, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses, mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black smartwatch on his left wrist, ONE yellow-and-black mechanical pencil (only this one pencil exists). RIYA MENON: Indian woman, 24, slim, round friendly face, large dark eyes, shoulder-length straight black hair in a low ponytail, small silver stud earrings, olive-green cotton kurta over blue jeans, company lanyard with a plain white card, no glasses. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Kabir: Indian man, 32, slim, oval face, tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, mid-grey bomber over blue T-shirt, one yellow-and-black pencil. Riya: Indian woman, 24, black low ponytail, olive kurta, jeans, lanyard.

WHAT MOVES: 0.0 to 0.8 s: Kabir leans in over the laptop, Riya beside him with one hand resting on the desk. 0.8 to 2.6 s: Riya says one line quietly, glancing at the screen then at him; she does not wave her arms. 2.8 to 4.0 s: Kabir slowly raises one hand to his mouth and whispers one short line through his fingers. 4.0 to 5.0 s: he straightens a little, his face pale and still.

CAMERA: Locked-off medium close-up from behind the laptop, very slight push-in.

PHYSICS: The screen's glow lights both faces from below with a cool white-blue cast and moves as they shift. The laptop is open at a natural angle with its screen facing them, not the camera.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly.

VOICES (clearly different from each other):
- RIYA: a young woman's voice, clear mid-high pitch, quick and steady.
- KABIR: a young man's voice, warm medium-low baritone, quick and dry, quieter when he avoids something.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 0.9 s, RIYA: "तीन सेकंड की आवाज़ काफ़ी होती है।" (pronounced: Teen second ki aawaaz kaafi hoti hai.)
2. at about 2.9 s, KABIR: "मेरी अपनी आवाज़।" (pronounced: Meri apni aawaaz.)
Each line must be clearly audible.

AUDIO: Office ambience, a faint laptop fan, Riya's line, his whisper.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Riya @ 0.9 s: तीन सेकंड की आवाज़ काफ़ी होती है। / Teen second ki aawaaz kaafi hoti hai. / Three seconds of voice is enough.
- Kabir @ 2.9 s: मेरी अपनी आवाज़। / Meri apni aawaaz. / My own voice.

**Post note:** RETAKE (batch 3 take had the screen facing the camera, away from the people). In post I cut a 1.5 s full-screen cutaway of the PROP-STAGE still (slow push-in) between Riya's line and his whisper, so no stage video is needed.

## CLIP 10: SPIKE (0:45 to 0:50)

**References to attach for the keyframe:** CS-KABIR, LOC-BLR

### KEYFRAME (image mode)
```
Side-on shot in an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors. KABIR has just stood up from his desk, his chair mid-spin, a phone pressed to his ear, in the aisle between rows of desks, the aisle leading to a glass door at the end. Motion in his whole body. KABIR RAO: Indian man, 32, slim, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses, mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black smartwatch on his left wrist, ONE yellow-and-black mechanical pencil (only this one pencil exists). Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Kabir: Indian man, 32, slim, oval face, tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, mid-grey bomber over blue T-shirt, one yellow-and-black pencil.

WHAT MOVES: 0.0 to 0.7 s: as he stands, his arm knocks the yellow-and-black pencil off the desk (it lies there in the earlier shots) and it clatters to the floor; the chair spins and bangs the desk. 0.7 to 3.8 s: he sprints along the aisle toward the glass door, jacket flying, phone at his ear; between 1.0 and 2.5 s he shouts one line into the phone, out of breath. 3.8 to 5.0 s: he hits the glass door with his shoulder and pushes through.

CAMERA: Handheld MEDIUM tracking shot from the side at his pace (his head and upper body fill the frame, not a wide shot), slightly low angle, with real camera shake.

PHYSICS: Running looks natural: weight shifts, arms drive, jacket and hair flow with the motion. The chair spins to a stop. The pencil bounces once.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly.

VOICES (clearly different from each other):
- KABIR: a young man's voice, warm medium-low baritone, quick and dry, quieter when he avoids something.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 1.0 s, KABIR: "मम्मी, मत भेजना!" (pronounced: Mummy, mat bhejna!)
Each line must be clearly audible.

AUDIO: Fast footsteps on the floor, panting, the chair bang, the pencil clatter, the glass door thud, a ringing tone from the phone.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Kabir @ 1.0 s: मम्मी, मत भेजना! / Mummy, mat bhejna! / Mummy, don't send it!

**Post note:** Fallback if the sprint looks broken at this resolution: he stands, grabs his jacket from the chair and strides fast out of frame with the phone at his ear, same line, same timing. Add office ambience and footsteps in post.

## CLIP 11: FRICTION (0:50 to 0:55)

**References to attach for the keyframe:** CS-SUSHMA

### KEYFRAME (image mode)
```
Close-up of SUSHMA at the dining table in a small middle-class Indian flat in Pune at night: warm tungsten light, steel kitchen counter and containers, a wooden dining table with a plastic runner, the phone held to her right ear in a normal grip, her eyes glistening, her face still and drawn, reading glasses on her nose. SUSHMA RAO: Indian woman, 58, 155 cm, medium build, wheatish skin with deep smile lines, greying black hair in a loose low bun with silver streaks, a small round red bindi on her forehead, round tortoiseshell reading glasses (pushed up on her head unless stated), small gold nose stud, small gold earrings, a sage-green cotton saree with a thin printed border over a deep teal blouse, a thin gold bangle on each wrist, no necklace, flour on her hands. Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: Sushma: Indian woman, 58, greying bun, small red bindi, reading glasses on her head, gold nose stud, sage-green saree over a deep teal blouse, floury hands.

WHAT MOVES: 0.0 to 2.6 s: she listens with the phone at her ear, very still, her eyes slowly filling; a single tear runs down one cheek. No sobbing, no open mouth. 2.8 to 4.0 s: she whispers one short line, lips matching, barely audible. 4.0 to 5.0 s: she lowers the phone slowly from her ear and looks down at it.

CAMERA: Handheld close-up, slow push-in, eye level.

PHYSICS: A tear runs down under gravity. The phone comes down from her ear with natural arm weight.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly. IMPORTANT: the phone is completely silent in this clip. Nobody but the people listed under DIALOGUE speaks. Sushma reacts as if she is hearing a crying, panicked voice on the phone starting at about 0.2 s, and she stops her own speech while it plays.

VOICES (clearly different from each other):
- SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear.

DIALOGUE in natural conversational Hindi, in this order, no overlap:
1. at about 3.0 s, SUSHMA: "कौन-सा कबीर?" (pronounced: Kaun-sa Kabir?)
Each line must be clearly audible.

AUDIO: Her shaky breath, a clock tick, a very soft call-waiting chime.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**

- Cloned voice (phone) @ 0.2 s: मम्मी, मुझसे प्यार है तो भेजो! / Mummy, mujhse pyaar hai toh bhejo! / Mummy, if you love me, send it!
- Sushma @ 3.0 s: कौन-सा कबीर? / Kaun-sa Kabir? / Which Kabir?

**Phone voice (added in post, not generated in this clip):** "मम्मी, मुझसे प्यार है तो भेजो!" at 0.2 s. I take it from the voice session and filter it to sound like a phone.

**Post note:** RETAKE (batch 3 take had open-mouthed sobbing and a garbled banner). The thumb beat is now clip 12.

## CLIP 12: BUTTON (0:55 to 1:00 (freeze made in post))

**References to attach for the keyframe:** CS-SUSHMA (for the hands)

### KEYFRAME (image mode)
```
First-person POV looking down at a phone held in one hand (natural grip, four fingers behind, thumb free). The screen faces the camera because the camera is her eyes. The screen is a plain dark payment screen with a large plain green button at the bottom and a plain green call-accept button on a banner at the top, no text. Her other hand rests on a wooden table with a little flour. Warm kitchen light, shallow depth of field. No face visible.  Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE (video mode, 6 s)
```
Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.

PEOPLE: 

WHAT MOVES: 0.0 to 3.0 s: her thumb trembles slightly above the glass, drifting slowly between the upper and lower buttons, never touching. A single tear falls onto the back of the hand holding the phone. 3.0 to 6.0 s: the thumb stops, hovering, completely still, between the two buttons.

CAMERA: Locked-off POV insert from her eye level, very shallow depth of field on the thumb.

PHYSICS: The thumb hovers a few millimetres above the glass and trembles. The tear falls under gravity and lands on skin. Natural phone grip.

STANDING RULES: STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.

LIP SYNC: Only the person who is speaking moves their lips, and every word matches their lips exactly.

VOICES (clearly different from each other):
- none (no one on screen speaks)

DIALOGUE in natural conversational Hindi, in this order, no overlap:
none
Each line must be clearly audible.

AUDIO: Room sound drops away. A faint ringtone and a muffled, begging voice overlap, both quiet. Her breath.

STYLE: Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos or readable writing anywhere in the picture. No background music.

DURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.
```

**Dialogue for your check**


**Post note:** Freeze at 0:57 and hold; caption कौन-सा कबीर? and EP 2 →; cut to black at 0:59.5. I add the UI text and the call banner. The faint 'मम्मी...' is cut from voice session A.

## CLIP INS-9: PROP (still for clip 09)

**References to attach for the keyframe:** PROP-STAGE, CS-KABIR

### KEYFRAME (image mode)
```
Photorealistic 16:9 still of KABIR RAO on a modern tech conference stage at a lectern, mid-sentence, one hand raised palm-up, a headset microphone at his cheek, a large screen behind him with an abstract waveform and no text, a dark blurred audience in the foreground. KABIR RAO: Indian man, 32, slim, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses, mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black smartwatch on his left wrist, ONE yellow-and-black mechanical pencil (only this one pencil exists). Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated. Photorealistic, 16:9, natural skin with pores and fine detail, real fabric texture, shallow depth of field, teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.
```

### ANIMATE
None. Still only, see the post note.

**Dialogue for your check**

- Kabir @ 0.6 s: बस तीन सेकंड की आवाज़ चाहिए। और क्लोन तैयार। / Bas teen second ki aawaaz chahiye. Aur clone taiyaar. / I only need three seconds of voice. And the clone is ready.

**Post note:** STILL ONLY: do not make a video. Use the approved PROP-STAGE picture; I put it on the laptop screen in clip 09 with a slow push-in. Not counted in the 60 seconds.

