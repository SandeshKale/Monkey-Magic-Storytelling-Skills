# Per-clip review checklist (use for every clip)

1. **Hook / beat:** the planned action happens at the planned times (check against the clip's WHAT MOVES).
2. **Audio:** only the intended voices; lines start within about 0.3 s of the plan; no stray speech or sobbing inside a phone-voice window; ambience missing is fixed in post.
3. **Lip-sync:** mouth moves only when that person speaks.
4. **Face and look** match the canon contact sheet (CS-SUSHMA, CS-KABIR, CS-RIYA).
5. **Standing rule 1, objects:** real hand grips, correct anatomy (five fingers, natural joints), screens facing the user, a phone at the ear on calls, a laptop open and facing its user, strict physics.
6. **Standing rule 2, performance:** subtle, restrained, naturalistic. Fail on wide-open mouths, bulging eyes, flailing, slapping, theatrical gestures.
7. **Continuity:** one pencil; props where the last clip left them; wardrobe unchanged.
8. **Spec:** v1 clips were 6 s at about 400 px (retired). v2 shots (`12-ep01-v2-clip-prompts.md`) are 15 s, 480p, 9:16; use only the KEEP window; upscale to 1080x1920 in the edit.
9. **Lip-window check at 4 fps (mandatory for every take, from the audit in `11-audit-ep01-final.md`):**
   1. List every spoken line of the shot with its planned window (clip time). Phone-voice lines count too; they have a window but no speaking mouth.
   2. Render the take at 4 fps with timestamps: `python3 tools/frame_audit.py TAKE.mp4 OUT --fps 4 --tile 8x4`, and read the speech-activity windows in `report.txt` (the take's own audio).
   3. For each window, step through the frames from 1.0 s before to 1.0 s after and mark each frame mouth OPEN-MOVING or CLOSED-STILL.
   4. **Own line:** the mouth starts moving within 0.15 s of the audio window start and stops within 0.15 s of its end. 0.15 to 0.4 s off is SOFT. More than 0.4 s off is FAIL (retake).
   5. **Outside every own-line window:** the mouth must be CLOSED-STILL in every frame. Any mouthing, muttering or lips parted for a frame run longer than 0.25 s is FAIL.
   6. **Phone-voice window (post-placed):** the listener's mouth must be CLOSED-STILL for the whole window plus 0.2 s either side. Any movement is FAIL.
   7. **Covered mouth:** no line may be spoken while a hand, phone or object covers the mouth. FAIL.
   8. Check the first and last 0.5 s of the KEEP window too: a mouth that is already moving at the cut point will look early or late once cut.
   9. Write the result as a table: line, planned window, audio window, mouth start, mouth stop, offset, FAIL/SOFT/OK.

## Continuity rule: Sushma's reading glasses
- C01, C02, C03-cutaways: **pushed up on her head.**
- C04: she pulls them **down onto her nose** at about 2.6 to 3.1 s. This is the only switch, and it is intended.
- C05, C07, C11 (and any shot of her face after C04): **on her nose.**
- C12 is a POV hands-only insert, no glasses visible.
Any clip after C04 that shows them on her head is a continuity error.
