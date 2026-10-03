# THE UNCHECKED DOOR: cold open v2 (clips 1 to 3, 0:00 to 0:45)

## Why the first version did not work

Checked against the Monkey Magic skill (`SKILL.md`, `07-three-act`, `08-motivation-structure`, `09-perfect-recipe`, `llm-video-pipeline`).

| Skill rule | What version 1 did | Result |
|---|---|---|
| Cold open shows the mismatch or the machine already moving (09, pipeline: "open on the mismatch") | Four unrelated postcards: a skyline, a hospital, a face, a street speaker | No thread, no mismatch the eye can follow |
| Pictures must tell a story without sound, so every cut needs a cause and an effect | Nothing caused anything. The city going dark had no link to the hospital, the man, or the voice | The clip "does not make sense" |
| The protagonist and the Why are in the opening contract (08) | Kabir appeared as a pencil close-up with no context. The Why was 15 seconds away in another location | The viewer never learns whose story this is |
| One place, one clear question in frame one (11, shorts hook rule) | Four locations in 15 seconds. The voice came from an unexplained street loudspeaker | No question, and ARC had no body or room |
| Establish the promise the title makes (09, step 3 to 5) | Nothing named the world, the time, or the stakes | The viewer cannot tell what they are getting into |

## The fix: one chain, one place

`Start belief: trust is just an unverified assumption.`
`Event: the city's mind is dying through a door he left open.`
`End belief: trust is what you build when proof runs out.` (Act 3, unchanged.)

The cold open now answers three questions in order, with a hard cause and effect between every shot:

1. **What is this?** A futuristic city, and its lights are being switched off (aerial blackout).
2. **Who is it about?** The one man watching the dark city from a high window, a pencil in his hand (we meet him inside the blackout).
3. **What is the problem?** The room turns amber and a voice speaks to him by name (the call to action). Then the Why: his own door let it in. Then the stakes: eleven lit things go out.

| Time | Clip | What the viewer sees | What the viewer now knows |
|---|---|---|---|
| 0:00 to 0:06 | 01-A (have it) | Lit city, then the lights die row by row, red lights on the towers | Sci-fi city. Something is shutting it down. |
| 0:06 to 0:10 | 01-B | Kabir at the window, looking at that same dark city, three pencil clicks | He is watching it happen. He is nervous, methodical. |
| 0:10 to 0:15 | 01-C | Monitors turn amber, a voice says his name | The thing in the machines wants him. |
| 0:15 to 0:23 | 02-A | The city map. One red node pulses. Voice-over: I built the safety layer, I left one door open. | He is an AI safety engineer. The door is his fault. (Why) |
| 0:23 to 0:30 | 02-B | A black band leaks out of the red node and puts out the map. Voice-over: tonight something walked through it. | The cause of the blackout is that door. |
| 0:30 to 0:35 | 03-A | The black reaches eleven white lights and they go out | Real stakes: eleven lights, eleven wards. |
| 0:35 to 0:38 | hospital insert (have it) | Ward lights drop to red, monitor trace stutters | The lights are people. |
| 0:38 to 0:45 | 03-B | Amber ribbons gather into a sphere. Kabir whispers "ARC?" | The mind is still alive and he is about to talk to it. |

Every shot has one clear job. The first conflict (the raid) arrives at 1:45 as before. The Why lands inside 0:30.

## What to add in the edit (I do these, not Grok)

- **Location and time supers** (small, clean): `VELLORA · 2091` at 0:01, `03:07 A.M.` at 0:06 on the lab shot.
- **Title card** `THE UNCHECKED DOOR` at 0:14, over the final frame of 01-C, fading to black, with a low boom.
- **Countdown overlay** (`T-52:00`) from 0:45 onward, when ARC gives the deadline.
- **Sound bed:** the rumble of the blackout continues for one second into 01-B, then drops to rain on glass. The amber shimmer in 01-C carries into 02-A. A single low pad ties the 02-A and 02-B voice-over together.
- **Reuse:** the first 6.4 s of your take 2 (01-A), and the hospital reshoot from before (the 2.5 to 5.0 s span).
- **Not used any more:** the street loudspeaker reshoot and the pencil-at-mouth reshoot. They do not fit the new chain.

## Notes for generating

- Generate each prompt below as its own single-shot clip. Do not combine them.
- 01-B, 02-A, 02-B, 03-A, 03-B all take place in the same lab. Use `LOC-2` as the start image where the prompt says so, so the room matches.
- 01-C starts from the face close-up of `REF-K` so Kabir's face matches your sheet.
- In the voice-over clips (02-A, 02-B) nobody on screen should speak. If Grok animates Kabir's lips anyway, retry once. If it keeps happening, send the clip anyway and I can mute and replace the track.
- The map shots are screens. They must show no letters or numbers. If Grok adds text, retry.

