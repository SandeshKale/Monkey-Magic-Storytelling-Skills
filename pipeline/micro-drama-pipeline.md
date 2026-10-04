---
name: Micro Drama Pipeline
description: >-
  Use when producing an AI micro drama episode (vertical short video) with a
  script-writer and reviewer (Claude Code), a video generator (Grok Imagine),
  and an orchestrator assembling the final cut with ffmpeg.
---
# Micro drama pipeline (orchestrator + Grok Imagine + Claude Code)

Three roles. The orchestrator (this bot) runs the loop, drives the browser for Grok and Claude, does all quality checks and post-production. Claude Code writes scripts and prompts and approves output. Grok Imagine generates keyframes, clips and voice takes. Nobody publishes or buys anything.

## 0. Inputs to confirm once
- Storytelling skill repo plus the branch Claude writes to. Pull it before every batch; the clip prompts file there is the source of truth.
- The Claude Code session URL to resume.
- Which Grok account. Use the PAID one: free plans cap clips and hit paywalls. Never upgrade or buy.
- Episode format: aspect ratio (9:16), number of clips, seconds per clip, language.

## 1. Standing quality rules (in every prompt and every review)
1. **Real object handling and physics.** Hands really grip objects, five fingers, natural joints. Screens face the person using them (the camera sees the back of the phone or laptop, except in a deliberate first-person POV insert). The phone is held at the ear on calls with the mic near the mouth. Gravity, weight, cloth, hair and liquids behave naturally, and lighting stays consistent.
2. **Subtle, naturalistic performance.** Feeling shows in eyes, brow, breath and hands. No wide-open mouths, bulging eyes, sobbing, flailing, head-slapping or theatrical gestures. Tears are at most glistening eyes or a single tear.
3. **Photoreal cinema, not AI look.** Name the shot type, camera move (one slow push-in with slight handheld sway), lens and lighting. Ask for natural skin with pores and real fabric. Avoid plastic skin, heavy HDR, oversharpening and fake glow.
4. **No text in generations.** Grok garbles text. Add every caption, banner, UI card and title in post.
5. **Continuity locks.** Repeat the exact character description (face, hair, marks, clothes, glasses position) in every prompt. Glasses switching between nose and head is a common drift, so state where they are.

Keep these in a reusable REALISM-LOCK text and append it to every Grok prompt unless the prompt already contains it.

## 1b. Hard-won rules from the stringent Episode 1 audit (non-negotiable)
1. **Mouth discipline.** Grok animates mouths for the whole clip. Every ANIMATE prompt must say "mouth closed and still except while speaking the line". Put the line in the middle (about 1.5–3.0 s) and trim the clip tight around it. Never let a mouth move during silence or during someone else's (phone) voice.
2. **One speaker, one visible mouth, one line per clip.** Never cover the mouth during a line, and don't cut to a silent person speaking. A cutaway with someone talking needs real audio for it.
3. **Face lock.** Generate every keyframe for a character from the SAME character-sheet frame and angle family. Use the identical hair, glasses, stubble and jaw words in every prompt, and reject any take where they differ. Keep faces that must match in medium close-up, never in wide corridor shots. Before approving, check identity across ALL of that character's clips side by side, not just within one clip.
4. **Wardrobe negatives.** State the jewellery explicitly and forbid the rest (e.g. "no necklace, no jewellery except the stated bangles and nose stud").
5. **Handling budget.** One object per hand per clip. No hand-offs, no ear-to-hand phone transitions, no hands clasped over objects. Cut away between phone states instead of animating them. Check for extra limbs and hands from nowhere.
6. **Phones.** The screen faces the actor and all screen content is overlaid in post. Use a POV screen insert at most once per episode, and make the thumb belong to the hand holding the phone.
7. **Motion.** When the script says run, generate a rear or side tracking shot, not a frontal walk, and sell it with hard sound effects in post (chair, pencil drop).
8. **Restraint vocabulary.** Never write "wide open mouth" or "eyes wide". Use "slight tremble of the lip" and "eyes glisten".
9. **Edit.** Don't cut every shot on a rigid grid. Overlap audio across cuts by 0.2–0.3 s (J/L cuts), and lay continuous room-tone and ringtone beds.
10. **Review at 4 fps, with audio.** Contact sheets at 1 fps miss sync errors. For every line, find its audio window (silencedetect or speech recognition), then check that the lip-start and lip-stop frames fall inside it before accepting a take. Use a frame-audit script (4 frames/s, timestamped) and do this yourself before Claude sees anything. A picture-only approval is never final.

