#!/usr/bin/env python3
"""Build the 12 x 5 s Grok prompts (plus one insert) for AWAAZ Episode 1.

Run: python3 build_clip_prompts.py  ->  writes 04-ep01-clip-prompts.md next to this file.
Every clip gets two prompts: a keyframe still (image mode) and an animate prompt (video mode).
"""
import os

STYLE_STILL = ("Photorealistic, vertical 9:16, natural skin with pores and fine detail, real fabric texture, shallow depth of field, "
               "teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, "
               "no readable writing on any screen or sign.")
STYLE_VIDEO = ("Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics "
               "(gravity, momentum, cloth, hair, liquid all behave naturally). Instant hard cuts only, no dissolves. No text, subtitles, logos "
               "or readable writing anywhere in the picture. No background music.")

FULL = {
    "S": "SUSHMA RAO: Indian woman, 58, 155 cm, medium build, wheatish skin with deep smile lines, greying black hair in a loose low bun with silver streaks, a small round red bindi on her forehead, round tortoiseshell reading glasses (pushed up on her head unless stated), small gold nose stud, small gold earrings, a sage-green cotton saree with a thin printed border over a deep teal blouse, a thin gold bangle on each wrist, no necklace, flour on her hands.",
    "K": "KABIR RAO: Indian man, 32, slim, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses, mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black smartwatch on his left wrist, ONE yellow-and-black mechanical pencil (only this one pencil exists).",
    "R": "RIYA MENON: Indian woman, 24, slim, round friendly face, large dark eyes, shoulder-length straight black hair in a low ponytail, small silver stud earrings, olive-green cotton kurta over blue jeans, company lanyard with a plain white card, no glasses.",
}
SHORT = {
    "S": "Sushma: Indian woman, 58, greying bun, small red bindi, reading glasses on her head, gold nose stud, sage-green saree over a deep teal blouse, floury hands.",
    "K": "Kabir: Indian man, 32, slim, oval face, tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, mid-grey bomber over blue T-shirt, one yellow-and-black pencil.",
    "R": "Riya: Indian woman, 24, black low ponytail, olive kurta, jeans, lanyard.",
}
VOICE = {
    "S": "SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear.",
    "K": "KABIR: a young man's voice, warm medium-low baritone, quick and dry, quieter when he avoids something.",
    "R": "RIYA: a young woman's voice, clear mid-high pitch, quick and steady.",
    "C": "THE CLONED VOICE: Kabir's own young male voice but thin, tinny and slightly too smooth, as heard through a cheap phone speaker, crying and panicked. It comes only from the phone; nobody on screen moves their lips for it.",
}
PUNE = "a small middle-class Indian flat in Pune at night: warm tungsten light, steel kitchen counter and containers, a wooden dining table with a plastic runner"
BLR = "an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors"