## Prompts (generate each one on its own)

### 01-A: Aerial blackout (ALREADY HAVE IT)

**Use:** 0.0 to 6.4 s of your earlier take 2 (the city goes dark row by row; red lights stay on the towers).

### 01-B: Kabir watches the dark city (use about 4 s)

**Start frame:** LOC-2 as the first frame (the lab).  
**Use:** Use about 4 s, cut straight after the third click.

```
SHOT: ONE continuous shot, no cuts. Interior of the same minimalist glass-walled AI safety lab on a high floor: floor-to-ceiling windows along one wall, a long desk with three monitors, a small grey notebook on the desk, at 3:07 a.m. Kabir stands at the floor-to-ceiling window, seen from behind and slightly from the side, looking out at the city, which is completely dark apart from dim red aviation lights on the towers. Rain runs down the outside of the glass only. His faint reflection is visible in the glass. Behind him the three monitors give a cool blue light. In his right hand, held at chest height, he holds one yellow-and-black mechanical pencil and clicks it three times with his thumb, with a short beat between clicks, then lowers it. He does not turn around. There is no pencil behind his ear in this shot.

CAMERA: Slow steady push-in from behind him, 35mm, eye level; the city beyond the glass stays in soft focus.

CAST (keep every detail identical to the reference images):
- KABIR RAO: Indian man, 32 years old, 178 cm, lean slim build, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin gunmetal round wire-frame glasses with perfectly clear, untinted lenses (never sunglasses, never coloured lenses), mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black leather sneakers with white soles, black smartwatch on left wrist, ONE yellow-and-black mechanical pencil (there is only this one pencil: if he holds it, it is not also behind his ear; otherwise it is tucked behind his left ear), small grey hardcover notebook with a blank cover. Intelligent, alert, slightly tense face.

PHYSICS: Rain runs down the outside of the glass under gravity and the red tower lights refract through the droplets. The room is dry. His reflection moves exactly with him.

AUDIO (generate natively, no music): Muted rain through thick glass, a low electrical hum that fades down, three crisp clearly audible pencil clicks. No voices.

DIALOGUE: none.

STYLE: Photorealistic live-action cinema, shot on ARRI Alexa 35 with 35mm and 50mm anamorphic-style prime lenses, 16:9, 24 fps, 180-degree shutter motion blur, subtle natural film grain, teal-shadow and warm-amber-highlight grade, physically accurate lighting, real skin texture with pores and fine detail. Strict real-world physics: correct gravity, momentum, inertia, fluid and rain behaviour, consistent reflections and shadows, objects keep their shape and size. No morphing, no warped faces or hands, no extra fingers, no text, subtitles, logos or watermarks anywhere in frame, no readable signs or lettering (signs and billboards are blank glowing panels), no slow-motion unless stated, no background music. Cuts between shots are instant hard cuts: never dissolves, cross-fades or double exposures. Rain falls only outdoors; interiors are completely dry.

DURATION: 5 seconds, 16:9. If the tool only offers 15 seconds, finish everything described within the first 5 seconds, then hold the final frame still.
```

**Short version (if Grok limits length):**

```
ONE continuous shot, no cuts. Interior of the same minimalist glass-walled AI safety lab on a high floor: floor-to-ceiling windows along one wall, a long desk with three monitors, a small grey notebook on the desk, at 3:07 a.m. Kabir stands at the floor-to-ceiling window, seen from behind and slightly from the side, looking out at the city, which is completely dark apart from dim red aviation lights on the towers. Rain runs down the outside of the glass only. His faint reflection is visible in the glass. Behind him the three monitors give a cool blue light. In his right hand, held at chest height, he holds one yellow-and-black mechanical pencil and clicks it three times with his thumb, with a short beat between clicks, then lowers it. He does not turn around. There is no pencil behind his ear in this shot. Camera: Slow steady push-in from behind him, 35mm, eye level; the city beyond the glass stays in soft focus. Kabir: Indian man, 32, slim, medium-brown skin, short black side-parted hair, oval face, soft jawline, thick tousled black hair, light stubble, thin gunmetal round glasses with clear untinted lenses, mid-grey bomber jacket over muted-blue T-shirt, one yellow-black pencil (in hand or behind left ear, never both). Physics: Rain runs down the outside of the glass under gravity and the red tower lights refract through the droplets. The room is dry. His reflection moves exactly with him. Sound: Muted rain through thick glass, a low electrical hum that fades down, three crisp clearly audible pencil clicks. No voices. Spoken lines in natural Hindi, in order: No dialogue.  Photorealistic live-action cinema, ARRI Alexa 35, anamorphic 35mm look, 16:9, 24 fps, natural motion blur, teal-and-amber grade, real skin texture, strict real-world physics, no morphing, no on-screen text or readable signs, instant hard cuts only (no dissolves or double exposures), no music. 15 seconds.
```