## 2. Claude Code (writer and approver)
- Claude writes: the series bible, per-clip KEYFRAME and ANIMATE prompts with timed beats (e.g. 0.0–1.2 s), dialogue with timings, voice-session prompts, a post note per clip, and a review checklist that includes the standing rules. It commits to the repo branch.
- Usage is limited. Send work in batches with one compact message asking for a per-item APPROVE or REJECT, in/out points, and exact retake notes.
- Claude Code's upload doesn't take video, and multi-select uploads only one file. Send ONE image per attachment: a labeled contact strip (1 frame/s, clip ID burned in) or a full-episode sheet. Say plainly that audio can't be judged from images.
- Claude may judge an older strip when several are attached. Tell it which take is new, and cross-check its notes against the frames before acting on a reject.
- Ask it to re-check already-approved clips whenever a new rule is added.

## 3. Grok Imagine (generator)
- Method per clip: (1) image mode at 9:16 with reference images attached plus the KEYFRAME prompt, keeping the face that matches the reference; (2) video mode with that keyframe as start image, 6 s, 9:16, plus the ANIMATE prompt.
- Make character contact sheets and approved hero frames first, and attach them for every keyframe. Attach ONE reference when two-file uploads get stuck (Submit stays disabled), and reload the page if stuck.
- Output is about 6 s at roughly 400–450×700 even when 9:16 is chosen; upscale in post. Keyframes sometimes come out square, so check.
- Phone or offscreen voices: generate separate voice-session clips and use their audio only. Grok voices come out high-pitched (~250–320 Hz), so pitch down in post rather than retaking endlessly.
- Download the MP4 or image itself, never the "segments" zip. Downloads land in ~/Downloads with UUID names. Record every path immediately, because workers sometimes report another clip's path; verify with md5 and timestamps.
- Grok tends to overact crying scenes even when told not to. Re-prompt with: "face still and quiet, worry only in eyes and brow, lips closed except when speaking, eyes glisten only." Retake at most twice, then pick the most restrained take.
- If a generation stalls more than ~3 min, reload and retry once, then move on.
- The browser automation can't open file:// URLs; open prompt text files through native file-open controls to copy them.

## 4. Orchestrator loop
1. Pull the repo and extract each clip's KEYFRAME and ANIMATE blocks into text files (e.g. C05-KEY.txt, C05-ANIM.txt).
2. Dispatch one browser worker per batch with the exact rule checks to apply before downloading, a retake limit, and a demand for exact download paths.
3. When a batch returns, copy files to the project folder with clear names (keep old takes in old/), then build contact strips with ffmpeg and inspect them yourself against the standing rules. Measure voice pitch and speech gaps (silencedetect) for audio.
4. Retake obvious rule breaks before spending Claude's usage. Then send Claude one review batch.
5. Loop until every clip is approved, with in/out points.