# id, time, beat, loc, chars, keyframe, action, camera, physics, audio, dialogue[(who, hindi, roman, english, at_s)], refs, post
CLIPS = [
 dict(id="01", t="0:00 to 0:05", beat="HOOK", loc="PUNE", chars=["S"],
  kf=f"Close-up of SUSHMA in the kitchen of {PUNE}. A phone is pressed to her ear in her floury right hand, a little flour dusted on her cheek, her left hand flat on the steel counter beside a steel plate of dough. Reading glasses pushed up on her head. Her expression has only just begun to change from ordinary to alarmed.",
  act="0.0 to 0.3 s: she is already on the call, the phone at her ear. 0.3 to 2.2 s: someone on the other end is crying and begging (you do not hear them in this clip); within about a second her face tightens, her eyes widen slightly and her breath catches, and her left hand rests firmly on the counter edge; her mouth stays closed or barely parted. 2.4 to 3.4 s: she says one soft word, lips matching. 3.4 to 5.0 s: she stares ahead, very still, her eyes glistening and filling slowly; no gasping, no wide eyes.",
  cam="Handheld CLOSE-UP, her face fills the frame with shoulders just visible, eye level, slow push-in.",
  phys="Flour dust falls from her fingers. Her hand shakes with real fear. The phone rests against her cheek and presses her hair slightly.",
  aud="Kitchen ambience only: exhaust fan hum, a distant pressure-cooker whistle, a wall clock ticking, her breath. No phone ringing.",
  dia=[("C","मम्मी! मम्मी, मुझे बचा लो!","Mummy! Mummy, mujhe bacha lo!","Mummy! Mummy, save me!",0.3),("S","कबीर?","Kabir?","Kabir?",2.5)],
  refs="CS-SUSHMA, LOC-PUNE", post="Title card AWAAZ · EP 1 and the word PUNE in the first second."),
 dict(id="02", t="0:05 to 0:10", beat="FRICTION", loc="PUNE", chars=["S"],
  kf=f"Medium close-up of SUSHMA at the kitchen counter in {PUNE}, the phone pressed to her ear with her right hand, her left hand flat on the steel counter with white flour handprints around it. Her face is frozen in dawning panic.",
  act="0.0 to 0.4 s: she stands rigid, listening. 0.4 to 2.8 s: the tinny crying voice from the phone speaks; her face tightens, her lips tremble slightly and her eyes glisten; her left hand presses on the counter edge and leaves white floury fingerprints on the steel; no sobbing, no open-mouthed crying. 3.0 to 4.4 s: she speaks, her voice cracking, lips matching. 4.4 to 5.0 s: she closes her eyes for a moment and breathes in slowly.",
  cam="Handheld medium close-up, a little lower than eye level, slow push-in.",
  phys="Flour smears naturally under her fingers. Her saree pallu slips a few centimetres off her shoulder as she grips.",
  aud="The same kitchen ambience, the thin phone voice, her breath.",
  dia=[("C","एक्सीडेंट हो गया। पुलिस ने पकड़ लिया।","Accident ho gaya. Police ne pakad liya.","There's been an accident. The police have me.",0.5),("S","हे भगवान! तू ठीक है?","Hey Bhagwan! Tu theek hai?","Oh God! Are you okay?",3.0)],
  refs="CS-SUSHMA, LOC-PUNE", post=""),
 dict(id="03", t="0:10 to 0:15", beat="FRICTION", loc="BLR", chars=["K"],
  kf=f"Medium close-up of KABIR at a lit desk in {BLR}. Headphones around his neck, a yellow-and-black pencil in his right hand, two monitors with blurred illegible code behind him. His phone lies face-up on the desk, its screen lit with a contact photo of a smiling older woman.",
  act="0.0 to 0.8 s: the phone buzzes and lights up; he glances at it. 0.8 to 1.8 s: his jaw tightens, his thumb hovers over the screen. 1.8 to 2.5 s: he swipes it away and flips the phone face-down. 2.5 to 3.8 s: he says one quiet line without looking at it. 3.8 to 5.0 s: he goes back to typing, the pencil tapping the desk.",
  cam="Handheld medium close-up from slightly to his left, shallow depth of field.",
  phys="The phone vibrates on the desk with a real buzz. The pencil taps the desk at a steady rhythm. Rain trickles down the window behind.",
  aud="Office night ambience: air conditioning hum, distant rain, keyboard clicks, the phone buzz, pencil taps.",
  dia=[("K","बाद में, मम्मी।","Baad mein, Mummy.","Later, Mummy.",2.6)],
  refs="CS-KABIR, LOC-BLR", post="Place BENGALURU super."),
 dict(id="04", t="0:15 to 0:20", beat="FRICTION", loc="PUNE", chars=["S"],
  kf=f"Medium close-up of SUSHMA seated at the small wooden dining table in {PUNE}. A phone lies flat on the table in front of her. A steel thali with half-eaten dinner is pushed aside. Her reading glasses are pushed up on her head. Her hands rest on the table beside the phone, lightly floury and trembling. Her face is tense and still, her mouth closed.",
  act="0.0 to 3.0 s: she sits almost motionless, staring down at the phone with her mouth CLOSED. She makes no sound and says no words: only her chest rising and falling and her hands trembling slightly. There is no sobbing, no whimpering and no muttering. 2.6 to 3.1 s: with one hand she pulls her reading glasses down onto her nose. 3.3 to 4.5 s: she taps the phone screen with a shaking finger and says one short line, lips matching, voice small and shaky. 4.5 to 5.0 s: she keeps her eyes on the screen. NO large gestures: no hand to her head, no slapping the table.",
  cam="Handheld medium close-up, slight push-in, eye level.",
  phys="The glasses slide down her head and land on her nose naturally. The thali rattles slightly as the table shakes under her trembling hands.",
  aud="Fan hum, a clock tick, her fast breathing. She is silent until her one line.",
  dia=[("C","चालीस हज़ार यूपीआई करो। अभी। किसी को मत बताना।","Chaalis hazaar UPI karo. Abhi. Kisi ko mat batana.","Send forty thousand on UPI. Now. Don't tell anyone.",0.1),("S","भेज रही हूँ, बेटा।","Bhej rahi hoon, beta.","I'm sending it, son.",3.4)],
  refs="CS-SUSHMA, LOC-PUNE", post="RETAKE of the rejected take 1, which had Sushma vocalising during the phone-voice window and slapping her head."),
 dict(id="05", t="0:20 to 0:25", beat="FRICTION", loc="PUNE", chars=["S"],
  kf=f"Close-up of SUSHMA's face at the dining table in {PUNE}, lit from below by the glow of a phone screen held just below frame, reading glasses ON HER NOSE (not pushed up on her head, for the whole shot), her eyes moving along the screen, lips slightly parted.",
  act="Her reading glasses stay on her nose for the whole shot; they never go up onto her head. 0.0 to 1.2 s: she reads, eyes moving, lips moving silently. 1.2 s: she stops, her brow drawing together. 1.4 to 3.0 s: she says one slow line quietly, lips matching, doubt in her voice, mouth only slightly open. 3.2 to 4.2 s: a sharp voice on the phone (not heard in this clip) makes her give a small start: her shoulders tighten and her eyes flick up; no big flinch. 4.2 to 5.0 s: she looks back at the screen, undecided.",
  cam="Handheld close-up with a slow push-in; the phone glow lights her face.",
  phys="Phone light flickers on her glasses lenses. Her flinch moves her whole head a few centimetres back.",
  aud="Fan hum, a clock tick, her breathing, the phone voice.",
  dia=[("S","ये नाम तो राहुल का है?","Ye naam toh Rahul ka hai?","This name is Rahul's?",1.4),("C","जल्दी करो, मम्मी!","Jaldi karo, Mummy!","Hurry, Mummy!",3.2)],
  refs="CS-SUSHMA", post="Add the UPI receiver-name overlay (a made-up name) if you want the viewer to read what she reads."),
 dict(id="06", t="0:25 to 0:30", beat="FRICTION", loc="BLR", chars=["K","R"],
  kf=f"Medium two-shot in {BLR}. KABIR sits at the lit desk on the right, typing. RIYA arrives from the left with a white mug, olive kurta, lanyard. Kabir's phone lies face-down on the desk between them.",
  act="0.0 to 1.0 s: Riya walks up; the face-down phone buzzes and creeps across the desk. 1.0 to 3.0 s: Riya looks at the phone and says one line. 3.0 to 4.5 s: Kabir looks at the phone, the annoyance leaves his face, he says one quiet line. 4.5 to 5.0 s: he snatches up the phone.",
  cam="Handheld medium two-shot at eye level, slight sway.",
  phys="The phone vibrates and slides on the desk. The mug steams slightly. Kabir's chair creaks as he sits up.",
  aud="Office ambience, keyboard clicks, the phone buzz, footsteps.",
  dia=[("R","कबीर, तुम्हारी मम्मी तीसरी बार कर रही हैं।","Kabir, tumhaari Mummy teesri baar kar rahi hain.","Kabir, your mother is calling a third time.",1.0),("K","मम्मी कभी तीन बार नहीं करतीं।","Mummy kabhi teen baar nahin kartin.","Mummy never calls three times.",3.2)],
  refs="CS-KABIR, CS-RIYA, LOC-BLR", post=""),
 dict(id="07", t="0:30 to 0:35", beat="FRICTION", loc="PUNE", chars=["S"],
  kf=f"Medium close-up of SUSHMA at the dining table in {PUNE}, on a phone call: the phone is held to her right ear in her right hand with a normal grip, her left hand resting on the table, reading glasses on her nose, her face tense and quiet.",
  act="0.0 to 0.9 s: she listens with the phone at her ear. 0.9 to 1.5 s: she hears a soft call-waiting beep, lowers the phone about 20 centimetres from her ear and looks at its screen; the BACK of the phone faces the camera and the screen glow lights her face and glasses (we never see the screen). 1.5 to 2.6 s: she says one puzzled line, looking from the phone to the table and back. 2.6 to 4.0 s: she listens to a panicked voice on the phone (not heard in this clip); her thumb rests near the edge of the phone, undecided. 4.0 to 5.0 s: she brings the phone back toward her ear slowly.",
  cam="Handheld medium close-up, slow push-in, eye level.",
  phys="Normal phone grip: four fingers behind, thumb at the side. The screen glow changes on her face as she tilts the phone. Her arm moves with natural weight.",
  aud="Fan hum, her breathing, a very soft call-waiting beep.",
  dia=[("S","तेरा फोन भी आ रहा है।","Tera phone bhi aa raha hai.","Your phone is calling too.",1.6),("C","पुलिस है! मत उठाओ, मम्मी!","Police hai! Mat uthao, Mummy!","It's the police! Don't answer, Mummy!",2.6)],
  refs="CS-SUSHMA, LOC-PUNE", post="RETAKE (batch 3 take held the phone up with its screen facing the camera). The call banner is shown in the C12 POV insert."),
 dict(id="08", t="0:35 to 0:40", beat="FRICTION", loc="BLR", chars=["K","R"],
  kf=f"Handheld two-shot in {BLR}. KABIR stands at his desk with a phone pressed to his ear, tense. RIYA stands beside him with a laptop tucked under her arm, frowning. Rain on the window behind them. A yellow-and-black pencil lies on the desk.",
  act="0.0 to 1.2 s: a ring tone is heard from his phone; he waits, tapping the desk with his free hand. 1.2 to 1.8 s: a busy beep; he lowers the phone. 1.8 to 2.6 s: he says one line. 2.6 to 4.2 s: Riya frowns, thinking, and says one line. 4.2 to 5.0 s: Kabir's eyes widen as it lands.",
  cam="Handheld two-shot, slight push-in on Kabir at the end.",
  phys="The phone ring and busy beep are heard from the handset, not the room. Kabir's breathing is audible.",
  aud="Office ambience, rain, the ring tone, a busy beep.",
  dia=[("K","बिज़ी जा रहा है।","Busy ja raha hai.","It's going busy.",1.8),("R","तुमने क्लोनिंग का डेमो दिया था ना?","Tumne cloning ka demo diya tha na?","You gave that cloning demo, didn't you?",2.6)],
  refs="CS-KABIR, CS-RIYA, LOC-BLR", post=""),
 dict(id="09", t="0:40 to 0:45", beat="SPIKE", loc="BLR", chars=["K","R"],
  kf=f"Medium shot in {BLR}. The camera sits just behind an open laptop on the desk: the BACK of the laptop lid fills the lower foreground (plain silver, no logo). Above it, KABIR stands leaning toward the screen and RIYA stands beside him, both looking down at the screen, their faces lit from below by its cool glow. A yellow-and-black pencil lies on the desk. The people face the laptop screen; the camera does not see the screen.",
  act="0.0 to 0.8 s: Kabir leans in over the laptop, Riya beside him with one hand resting on the desk. 0.8 to 2.6 s: Riya says one line quietly, glancing at the screen then at him; she does not wave her arms. 2.8 to 4.0 s: Kabir slowly raises one hand to his mouth and whispers one short line through his fingers. 4.0 to 5.0 s: he straightens a little, his face pale and still.",
  cam="Locked-off medium close-up from behind the laptop, very slight push-in.",
  phys="The screen's glow lights both faces from below with a cool white-blue cast and moves as they shift. The laptop is open at a natural angle with its screen facing them, not the camera.",
  aud="Office ambience, a faint laptop fan, Riya's line, his whisper.",
  dia=[("R","तीन सेकंड की आवाज़ काफ़ी होती है।","Teen second ki aawaaz kaafi hoti hai.","Three seconds of voice is enough.",0.9),("K","मेरी अपनी आवाज़।","Meri apni aawaaz.","My own voice.",2.9)],
  refs="CS-KABIR, CS-RIYA, LOC-BLR", post="RETAKE (batch 3 take had the screen facing the camera, away from the people). In post I cut a 1.5 s full-screen cutaway of the PROP-STAGE still (slow push-in) between Riya's line and his whisper, so no stage video is needed."),
 dict(id="10", t="0:45 to 0:50", beat="SPIKE", loc="BLR", chars=["K"],
  kf=f"Side-on shot in {BLR}. KABIR has just stood up from his desk, his chair mid-spin, a phone pressed to his ear, in the aisle between rows of desks, the aisle leading to a glass door at the end. Motion in his whole body.",
  act="0.0 to 0.7 s: as he stands, his arm knocks the yellow-and-black pencil off the desk (it lies there in the earlier shots) and it clatters to the floor; the chair spins and bangs the desk. 0.7 to 3.8 s: he sprints along the aisle toward the glass door, jacket flying, phone at his ear; between 1.0 and 2.5 s he shouts one line into the phone, out of breath. 3.8 to 5.0 s: he hits the glass door with his shoulder and pushes through.",
  cam="Handheld MEDIUM tracking shot from the side at his pace (his head and upper body fill the frame, not a wide shot), slightly low angle, with real camera shake.",
  phys="Running looks natural: weight shifts, arms drive, jacket and hair flow with the motion. The chair spins to a stop. The pencil bounces once.",
  aud="Fast footsteps on the floor, panting, the chair bang, the pencil clatter, the glass door thud, a ringing tone from the phone.",
  dia=[("K","मम्मी, मत भेजना!","Mummy, mat bhejna!","Mummy, don't send it!",1.0)],
  refs="CS-KABIR, LOC-BLR", post="Fallback if the sprint looks broken at this resolution: he stands, grabs his jacket from the chair and strides fast out of frame with the phone at his ear, same line, same timing. Add office ambience and footsteps in post."),
 dict(id="11", t="0:50 to 0:55", beat="FRICTION", loc="PUNE", chars=["S"],
  kf=f"Close-up of SUSHMA at the dining table in {PUNE}, the phone held to her right ear in a normal grip, her eyes glistening, her face still and drawn, reading glasses on her nose.",
  act="0.0 to 2.6 s: she listens with the phone at her ear, very still, her eyes slowly filling; a single tear runs down one cheek. No sobbing, no open mouth. 2.8 to 4.0 s: she whispers one short line, lips matching, barely audible. 4.0 to 5.0 s: she lowers the phone slowly from her ear and looks down at it.",
  cam="Handheld close-up, slow push-in, eye level.",
  phys="A tear runs down under gravity. The phone comes down from her ear with natural arm weight.",
  aud="Her shaky breath, a clock tick, a very soft call-waiting chime.",
  dia=[("C","मम्मी, मुझसे प्यार है तो भेजो!","Mummy, mujhse pyaar hai toh bhejo!","Mummy, if you love me, send it!",0.2),("S","कौन-सा कबीर?","Kaun-sa Kabir?","Which Kabir?",3.0)],
  refs="CS-SUSHMA", post="RETAKE (batch 3 take had open-mouthed sobbing and a garbled banner). The thumb beat is now clip 12."),
 dict(id="12", t="0:55 to 1:00 (freeze made in post)", beat="BUTTON", loc="PUNE", chars=[],
  kf="First-person POV looking down at a phone held in one hand (natural grip, four fingers behind, thumb free). The screen faces the camera because the camera is her eyes. The screen is a plain dark payment screen with a large plain green button at the bottom and a plain green call-accept button on a banner at the top, no text. Her other hand rests on a wooden table with a little flour. Warm kitchen light, shallow depth of field. No face visible.",
  act="0.0 to 3.0 s: her thumb trembles slightly above the glass, drifting slowly between the upper and lower buttons, never touching. A single tear falls onto the back of the hand holding the phone. 3.0 to 6.0 s: the thumb stops, hovering, completely still, between the two buttons.",
  cam="Locked-off POV insert from her eye level, very shallow depth of field on the thumb.",
  phys="The thumb hovers a few millimetres above the glass and trembles. The tear falls under gravity and lands on skin. Natural phone grip.",
  aud="Room sound drops away. A faint ringtone and a muffled, begging voice overlap, both quiet. Her breath.",
  dia=[],
  refs="CS-SUSHMA (for the hands)", post="Freeze at 0:57 and hold; KEEP the call banner and the ₹40,000 payment card on screen through the freeze so both choices stay visible; caption कौन-सा कबीर? and EP 2 → above them; cut to black at 0:59.5. I add the UI text and the call banner. The faint 'मम्मी...' is cut from voice session A."),
 dict(id="INS-9", t="still for clip 09", beat="PROP", loc="STAGE", chars=["K"],
  kf="Photorealistic 16:9 still of KABIR RAO on a modern tech conference stage at a lectern, mid-sentence, one hand raised palm-up, a headset microphone at his cheek, a large screen behind him with an abstract waveform and no text, a dark blurred audience in the foreground.",
  act="0.0 to 0.5 s: he steps up to the lectern mic. 0.5 to 3.5 s: he speaks one line to the audience, lips matching, with one hand raised, palm up, a small confident smile. 3.5 to 5.0 s: a ripple of audience murmur; he nods and keeps smiling.",
  cam="Locked-off medium close-up from the front of the stage, slow push-in.",
  phys="Stage light casts a clean key on his face. The headset mic moves with his jaw.",
  aud="PA-quality voice with a small amount of room echo, a faint audience murmur and applause at the end.",
  dia=[("K","बस तीन सेकंड की आवाज़ चाहिए। और क्लोन तैयार।","Bas teen second ki aawaaz chahiye. Aur clone taiyaar.","I only need three seconds of voice. And the clone is ready.",0.6)],
  refs="PROP-STAGE, CS-KABIR", still_only=True, post="STILL ONLY: do not make a video. Use the approved PROP-STAGE picture; I put it on the laptop screen in clip 09 with a slow push-in. Not counted in the 60 seconds."),
]

