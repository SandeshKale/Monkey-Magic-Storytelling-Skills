# AWAAZ Ep1 v4: sign-off audit

Source: v4 cut from the Drive link, 1080x1920, 24 fps, 60.0 s, loudness measured -16.0 LUFS (you reported -15.9). Method: 240 frames at 4 fps, 8-10 fps face and hand crops on every edited spot, audio windows and 100 ms levels around each edit, and a frame-by-frame PSNR comparison against v3 to prove what changed.

I cannot hear audio, so sync is judged from waveform against mouth frames. The shout and stage voice still need your ear.

## Verdict: SHIP
All three must-fixes from `14-audit-ep01-v3.md` are fixed, both soft fixes landed, and nothing else moved. No new defect was introduced. Remaining items are soft and do not need a retake or an edit.

## What changed (verified)
PSNR v3 vs v4: 0-12 s 56.5 dB (only re-encode noise), 29.1-49.7 s bit-identical, 49.7-52.8 s 50 dB. So S1, S4, S5 and S6 are untouched. Changed: 12-19 (S2), 19-29 (S3) and 52.83-59.5 (INS-B).

## Must-fix check
| # | v3 must-fix | v4 result |
|---|---|---|
| 1 | S7 whisper leads the audio by 1.1 s | **FIXED.** Whisper audio now 51.7-52.7 (level jumps at 51.7). Mouth starts at about 51.55, wide open 52.05-52.7, closed after. Lead about 0.15 s, within tolerance. The cut to INS-B at 52.83 lands right after the whisper ends (52.72); the ringtone begins at 52.8. No silent mouthing remains. |
| 2 | S3 silent mouthing 23.4-24.0 and the smile at 21.75-23.2 | **FIXED.** Two punch-ins (20.375-22.0 on the hands and phone; 22.0-24.0 on her right hand with the bangle, flour on the knuckles, phone at the lower edge) cover both. She returns at 24.0 with her lips closed and frowning; the mouth opens at about 24.2, L7 audio starts at 24.05 (late by 0.15 s, fine). Audio is continuous through both cuts (levels -13.8/-18.2 at 20.375). |
| 3 | S2 phone screen lit blue and readable | **FIXED.** The phone now shows dark glass with a faint warm glow for 13.25-19.0. The finger touch at about 16.4-16.7 sits on top with no halo or matte edge visible at 10 fps. The blue on his face and glasses stays, and is motivated by the laptop screen that faces him. |

## Soft fixes
- S2 call banner now exits at about 16.7, with the finger touch (was 16.25). OK.
- INS-B push-in: the hands and phone grow over 52.83-59.5. It no longer reads as a still frame. OK.

## Per shot
| Shot | Time | Verdict | Notes |
|---|---|---|---|
| S1 kitchen | 0-12.0 | PASS | Unchanged. Soft: mouth wide at 11.0-11.5. |
| S2 Kabir | 12.0-19.0 | PASS | Screen fixed, banner timing fixed, one finger touch then rest, pencil in the right hand. Soft: pout at 13.5-14.5. |
| S3 table | 19.0-29.0 | PASS | Fixed. Soft: 3.6 s of cutaway (20.375-24.0) is hand and phone only, so we do not see her face react to the demand; the second crop is nearly still. L8 mouth leads the audio by 0.15-0.4 s (soft, unchanged). |
| S4 Riya | 29.0-38.3 | PASS, soft | Unchanged. Same soft notes as v3: lips slightly parted under the off-screen Kabir (32.7-34.1), a faint smile at 34.7-35.3, laptop display toward the camera, L10 lead about 0.35 s. |
| S5 + INS-A | 38.3-46.1 | PASS | Unchanged. Spike lands, stage sync within 0.15 s. Soft: S5 watch on the right wrist. |
| S6 run | 46.1-49.7 | PASS | Unchanged. |
| S7 button | 49.7-52.83 | PASS | L19 lips closed 49.75-51.4; whisper in sync. Soft: the whisper is delivered with a wide mouth, and a trembling closed-lip curve at 50.8-51.4 reads close to a smile through tears. |
| INS-B | 52.83-59.5 | PASS | Banner 53.0-53.25, UPI card 53.25, caption 54.5, 'EP 2 →' 54.9, black 59.5-60.0. Hand motionless but the push-in keeps it alive. |

## Lip-window table (final)
| Line | Audio | Mouth | Result |
|---|---|---|---|
| L1 phone | 1.2-3.1 | closed | OK |
| L2 | 4.7-5.2 | 4.5-5.5 | OK |
| L3 phone | 6.5-8.8 | closed | OK |
| L4 | 10.4-12.0 | 10.25-12.0 | OK |
| L5 | 16.0-17.0 | 16.1-16.9 | OK |
| L6 phone | 20.2-22.8 | covered by the punch-ins | OK |
| L7 | 24.05-25.2 | 24.2-25.25 | OK |
| L8 | 27.4-29.2 | 27.0-29.0 | SOFT |
| L10 | 29.4-32.4 | 29.0-32.4 | SOFT |
| L11 off-screen | 32.7-34.1 | Riya parted and still | SOFT |
| L15 | 36.1-37.8 | 36.0-37.75 | OK |
| L16 stage | 40.1-42.4 | 40.0-42.4 | OK |
| L18 shout | 46.1-47.5 | face hidden | n/a |
| L19 clone | 48.9-50.9 | closed | OK |
| L20 whisper | 51.7-52.7 | 51.55-52.7 | OK |
11 OK, 3 SOFT, 0 FAIL, 1 n/a.

## One thing only you can do
Ear-check the shout (46.1-47.5, about 205 Hz: a shout lifts the pitch, but make sure it is a shout and not a squeak) and the stage line (about 119 Hz vs about 108 Hz for Kabir's real lines). Everything else I could measure is in range: clone 136-140 Hz, Kabir's real lines 107-108 Hz.

## Optional polish (not blocking)
- Flip S5A and S5B (38.3-39.8 and 43.4-46.1) horizontally to put the watch on the left wrist; check the hair parting still matches S2 and INS-A after the flip, and revert if not.
- Insert a 0.4 s face reaction between the two S3 punch-ins if you want to see her face react to the demand (needs 0.4 s from another shot, so only if the timing allows; skip otherwise).
- Next episode: add "no smile, jaw set, lips pressed" to every sad beat, and "mouth closed until the line" twice in every crying prompt.
