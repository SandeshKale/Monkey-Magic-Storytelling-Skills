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
