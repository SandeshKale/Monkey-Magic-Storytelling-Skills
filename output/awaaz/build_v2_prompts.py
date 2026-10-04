#!/usr/bin/env python3
"""Builds 12-ep01-v2-clip-prompts.md: AWAAZ Ep1 rebuild, 15 s Grok clips at 480p 9:16.
Every prompt is assembled from the same constant blocks, so the face-lock words are identical everywhere."""
import os

# ---------------------------------------------------------------- shared blocks
FACE = {
 "S": "FACE LOCK, SUSHMA RAO (same words in every prompt): Indian woman, 58 years old, round-oval face, wheatish skin with deep smile lines and a few age spots, heavy-lidded dark brown eyes, softly lined forehead, a small round red bindi, a small gold nose stud, greying black hair in a loose low bun with silver streaks. Jewellery: a thin gold bangle on each wrist, the nose stud and small gold stud earrings, NOTHING else. NO necklace, no chain, no pendant, no mangalsutra, no other jewellery.",
 "K": "FACE LOCK, KABIR RAO (same words in every prompt): Indian man, 32 years old, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses.",
 "R": "FACE LOCK, RIYA MENON (same words in every prompt): Indian woman, 24 years old, round friendly face with soft cheeks, large dark expressive eyes, shoulder-length straight black hair tied in a low ponytail with a few loose strands, small silver stud earrings, no glasses.",
}
WARD = {
 "S": "WARDROBE: sage-green cotton saree with a thin printed border over a deep teal blouse; a little flour on her forearm and knuckles.",
 "K": "WARDROBE: mid-grey bomber jacket over a muted-blue crew-neck T-shirt, black smartwatch on his left wrist.",
 "K_STAGE": "WARDROBE (older recorded talk, a different day): black blazer over a muted-blue crew-neck T-shirt, a headset microphone at his cheek, a conference lanyard, black smartwatch on his left wrist.",
 "R": "WARDROBE: olive-green cotton kurta over blue jeans, a company lanyard with a plain white card.",
}
GLASSES = {
 "head": "SUSHMA'S GLASSES: round tortoiseshell reading glasses pushed up on top of her head, resting above her forehead. They stay there for the whole shot; nothing touches them.",
 "nose": "SUSHMA'S GLASSES: round tortoiseshell reading glasses sitting on the bridge of her nose. They stay there for the whole shot; nothing touches them.",
}
CANON = {"S": "CANON-S", "K": "CANON-K", "R": "CANON-R"}
LOCK_RULE = "Medium close-up (head to mid-chest), at most 30 degrees off straight-on, never wider."
SILENT = "MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE."
RULES = ("STANDING RULES. (1) Objects are handled as a real person would: real hand grips, correct anatomy (five fingers, natural joints), screens facing the person who reads them, strict physics for weight, contact and motion. "
         "(2) Performance is subtle, restrained and naturalistic: feeling shown through small changes in the eyes, brow, breath and hands; no wide-open mouths, no bulging eyes, no flailing, no theatrical gestures.")
RULES_KF = "Objects held correctly with real hand grips and correct anatomy (five fingers, natural joints). Expression subtle and naturalistic, not exaggerated."
NOSCREEN = "Any screen is a plain dark glass rectangle with no readable content; real screen content is added in post."
STYLE_STILL = ("Photorealistic cinematic still, vertical 9:16, 85mm lens, shallow depth of field, natural skin with pores and fine detail, real fabric texture, "
               "teal shadows with warm practical light, handheld documentary realism. No text, no captions, no watermarks, no logos, no readable writing on any screen or sign.")
STYLE_VIDEO = ("Photorealistic live-action cinema, vertical 9:16, 24 fps, natural motion blur, real skin texture, strict real-world physics (gravity, momentum, cloth, hair, liquid behave naturally). "
               "One continuous shot, no cuts, no dissolves, no zooms to a new subject. No text, subtitles, logos or readable writing anywhere in the picture. No background music.")
PUNE = "a small middle-class Indian flat in Pune at night: warm tungsten ceiling light, a yellow bulb over the stove, steel containers, a wooden dining table with a plastic table runner"
BLR = "an open-plan tech startup office in Bengaluru at night: cool blue light, a few lit desks, rain on tall windows, dark monitors"
VOICE = {
 "S": "SUSHMA: a woman in her late 50s, warm, mid-low pitch, breathy and shaky with fear. Soft, never loud.",
 "K": "KABIR: a young man's deep, low chest-voice baritone, warm, quick, dry, quieter when he avoids something. NOT high, NOT thin.",
 "R": "RIYA: a young woman's voice, clear mid-high pitch, quick and steady.",
}