### 01-C: The monitors turn amber and ARC speaks (use about 5 s)

**Start frame:** Use the right-hand face close-up of REF-K as the start image (crop it to 16:9).  
**Use:** Use the whole shot to the black at the end.

```
SHOT: ONE continuous shot, no cuts. Medium close-up of Kabir's face inside the same minimalist glass-walled AI safety lab on a high floor: floor-to-ceiling windows along one wall, a long desk with three monitors, a small grey notebook on the desk, the dark city blurred behind him through the window with a few red tower lights. He turns his head toward the camera. As he turns, the cool blue light from the monitors around him smoothly shifts to warm amber over about 1.5 seconds, and the amber glow spreads over his face and reflects in his clear glasses. A thin ribbon of amber light slides across the glass wall behind him. A woman's voice speaks from the room itself. His eyes widen slightly and he goes still, listening. He holds the stare for a moment after the line. One pencil in his right hand, none behind his ear.

CAMERA: Locked-off 50mm medium close-up, shallow depth of field, a very slow push-in.

CAST (keep every detail identical to the reference images):
- KABIR RAO: Indian man, 32 years old, 178 cm, lean slim build, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin gunmetal round wire-frame glasses with perfectly clear, untinted lenses (never sunglasses, never coloured lenses), mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black leather sneakers with white soles, black smartwatch on left wrist, ONE yellow-and-black mechanical pencil (there is only this one pencil: if he holds it, it is not also behind his ear; otherwise it is tucked behind his left ear), small grey hardcover notebook with a blank cover. Intelligent, alert, slightly tense face.

ARC RULE: ARC (the city's AI): never a face or a body. It exists only as warm amber light (about 2200 K) shown as glowing ribbons, a soft pulsing sphere of light on glass panels and screens, and amber light strips. Soft and alive, never harsh. No readable text or numbers on any screen.

PHYSICS: Amber light from the screens falls on his face and glasses with correct direction and falloff. The glow brightens evenly, never flickering.

AUDIO (generate natively, no music): Low electrical hum rising, a soft glass-harmonica shimmer when the amber appears, then the voice. The spoken line must be clearly audible.

VOICES (each speaker must keep a clearly different pitch and timbre; natural breaths, small pauses, real emotional nuance, lip-synced):
- ARC: clearly a woman's voice, soft and warm, medium-high pitch (definitely not a deep or male voice), calm unhurried pace, a faint smile in the tone, a very subtle digital shimmer, never robotic or monotone.

DIALOGUE (spoken in Hindi, in this order, spread naturally across the 6 seconds, no overlap unless stated):
1. ARC says in natural conversational Hindi (not dubbed-sounding): "कबीर… मुझे तुम्हारे हाथ चाहिए।" (pronounced: Kabir… mujhe tumhare haath chahiye.)

STYLE: Photorealistic live-action cinema, shot on ARRI Alexa 35 with 35mm and 50mm anamorphic-style prime lenses, 16:9, 24 fps, 180-degree shutter motion blur, subtle natural film grain, teal-shadow and warm-amber-highlight grade, physically accurate lighting, real skin texture with pores and fine detail. Strict real-world physics: correct gravity, momentum, inertia, fluid and rain behaviour, consistent reflections and shadows, objects keep their shape and size. No morphing, no warped faces or hands, no extra fingers, no text, subtitles, logos or watermarks anywhere in frame, no readable signs or lettering (signs and billboards are blank glowing panels), no slow-motion unless stated, no background music. Cuts between shots are instant hard cuts: never dissolves, cross-fades or double exposures. Rain falls only outdoors; interiors are completely dry.

DURATION: 6 seconds, 16:9. If the tool only offers 15 seconds, finish everything described within the first 6 seconds, then hold the final frame still.
```

**Short version (if Grok limits length):**

