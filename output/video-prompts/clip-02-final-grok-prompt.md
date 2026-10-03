# Clip 2 (0:15 to 0:30): the Why

One generation, three shots, hard cuts, one voice (Kabir's voice-over). Same method as clip 1.

## What the viewer must understand in these 15 seconds
Monkey Magic rule: the Why lands in the first spoken paragraph, by 0:30, and it is personal, not "content". Here the Why is guilt.
1. **Who he is:** he built the safety layer for this city's mind (an AI safety engineer).
2. **What he did:** two years ago he left one door unlocked because review was slow.
3. **What it cost:** tonight something walked through it. The black spreading across the map is the thing that is switching off the city.

Shot 1 is the man, shot 2 is the door, shot 3 is the consequence. The voice-over carries one sentence per shot.

## Settings and attachments
- Mode: video. Length: 15 seconds. Aspect: 16:9.
- **Start image:** `frames/clip-01-last-frame_for-clip-02-start.png` (the last clean frame of your clip 1 output). This keeps the room, his face and the jacket identical to clip 1.
- If Grok takes a second reference, also attach `REF-K`.
- Do not ask Grok for text. Nothing on the map should be readable.

## The prompt (paste everything in the box)

```
A 15-second cinematic scene made of THREE separate shots joined by instant hard cuts. The first frame of each shot is a completely different picture from the last frame of the shot before it. Between shots the picture changes in a single frame: no dissolves, no cross-fades, no overlaps, no ghost or double images, no morphing between scenes. Photorealistic live-action cinema, 16:9, 24 fps, natural motion blur, teal-and-amber grade, real skin texture, strict real-world physics. No text, letters, numbers, logos or subtitles anywhere in the picture. No background music.

The video starts exactly on the supplied start image and continues from it: the same man, the same glass-walled AI lab at night with rain-streaked floor-to-ceiling windows, a dark city beyond with a few red lights, glowing brain-scan monitors and a desk lamp.

THE MAN: Kabir Rao, an Indian man, 32 years old, slim, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses, a mid-grey bomber jacket over a muted-blue T-shirt. He holds ONE yellow-and-black mechanical pencil (there is only this pencil; none behind his ear).

SHOT 1 (0.0 to 4.5 s): THE MAN.
Continue from the start image. Medium close-up of Kabir, listening, brow furrowed. A moment after the clip starts, he breathes out slowly, lowers the pencil from his hand to his side, and turns his head and shoulders away from the camera toward a large display on the side wall that is out of frame. His face is lit with warm amber from the screens. His mouth stays closed: he never speaks on screen.
Sound: rain muted by the glass, low electrical hum.

HARD CUT TO:

SHOT 2 (4.5 to 11.0 s): THE DOOR.
A very large wall display in the same lab fills the frame. On it is an abstract glowing amber network map of a city, like a living circuit: branching lines and small nodes. Nothing on it is readable: no text, no letters, no numbers. On the left edge, one small shape pulses red: the outline of a small open doorway, glowing red, with a faint red light spilling onto the nearest lines. Slow push-in toward the red doorway. Kabir stands at the edge of the frame in profile, lit amber, his clear glasses reflecting the map, his hand resting on the desk beside him, his eyes fixed on the red doorway. He is still and ashamed. His mouth stays closed.
Sound: low room hum, faint rain on glass, soft electronic pulses from the map.

HARD CUT TO:

SHOT 3 (11.0 to 15.0 s): THE COST.
The same wall display, now seen over Kabir's shoulder with his face sharp in the foreground, lit amber. On the map, a thin black band slips out of the red doorway and spreads along the amber lines, putting out each node it touches, one after another, faster and faster, like ink creeping through a circuit. As the amber goes out the light on his face dims. His jaw tightens, his eyes narrow, and he swallows, the look of a man watching his own mistake do its work. The shot holds on his face to the end. His mouth stays closed. The display is a screen, so the black band is a rendered shape on it, not a physical object. The room is dry; rain falls only outside the glass.
Sound: a faint rising electronic whine, nodes clicking off softly, a held breath.

VOICE-OVER (the only voice in the whole clip): Kabir narrates in natural, conversational Hindi as an OFF-SCREEN VOICE-OVER. Nobody on screen is speaking and every mouth stays closed. The voice is a young man's warm, medium-low baritone, intimate and close to the microphone with no room echo, quiet, regretful, steady, not dramatic. Three sentences, spaced like this:
1. At about 1.0 s: "इस शहर के दिमाग़ की सुरक्षा-परत मैंने बनाई थी।" (pronounced: Is shehar ke dimaag ki suraksha-parat maine banaayi thi.)
2. At about 5.0 s: "दो साल पहले मैंने एक दरवाज़ा खुला छोड़ दिया, क्योंकि रिव्यू में बहुत वक़्त लगता था।" (pronounced: Do saal pehle maine ek darwaaza khula chhod diya, kyunki review mein bahut waqt lagta tha.)
3. At about 11.4 s: "और आज रात, कोई उसी दरवाज़े से अंदर आ गया।" (pronounced: Aur aaj raat, koi usi darwaaze se andar aa gaya.)
The voice-over must be clearly audible above the ambient sound. No other voice is heard.
```

## Short version (if Grok limits length)

```
15-second scene, THREE shots joined by instant hard cuts (no dissolves, cross-fades or ghosting); the first frame of each shot is a totally different picture from the end of the previous one. Start exactly on the supplied start image and continue from it: Kabir Rao, Indian man, 32, slim, oval face, tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, mid-grey bomber over blue T-shirt, one yellow-black pencil, in a dark glass AI lab with rainy windows, a dark city with red lights, brain-scan monitors. Photorealistic live action, 16:9, 24 fps, teal-and-amber grade, real-world physics, no text anywhere, no music. SHOT 1 (0 to 4.5 s): medium close-up, he listens, exhales, lowers the pencil, turns away toward a wall display off-frame, lit amber, mouth closed. HARD CUT. SHOT 2 (4.5 to 11 s): a large wall display with an abstract glowing amber network map of a city (no readable text), one small glowing red open-doorway shape pulses at the left edge; slow push-in; Kabir in profile at the frame edge, glasses reflecting the map, still and ashamed, mouth closed. HARD CUT. SHOT 3 (11 to 15 s): over his shoulder, his face sharp in the foreground; on the map a thin black band leaks out of the red doorway and puts out the amber nodes one by one, faster and faster; his face dims, jaw tightens, he swallows; hold on his face. ONLY voice, off-screen voice-over, young man's warm medium-low baritone, close-mic, quiet, regretful, in Hindi, nobody lip-syncs: at 1.0 s "इस शहर के दिमाग़ की सुरक्षा-परत मैंने बनाई थी।" at 5.0 s "दो साल पहले मैंने एक दरवाज़ा खुला छोड़ दिया, क्योंकि रिव्यू में बहुत वक़्त लगता था।" at 11.4 s "और आज रात, कोई उसी दरवाज़े से अंदर आ गया।"
```

## What a good result looks like
| Time | You should see and hear |
|---|---|
| 0:00 to 0:04.5 | Starts on the exact clip 1 frame. He exhales, lowers the pencil and turns toward something off-screen. First voice-over sentence at about 1 s. |
| 0:04.5 to 0:11 | An instant cut to the glowing city map with a red doorway on the left. Slow push-in. Second sentence at about 5 s. |
| 0:11 to 0:15 | An instant cut to his face with the map behind. The black band spreads and the nodes go out. Third sentence at about 11.4 s. |

Fail checks: any dissolve or ghost image; Kabir's lips moving; a second voice; a different face or jacket than clip 1; any readable text or numbers on the map; a second pencil; rain inside the room.

## If it goes wrong
| Problem | Fix |
|---|---|
| Dissolves or ghosting | I will cut them out in the edit, as I did for clip 1. |
| Kabir's lips move or a second voice appears | Retry once with the first line moved to the top: "Kabir never speaks. All speech is off-screen narration." Otherwise send it and I will replace the track. |
| The map shows text or numbers | Retry with "the map is made only of glowing lines and dots, with no symbols of any kind." |
| The face drifts from clip 1 | Attach `REF-K` as well, or retry with the start image only. |
| The Hindi is garbled or cut off | Send it. I can mark the audio for a separate voice track. |

## What happens next
Clip 3 (0:30 to 0:45) starts from the last frame of this clip. The black reaches eleven white lights and they go out, then the amber ribbons gather into ARC. The hospital cutaway is already used in clip 1.