# ---------------------------------------------------------------- shots
# beats: (t0, t1, text). dia: (who, hindi, roman, english, clip_t0, clip_t1, source)  source GROK | VS
SHOTS = [
 dict(id="S1", name="HOOK: the call", edit=(0.0, 12.0), keep=(0.0, 12.0), gen=15, loc="PUNE", chars=["S"], glasses="head",
  refs="CANON-S, LOC-PUNE (panels 1 and 2)",
  kf=f"Medium close-up of SUSHMA in the kitchen of {PUNE}. Her RIGHT hand holds a phone against her right ear with a correct grip, thumb behind the phone, fingers wrapped around the back, the microphone end near her cheek. Her LEFT hand rests flat on the steel counter beside a steel plate of dough. A little flour on her left cheek. She looks just slightly ahead, ordinary and calm, mouth closed. Steel containers and the stove softly out of focus behind her.",
  beats=[(0.0, 1.0, "She is already on the call: the phone stays at her right ear. Calm, mouth closed and still, eyes forward."),
         (1.0, 4.2, "She listens. Mouth closed and still. Her face tightens slowly: brow draws together, breath catches at about 2.5 s, eyes begin to glisten. Left hand presses lightly on the counter edge. Nothing else moves."),
         (4.5, 5.3, "She says one soft word, lips matching, then the mouth closes again."),
         (5.3, 9.6, "She listens. Mouth closed and still. The fear deepens in small steps: a swallow, a tremble in the lower lip, her eyes filling. No wide eyes."),
         (9.6, 11.6, "She says one short line, soft and shaking, lips matching, then the mouth closes."),
         (11.6, 15.0, "She holds still, eyes glistening, mouth closed, phone still at her ear. (Not used in the edit; keep it perfectly calm.)")],
  dia=[("S", "कबीर?", "Kabir?", "Kabir?", 4.6, 5.2, "GROK"),
       ("S", "हे भगवान! तू ठीक है?", "Hey Bhagwan! Tu theek hai?", "Oh God! Are you okay?", 9.8, 11.4, "GROK")],
  phone=[("मम्मी! मम्मी, मुझे बचा लो!", "Mummy! Mummy, mujhe bacha lo!", 1.5, 3.8, "VS-1"),
         ("एक्सीडेंट हो गया। पुलिस ने पकड़ लिया।", "Accident ho gaya. Police ne pakad liya.", 6.3, 9.0, "VS-1")],
  hand="RIGHT hand: the phone, at the right ear from the first frame to the last; it never leaves the ear. LEFT hand: flat on the counter. Nothing else is touched. No ear-to-hand transition. The screen is never seen.",
  cam="Medium close-up, her face and shoulders fill the frame, eye level, locked-off with a very slow push-in (about 5 percent over 15 s).",
  phys="The phone is held steadily against the ear. Flour on her knuckles stays on the hand. Cloth of the saree moves only with her breathing.",
  aud="Only Sushma's two lines are spoken. The caller on the phone is completely silent in this clip. No music. Quiet room only.",
  post="OVERLAY: title card 'AWAAZ · EP 1' at 0.0-1.0 s over the first frames; super 'PUNE' at 0.6-2.4 s, lower left. ROOM TONE: kitchen bed from 0.0 s (exhaust-fan hum, a distant pressure cooker, faint street) at about -30 dB. PHONE VOICE (VS-1, phone-filtered) at the times above. J-CUT: office room tone fades in at 11.5 s under her last word. L-CUT: kitchen fan hum continues 0.6 s into S2."),

 dict(id="S2", name="Kabir declines", edit=(12.0, 19.0), keep=(1.0, 8.0), gen=15, loc="BLR", chars=["K"],
  refs="CANON-K, LOC-BLR (panels 2 and 5)",
  kf=f"Medium close-up of KABIR at a lit desk in {BLR}. He sits facing a laptop whose lid back is toward the camera and whose screen faces him. In his RIGHT hand he holds the yellow-and-black mechanical pencil in a normal writing grip, its tip resting on the desk. His LEFT hand rests beside a phone lying face-up on the desk in front of him; the phone's screen is angled up toward him and shows only a faint glow to the camera. A white mug and headphones around his neck. He is tired and focused, mouth closed.",
  beats=[(0.0, 2.0, "He looks at the laptop screen, tired and focused, mouth closed and still. The right-hand pencil taps the desk slowly, three soft taps."),
         (2.0, 3.0, "The phone lights up on the desk: a faint glow on his face. His eyes drop to it. His jaw tightens a little. Mouth closed and still."),
         (3.0, 3.8, "His LEFT thumb touches the phone screen once and the glow dims. The phone stays face-up where it is."),
         (4.0, 5.3, "He says one short line, low and flat, eyes on the laptop, lips matching, then the mouth closes."),
         (5.3, 8.0, "He goes back to the work, mouth closed and still. The pencil taps the desk."),
         (8.0, 15.0, "He keeps working, almost still. (Not used in the edit.)")],
  dia=[("K", "बाद में, मम्मी।", "Baad mein, Mummy.", "Later, Mummy.", 4.0, 5.3, "GROK")],
  phone=[],
  hand="RIGHT hand: the pencil, writing grip, taps the desk and never lets go. LEFT hand: only the thumb touches the phone, once; the phone never leaves the desk and is not flipped or lifted. The laptop and phone screens face Kabir, never the camera.",
  cam="Medium close-up from slightly left of centre, eye level, locked-off with a slow push-in.",
  phys="The pencil taps lightly and bounces back; the phone is still. Blue screen glow on his face and glasses, no lens tint.",
  aud="Only Kabir's one line is spoken. No other voice. Quiet office hum.",
  post="OVERLAY: super 'BENGALURU' at 12.3-14.0 s; incoming-call banner 'MUMMY' slides in at the top at 13.0 s and slides out at 14.2 s (the phone screen is never visible, so the banner carries it). SFX: phone vibration buzz at 13.0-14.0 s on wood; pencil taps (add layered taps to cover any soft ones). ROOM TONE: office bed (HVAC hum, rain on glass) from 11.5 s to 19.3 s at about -28 dB. J-CUT: the scam voice (S3 line 1) starts at 18.7 s, 0.3 s before the cut, over Kabir's last frames."),

 dict(id="S3", name="The demand", edit=(19.0, 29.0), keep=(1.0, 11.0), gen=15, loc="PUNE", chars=["S"], glasses="nose",
  refs="CANON-S, LOC-PUNE (panels 3 and 4)",
  kf=f"Medium close-up of SUSHMA sitting at the small wooden dining table in {PUNE}, a steel thali with unfinished dinner pushed aside, a water jug behind. A phone lies face-up on the table in front of her, its screen angled toward her (the camera sees it only at the bottom edge of the frame, from behind). Her RIGHT hand rests flat on the table beside the phone, her LEFT hand rests on the table edge. She looks at the phone, worried, mouth closed. Slight three-quarter angle.",
  beats=[(0.0, 1.0, "She listens to the phone. Mouth closed and still. Hands resting on the table."),
         (1.0, 5.2, "She keeps listening: mouth closed and still. Slow tightening of the brow, a swallow, a small nod of understanding. Eyes glisten."),
         (5.9, 7.3, "She says one line softly, lips matching, eyes on the phone, then the mouth closes."),
         (7.3, 8.6, "She leans a few degrees forward and reads the phone, eyes narrowing as if squinting. Mouth closed and still. Hands stay on the table."),
         (8.7, 10.5, "She says one line, puzzled, lips matching, then the mouth closes."),
         (10.5, 15.0, "She stays frozen, eyes on the phone, mouth closed. (Not used in the edit.)")],
  dia=[("S", "भेज रही हूँ, बेटा।", "Bhej rahi hoon, beta.", "I'm sending it, son.", 5.9, 7.3, "GROK"),
       ("S", "ये नाम तो राहुल का है?", "Ye naam toh Rahul ka hai?", "This name is Rahul's?", 8.7, 10.5, "GROK")],
  phone=[("चालीस हज़ार यूपीआई करो। अभी। किसी को मत बताना।", "Chaalis hazaar UPI karo. Abhi. Kisi ko mat batana.", 0.7, 4.6, "VS-1")],
  hand="BOTH hands rest on the table; she never touches the phone. The phone lies flat, screen toward her. Her glasses are already on her nose and nothing touches them. No tapping, no lifting.",
  cam="Medium close-up, slight three-quarter, eye level, locked-off with a slow push-in.",
  phys="The phone lies still on the table. Her breath moves the saree slightly.",
  aud="Only Sushma's two lines are spoken. The phone is completely silent in this clip. Quiet room only.",
  post="PHONE VOICE (VS-1, phone-filtered) plays at edit 18.7-22.6 s (it begins in the last 0.3 s of S2). OVERLAY: UPI card 'RAHUL VERMA  ₹40,000' (lower third, white card, green button) fades in at edit 26.2 s and holds to 29.0 s and into the cut. ROOM TONE: kitchen/dining bed (fan hum, distant street) from 19.0 s at about -30 dB. J-CUT into S4: Kabir's phone buzzing on a desk at 28.7 s."),

 dict(id="S4", name="Riya notices", edit=(29.0, 39.0), keep=(1.0, 11.0), gen=15, loc="BLR", chars=["R"],
  refs="CANON-R, LOC-BLR (panels 2 and 5)",
  kf=f"Medium close-up of RIYA standing at a desk in {BLR}. An open laptop sits on the desk in front of her with its lid back toward the camera and its screen facing her. Her fingertips rest lightly on the desk edge on both sides. She looks off to the right (toward Kabir, who is off camera), concerned, mouth closed. No mug, no bag, nothing in her hands. Slight three-quarter angle.",
  beats=[(0.0, 1.0, "She looks down at the laptop, then lifts her eyes to the right. Mouth closed and still."),
         (1.5, 4.4, "She says one line to Kabir off camera, steady, lips matching, then the mouth closes."),
         (4.4, 6.9, "She watches him. Mouth closed and still. Her brow draws slightly, her expression moves from teasing to unease in small steps."),
         (6.9, 7.4, "She glances down at the laptop, a small breath in. Mouth closed."),
         (7.4, 9.6, "She says one line, quieter, thinking aloud, lips matching, then the mouth closes."),
         (9.6, 15.0, "She keeps looking at him, eyes narrowing slightly, mouth closed. (Not used in the edit.)")],
  dia=[("R", "कबीर, तुम्हारी मम्मी तीसरी बार कर रही हैं।", "Kabir, tumhaari Mummy teesri baar kar rahi hain.", "Kabir, your mother is calling a third time.", 1.5, 4.4, "GROK"),
       ("R", "तुमने क्लोनिंग का डेमो दिया था ना?", "Tumne cloning ka demo diya tha na?", "You gave that cloning demo, didn't you?", 7.4, 9.6, "GROK")],
  phone=[],
  hand="BOTH hands: fingertips rest on the desk edge for the whole shot. The laptop is open on the desk with its screen toward her, lid back to camera, and is never touched or moved. No mug, no laptop under her arm.",
  cam="Medium close-up, slight three-quarter, eye level, locked-off.",
  phys="Nothing moves except Riya's face, breath and eyes.",
  aud="Only Riya's two lines are spoken. Kabir is off camera and silent in this clip. Quiet office hum.",
  post="OFF-SCREEN KABIR (VS-3 take, clean, not phone-filtered): 'मम्मी कभी तीन बार नहीं करतीं।' ('Mummy kabhi teen baar nahin kartin.') at edit 32.9-34.6 s, over Riya's listening face (her mouth is closed). SFX: phone buzz on wood 28.7-29.6 s; at 34.7-35.3 s a muffled dial ring-ring-ring and then the fast busy beeps of a failed call from off camera (J into her second line). ROOM TONE: office bed -28 dB. J-CUT into S5: stage-talk audio from a laptop speaker starts at 40.1 s."),

 dict(id="S5", name="The spike: his own voice", edit=(39.0, 47.5), keep=(0.0, 7.5), gen=15, loc="BLR", chars=["K"],
  refs="CANON-K, LOC-BLR (panel 2), INS-A (cut in from the stage insert)",
  kf=f"Medium close-up of KABIR leaning forward over an open laptop on a desk in {BLR}. The laptop's lid back is toward the camera and its screen faces him; a cold blue glow from the screen lights his face and shows faintly in his clear glasses. His LEFT hand rests flat on the desk. His RIGHT arm hangs relaxed at his side. A single yellow-and-black pencil lies on the desk at the left edge of the frame. He stares at the screen, mouth closed, concentrating.",
  beats=[(0.0, 1.5, "He stares at the screen, mouth closed and still. Blue glow on his face."),
         (1.5, 4.5, "He keeps staring. (This part is replaced in the edit by the stage insert INS-A. Stay very still, mouth closed.)"),
         (4.5, 5.2, "His breath stops. His eyes widen only slightly and his face goes still."),
         (5.2, 6.2, "His RIGHT hand rises slowly and settles over his mouth, fingers together. One deliberate movement, no jerking."),
         (6.2, 7.5, "He holds: hand over his mouth, eyes fixed on the screen, absolutely still, breathing very shallowly."),
         (7.5, 15.0, "He holds still. (Not used in the edit.)")],
  dia=[],
  phone=[],
  hand="LEFT hand: flat on the desk the whole time. RIGHT hand: one slow movement from his side to his mouth, then stays there. The pencil is only lying on the desk, never held. The laptop screen faces Kabir; the camera sees only the lid.",
  cam="Medium close-up from the front, eye level, locked-off with a very slow push-in.",
  phys="The laptop and desk are still. Blue light flickers softly on his face.",
  aud="Nobody speaks in this clip. His breath only. Quiet office hum.",
  post="EDIT: use clip 0.0-1.5 s at edit 39.0-40.5 s, then cut to INS-A (stage insert) for edit 40.5-44.5 s, then clip 4.5-7.5 s at edit 44.5-47.5 s. GRADE: colour drains from his face by about 15 percent from edit 45.0 to 47.5 s. AUDIO: INS-A's audio (the recorded talk) starts at 40.1 s through a laptop-speaker filter over Kabir's face and ends at 43.8 s. SFX: a low heartbeat-like sub tone from 44.8 s. No speech from Kabir: the line 'मेरी अपनी आवाज़' from the old script is dropped (his covered mouth would repeat last time's sync fault). J-CUT into S6: footsteps and a chair bang at 47.0-47.4 s."),

 dict(id="INS-A", name="Stage insert (recorded talk, own audio)", edit=(40.5, 44.5), keep=(0.0, 4.0), gen=15, loc="STAGE", chars=["K"], ward="K_STAGE",
  refs="CANON-K, PROP-STAGE",
  kf="Medium close-up of KABIR RAO on a modern tech conference stage at a lectern, a large screen behind him showing only an abstract audio waveform with no text, an audience of blurred shapes in the dark foreground, stage lighting. A headset microphone at his cheek. His LEFT hand rests on the lectern. His RIGHT hand is relaxed at his side. He looks slightly out toward the audience, confident, mouth closed. Slight three-quarter angle.",
  beats=[(0.0, 0.6, "He looks out at the audience, confident, mouth closed and still."),
         (0.7, 3.3, "He says one line to the audience, clear and easy, a small open-palm gesture of his RIGHT hand at the middle of the line, lips matching, then the mouth closes with a half-smile."),
         (3.3, 4.0, "He holds the half-smile, mouth closed and still."),
         (4.0, 15.0, "He stays calm and nearly still. (Not used in the edit.)")],
  dia=[("K", "तीन सेकंड की आवाज़ काफ़ी होती है।", "Teen second ki aawaaz kaafi hoti hai.", "Three seconds of voice is enough.", 0.7, 3.3, "GROK")],
  phone=[],
  hand="LEFT hand: rests on the lectern. RIGHT hand: one small open-palm gesture, then back to his side. Nothing held.",
  cam="Medium close-up, slight three-quarter, eye level, locked-off.",
  phys="Stage light and the screen glow are steady; the headset mic stays at his cheek.",
  aud="Only Kabir's one line is spoken, as if recorded on a stage mic. Faint hall reverb. No applause.",
  post="This is the 'recorded talk' on Riya's laptop. Treat it as footage: desaturate by about 15 percent, slight vignette, subtle softening. AUDIO: keep Grok's own spoken audio (he lip-syncs it), laptop-speaker filter (band-limited 200 Hz-6 kHz). Pitch-match this voice to Kabir's other lines (S2, VS-1, VS-3): choose the VS-1 and VS-3 takes closest to this timbre, then shift +/-2 semitones if needed. Generate this one early; it is the reference for the cloned voice."),

 dict(id="S6", name="The run (rear tracking)", edit=(47.5, 52.0), keep=(2.0, 6.5), gen=15, loc="BLR", chars=["K"], rear=True,
  refs="CANON-K (for hair and jacket only), LOC-BLR (panel 3, the long aisle)",
  kf=f"Medium shot from directly behind KABIR RAO, who is running down a long aisle between desks in {BLR}, glass walls and strip lights ahead. The back of his head, his shoulders and his torso fill the frame. His RIGHT hand holds a phone against his right ear. His LEFT arm swings with his stride. His mid-grey bomber jacket flaps behind him. His face is never visible. Slightly low camera, behind him.",
  beats=[(0.0, 2.0, "He is already running: a firm, fast stride, jacket flapping, the camera tracking from directly behind at the same speed. (Not used in the edit.)"),
         (2.0, 6.5, "He keeps running at the same pace; the camera stays behind him. His head turns slightly left and right once as he passes desks. The phone stays at his right ear."),
         (6.5, 15.0, "He keeps running, receding slightly. (Not used in the edit.)")],
  dia=[],
  phone=[],
  hand="RIGHT hand: the phone at the right ear for the whole shot (never moves from the ear; no transition). LEFT arm: swings naturally with the stride. Nothing else is held. His face is never visible.",
  cam="REAR TRACKING shot: camera directly behind him, waist to head height, moving at the same speed as the runner, steady, slight handheld sway.",
  phys="Real running mechanics: heel-toe stride, arm swing opposite to the leg, jacket and hair trailing, weight shifting with each step.",
  aud="Nobody speaks in this clip. Footsteps and breath only.",
  post="No speech is generated; his mouth is not visible. VOICE: Kabir shouting 'मम्मी, मत भेजना!' ('Mummy, mat bhejna!') from VS-3 (clean, not phone-filtered; breathless) at edit 47.7-49.1 s. SFX: running footsteps on polished floor, jacket cloth, breath; ringback tone from the phone, faint, at 49.5-51.8 s; a chair spinning and hitting a desk at 47.0-47.4 s (before the shot). ROOM TONE: office bed. J-CUT into S7: the scam voice (L19) starts at 51.5 s over the last 0.5 s of the run."),

 dict(id="S7", name="BUTTON: the thumb", edit=(52.0, 56.5), keep=(0.0, 4.5), gen=15, loc="PUNE", chars=["S"], glasses="nose",
  refs="CANON-S, LOC-PUNE (panels 3 and 4)",
  kf=f"Medium close-up of SUSHMA sitting at the small wooden dining table in {PUNE}. A phone lies face-up on the table in front of her, screen toward her, seen only at the bottom edge of the frame from behind. Her RIGHT hand rests flat on the table beside it, her LEFT hand rests on the table edge. Her eyes are lowered to the phone, glistening, tears just starting. Mouth closed. Slight three-quarter angle.",
  beats=[(0.0, 2.4, "She listens to the phone. Mouth closed and still. Tears run slowly down her cheeks; her lower lip trembles very slightly. Eyes on the phone."),
         (2.4, 2.8, "She raises her eyes a few degrees, as if looking at something far away. Mouth closed."),
         (2.9, 3.9, "She whispers one line, barely audible, lips matching, then the mouth closes."),
         (3.9, 4.5, "She stares at the phone, tears falling, mouth closed and still."),
         (4.5, 15.0, "She holds still. (Not used in the edit.)")],
  dia=[("S", "कौन-सा कबीर?", "Kaun-sa Kabir?", "Which Kabir?", 2.9, 3.9, "GROK")],
  phone=[("मम्मी, मुझसे प्यार है तो भेजो!", "Mummy, mujhse pyaar hai toh bhejo!", -0.5, 1.9, "VS-2")],
  hand="BOTH hands rest on the table; she does not touch the phone in this shot. The phone lies flat, screen toward her. Glasses on her nose, untouched.",
  cam="Medium close-up, slight three-quarter, eye level, locked-off with a very slow push-in.",
  phys="Tears follow the contour of her cheek and fall; the phone lies still.",
  aud="Only Sushma's one whispered line is spoken. The phone is completely silent in this clip. Quiet room only.",
  post="PHONE VOICE (VS-2, phone-filtered) at edit 51.5-53.9 s (starts 0.5 s before the cut). ROOM TONE: dining bed -30 dB, which DROPS to silence at 56.5 s on the cut to INS-B. Then INS-B."),

 dict(id="INS-B", name="BUTTON insert: top-down thumb (the one allowed POV screen)", edit=(56.5, 60.0), keep=(0.0, 3.5), gen=15, loc="PUNE", chars=["S"], hands_only=True,
  refs="CANON-S (wrist and hand skin tone only), LOC-PUNE (panel 4)",
  kf=f"Top-down point-of-view close-up of the wooden dining table in {PUNE}. A phone lies flat on the table, its screen facing up toward the camera, a plain dark glass rectangle with no readable content. SUSHMA'S RIGHT hand, an older woman's hand with fine wrinkles, a thin gold bangle on the wrist and flour on the knuckles, hovers just above the lower part of the screen with the thumb extended. Her LEFT hand rests flat on the table edge. A faint dusting of flour on the table. Nothing else in frame; no face.",
  beats=[(0.0, 1.5, "Her right thumb hovers above the screen and trembles very slightly, a few millimetres of shake. Her left hand stays flat."),
         (1.5, 3.5, "The thumb drifts a little to one side, then back to the middle. It never touches the screen."),
         (3.5, 15.0, "The thumb hangs in the air, trembling. (Not used in the edit; the freeze happens in post.)")],
  dia=[],
  phone=[],
  hand="The phone lies flat and is not touched. RIGHT hand: only the thumb moves, hovering and trembling, never touching the glass. LEFT hand: flat on the table. This is the one deliberate screen-to-camera shot in the episode; the screen is plain dark glass and all content is added in post.",
  cam="Top-down POV, locked-off, slight push-in. No face visible.",
  phys="The thumb's tremor is small and real. The phone stays still on the table.",
  aud="Nobody speaks. Faint breath only.",
  post="OVERLAYS (on the plain dark screen and the frame): the screen shows two round green buttons, ACCEPT and PAY, drawn in post and tracked to the phone (the top-down shot is locked-off, so no tracking is needed). A call banner 'KABIR  इनकमिंग कॉल' at the top of the frame; the UPI card 'RAHUL VERMA  ₹40,000 / भेजें ₹40,000' in the lower third; caption 'कौन-सा कबीर?' centred at 58.0 s; 'EP 2 →' bottom right at 58.4 s. FREEZE: freeze the frame at edit 58.0 s through 59.5 s; CUT TO BLACK at 59.5 s to 60.0 s. AUDIO: a ringtone bed (a generic marimba-style ring, not a branded tone) from 56.5 s to 59.5 s; under it, a muffled loop of VS-2's begging voice, low-passed, at about -18 dB, 56.6-58.5 s; room tone gone from 56.5 s, silent after the cut to black."),
]

