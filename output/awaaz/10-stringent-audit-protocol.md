# Stringent audit protocol (use for every future video)

Why this exists: my earlier reviews looked at 1 to 2 frames per second and judged sync and handling by eye. At 4 frames per second a raw Grok clip (C06) shows Riya's lips moving from about 0.25 s while her voice does not start until about 1.1 s: a lead of roughly 0.8 s that the coarse sheets hid. Audio/lip sync, face drift, object handling and phone screens all need frame-level evidence, not impressions.

## Tooling
`python3 tools/frame_audit.py VIDEO OUTDIR --fps 4 --tile 6x4` writes timestamped contact sheets (every 0.25 s, stamped) and `report.txt` (specs, hard cuts, speech-like windows to 0.1 s, share of digital silence, loudness). Sheets are read in order; every finding must cite a timestamp.

## Pass 1: audio-to-lip sync (per speaking line)
1. From `report.txt`, take each speech window (start/end).
2. On the 0.25 s sheets, find the first and last frame where that character's mouth moves.
3. **Lead/lag = (first mouth frame) minus (window start).** Pass within plus or minus 0.15 s. Mark 0.15 to 0.4 s as soft, over 0.4 s as FAIL.
4. Check no mouth movement occurs outside any window (silent talking) and no voice occurs with a closed mouth (dubbed-sounding).
5. Voice-over lines: every visible mouth must be closed.
6. Phone-voice lines placed in post: confirm they sit inside the listener's reaction and never overlap the listener's own line.

## Pass 2: identity consistency (per character, every 0.25 s)
Compare each frame with the canon contact sheet and with the previous clip's last frame:
- Face: jaw width, forehead height, nose, eye spacing, age.
- Hair: parting side, volume, length, grey streaks, bun position.
- Glasses: shape, frame colour, on nose vs on head (Sushma: head in C01 to C02, nose from C04).
- Wardrobe: colours, collar, sleeves, jacket open or closed, lanyard card position, bindi, bangles, necklace.
- Props held: pencil count (one), mug, laptop.
FAIL if any item changes without a story reason, within a clip or across a cut.

## Pass 3: object interaction (every frame where a hand touches something)
- Hand anatomy: five fingers, natural joints, fingers wrapped around the object (phone: four fingers behind, thumb at the side).
- Contact and weight: no floating, no passing through, no objects appearing or vanishing.
- Phone on a call: at the ear, microphone near the mouth, screen against the face, not held out facing the camera.
- Phone being read: screen faces the reader; the camera sees the back unless it is a deliberate POV insert.
- Laptop: open, screen faces its user.
- Mug, pencil, keyboard: consistent position frame to frame.

## Pass 4: screens
- Orientation: which way does each screen face (user or camera)?
- Content: blank or intended; no garbled text, fake brands, or UI that changes between frames.
- Lighting: a lit screen lights the face from the correct side.
- Overlays added in post: legible, positioned over the right screen, and visible for the whole beat they explain.

## Pass 5: motion and performance
- Physics: gravity, cloth, hair, steam (steam that is constant while the mug moves is a tell), liquid.
- Restraint: no wide-open mouths, bulging eyes, flailing, slapping.
- Continuity of action across cuts: a hand that holds a phone before a cut still holds it after.

## Pass 6: assembly
Cut points land on action; audio crossfades; no gaps; loudness about -16 LUFS; freeze frames keep the information the question needs.

## Report format
For each clip: a table of findings (timestamp, category, severity: FAIL / SOFT / OK, one-line evidence). A clip is APPROVED only with zero FAIL. Soft items are listed with the fix.

## Mitigations for the next videos (from what keeps going wrong)
1. **Shorter shots.** Plan 4 s of action per generation and use the best 3 to 4 s; most defects grow after about 4 s.
2. **One person speaking per clip,** and put the other person's line in a separate clip (reverse shot). Two lip-synced voices in one generation produce most sync and identity errors.
3. **Anchor every face** with a keyframe from the canon sheet and, for each cut, use the previous clip's last frame as the start frame.
4. **Avoid complex handling** (picking up phones, passing objects, laptop turns). Stage the object already in place and show only the reaction; add the object action as a cutaway.
5. **Never show a phone screen to the camera** except in a deliberate POV insert; put screen content in post.
6. **Measure and shift.** After measuring each clip's lead or lag, shift that clip's audio by the measured amount in the edit instead of retaking when the lead is under 0.5 s.
7. **Review at 4 fps** before approving anything.