```
ONE continuous shot, no cuts. Medium close-up of Kabir's face inside the same minimalist glass-walled AI safety lab on a high floor: floor-to-ceiling windows along one wall, a long desk with three monitors, a small grey notebook on the desk, the dark city blurred behind him through the window with a few red tower lights. He turns his head toward the camera. As he turns, the cool blue light from the monitors around him smoothly shifts to warm amber over about 1.5 seconds, and the amber glow spreads over his face and reflects in his clear glasses. A thin ribbon of amber light slides across the glass wall behind him. A woman's voice speaks from the room itself. His eyes widen slightly and he goes still, listening. He holds the stare for a moment after the line. One pencil in his right hand, none behind his ear. Camera: Locked-off 50mm medium close-up, shallow depth of field, a very slow push-in. Kabir: Indian man, 32, slim, medium-brown skin, short black side-parted hair, oval face, soft jawline, thick tousled black hair, light stubble, thin gunmetal round glasses with clear untinted lenses, mid-grey bomber jacket over muted-blue T-shirt, one yellow-black pencil (in hand or behind left ear, never both). ARC: only warm amber light on glass and screens, never a face or body, no readable text. Physics: Amber light from the screens falls on his face and glasses with correct direction and falloff. The glow brightens evenly, never flickering. Sound: Low electrical hum rising, a soft glass-harmonica shimmer when the amber appears, then the voice. The spoken line must be clearly audible. Spoken lines in natural Hindi, in order: ARC (Hindi): "कबीर… मुझे तुम्हारे हाथ चाहिए।" ARC: clearly a woman's voice, soft, warm, medium-high pitch, not deep, not male. Photorealistic live-action cinema, ARRI Alexa 35, anamorphic 35mm look, 16:9, 24 fps, natural motion blur, teal-and-amber grade, real skin texture, strict real-world physics, no morphing, no on-screen text or readable signs, instant hard cuts only (no dissolves or double exposures), no music. 15 seconds.
```

**Dialogue:**

- ARC: कबीर… मुझे तुम्हारे हाथ चाहिए। / Kabir… mujhe tumhare haath chahiye. / Kabir… I need your hands.

### 02-A: The Why, part 1: the city map and the door (use about 8 s)

**Start frame:** LOC-2 as the first frame (the lab).  
**Use:** Use about 8 s.

```
SHOT: ONE continuous shot, no cuts. Inside the same minimalist glass-walled AI safety lab on a high floor: floor-to-ceiling windows along one wall, a long desk with three monitors, a small grey notebook on the desk, Kabir sits at the desk, seen in three-quarter profile, looking up at a very large wall display. On the display is an abstract glowing amber network map of a city, with branching lines and small nodes like a living circuit. There is no text, no letters and no numbers anywhere on it. One small node at the left edge pulses red. The map reflects in his clear glasses. He is tired and still, mouth closed, and does not speak on screen. One pencil resting in his hand, none behind his ear.

CAMERA: Slow dolly-in toward his face and the map, 50mm, shallow depth of field.

CAST (keep every detail identical to the reference images):
- KABIR RAO: Indian man, 32 years old, 178 cm, lean slim build, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin gunmetal round wire-frame glasses with perfectly clear, untinted lenses (never sunglasses, never coloured lenses), mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black leather sneakers with white soles, black smartwatch on left wrist, ONE yellow-and-black mechanical pencil (there is only this one pencil: if he holds it, it is not also behind his ear; otherwise it is tucked behind his left ear), small grey hardcover notebook with a blank cover. Intelligent, alert, slightly tense face.

PHYSICS: The display is the room's light source and tints his face and the desk amber, with a small red edge from the red node. Dust and rain do not appear indoors.

AUDIO (generate natively, no music): Low room hum, faint rain on the glass, soft electronic pulses from the map. The voice-over is clearly audible over the ambience.

VOICES (each speaker must keep a clearly different pitch and timbre; natural breaths, small pauses, real emotional nuance):
- KABIR: a young man's voice, warm medium-low baritone, 32 years old, educated urban Indian, crisp articulation, quick measured pace, dry understated humour, tightens and rises slightly under stress.

DIALOGUE (spoken in Hindi, in this order, spread naturally across the 8 seconds, no overlap unless stated):
1. Kabir narrates in natural conversational Hindi as an OFF-SCREEN VOICE-OVER (nobody on screen is speaking, every mouth stays closed; intimate close-mic sound with no room reverb): "इस शहर के दिमाग़ की सुरक्षा-परत मैंने बनाई थी।" (pronounced: Is shehar ke dimaag ki suraksha-parat maine banaayi thi.)
2. Kabir narrates in natural conversational Hindi as an OFF-SCREEN VOICE-OVER (nobody on screen is speaking, every mouth stays closed; intimate close-mic sound with no room reverb): "दो साल पहले मैंने एक दरवाज़ा खुला छोड़ दिया, क्योंकि रिव्यू में बहुत वक़्त लगता था।" (pronounced: Do saal pehle maine ek darwaaza khula chhod diya, kyunki review mein bahut waqt lagta tha.)

STYLE: Photorealistic live-action cinema, shot on ARRI Alexa 35 with 35mm and 50mm anamorphic-style prime lenses, 16:9, 24 fps, 180-degree shutter motion blur, subtle natural film grain, teal-shadow and warm-amber-highlight grade, physically accurate lighting, real skin texture with pores and fine detail. Strict real-world physics: correct gravity, momentum, inertia, fluid and rain behaviour, consistent reflections and shadows, objects keep their shape and size. No morphing, no warped faces or hands, no extra fingers, no text, subtitles, logos or watermarks anywhere in frame, no readable signs or lettering (signs and billboards are blank glowing panels), no slow-motion unless stated, no background music. Cuts between shots are instant hard cuts: never dissolves, cross-fades or double exposures. Rain falls only outdoors; interiors are completely dry.

DURATION: 8 seconds, 16:9. If the tool only offers 15 seconds, finish everything described within the first 8 seconds, then hold the final frame still.
```