VS = [
 ("VS-1", "Cloned voice, session 1 (lines 1, 3, 6)", "Cloned (scam) voice, thin, panicked, crying", [
   (0.3, "मम्मी! मम्मी, मुझे बचा लो!", "Mummy! Mummy, mujhe bacha lo!"),
   (3.6, "एक्सीडेंट हो गया। पुलिस ने पकड़ लिया।", "Accident ho gaya. Police ne pakad liya."),
   (8.0, "चालीस हज़ार यूपीआई करो। अभी। किसी को मत बताना।", "Chaalis hazaar UPI karo. Abhi. Kisi ko mat batana.")]),
 ("VS-2", "Cloned voice, session 2 (line 19, three deliveries)", "Cloned (scam) voice, begging, sobbing", [
   (0.3, "मम्मी, मुझसे प्यार है तो भेजो!", "Mummy, mujhse pyaar hai toh bhejo!"),
   (5.2, "मम्मी, मुझसे प्यार है तो भेजो!", "Mummy, mujhse pyaar hai toh bhejo!"),
   (10.2, "मम्मी, मुझसे प्यार है तो भेजो!", "Mummy, mujhse pyaar hai toh bhejo!")]),
 ("VS-3", "Kabir's real voice, session 3 (lines 11 and 18)", "Kabir's real voice, NOT crying", [
   (0.5, "मम्मी कभी तीन बार नहीं करतीं।", "Mummy kabhi teen baar nahin kartin."),
   (5.0, "मम्मी, मत भेजना!", "Mummy, mat bhejna!"),
   (9.5, "मम्मी, मत भेजना!", "Mummy, mat bhejna!")]),
]