VOICE_SESSIONS = [
 ("VS-A", "Cloned voice, session A (lines 1 and 3)", [
   (0.2,"मम्मी! मम्मी, मुझे बचा लो!","Mummy! Mummy, mujhe bacha lo!"),
   (2.9,"एक्सीडेंट हो गया। पुलिस ने पकड़ लिया।","Accident ho gaya. Police ne pakad liya.")]),
 ("VS-B", "Cloned voice, session B (lines 6 and 9)", [
   (0.2,"चालीस हज़ार यूपीआई करो। अभी। किसी को मत बताना।","Chaalis hazaar UPI karo. Abhi. Kisi ko mat batana."),
   (4.3,"जल्दी करो, मम्मी!","Jaldi karo, Mummy!")]),
 ("VS-C", "Cloned voice, session C (lines 13 and 19)", [
   (0.2,"पुलिस है! मत उठाओ, मम्मी!","Police hai! Mat uthao, Mummy!"),
   (3.0,"मम्मी, मुझसे प्यार है तो भेजो!","Mummy, mujhse pyaar hai toh bhejo!")]),
]


def voice_session(tag, title, lines):
    dl = "\n".join(f'{i + 1}. at about {at:.1f} s: "{hi}" (pronounced: {ro})' for i, (at, hi, ro) in enumerate(lines))
    return (f"Animate the start image as ONE continuous 6-second shot, no cuts. Close-up of KABIR RAO, an Indian man, 32, oval face, thick tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, sitting in the dark driver's seat of a parked car at night, his face lit only by a phone held close to his mouth, crying and panicked, out of breath. "
            f"He speaks the lines below into the phone in natural conversational Hindi, sobbing, his voice cracking, with a short ragged sob between lines. His normal LOW chest voice, a grown man's hoarse, cracking baritone, as if crying through a clenched throat: NOT high-pitched, NOT falsetto, NOT a boy's voice. The same low voice he uses in normal conversation, only broken by sobs and shaking. Lips match every word exactly. Nobody else speaks. No music, no text.\n\nDIALOGUE:\n{dl}\n\n"
            f"STYLE: {STYLE_VIDEO}\n\nDURATION: 6 seconds. Each line must be said fully and clearly inside its time window.")