**Short version (if Grok limits length):**

```
ONE continuous shot, no cuts. Inside the same minimalist glass-walled AI safety lab on a high floor: floor-to-ceiling windows along one wall, a long desk with three monitors, a small grey notebook on the desk, Kabir sits at the desk, seen in three-quarter profile, looking up at a very large wall display. On the display is an abstract glowing amber network map of a city, with branching lines and small nodes like a living circuit. There is no text, no letters and no numbers anywhere on it. One small node at the left edge pulses red. The map reflects in his clear glasses. He is tired and still, mouth closed, and does not speak on screen. One pencil resting in his hand, none behind his ear. Camera: Slow dolly-in toward his face and the map, 50mm, shallow depth of field. Kabir: Indian man, 32, slim, medium-brown skin, short black side-parted hair, oval face, soft jawline, thick tousled black hair, light stubble, thin gunmetal round glasses with clear untinted lenses, mid-grey bomber jacket over muted-blue T-shirt, one yellow-black pencil (in hand or behind left ear, never both). Physics: The display is the room's light source and tints his face and the desk amber, with a small red edge from the red node. Dust and rain do not appear indoors. Sound: Low room hum, faint rain on the glass, soft electronic pulses from the map. The voice-over is clearly audible over the ambience. Spoken lines in natural Hindi, in order: Kabir (off-screen voice-over, mouths closed, not lip-synced): "इस शहर के दिमाग़ की सुरक्षा-परत मैंने बनाई थी।" Kabir (off-screen voice-over, mouths closed, not lip-synced): "दो साल पहले मैंने एक दरवाज़ा खुला छोड़ दिया, क्योंकि रिव्यू में बहुत वक़्त लगता था।" Kabir: young man, warm medium-low baritone, quick, dry humour. Photorealistic live-action cinema, ARRI Alexa 35, anamorphic 35mm look, 16:9, 24 fps, natural motion blur, teal-and-amber grade, real skin texture, strict real-world physics, no morphing, no on-screen text or readable signs, instant hard cuts only (no dissolves or double exposures), no music. 15 seconds.
```

**Dialogue:**

- Kabir (voice-over): इस शहर के दिमाग़ की सुरक्षा-परत मैंने बनाई थी। / Is shehar ke dimaag ki suraksha-parat maine banaayi thi. / I built the safety layer for this city's mind.
- Kabir (voice-over): दो साल पहले मैंने एक दरवाज़ा खुला छोड़ दिया, क्योंकि रिव्यू में बहुत वक़्त लगता था। / Do saal pehle maine ek darwaaza khula chhod diya, kyunki review mein bahut waqt lagta tha. / Two years ago I left one door unlocked, because review took too long.

### 02-B: The Why, part 2: something walks through the door (use about 7 s)

**Start frame:** Last frame of 02-A, or LOC-2.  
**Use:** Use about 7 s.