def vs_prompt(tag, title, kind, lines):
    dl = "\n".join(f'{i + 1}. at about {at:.1f} s: "{hi}" (pronounced: {ro})' for i, (at, hi, ro) in enumerate(lines))
    if tag == "VS-3":
        mood = ("He is NOT crying. Line 1 is muttered low and quietly to himself, shocked and flat. Lines 2 and 3 are shouted while running, out of breath, urgent, a hard exhale after each word group "
                "(line 3 is a second delivery with a little more fear)")
    elif tag == "VS-2":
        mood = ("He is crying and begging, his voice cracking, a ragged sob between the deliveries. Delivery 1 is desperate and shaky, delivery 2 is quieter and broken, delivery 3 is pleading through tears")
    else:
        mood = "He is crying and panicked, out of breath, his voice cracking, a short ragged sob between lines"
    return (f"Animate the start image as ONE continuous 15-second shot, no cuts. Medium close-up of KABIR RAO, an Indian man, 32, oval face, thick tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, sitting in the dark driver's seat of a parked car at night, his face lit only by a phone held close to his mouth. "
            f"He speaks the lines below, one after another, in natural conversational Hindi. {mood}. "
            f"VOICE: his deep, low CHEST voice, a grown man's baritone with weight in the chest, steady in pitch around the low range of a man's speaking voice. NOT high-pitched, NOT falsetto, NOT thin, NOT a boy's voice, NOT a whisper. It may crack and shake, but it always comes back down to the low chest register. "
            f"Lips match every word exactly. Between lines his mouth stays closed and still. Nobody else speaks. No music, no text, no ambience.\n\n"
            f"DIALOGUE (each line fully and clearly inside its time window, with at least 1.5 seconds of silence between lines):\n{dl}\n\n"
            f"STYLE: {STYLE_VIDEO}\n\nDURATION: 15 seconds, 9:16, 480p.")


