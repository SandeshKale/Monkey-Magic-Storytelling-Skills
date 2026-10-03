# Clip 1 (0:00 to 0:15): final Grok prompt

One generation, three shots, hard cuts. This replaces the earlier clip 1 prompts. (The shot-by-shot prompts in `cold-open-v2.md` stay as the fallback if Grok will not cut cleanly.)

## What the viewer must understand in these 15 seconds
1. **Where and what:** a futuristic city at night, and its lights are being switched off.
2. **Why it matters:** people are on life support in that city, and the power failure reaches a hospital bed.
3. **Who it is about:** a man in a lab who realises this is his fault, and something calls him by name.

Shot 1 is the event, shot 2 is the consequence, shot 3 is the person. Each shot causes the next.

## Settings and attachments
- Mode: video. Length: 15 seconds. Aspect: 16:9.
- Attach `LOC-1` (your aerial city still) as the start image if Grok takes only one image.
- If Grok takes more than one reference, also attach `REF-K` (the Kabir sheet) so shot 3 matches his face.
- Add the text overlays (`VELLORA · 2091 · 03:07 A.M.`, the title card) in the edit. Do not ask Grok for text.

## The prompt (paste everything in the box)

```
A 15-second cinematic cold open made of THREE separate shots joined by instant hard cuts. Between shots the picture changes completely in a single frame: no dissolves, no cross-fades, no overlaps, no ghost or double images, no morphing between scenes. Photorealistic live-action cinema, 16:9, 24 fps, natural motion blur, teal-and-amber grade, real skin texture, strict real-world physics. No text, letters, numbers, logos or subtitles anywhere in the picture. No background music.

SHOT 1 (0.0 to 5.0 s): THE CITY GOES DARK.
Slow aerial drone push-in over a vast futuristic coastal megacity at 3 a.m. in heavy monsoon rain, with clearly visible falling rain streaks. A long suspension bridge crosses dark water. In the first second every tower, street and the bridge are brightly lit with warm amber light. Starting in the foreground and sweeping to the far horizon over about three seconds, the lights go out row by row, until the city is almost completely black. Only a few dim red aviation lights on the tower tops and the dark sea remain.
Sound: deep sub-bass rumble, dull thunks of transformers shutting down that arrive a moment after each row goes dark (light travels faster than sound), steady rain.

HARD CUT TO:

SHOT 2 (5.0 to 9.5 s): A HOSPITAL FEELS IT.
Interior of a hospital ward at night, locked-off medium shot of a patient monitor on a stand beside a bed, with a ventilator hose. The patient is only a blurred shape under a white sheet; no face is visible. At the start the ward is lit cool white. About 0.8 seconds into this shot the main lights die and the room is lit only by dim red emergency light. The green heart trace on the monitor wavers and thins, the ventilator hose pauses for a beat, then both carry on steadily on battery backup. The monitor shows only a green trace and plain shapes, no readable text.
Sound: ward hum cuts out, monitor beeps stutter and then steady, a faint distant alarm. No voices.

HARD CUT TO:

SHOT 3 (9.5 to 15.0 s): A MAN WHO KNOWS WHY.
Medium close-up of Kabir Rao inside a glass-walled AI lab at night. Behind him, out of focus, are rain-streaked floor-to-ceiling windows and a dark city with a few red lights. He is an Indian man, 32 years old, slim, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top, light stubble, thin gunmetal round wire-frame glasses with perfectly clear untinted lenses, a mid-grey bomber jacket over a muted-blue T-shirt. In his right hand at chest height he holds ONE yellow-and-black mechanical pencil (there is no other pencil; none behind his ear). He stares at something off-screen, brow furrowed, breathing quickly, the look of a man who realises the disaster is his fault. He clicks the pencil three times with his thumb with a short beat between clicks. Then monitors around him change from cool blue to warm amber over about 1.5 seconds and the amber glow spreads across his face and reflects in his clear glasses. A calm woman's voice speaks from the room itself and he goes completely still, listening. The shot holds on his face until the end. The room is dry; rain falls only outside the glass.
Sound: rain muted by the glass, three crisp clearly audible pencil clicks, a soft rising glass-harmonica shimmer as the amber appears, then the voice.

VOICE (the only voice in the whole clip): a calm, soft, warm, young woman's voice, medium-high pitch, clearly higher than any man's voice (definitely not a deep or male voice), with a faint smile in the tone, speaking natural conversational Hindi at about 12.5 seconds. Nobody on screen moves their lips. Kabir does not speak. Line: "कबीर… मुझे तुम्हारे हाथ चाहिए।" (pronounced: Kabir… mujhe tumhare haath chahiye.) The line must be clearly audible above the ambient sound.
```