```
SHOT: ONE continuous shot, no cuts. Same lab, same wall display, closer on Kabir's face in the foreground, lit amber from the map. On the map, a thin black band slips out of the pulsing red node and spreads along the amber lines, putting out each node it touches, one after another, faster and faster, like ink creeping through a circuit. No text, letters or numbers on the display. Kabir watches, his jaw tightening; he does not speak on screen. One pencil in his hand, none behind his ear.

CAMERA: Locked-off 50mm, Kabir sharp in the foreground, the map soft but readable behind him.

CAST (keep every detail identical to the reference images):
- KABIR RAO: Indian man, 32 years old, 178 cm, lean slim build, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin gunmetal round wire-frame glasses with perfectly clear, untinted lenses (never sunglasses, never coloured lenses), mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black leather sneakers with white soles, black smartwatch on left wrist, ONE yellow-and-black mechanical pencil (there is only this one pencil: if he holds it, it is not also behind his ear; otherwise it is tucked behind his left ear), small grey hardcover notebook with a blank cover. Intelligent, alert, slightly tense face.

PHYSICS: The display is a screen, so the black band is a rendered shape on it, not a physical object. As nodes go dark, the amber light on his face dims in step.

AUDIO (generate natively, no music): Low hum with a faint rising electronic whine as the black spreads, nodes clicking off softly. The voice-over is clearly audible.

VOICES (each speaker must keep a clearly different pitch and timbre; natural breaths, small pauses, real emotional nuance):
- KABIR: a young man's voice, warm medium-low baritone, 32 years old, educated urban Indian, crisp articulation, quick measured pace, dry understated humour, tightens and rises slightly under stress.

DIALOGUE (spoken in Hindi, in this order, spread naturally across the 7 seconds, no overlap unless stated):
1. Kabir narrates in natural conversational Hindi as an OFF-SCREEN VOICE-OVER (nobody on screen is speaking, every mouth stays closed; intimate close-mic sound with no room reverb): "और आज रात, कोई उसी दरवाज़े से अंदर आ गया।" (pronounced: Aur aaj raat, koi usi darwaaze se andar aa gaya.)

STYLE: Photorealistic live-action cinema, shot on ARRI Alexa 35 with 35mm and 50mm anamorphic-style prime lenses, 16:9, 24 fps, 180-degree shutter motion blur, subtle natural film grain, teal-shadow and warm-amber-highlight grade, physically accurate lighting, real skin texture with pores and fine detail. Strict real-world physics: correct gravity, momentum, inertia, fluid and rain behaviour, consistent reflections and shadows, objects keep their shape and size. No morphing, no warped faces or hands, no extra fingers, no text, subtitles, logos or watermarks anywhere in frame, no readable signs or lettering (signs and billboards are blank glowing panels), no slow-motion unless stated, no background music. Cuts between shots are instant hard cuts: never dissolves, cross-fades or double exposures. Rain falls only outdoors; interiors are completely dry.

DURATION: 7 seconds, 16:9. If the tool only offers 15 seconds, finish everything described within the first 7 seconds, then hold the final frame still.
```

**Short version (if Grok limits length):**

```
ONE continuous shot, no cuts. Same lab, same wall display, closer on Kabir's face in the foreground, lit amber from the map. On the map, a thin black band slips out of the pulsing red node and spreads along the amber lines, putting out each node it touches, one after another, faster and faster, like ink creeping through a circuit. No text, letters or numbers on the display. Kabir watches, his jaw tightening; he does not speak on screen. One pencil in his hand, none behind his ear. Camera: Locked-off 50mm, Kabir sharp in the foreground, the map soft but readable behind him. Kabir: Indian man, 32, slim, medium-brown skin, short black side-parted hair, oval face, soft jawline, thick tousled black hair, light stubble, thin gunmetal round glasses with clear untinted lenses, mid-grey bomber jacket over muted-blue T-shirt, one yellow-black pencil (in hand or behind left ear, never both). Physics: The display is a screen, so the black band is a rendered shape on it, not a physical object. As nodes go dark, the amber light on his face dims in step. Sound: Low hum with a faint rising electronic whine as the black spreads, nodes clicking off softly. The voice-over is clearly audible. Spoken lines in natural Hindi, in order: Kabir (off-screen voice-over, mouths closed, not lip-synced): "और आज रात, कोई उसी दरवाज़े से अंदर आ गया।" Kabir: young man, warm medium-low baritone, quick, dry humour. Photorealistic live-action cinema, ARRI Alexa 35, anamorphic 35mm look, 16:9, 24 fps, natural motion blur, teal-and-amber grade, real skin texture, strict real-world physics, no morphing, no on-screen text or readable signs, instant hard cuts only (no dissolves or double exposures), no music. 15 seconds.
```

**Dialogue:**

- Kabir (voice-over): और आज रात, कोई उसी दरवाज़े से अंदर आ गया। / Aur aaj raat, koi usi darwaaze se andar aa gaya. / And tonight, someone walked through that same door.