def keyframe(s):
    ch = s["chars"][0]
    if s.get("hands_only"):
        return f"{s['kf']} The hand is Sushma's: {FACE['S']} {RULES_KF} {NOSCREEN} {STYLE_STILL}"
    ward = WARD[s.get("ward", ch)]
    parts = [s["kf"], FACE[ch], ward]
    if s.get("glasses"):
        parts.append(GLASSES[s["glasses"]])
    parts.append("The face is never visible in this shot." if s.get("rear") else LOCK_RULE)
    parts += [RULES_KF, NOSCREEN, STYLE_STILL]
    return " ".join(parts)


def animate(s):
    ch = s["chars"][0]
    beats = "\n".join(f"- {a:.1f} to {b:.1f} s: {t}" for a, b, t in s["beats"])
    dia = [d for d in s["dia"]]
    dl = "\n".join(f'{i + 1}. {({"S": "SUSHMA", "K": "KABIR", "R": "RIYA"}[w])} at {a:.1f} to {b:.1f} s: "{hi}" (pronounced: {ro})' for i, (w, hi, ro, en, a, b, src) in enumerate(dia)) or "none (nobody speaks in this clip)"
    lines = []
    lines.append(f"Animate the supplied start image as ONE continuous 15-second shot, no cuts. Keep the person, the place, the clothes, the glasses and the light EXACTLY as in the start image; do not change the face at any point.")
    if s.get("hands_only"):
        lines.append(f"PERSON: only Sushma's right hand and left hand are visible. {FACE['S']}")
    else:
        lines.append(f"PERSON: {FACE[ch]} {WARD[s.get('ward', ch)]}" + (f" {GLASSES[s['glasses']]}" if s.get("glasses") else ""))
    lines.append(f"TIMED BEATS (the whole 15 seconds):\n{beats}")
    lines.append(f"HANDLING BUDGET: {s['hand']}")
    lines.append(f"CAMERA: {s['cam']}")
    lines.append(f"PHYSICS: {s['phys']}")
    lines.append(RULES)
    if dia:
        who = sorted({d[0] for d in dia})
        lines.append("LIP SYNC: " + SILENT + " Only the person speaking moves their lips, only inside the time windows listed under DIALOGUE, and every word matches their lips exactly. Outside those windows the mouth does not move at all: no mouthing, no muttering, no smiling with the lips parted.")
        lines.append("VOICE: " + " ".join(VOICE[w] for w in who))
    else:
        lines.append("LIP SYNC: nobody speaks. " + SILENT + " (The mouth never moves.)")
    lines.append(f"DIALOGUE in natural conversational Hindi, in this order, no overlap:\n{dl}\nEach line must be clearly audible.")
    lines.append(f"AUDIO: {s['aud']}")
    lines.append(f"STYLE: {STYLE_VIDEO}")
    lines.append("DURATION: 15 seconds, 9:16, 480p. Large faces and hands, simple background, no tiny details.")
    return "\n\n".join(lines)