RULES = 'STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), a phone held to the ear with its microphone near the mouth on calls, screens facing the person who reads them, a laptop open facing its user, strict physics for weight, contact and motion. (2) Performances are subtle, restrained and naturalistic, never exaggerated: show feeling through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.'
RULES_KF = 'Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints); a phone at the ear on calls; screens facing the person using them. Expression subtle and naturalistic, not exaggerated.'


def keyframe(c):
    who = " ".join(FULL[k] for k in c["chars"])
    aspect = "16:9" if c["id"] == "INS-9" else "vertical 9:16"
    return f"{c['kf']} {who} {RULES_KF} {STYLE_STILL.replace('vertical 9:16', aspect)}"


def animate(c):
    who = " ".join(SHORT[k] for k in c["chars"])
    own = [d for d in c["dia"] if d[0] != "C"]
    clone = [d for d in c["dia"] if d[0] == "C"]
    speakers = []
    for who_, *_ in own:
        if who_ not in speakers:
            speakers.append(who_)
    voices = "\n".join("- " + VOICE[s] for s in speakers) or "- none (no one on screen speaks)"
    dl = "\n".join(
        f'{i + 1}. at about {at:.1f} s, {({"S": "SUSHMA", "K": "KABIR", "R": "RIYA"}[w])}: "{hi}" (pronounced: {ro})'
        for i, (w, hi, ro, en, at) in enumerate(own)) or "none"
    lips = "Only the person who is speaking moves their lips, and every word matches their lips exactly."
    if clone:
        times = ", ".join(f"{d[4]:.1f} s" for d in clone)
        lips += (f" IMPORTANT: the phone is completely silent in this clip. Nobody but the people listed under DIALOGUE speaks. "
                 f"Sushma reacts as if she is hearing a crying, panicked voice on the phone starting at about {times}, and she stops her own speech while it plays.")
    aspect = "landscape 16:9" if c["id"] == "INS-9" else "vertical 9:16"
    style = STYLE_VIDEO.replace("vertical 9:16", aspect)
    return (f"Animate the supplied start image as ONE continuous shot, 6 seconds long, no cuts. All of the action below happens in the first 5 seconds; after that, hold the final pose almost still. Keep the people, the place, the clothes and the light EXACTLY as in the start image; do not change any face.\n\n"
            f"PEOPLE: {who}\n\nWHAT MOVES: {c['act']}\n\nCAMERA: {c['cam']}\n\nPHYSICS: {c['phys']}\n\n"
            f"STANDING RULES: {RULES}\n\nLIP SYNC: {lips}\n\nVOICES (clearly different from each other):\n{voices}\n\n"
            f"DIALOGUE in natural conversational Hindi, in this order, no overlap:\n{dl}\nEach line must be clearly audible.\n\n"
            f"AUDIO: {c['aud']}\n\nSTYLE: {style}\n\nDURATION: 6 seconds (the maximum the tool gives). Large faces and hands, simple background, no tiny details.")