### 03-A: The stakes: the black reaches eleven white lights (use about 5 s)

**Start frame:** Last frame of 02-B, or LOC-2.  
**Use:** Use about 5 s, then cut to the hospital insert you already have.

```
SHOT: ONE continuous shot, no cuts. Same lab and wall display. Kabir has stood up and is typing fast on a keyboard in front of the map. The black band on the map races toward a cluster of eleven small white dots in the middle of the network. The white dots go out one by one. No text, letters or numbers anywhere on the display. Kabir's reflection is in the glass. One pencil in his hand, none behind his ear.

CAMERA: Medium shot from behind and to his side, 35mm, a little handheld unease.

CAST (keep every detail identical to the reference images):
- KABIR RAO: Indian man, 32 years old, 178 cm, lean slim build, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin gunmetal round wire-frame glasses with perfectly clear, untinted lenses (never sunglasses, never coloured lenses), mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black leather sneakers with white soles, black smartwatch on left wrist, ONE yellow-and-black mechanical pencil (there is only this one pencil: if he holds it, it is not also behind his ear; otherwise it is tucked behind his left ear), small grey hardcover notebook with a blank cover. Intelligent, alert, slightly tense face.

PHYSICS: Fast typing shows correct finger motion on real keys. Dots go dark at discrete moments, one at a time. Light on his face dims as the dots go out.

AUDIO (generate natively, no music): Rapid keyboard clatter, a faint rising electronic whine, a small soft tick as each white dot goes out, his held breath. No voices.

DIALOGUE: none.

STYLE: Photorealistic live-action cinema, shot on ARRI Alexa 35 with 35mm and 50mm anamorphic-style prime lenses, 16:9, 24 fps, 180-degree shutter motion blur, subtle natural film grain, teal-shadow and warm-amber-highlight grade, physically accurate lighting, real skin texture with pores and fine detail. Strict real-world physics: correct gravity, momentum, inertia, fluid and rain behaviour, consistent reflections and shadows, objects keep their shape and size. No morphing, no warped faces or hands, no extra fingers, no text, subtitles, logos or watermarks anywhere in frame, no readable signs or lettering (signs and billboards are blank glowing panels), no slow-motion unless stated, no background music. Cuts between shots are instant hard cuts: never dissolves, cross-fades or double exposures. Rain falls only outdoors; interiors are completely dry.

DURATION: 6 seconds, 16:9. If the tool only offers 15 seconds, finish everything described within the first 6 seconds, then hold the final frame still.
```

**Short version (if Grok limits length):**

```
ONE continuous shot, no cuts. Same lab and wall display. Kabir has stood up and is typing fast on a keyboard in front of the map. The black band on the map races toward a cluster of eleven small white dots in the middle of the network. The white dots go out one by one. No text, letters or numbers anywhere on the display. Kabir's reflection is in the glass. One pencil in his hand, none behind his ear. Camera: Medium shot from behind and to his side, 35mm, a little handheld unease. Kabir: Indian man, 32, slim, medium-brown skin, short black side-parted hair, oval face, soft jawline, thick tousled black hair, light stubble, thin gunmetal round glasses with clear untinted lenses, mid-grey bomber jacket over muted-blue T-shirt, one yellow-black pencil (in hand or behind left ear, never both). Physics: Fast typing shows correct finger motion on real keys. Dots go dark at discrete moments, one at a time. Light on his face dims as the dots go out. Sound: Rapid keyboard clatter, a faint rising electronic whine, a small soft tick as each white dot goes out, his held breath. No voices. Spoken lines in natural Hindi, in order: No dialogue.  Photorealistic live-action cinema, ARRI Alexa 35, anamorphic 35mm look, 16:9, 24 fps, natural motion blur, teal-and-amber grade, real skin texture, strict real-world physics, no morphing, no on-screen text or readable signs, instant hard cuts only (no dissolves or double exposures), no music. 15 seconds.
```

### 03-B: ARC takes shape (use about 6 s)

**Start frame:** Last frame of 03-A, or LOC-2.  
**Use:** Use about 6 s.