## 5. Assembly (ffmpeg, scripted)
- Keep a re-runnable assemble.sh with per-clip overrides (file, in, out, phone-line times) and a pitch setting, so a single retake swaps in without rebuilding everything.
- Trim each clip to its slot. Time-stretch short clips with the audio stretched at the same pitch.
- Phone voice: cut lines from the voice sessions, pitch down about 7 semitones (more sounds unnatural), band-pass 300–3400 Hz with light compression, place them at scripted times without overlapping on-screen lines, and duck clip audio about 14 dB underneath.
- Add low room ambience generated with lavfi noise per location, sound effects (beeps, ringtones), and all text overlays in a font that covers the script's language (e.g. Noto Sans Devanagari).
- Scale or crop to 1080×1920, 24 fps, H.264 High, yuv420p, AAC, +faststart, and normalize to about -16 LUFS. Run speech recognition on the result to confirm lines are audible, then build a sheet with a frame every 2 s and inspect it.
- Final freeze: keep the story-critical UI (call banner, payment card) on screen under the cliffhanger caption.

## 6. Delivery
- Upload ONLY the final cut (no intermediates) to a dedicated Google Drive folder per series or episode, as video/mp4 or .m4v, and set its sharing to anyone with the link can view. Give that link to Claude for a stringent audit with audio, which is the real final gate, then to the user.
- Send Claude the final sheet for approval and fix its must-fix items.
- Deliver to the user: chat attachments over about 25 MB may fail on mobile, so also upload to Google Drive. Upload with a .m4v (or proper video/mp4) type. A file stored as application/mp4 shows as an "Unsupported file type" in the Drive iPhone app.
- Tell the user honestly what Claude couldn't check (audio) and offer quick fixes, such as voice pitch.

## Efficiency rules (2026-10-04, Sandesh: less time, less limit, same quality)
- Gate the keyframe before any video: face match to canon, banned items (e.g. no necklace), grips, screen direction, 9:16. Video generation is the expensive step.
- References: ONE 9:16 face-only canon per character (refs/CANON-<X>-916.jpg), attached alone; the location goes in text. Never use side-by-side composites; Grok copies the layout and aspect. Check canons for banned items before use.
- Generate each 15 s shot once and use only its KEEP window; trim around flaws instead of regenerating. Retake only what an edit can't fix.
- Download the MP4 immediately after each render and verify the path, time and resolution before starting the next. Never use segments zips.
- Run lip-window (silencedetect + 4 fps frames), pitch, framing and resolution checks locally with scripts. Spend Claude's limit only on one stringent audit of the final cut from the Drive link, with all must-fixes returned in one message.
- Batch Grok work with one computerUse worker; do local checks and assembly prep in parallel.

## Identity and phone locks (2026-10-05, Sandesh: fix once and for all)
- Character look: the contact sheet (refs/CS-<NAME>.jpg) is the single source of truth for every shot. Grok copies a reference's layout, so attach its 9:16 face crop (CANON-<X>-916.jpg) and never the sheet itself. Gate EVERY keyframe by placing it side by side with the contact sheet (a local montage) and checking face shape, age, hair parting, stubble, glasses, wardrobe and jewellery. Reject on any mismatch before animating. After each batch, check all of a character's keyframes together against the sheet. Never add identity words that the sheet doesn't show.
- Phone: append the PHONE LOCK block below verbatim to every KEY and ANIM prompt with a phone in it (not microphones). The gate rejects any take that breaks it; there are no edit-fix exceptions for phone handling.

> PHONE LOCK (any shot with a phone): On a call, the phone is held in ONE hand, pressed flat against the ear, screen side touching the cheek, the bottom of the phone pointing toward the corner of the mouth; four fingers wrap the back, the thumb on the near edge; the elbow is bent and close to the body; the phone never floats, never leaves the ear, never changes hands, and never faces the camera. Off a call, the phone lies flat on the table or is held at chest height with the screen facing the person's eyes, never the camera; any touch is one thumb of the hand holding it (or one finger of the free hand on a phone lying flat), then the hand returns to rest. The phone has real weight and casts a shadow; a hand resting on it doesn't slide. The listener's lips stay pressed together and still while the other voice speaks. One phone in frame, rigid, one consistent model, dark screen with no readable content.