def main():
    o = []
    w = o.append
    w("# AWAAZ Episode 1: clip prompts (6-second clips, about 400x736)\n")
    w("""**Output limits (paid Grok account, as reported):** videos still render at 6 seconds and about 400x736. Generations are no longer rationed.

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
""")
    w("""## The phone voice is made separately (new)
Grok gave the phone voice to the person on screen, or not at all, so the cloned voice is **not** generated inside the Sushma clips any more. Instead:

1. In each Sushma clip, the phone is silent and she reacts to it. Only her own lines are spoken.
2. Generate the three **voice sessions** below: Kabir crying into a phone in a parked car. We use only the **audio**; the picture is thrown away. Start from the Kabir contact sheet face crop.
3. I cut each line from the sessions, filter it to sound like a cheap phone speaker (narrow band, slight distortion), and place it at the exact time shown on each clip.

This also keeps the cloned voice close to the real Kabir's voice, which is the point of the story.

""")
    for tag, title, lines in VOICE_SESSIONS:
        w(f"### {tag}: {title}\n")
        w("Start image: crop of `CS-KABIR` (face). Video mode, 6 seconds, any aspect. Keep the best take.\n")
        w("```\n" + voice_session(tag, title, lines) + "\n```\n")
    for c in CLIPS:
        w(f"## CLIP {c['id']}: {c['beat']} ({c['t']})\n")
        w(f"**References to attach for the keyframe:** {c['refs']}\n")
        w("### KEYFRAME (image mode)\n```\n" + keyframe(c) + "\n```\n")
        if c.get("still_only"):
            w("### ANIMATE\nNone. Still only, see the post note.\n")
        else:
            w("### ANIMATE (video mode, 6 s)\n```\n" + animate(c) + "\n```\n")
        w("**Dialogue for your check**\n")
        for who_, hi, ro, en, at in c["dia"]:
            nm = {"C": "Cloned voice (phone)", "S": "Sushma", "K": "Kabir", "R": "Riya"}[who_]
            w(f"- {nm} @ {at:.1f} s: {hi} / {ro} / {en}")
        w("")
        cl = [d for d in c["dia"] if d[0] == "C"]
        if cl:
            w("**Phone voice (added in post, not generated in this clip):** " + "; ".join(f'"{d[1]}" at {d[4]:.1f} s' for d in cl) + ". I take it from the voice session and filter it to sound like a phone.\n")
        if c["post"]:
            w(f"**Post note:** {c['post']}\n")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "04-ep01-clip-prompts.md")
    open(path, "w", encoding="utf-8").write("\n".join(o) + "\n")
    print("wrote", path, len(CLIPS), "clips")


if __name__ == "__main__":
    main()