```
SHOT: ONE continuous shot, no cuts. Inside the same minimalist glass-walled AI safety lab on a high floor: floor-to-ceiling windows along one wall, a long desk with three monitors, a small grey notebook on the desk, the amber ribbons of light move across the glass wall and gather into a soft pulsing sphere of amber light on the glass, about the size of a basketball, with the dark city beyond. Kabir steps back from the desk and faces it. He speaks one quiet word to it. The sphere brightens once in answer. No text anywhere.

CAMERA: Medium shot, 35mm, slow orbit around Kabir ending on a profile view with the sphere beyond.

CAST (keep every detail identical to the reference images):
- KABIR RAO: Indian man, 32 years old, 178 cm, lean slim build, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin gunmetal round wire-frame glasses with perfectly clear, untinted lenses (never sunglasses, never coloured lenses), mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black leather sneakers with white soles, black smartwatch on left wrist, ONE yellow-and-black mechanical pencil (there is only this one pencil: if he holds it, it is not also behind his ear; otherwise it is tucked behind his left ear), small grey hardcover notebook with a blank cover. Intelligent, alert, slightly tense face.

ARC RULE: ARC (the city's AI): never a face or a body. It exists only as warm amber light (about 2200 K) shown as glowing ribbons, a soft pulsing sphere of light on glass panels and screens, and amber light strips. Soft and alive, never harsh. No readable text or numbers on any screen.

PHYSICS: The sphere is light projected on glass, so it has no depth and no shadow. Its amber light falls on Kabir's face and the desk with correct falloff.

AUDIO (generate natively, no music): Low hum, a warm glass-harmonica tone on the sphere's pulse, one footstep. His whispered word is clearly audible.

VOICES (each speaker must keep a clearly different pitch and timbre; natural breaths, small pauses, real emotional nuance, lip-synced):
- KABIR: a young man's voice, warm medium-low baritone, 32 years old, educated urban Indian, crisp articulation, quick measured pace, dry understated humour, tightens and rises slightly under stress.

DIALOGUE (spoken in Hindi, in this order, spread naturally across the 7 seconds, no overlap unless stated):
1. Kabir says in natural conversational Hindi (not dubbed-sounding): "ARC…?" (pronounced: ARC…?)

STYLE: Photorealistic live-action cinema, shot on ARRI Alexa 35 with 35mm and 50mm anamorphic-style prime lenses, 16:9, 24 fps, 180-degree shutter motion blur, subtle natural film grain, teal-shadow and warm-amber-highlight grade, physically accurate lighting, real skin texture with pores and fine detail. Strict real-world physics: correct gravity, momentum, inertia, fluid and rain behaviour, consistent reflections and shadows, objects keep their shape and size. No morphing, no warped faces or hands, no extra fingers, no text, subtitles, logos or watermarks anywhere in frame, no readable signs or lettering (signs and billboards are blank glowing panels), no slow-motion unless stated, no background music. Cuts between shots are instant hard cuts: never dissolves, cross-fades or double exposures. Rain falls only outdoors; interiors are completely dry.

DURATION: 7 seconds, 16:9. If the tool only offers 15 seconds, finish everything described within the first 7 seconds, then hold the final frame still.
```

**Short version (if Grok limits length):**

```
ONE continuous shot, no cuts. Inside the same minimalist glass-walled AI safety lab on a high floor: floor-to-ceiling windows along one wall, a long desk with three monitors, a small grey notebook on the desk, the amber ribbons of light move across the glass wall and gather into a soft pulsing sphere of amber light on the glass, about the size of a basketball, with the dark city beyond. Kabir steps back from the desk and faces it. He speaks one quiet word to it. The sphere brightens once in answer. No text anywhere. Camera: Medium shot, 35mm, slow orbit around Kabir ending on a profile view with the sphere beyond. Kabir: Indian man, 32, slim, medium-brown skin, short black side-parted hair, oval face, soft jawline, thick tousled black hair, light stubble, thin gunmetal round glasses with clear untinted lenses, mid-grey bomber jacket over muted-blue T-shirt, one yellow-black pencil (in hand or behind left ear, never both). ARC: only warm amber light on glass and screens, never a face or body, no readable text. Physics: The sphere is light projected on glass, so it has no depth and no shadow. Its amber light falls on Kabir's face and the desk with correct falloff. Sound: Low hum, a warm glass-harmonica tone on the sphere's pulse, one footstep. His whispered word is clearly audible. Spoken lines in natural Hindi, in order: Kabir (Hindi): "ARC…?" Kabir: young man, warm medium-low baritone, quick, dry humour. Photorealistic live-action cinema, ARRI Alexa 35, anamorphic 35mm look, 16:9, 24 fps, natural motion blur, teal-and-amber grade, real skin texture, strict real-world physics, no morphing, no on-screen text or readable signs, instant hard cuts only (no dissolves or double exposures), no music. 15 seconds.
```

**Dialogue:**

- Kabir: ARC…? / ARC…? / ARC…?