## Short version (if Grok limits length)

```
15-second cold open, THREE shots joined by instant hard cuts (no dissolves, cross-fades or ghosting). Photorealistic live action, 16:9, 24 fps, teal-and-amber grade, real-world physics, no text anywhere, no music. SHOT 1 (0 to 5 s): aerial push-in over a futuristic coastal megacity at night in heavy rain; at first everything is lit amber, then the lights go out row by row from foreground to horizon until only dim red aviation lights remain; rumble and delayed transformer thunks. HARD CUT. SHOT 2 (5 to 9.5 s): locked-off hospital ward, monitor and ventilator hose beside a bed, patient a blurred shape under a sheet, no face; cool white light, then at about 0.8 s the lights die to dim red emergency light, the green trace wavers, the hose pauses and resumes on backup; beeps stutter. HARD CUT. SHOT 3 (9.5 to 15 s): medium close-up of Kabir, Indian man, 32, slim, oval face, tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, mid-grey bomber over blue T-shirt, in a dark glass lab with a dark rainy city behind him; he holds one yellow-and-black pencil in his right hand (none behind his ear), stares off-screen worried, clicks it three times, then the monitors turn warm amber and light his face and glasses; a calm young woman's voice, clearly higher than a man's, says in Hindi from the room (no lips move): "कबीर… मुझे तुम्हारे हाथ चाहिए।" Kabir does not speak. Hold on his face.
```

## What a good result looks like (check in this order)
| Time | You should see and hear |
|---|---|
| 0:00 to 0:05 | Lit city, then a visible sweep of darkness, red lights left on the towers. Rumble, then dull thunks. |
| 0:05 to 0:09.5 | An instant cut to the ward. Lights die to red at about 0:06. The trace wavers and recovers. Beeps stutter. |
| 0:09.5 to 0:15 | An instant cut to Kabir. Worried face. Three pencil clicks. The room turns amber on his face and glasses. A woman's voice says the Hindi line at about 0:12 to 0:13. |

Fail checks: any dissolve or ghost image; the city staying lit; a second pencil; tinted lenses; a male voice; a second voice; any readable text; rain inside the room.

## If it still goes wrong
| Problem | Fix |
|---|---|
| Dissolves or ghost images between shots | Add one sentence at the top: "This is three separate video clips edited together; each shot starts on a different set with a different camera." Still failing: generate the three shots separately (prompts in `cold-open-v2.md` and `clip-01-reshoots.md`) and let me cut them. |
| The city does not go dark | Lead shot 1 with "The key event: the city's lights go out." Attach `LOC-1` as the start image and say the shot ends on a mostly black city. |
| Kabir's face does not match the sheet | Attach `REF-K` and generate shot 3 alone from the face crop. I can cut it in. |
| The voice is male or the Hindi is garbled | Keep the picture. Send it to me; I will mark the audio for a separate voice track. |
| No pencil clicks | I will add them in the edit. |

## Effect on the next clips
The hospital shot now lives in clip 1, so clip 3 (`03-A`) does not need its hospital cutaway. Go straight from the dots going out to the ARC sphere.