def fmt_t(x):
    return f"{x:.1f}"


def edit_time(s, clip_t):
    return s["edit"][0] + (clip_t - s["keep"][0])


def main():
    o = []
    w = o.append
    w("# AWAAZ Episode 1, v2 rebuild: 15-second clips at 480p\n")
    w("Rebuild approved under `11-audit-ep01-final.md` and all ten of its rules, plus the standing realism, physics and subtle-acting rules. "
      "The old 12-clip plan (`04-ep01-clip-prompts.md`) is retired. The story, the 60-second length and the lines are the same, trimmed to the lines that earn their place.\n")
    w("## What changed and why\n")
    w("| Audit finding | Rule applied here |\n|---|---|\n"
      "| Mouths moved with no line (3.0-4.75 s, 36.0 s) | Every ANIMATE prompt says `MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE`, with timed speaking windows. Every line sits mid-shot. |\n"
      "| Early or late lips (0.4 s) | Windows are planned, then checked at 4 fps against the audio (see `00-review-checklist.md`, item 9). |\n"
      "| Phone voice over a moving mouth (50.2-52.2 s) | The phone voice is only placed while the listener's mouth is closed. It is never generated in the shot. |\n"
      "| Mouth covered during a line (44.25 s) | No line is spoken with a hand on the mouth. The old line 17 is dropped. |\n"
      "| Three different Kabirs, a necklace | One canonical face frame per character, an identical face-lock block in every prompt, medium close-up only, 'no necklace' in every Sushma prompt. |\n"
      "| Handling failures | A handling budget per shot: one object per hand, no ear-to-hand transitions, screens toward the actor, glasses never moved. |\n"
      "| Walk instead of run | The run is a rear tracking shot. His face is never needed. |\n"
      "| Silent stage cutaway | The stage cutaway is its own shot with its own spoken audio (INS-A). |\n"
      "| Metronomic 5 s cuts | Shots run 4.5-12 s with planned J and L audio overlaps. |\n")
    w("## The plan: 60 seconds in 7 shots (plus 2 short inserts)\n")
    w("Format: Grok Imagine, 15-second clips, 480p, 9:16. Generate every shot at 15 s; the beats are spread over the whole 15 s; the edit uses only the KEEP window and the rest is a safe hold. Upscale to 1080x1920 in post (Lanczos, light sharpening, film grain).\n")
    w("| Shot | Edit time | Length | Place | Speaker (visible mouth) | Lines | KEEP from the 15 s clip |\n|---|---|---|---|---|---|---|")
    rows = [("S1", "0.0-12.0", "12.0", "Pune kitchen", "Sushma", "2 own + 2 phone", "0.0-12.0"),
            ("S2", "12.0-19.0", "7.0", "Bengaluru desk", "Kabir", "1", "1.0-8.0"),
            ("S3", "19.0-29.0", "10.0", "Pune table", "Sushma", "2 own + 1 phone", "1.0-11.0"),
            ("S4", "29.0-39.0", "10.0", "Bengaluru desk", "Riya", "2 own + 1 off-screen Kabir", "1.0-11.0"),
            ("S5", "39.0-47.5", "8.5 (4.5 + INS-A 4.0)", "Bengaluru desk", "none (reaction)", "stage audio plays", "0.0-1.5 and 4.5-7.5"),
            ("INS-A", "40.5-44.5", "4.0", "Conference stage", "Kabir (recorded)", "1", "0.0-4.0"),
            ("S6", "47.5-52.0", "4.5", "Aisle, rear tracking", "none (rear view)", "1 dubbed shout", "2.0-6.5"),
            ("S7", "52.0-56.5", "4.5", "Pune table", "Sushma", "1 own + 1 phone", "0.0-4.5"),
            ("INS-B", "56.5-60.0", "3.5", "Top-down thumb", "none", "ringtone + muffled voice", "0.0-3.5")]
    for r in rows:
        w("| " + " | ".join(r) + " |")
    w("\nSeven main shots (S1-S7); INS-A is cut inside S5 and INS-B closes S7. Total: 12.0 + 7.0 + 10.0 + 10.0 + 8.5 + 4.5 + 4.5 + 3.5 = 60.0 s. "
      "Generations: 9 video clips (S1-S7, INS-A, INS-B), 3 voice sessions, plus the keyframe stills and 3 canonical crops.\n")
    w("**Lines kept (15 of 20):** 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 15, 16, 18, 19, 20. **Dropped (5):** 9 ('Jaldi karo'), 12 and 13 (the 'two Kabirs' banner beat, now carried by the final insert), 14 ('busy ja raha hai', replaced by dial-and-busy SFX), 17 ('Meri apni aawaaz', dropped to avoid a covered-mouth line). "
      "**Moved:** line 16 ('Teen second ki aawaaz kaafi hoti hai') is now the recorded stage talk, spoken by Kabir himself, which is the story's irony.\n")
    w("### The edit at a glance (J and L overlaps)\n")
    w("| Edit time | Overlap | What |\n|---|---|---|\n"
      "| 11.5 s | J-cut S1 to S2 | Office room tone fades in under Sushma's last word. |\n"
      "| 12.0-12.6 s | L-cut | Kitchen fan hum continues over the first frames of S2. |\n"
      "| 18.7 s | J-cut S2 to S3 | The scam voice (line 6) starts 0.3 s before the cut, over Kabir's last frames. |\n"
      "| 28.7 s | J-cut S3 to S4 | Kabir's phone buzzing on a desk starts under the end of S3. |\n"
      "| 40.1 s | J-cut S5 to INS-A | The recorded talk starts through a laptop speaker over Kabir's face, 0.4 s before the stage picture. |\n"
      "| 47.0-47.4 s | J-cut S5 to S6 | Chair bang and footsteps begin before the run shot. |\n"
      "| 51.5 s | J-cut S6 to S7 | The scam voice (line 19) begins 0.5 s before the cut, over the run. |\n"
      "| 56.5 s | Hard cut S7 to INS-B | Room tone drops to nothing; ringtone and muffled voice take over. |\n")
    w("## Canonical faces and the face-lock method\n")
    w("1. Open the approved contact sheets `CS-SUSHMA`, `CS-KABIR`, `CS-RIYA`. Crop **row 1, column 1** (neutral, facing the camera) of each to a square head-and-shoulders image. Save as `CANON-S`, `CANON-K`, `CANON-R`. These three images are the only face references, ever.")
    w("2. Attach the matching `CANON-` file to **every** keyframe of that character, together with the location panel named in the shot. Paste the FACE LOCK block exactly as written; do not reword it between prompts.")
    w("3. Keep every shot a medium close-up (head to mid-chest), at most 30 degrees off straight-on. No wide shots of a face, no profile. The only exceptions are the rear run shot (face never visible) and the hands-only insert.")
    w("4. Accept a keyframe only if hair, jaw, glasses and (for Sushma) the absence of any necklace match `CANON-` side by side. Reject and regenerate otherwise. Do not animate a keyframe that is not an exact match.")
    w("5. The wardrobe lines are not part of the face lock; they differ only for the stage insert (INS-A), which is an older recorded talk.\n")
    w("**Jewellery note:** you asked for 'no necklace, no jewellery except the stated bangles and nose stud'. Sushma's canonical sheet also has small gold stud earrings, so the stated list in the block is bangles, nose stud and stud earrings. If you prefer none, delete 'and small gold stud earrings' in `FACE LOCK, SUSHMA RAO` and in `CS-SUSHMA`.\n")
    w("### FACE LOCK blocks (paste verbatim)\n")
    for k, n in (("S", "Sushma"), ("K", "Kabir"), ("R", "Riya")):
        w(f"**{n}**\n```\n{FACE[k]}\n```\n")
    w("**Wardrobe and glasses blocks**\n```\n" + "\n".join([WARD["S"], WARD["K"], WARD["K_STAGE"], WARD["R"], GLASSES["head"], GLASSES["nose"]]) + "\n```\n")
    w("**Sushma's glasses continuity:** on her head in S1, on her nose in S3, S7 and the insert. Nothing in any shot moves them; the switch happens between shots, off camera.\n")
    w("## Voice sessions for Kabir (15 s each)\n")
    w("Why: Grok gives a phone voice to the person on screen, or none, so the scam voice and Kabir's off-screen lines are made here and placed in post. Make them **before** the shots so the voice is fixed first, and make **INS-A** early: Kabir speaks in it on camera, so it is the reference timbre. "
      "Pick the VS take closest to INS-A's voice. Use the audio only; throw the picture away. Start image: the `CANON-K` crop. Video mode, 15 s, 9:16, 480p. The voice is a deep, low CHEST voice, never thin or high.\n")
    w("Post for the cloned voice (VS-1 and VS-2): band-limit to 300-3400 Hz, mild distortion and compression, slightly too smooth; no pitch shift unless the take is above a man's normal range, then lower it by up to 3 semitones. VS-3 is not phone-filtered.\n")
    for tag, title, kind, lines in VS:
        w(f"### {tag}: {title}\n")
        w("```\n" + vs_prompt(tag, title, kind, lines) + "\n```\n")
    w("## Method for every shot\n")
    w("1. Image mode: attach the listed references, paste the KEYFRAME prompt. Pass the side-by-side face check against `CANON-`.\n2. Video mode: start image = the approved keyframe, **15 s, 9:16, 480p**, paste the ANIMATE prompt.\n3. Send the clip back to me. I check it at 4 fps against the speech windows before you spend another generation.\n4. Order: `CANON` crops, VS-1, VS-2, VS-3, INS-A (reference voice), then S1 to S7 and INS-B.\n")
    for s in SHOTS:
        w(f"---\n\n## {s['id']}: {s['name']}\n")
        w(f"**Edit window:** {fmt_t(s['edit'][0])}-{fmt_t(s['edit'][1])} s ({fmt_t(s['edit'][1] - s['edit'][0])} s). **Generate:** {s['gen']} s, 9:16, 480p. **KEEP clip time:** {fmt_t(s['keep'][0])}-{fmt_t(s['keep'][1])} s.")
        w(f"**Attach for the keyframe:** {s['refs']}\n")
        w("### KEYFRAME (image mode)\n```\n" + keyframe(s) + "\n```\n")
        w("### ANIMATE (video mode, 15 s)\n```\n" + animate(s) + "\n```\n")
        w("**Handling budget:** " + s["hand"] + "\n")
        w("**Dialogue timings** (clip time, then edit time)\n")
        if not s["dia"] and not s["phone"]:
            w("- None in this clip.")
        for who_, hi, ro, en, a, b, src in s["dia"]:
            nm = {"S": "Sushma", "K": "Kabir", "R": "Riya"}[who_]
            w(f"- {nm} (Grok lip-sync, mouth open only here): clip {fmt_t(a)}-{fmt_t(b)} s, edit {fmt_t(edit_time(s, a))}-{fmt_t(edit_time(s, b))} s: {hi} / {ro} / {en}")
        for hi, ro, a, b, src in s["phone"]:
            w(f"- Phone voice from {src} (post; listener's mouth closed): clip {fmt_t(a)}-{fmt_t(b)} s, edit {fmt_t(edit_time(s, a))}-{fmt_t(edit_time(s, b))} s: {hi} / {ro}")
        if s["id"] == "S4":
            w("- Off-screen Kabir (VS-3, post; Riya's mouth closed): clip 4.9-6.6 s, edit 32.9-34.6 s: मम्मी कभी तीन बार नहीं करतीं। / Mummy kabhi teen baar nahin kartin.")
        if s["id"] == "S6":
            w("- Kabir shout (VS-3, post; face not visible): edit 47.7-49.1 s: मम्मी, मत भेजना! / Mummy, mat bhejna!")
        w("")
        w("**Post note (overlays, SFX, room tone, ringtone, J/L overlaps):** " + s["post"] + "\n")
    w("---\n\n## Pre-flight checks before you generate\n")
    w("- Every ANIMATE prompt contains the sentence `MOUTH CLOSED AND STILL EXCEPT WHILE SPEAKING THE LINE.`\n- Each phone-voice window (S1 1.5-3.8 and 6.3-9.0 s; S3 edit 18.7-22.6 s; S7 edit 51.5-53.9 s) falls in a stretch where the listener's mouth is closed.\n- No shot has two visible mouths. S4's Kabir reply is off-screen audio over Riya's closed mouth.\n- No shot moves an object between ear and hand, flips a phone, or turns a screen to the camera, except INS-B.\n- Accept a take only if it passes the lip-window check in `00-review-checklist.md` item 9.\n")
    w("## Hindi check\nThe lines are written by an AI and I cannot hear them. A native speaker should check the register before release. Disclosure: if you publish Grok-generated video and voices, apply the platform's synthetic-media label, and say so in the caption.\n")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "12-ep01-v2-clip-prompts.md")
    open(path, "w", encoding="utf-8").write("\n".join(o) + "\n")
    print("wrote", path, len(SHOTS), "shots")


if __name__ == "__main__":
    main()
