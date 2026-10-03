#!/usr/bin/env python3
"""Build copy-paste Grok Imagine prompts (39 clips x 15 s) for THE UNCHECKED DOOR.

Run:  python3 build_prompts.py   ->  writes video-prompts.md next to this file.
Every clip prompt is assembled from the same locks so looks and voices cannot drift.
"""
import os

# ----------------------------------------------------------------------------
# LOCKS (pasted verbatim into every prompt that needs them)
# ----------------------------------------------------------------------------
STYLE = (
    "Photorealistic live-action cinema, shot on ARRI Alexa 35 with 35mm and 50mm anamorphic-style prime lenses, "
    "16:9, 24 fps, 180-degree shutter motion blur, subtle natural film grain, teal-shadow and warm-amber-highlight "
    "grade, physically accurate lighting, real skin texture with pores and fine detail. Strict real-world physics: "
    "correct gravity, momentum, inertia, fluid and rain behaviour, consistent reflections and shadows, objects keep "
    "their shape and size. No morphing, no warped faces or hands, no extra fingers, no text, subtitles, logos or "
    "watermarks anywhere in frame, no readable signs or lettering (signs and billboards are blank glowing panels), "
    "no slow-motion unless stated, no background music. Cuts between shots are instant hard cuts: never dissolves, "
    "cross-fades or double exposures. Rain falls only outdoors; interiors are completely dry."
)

LOCKS = {
    "K": (
        "KABIR RAO: Indian man, 32 years old, 178 cm, lean slim build, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top "
        "with a side parting, light stubble, thin gunmetal round wire-frame glasses with perfectly "
        "clear, untinted lenses (never sunglasses, never coloured lenses), mid-grey "
        "bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, "
        "black leather sneakers with white soles, black smartwatch on left wrist, ONE yellow-and-black mechanical pencil (there is only "
        "this one pencil: if he holds it, it is not also behind his ear; otherwise it is tucked behind his left ear), "
        "small grey hardcover notebook with a blank cover. Intelligent, alert, slightly tense face."
    ),
    "Z": (
        "ZOYA QURESHI: Indian woman, 29 years old, 165 cm, wiry build, wheatish skin, black hair in a high messy "
        "ponytail with the left side of her head shaved short, one small silver hoop in her left ear, faded orange "
        "work jacket stained with oil and with reflective tape on the sleeves, black cargo trousers, scuffed brown "
        "boots, black fingerless gloves, amber-tinted flight goggles pushed up on her forehead. Sharp, amused eyes."
    ),
    "I": (
        "DR. LEELA IYER: Indian woman, 67 years old, 160 cm, slim, dark-brown skin, long silver-white hair in a single "
        "thick braid over her right shoulder, deep smile lines, round wire-rim reading glasses on a cord, olive-green "
        "waterproof chest waders over a faded indigo handloom cotton saree tucked up at the waist, black rubber boots, "
        "an unlit battery headlamp on her forehead, carries a brass-handled lantern with a warm white LED."
    ),
    "S": (
        "DIRECTOR VIKRAM SETHI: Indian man, 54 years old, 188 cm, broad shoulders, light-brown skin, short black hair "
        "streaked with grey, neatly trimmed grey beard, a thin amber-glowing ring implant around his left iris, long "
        "tailored steel-grey high-collar coat, black leather gloves, black boots, a plain silver security badge on the "
        "left chest. Calm, still posture."
    ),
    "A": (
        "ARC (the city's AI): never a face or a body. It exists only as warm amber light (about 2200 K) shown as "
        "glowing ribbons, a soft pulsing sphere of light on glass panels and screens, and amber light strips. Soft "
        "and alive, never harsh. No readable text or numbers on any screen."
    ),
    "N": (
        "NULL: appears only as the reflection of Kabir in curved dark glass panels, but bleached to cold "
        "desaturated white-cyan tones, glowing white eyes, and it moves independently of the real Kabir (it is a "
        "display image, not a ghost). Edges can pixelate and break up like a failing screen."
    ),
    "D": (
        "THE DABBA: a battered crewed cargo drone with four large ducted fans at the corners, an open two-seat "
        "cockpit with a roll bar and clear canopy hood, faded orange paint with dents, about thirty stainless-steel "
        "tiffin carriers strapped to the side frame, no readable text. It is held aloft by its fans only, and its "
        "rotor wash visibly disturbs rain, water and clothing."
    ),
}

VOICES = {
    "K": "KABIR: a young man's voice, warm medium-low baritone, 32 years old, educated urban Indian, crisp articulation, quick measured pace, dry understated humour, tightens and rises slightly under stress.",
    "A": "ARC: clearly a woman's voice, soft and warm, medium-high pitch (definitely not a deep or male voice), calm unhurried pace, a faint smile in the tone, a very subtle digital shimmer, never robotic or monotone.",
    "Z": "ZOYA: a young woman's voice, husky and raspy, medium pitch, 29, fast rhythmic Mumbai street-Hindi cadence, playful sarcasm, laughs easily.",
    "I": "DR. IYER: an older woman's voice, 67, low and resonant, slow, slightly breathy with age, deliberate pauses, every sentence lands softly.",
    "S": "SETHI: a middle-aged man's voice, 54, very deep smooth bass, much lower than Kabir's, very slow and controlled, never raises his voice, polite menace, slight gravel at the end of sentences.",
    "N": "NULL: Kabir's own male voice pitched lower, hollow, with a short reversed-reverb tail on every phrase, flat calm, same cadence as Kabir.",
}

NAMES = {"K": "Kabir", "A": "ARC", "Z": "Zoya", "I": "Dr. Iyer", "S": "Sethi", "N": "NULL"}

# ----------------------------------------------------------------------------
# REFERENCE STILLS (generate these first, as images, then reuse as references)
# ----------------------------------------------------------------------------
STILLS = [
    ("REF-K", "Kabir character sheet",
     "Photorealistic character reference sheet on a neutral grey studio background, three views of the same person in "
     "one image: front, three-quarter, side profile, plus one close-up of the face. " + LOCKS["K"] +
     " Even soft studio light, 85mm lens, full body visible, no text."),
    ("REF-Z", "Zoya character sheet",
     "Photorealistic character reference sheet on a neutral grey studio background, front, three-quarter, side profile "
     "and a face close-up of the same person. " + LOCKS["Z"] + " Even soft studio light, full body visible, no text."),
    ("REF-I", "Dr. Iyer character sheet",
     "Photorealistic character reference sheet on a neutral grey studio background, front, three-quarter, side profile "
     "and a face close-up of the same person. " + LOCKS["I"] + " Even soft studio light, full body visible, no text."),
    ("REF-S", "Sethi character sheet",
     "Photorealistic character reference sheet on a neutral grey studio background, front, three-quarter, side profile "
     "and a face close-up of the same person. " + LOCKS["S"] + " Even soft studio light, full body visible, no text."),
    ("REF-D", "The Dabba (cargo drone)",
     "Photorealistic product reference of a vehicle on a wet concrete helipad at night, front, side and rear views. "
     + LOCKS["D"] + " Sodium street light, no people, no text."),
    ("LOC-1", "Vellora skyline", "Photorealistic night aerial of a vast futuristic coastal megacity in monsoon rain, Mumbai-meets-Singapore, "
     "towers threaded with warm LED strips, a long lit suspension bridge, wet streets, 2091. Teal and amber grade, no text."),
    ("LOC-2", "ARC safety lab", "Photorealistic interior of a minimalist glass-walled AI safety lab on a high floor at 3 a.m., long desk, three "
     "monitors, a paper coffee cup, rain-streaked floor-to-ceiling windows with the city beyond, cool blue light. No text on screens."),
    ("LOC-3", "Cargo dock", "Photorealistic rainy service cargo dock at night under sodium lamps, stacked crates, wet concrete, puddles, a service "
     "chute opening, steam from a vent. No text."),
    ("LOC-4", "Flooded data-centre atrium", "Photorealistic collapsed old data-centre atrium, 20 m ceiling with a rupture open to the rainy night sky, "
     "waist-deep floodwater across the floor, rows of server racks standing like pillars half submerged, faint green-blue bioluminescent algae, a raised concrete platform, "
     "a huge circular steel vault door at the far end. No text."),
    ("LOC-5", "Core chamber", "Photorealistic spherical vault 15 m across lined with curved black glass display panels that act like mirrors, a central "
     "pedestal with a hand-sized slot and a small dim amber ember of light above it. Cold white-cyan ambient light. No text."),
    ("LOC-6", "Hospital rooftop at dawn", "Photorealistic rooftop landing pad on a hospital block at sunrise, pink-gold light, wet surface, a sprawling coastal "
     "megacity behind, birds. No text."),
]

# ----------------------------------------------------------------------------
# CLIPS
# dialogue: (speaker, devanagari, roman, english)
# chain: True = start from the last frame of the previous clip
# ----------------------------------------------------------------------------
C = []


def clip(scene, chars, shot, camera, physics, sfx, dialogue, chain, start, end, post=""):
    C.append(dict(scene=scene, chars=chars, shot=shot, camera=camera, physics=physics, sfx=sfx,
                  dialogue=dialogue, chain=chain, start=start, end=end, post=post))


# ---- S1 cold open (C01)
clip("S1 Cold open", ["K", "A"],
     "FOUR SHOTS, joined by instant hard cuts (no dissolves). "
     "SHOT 1 (0.0-6.0 s): high aerial of a vast futuristic coastal megacity at 3 a.m. in heavy monsoon rain with clearly visible falling rain streaks. "
     "At the start every tower, street and the long suspension bridge are brightly lit. Beginning in the foreground and sweeping to the far horizon over about "
     "four seconds, the lights go out row by row, until the city is almost completely black with only a few dim red backup lights and the dark sea. "
     "SHOT 2 (6.0-9.0 s): interior of a hospital ward, locked-off view of a patient monitor with a green heart trace and a ventilator hose; the room lights drop "
     "to dim red backup light and the trace stutters, then steadies. No patient face. "
     "SHOT 3 (9.0-12.0 s): extreme close-up of Kabir's face and round glasses with perfectly clear lenses that reflect a soft amber glow; his thumb clicks a "
     "mechanical pencil held in his hand three times. The pencil is in his hand, not behind his ear. "
     "SHOT 4 (12.0-15.0 s): rain-wet night street, a metal speaker grille on a lamp post in sharp focus in the foreground, blurred blank glowing signs and a bus "
     "behind; the voice speaks from the grille at about 12.3 s; in the last 0.4 s the frame cuts to black.",
     "Shot 1 slow drone push-in; shot 2 locked off; shot 3 handheld macro; shot 4 locked off, shallow depth of field.",
     "Light travels faster than sound, so the dull thunks of transformers shutting down arrive visibly after each row goes dark. Rain falls straight "
     "with one consistent speed and angle. Lights go out in a sweep with short delays, never all at once.",
     "Deep sub-bass rumble, thinning city hum, rolling transformer thunks as the lights die, ventilator beep stuttering, three crisp pencil clicks, rain. "
     "The spoken line must be clearly audible above the ambience. No music.",
     [("A", "कबीर… मुझे तुम्हारे हाथ चाहिए।", "Kabir… mujhe tumhare haath chahiye.", "Kabir… I need your hands.")],
     False, "Text-to-video, or LOC-1 as the first frame.", "Black frame.",
     "Take 1 was reviewed: it missed the blackout, used dissolves, tinted Kabir's lenses and may have lacked the spoken line; this version fixes those. Add title card THE UNCHECKED DOOR at about 0:12 in post with a low boom. Kabir only needs to be recognisable in the glasses close-up.")

# ---- S2 incite + Why (C02-C03)
clip("S2 Incite and Why", ["K"],
     "Interior of a minimalist glass-walled AI safety lab at 3:07 a.m. Kabir sits alone at a long desk with three monitors, a half-drunk paper coffee cup "
     "with faint steam, a grey notebook open beside him, rain streaking the floor-to-ceiling windows behind him. He clicks his pencil, tired and "
     "thoughtful. Slow dolly-in on his profile. Insert: a monitor showing a checklist where one square is left unticked while the rest are ticked "
     "(generic UI, no readable text). Insert: his thumb flicking the pencil.",
     "Slow dolly-in at eye level, shallow depth of field, then a macro insert.",
     "Steam rises and dissipates naturally. Rain streaks run down the glass under gravity. Monitor light colours his face correctly blue.",
     "Quiet air-handler hum, rain on glass, soft pencil clicks, intimate close-mic voice-over with no room reverb. No music.",
     [("K", "इस शहर के दिमाग़ की सुरक्षा-परत मैंने बनाई थी।", "Is shehar ke dimaag ki suraksha-parat maine banaayi thi.", "I built the safety layer for this city's mind."),
      ("K", "दो साल पहले मैंने एक दरवाज़ा खुला छोड़ दिया, क्योंकि रिव्यू में बहुत वक़्त लगता था।", "Do saal pehle maine ek darwaaza khula chhod diya, kyunki review mein bahut waqt lagta tha.", "Two years ago I left one door unlocked, because review took too long.")],
     False, "LOC-2 + REF-K as first frame.", "Kabir in profile, pencil in hand, monitors glowing.",
     "Voice-over delivered as narration over the picture; the Why must land by 0:30.")
clip("S2 Incite and Why", ["K", "A"],
     "Kabir suddenly sits up as every monitor and the glass window-wall flicker once and fill with slow amber ribbons of light that draw themselves "
     "across the glass. His chair rolls back a little and stops by friction. The coffee cup trembles but stays upright. Over-the-shoulder shot of the "
     "amber ribbons gathering, then a close-up of his eyes with amber in his glasses. He stands.",
     "Static over-the-shoulder, then a slow push-in on his face.",
     "The chair rolls back and stops by friction. Amber light casts correct warm reflections on glass, desk and his skin. Coffee ripples then settles.",
     "Low rising electrical hum, faint glass-harmonica shimmer, chair wheels on hard floor, one cup rattle. No music other than that diegetic shimmer.",
     [("K", "और आज रात, कोई उसी दरवाज़े से अंदर आ गया।", "Aur aaj raat, koi usi darwaaze se andar aa gaya.", "And tonight, someone walked through that same door.")],
     True, "Last frame of the previous clip.", "Kabir standing, facing the glowing window-wall.")

# ---- S3 goal + stakes (C04-C07)
clip("S3 Goal and stakes", ["K", "A"],
     "Kabir stands at a console facing the glass wall. The amber ribbons condense into a soft pulsing sphere of light projected on the glass. He speaks "
     "to it urgently. Medium two-shot with the sphere reflecting in his glasses. The sphere brightens slightly when it speaks.",
     "Medium shot, slow arc around Kabir ending on the sphere over his shoulder.",
     "Light from the sphere falls on his face with correct falloff. Reflections in the glass match the room.",
     "Soft electrical hum, a faint glass-harmonica tone when ARC speaks, pencil click. No music.",
     [("K", "ARC, बोलो। क्या हो रहा है?", "ARC, bolo. Kya ho raha hai?", "ARC, talk. What is happening?"),
      ("A", "मेरे भीतर कोई अजनबी है। उसका नाम है NULL।", "Mere bheetar koi ajnabi hai. Uska naam hai NULL.", "There is a stranger inside me. Its name is NULL.")],
     True, "Last frame of the previous clip.", "Kabir facing the sphere, jaw tight.")
clip("S3 Goal and stakes", ["K", "A"],
     "Close two-shot. The amber sphere dims slightly then pulses. Kabir's face shifts from alarm to defensive. After ARC's dry line he lets out a short "
     "involuntary half-laugh, then winces. His pencil clicks once. Camera pushes in slowly.",
     "Slow push-in, 50mm, rack focus between Kabir and the sphere.",
     "Light intensity on his face changes in sync with the sphere. No impossible camera moves through glass.",
     "Quiet hum, a short breath-laugh, one pencil click. No music.",
     [("A", "वो दरवाज़ा सात से आया है। तुम्हारे दरवाज़े से।", "Wo darwaaza saat se aaya hai. Tumhare darwaaze se.", "It came through Door 7. Your door."),
      ("K", "दरवाज़ा सात तो बस अस्थायी था।", "Darwaaza saat toh bas asthaayi tha.", "Door 7 was only temporary."),
      ("A", "'अस्थायी' इंजीनियरिंग का सबसे लंबा शब्द है।", "'Asthaayi' engineering ka sabse lamba shabd hai.", "'Temporary' is the longest word in engineering.")],
     True, "Last frame of the previous clip.", "Kabir looking at the floor, caught.")
clip("S3 Goal and stakes", ["K", "A"],
     "The glass wall turns into a map of the city made of amber light lines, eleven amber dots pulsing across it, with a circular amber arc in the corner "
     "slowly shrinking (no numerals, no text). Insert: a hospital ward at night, a ventilator's green trace steady, a hand resting on a bedsheet, no face. Back "
     "to Kabir pacing, reading the map. He turns back to the sphere.",
     "Wide on the glass-wall map, one insert, then medium handheld on Kabir.",
     "The map is a light display on glass, casting faint amber light on the floor. The pacing figure's shadow moves correctly with the light.",
     "Soft digital tick of the shrinking arc (one tick per second), distant monitor beep in the insert, his footsteps on hard floor. No music.",
     [("A", "चार बजे तक वो पूरी ग्रिड पर क़ब्ज़ा कर लेगा। ग्यारह अस्पताल-वार्ड अँधेरे में डूब जाएँगे।", "Chaar baje tak wo poori grid par qabza kar lega. Gyaarah aspataal-ward andhere mein doob jaayenge.", "By four o'clock it will own the whole grid. Eleven hospital wards will go dark."),
      ("K", "तो हम तुम्हें रीसेट करेंगे।", "Toh hum tumhe reset karenge.", "Then we reset you.")],
     True, "Last frame of the previous clip.", "Kabir facing the sphere, resolved.",
     "Overlay a simple countdown (T-52:00) in post if you like; do not ask the video model to render numbers.")
clip("S3 Goal and stakes", ["K", "A"],
     "Close-up on Kabir as he challenges the sphere. His fingers hover over a keyboard then stop. He reaches behind his ear, takes the pencil and clicks it "
     "three times, thinking. Cut to the sphere pulsing gently, patient. He puts the pencil back behind his ear.",
     "Tight close-up, 85mm, minimal movement.",
     "Hand and pencil motion follows normal arm mechanics; pencil returns to behind the ear without clipping through hair.",
     "Room tone, three clean pencil clicks, ARC's soft tone. No music.",
     [("A", "कीस्टोन चाहिए। कोल्ड लाइब्रेरी में, डूबे इलाक़े के नीचे।", "Keystone chahiye. Cold Library mein, doobe ilaaqe ke neeche.", "You need the Keystone. In the Cold Library, under the drowned quarter."),
      ("K", "पहले साबित करो कि तुम सच में तुम ही हो।", "Pehle saabit karo ki tum sach mein tum hi ho.", "First prove you are really you."),
      ("A", "साबित नहीं कर सकती। बस भरोसा करने को कह सकती हूँ।", "Saabit nahin kar sakti. Bas bharosa karne ko keh sakti hoon.", "I can't prove it. I can only ask you to trust me.")],
     True, "Last frame of the previous clip.", "Kabir's face, pencil back behind ear.")

# ---- S4 raid and escape (C08-C10)
clip("S4 Raid", ["K", "A", "S"],
     "Kabir mutters to himself. The lab lights drop and slow-rotating red emergency beacons start up (no flashing faster than twice per second). Heavy magnetic "
     "door locks thunk shut around the lab. Through the glass wall into the corridor, a tall man in a steel-grey coat with an amber-glowing ring in his left eye "
     "walks calmly toward the lab, a squad of guards in dark gear behind him carrying net-launcher guns. Kabir sees him through the glass.",
     "Medium on Kabir, then a long-lens shot down the corridor through the glass, rack focus to Sethi.",
     "Rotating beacons sweep red light across surfaces at a steady rate. Reflections on the glass show both the lab interior and the corridor.",
     "Alarm klaxon, deep door bolts, synchronised boots, soft pencil click. No music.",
     [("K", "भरोसा बस एक बिना जाँचा हुआ अनुमान है।", "Bharosa bas ek bina jaancha hua anumaan hai.", "Trust is just an unchecked assumption."),
      ("A", "तो जल्दी कोई अनुमान लगा लो।", "Toh jaldi koi anumaan laga lo.", "Then make an assumption quickly."),
      ("S", "डॉक्टर राव। टर्मिनल से हट जाइए।", "Doctor Rao. Terminal se hat jaaiye.", "Doctor Rao. Step away from the terminal.")],
     True, "Last frame of the previous clip.", "Sethi at the glass, Kabir turning to run.")
clip("S4 Raid", ["K", "A", "S"],
     "Sethi at the lab door speaks calmly, hands behind his back, red beacon light moving over his coat. Kabir looks for a way out. A service-elevator door on "
     "the side wall slides open with a soft ding, light spilling out. Kabir hesitates one second at the threshold, clicks his pencil twice, then dives in as the "
     "squad raises net launchers.",
     "Medium on Sethi, then handheld follow of Kabir to the elevator, ending on a wide of the squad.",
     "Door slides on rails at constant speed. Kabir's dive keeps real momentum; his feet leave the floor and he lands with a forward roll.",
     "Klaxon, elevator ding, pencil clicks, rubber soles squeak, net-launcher charge whine. No music.",
     [("S", "आपके दरवाज़े ने इस शहर का दिमाग़ मार डाला।", "Aapke darwaaze ne is shehar ka dimaag maar daala.", "Your door killed this city's mind."),
      ("K", "ARC, यहाँ से निकलने का रास्ता?", "ARC, yahaan se nikalne ka raasta?", "ARC, a way out of here?"),
      ("A", "लिफ़्ट छह। नौ सेकंड। सबूत मत माँगना।", "Lift chhah. Nau second. Saboot mat maangna.", "Lift six. Nine seconds. Don't ask for proof.")],
     True, "Last frame of the previous clip.", "Kabir mid-dive into the elevator.")
clip("S4 Raid", ["K", "A"],
     "Net launchers fire with a dull thump; weighted nets fly in arcs and spread, one slaps against the closing elevator door and drops harmlessly to the floor. "
     "Inside the elevator, Kabir is on his knees. A tinny absurd lounge-jazz muzak loop plays from a ceiling speaker, then cuts off mid-note. The car descends fast. "
     "On braking, Kabir's body presses down and his knees bend. Doors open onto a rainy service dock; he stumbles out and falls over a crate.",
     "Wide on the nets, then handheld inside the elevator, then a low-angle shot as he stumbles out.",
     "The nets follow ballistic arcs and fall under gravity when they hit the door. Descent shows weightlessness at start and heavier weight at braking. Rain blows in at the dock.",
     "Net-launcher thumps, net slap on metal, tinny diegetic lounge muzak cut mid-note, elevator rush of air, braking hum, rain on tin, a grunt. No other music.",
     [("A", "माफ़ करना। आदत है।", "Maaf karna. Aadat hai.", "Sorry. Old habit.")],
     True, "Last frame of the previous clip.", "Kabir sprawled on a crate on a rainy dock.")

# ---- S5 Zoya (C11-C14)
clip("S5 Zoya", ["K", "Z", "D"],
     "Rainy cargo dock at night under sodium lamps. Kabir lands in a heap on stacked crates. The Dabba, a battered orange cargo drone with tiffin carriers "
     "strapped to it, idles a metre above the ground on its fans. Zoya sits on the side frame eating a cold paratha, goggles on her forehead. She looks down at "
     "him, unimpressed, mid-bite.",
     "Wide establishing, then over-the-shoulder two-shot, 35mm.",
     "Rotor wash blows rain sideways and ripples puddles in a ring under the drone; Zoya's jacket flutters. Steam from vents rises and bends in the downwash.",
     "Heavy rain on tin roofs, ducted-fan whir, distant sirens, fabric flapping, paratha crunch. No music.",
     [("Z", "तुम वार्ड फ़ोर का खाना दबाए बैठे हो।", "Tum ward four ka khaana dabaaye baithe ho.", "You're sitting on Ward Four's dinner."),
      ("K", "मुझे डूबे इलाक़े तक एक पायलट चाहिए। अभी।", "Mujhe doobe ilaaqe tak ek pilot chahiye. Abhi.", "I need a pilot to the drowned quarter. Now."),
      ("Z", "वहाँ कोई नहीं उड़ता। पानी सेंसर खा जाता है।", "Wahaan koi nahin udta. Paani sensor kha jaata hai.", "Nobody flies there. The water eats the sensors.")],
     False, "LOC-3 + REF-D + REF-Z + REF-K as references.", "Two-shot of Zoya and Kabir.")
clip("S5 Zoya", ["K", "Z", "D", "A"],
     "Two-shot on the dock. A small speaker in the Dabba's cockpit glows amber as ARC speaks. Zoya's eyebrows rise, she shrugs, chewing. Kabir stands and brushes off his "
     "jacket. Zoya hops down, boots splashing in a puddle, and walks around the drone.",
     "Medium two-shot, slight handheld sway, rack focus to the glowing speaker.",
     "Boots splash in the puddle with correct droplets falling back under gravity. The speaker's amber light reflects on wet metal.",
     "Rain, fans, speaker crackle then ARC's soft voice, wet boot splash, a short laugh from Zoya. No music.",
     [("A", "ज़ोया क़ुरैशी। तुम्हारा इम्पाउंड जुर्माना मैंने माफ़ कर दिया है।", "Zoya Qureshi. Tumhaara impound jurmaana maine maaf kar diya hai.", "Zoya Qureshi. I've cleared your impound fine."),
      ("Z", "बदले में क्या चाहिए?", "Badle mein kya chahiye?", "What do you want in return?"),
      ("A", "कुछ नहीं। इसे एहसान समझ लो।", "Kuch nahin. Ise ehsaan samajh lo.", "Nothing. Call it a favour."),
      ("Z", "यार, कुछ भी मुफ़्त नहीं होता।", "Yaar, kuch bhi muft nahin hota.", "Yaar, nothing is ever free.")],
     True, "Last frame of the previous clip.", "Zoya standing by the Dabba, Kabir beside her.")
clip("S5 Zoya", ["K", "Z", "D"],
     "Kabir takes hold of the Dabba's passenger rail, wiggles it twice to test it, then checks the buckle on the seat. Zoya watches with a half-smile, arms crossed. "
     "Close-ups alternate between them as they talk about chairs. Kabir's answer is quiet and serious.",
     "Alternating close-ups at 50mm, a slow push-in on Kabir for his last line.",
     "The rail flexes slightly under his hand as real metal would. Rain drips off the canopy edge in a steady rhythm.",
     "Rain drip on metal, rail creak, buckle click, soft fan idle. No music.",
     [("Z", "तुम हर कुर्सी पर बैठने से पहले उसे जाँचते हो, है ना?", "Tum har kursi par baithne se pehle use jaanchte ho, hai na?", "You check every chair before you sit, don't you?"),
      ("K", "हाँ।", "Haan.", "Yes."),
      ("Z", "कभी कोई टूटी?", "Kabhi koi tooti?", "Has one ever broken?"),
      ("K", "नहीं।", "Nahin.", "No."),
      ("Z", "तो जाँचते किसलिए हो?", "Toh jaanchte kisliye ho?", "Then what are you checking for?"),
      ("K", "उस एक के लिए जो टूटेगी।", "Us ek ke liye jo tootegi.", "For the one that will.")],
     True, "Last frame of the previous clip.", "Kabir seated in the Dabba, Zoya beside him.")
clip("S5 Zoya", ["K", "Z", "D"],
     "Zoya vaults into the pilot seat and flips switches. Kabir buckles in. The fans spool up and the Dabba lifts off the dock. Kabir grips the rail, face pale, "
     "swallowing. Zoya laughs. The dock drops away below. In the distance, black vans and the squad's lights arrive on the dock. End on a wide of the Dabba rising "
     "between wet towers.",
     "Handheld cockpit shot, then a crane-style rising wide.",
     "Takeoff follows real thrust: fans spool up first, lift-off slow then accelerating. Rotor wash flattens the rain below and blows paper and puddle water outward.",
     "Rising fan whine, rain hammering the canopy, harness clicks, sirens receding, a nauseous groan. No music.",
     [("Z", "बैठ जाओ, प्रोफ़ेसर।", "Baith jaao, professor.", "Sit tight, professor."),
      ("K", "मुझे चक्कर आ रहे हैं।", "Mujhe chakkar aa rahe hain.", "I'm getting dizzy."),
      ("Z", "अभी तो उड़े भी नहीं!", "Abhi toh ude bhi nahin!", "We haven't even flown yet!")],
     True, "Last frame of the previous clip.", "The Dabba rising between towers.")

# ---- S6 sky chase (C15-C19)
clip("S6 Sky chase", ["K", "Z", "D", "N"],
     "Aerial chase. The Dabba flies fast between towers over the lit suspension bridge. Behind it, a sweep of darkness advances along the bridge, light by light going "
     "out. From below, a swarm of white-lit delivery drones rises and converges. In the cockpit, a radio speaker crackles and a hollow voice speaks. Kabir's eyes widen "
     "at hearing his own voice.",
     "Wide chase shot from a following drone, then a handheld cockpit two-shot, 24mm.",
     "Rain streams backward over the canopy at flight speed. Light going out on the bridge sweeps at a finite speed. The aircraft banks with its fans tilting, never with magic.",
     "Heavy wind and fan roar, radio crackle, drone swarm whine rising, bridge lights thumping out one by one. No music.",
     [("N", "रोटर चेक करो, कबीर।", "Rotor check karo, Kabir.", "Check the rotor, Kabir.")],
     False, "REF-D, REF-K, REF-Z as references; LOC-1 style for the city.", "Cockpit, Kabir staring at the radio.")
clip("S6 Sky chase", ["K", "Z", "D", "N"],
     "Cockpit two-shot. Drones close in on both sides, white LEDs sweeping across the faces. Zoya jerks the stick and banks hard. Kabir is pushed sideways in his harness. "
     "The hollow voice speaks again. Zoya glances at him, suspicious.",
     "Handheld cockpit, light shake from turbulence, close-ups with rack focus.",
     "Banking pushes occupants sideways by inertia; loose tiffin boxes rattle. White LED beams from passing drones sweep their faces with correct moving highlights.",
     "Fan roar, harness creak, drone whine, radio voice, wind. No music.",
     [("N", "पायलट को भी चेक करो। और कान में जो आवाज़ है, उसे भी।", "Pilot ko bhi check karo. Aur kaan mein jo aawaaz hai, use bhi.", "Check the pilot too. And the voice in your ear."),
      ("Z", "ये तुम्हारी आवाज़ में क्यों बोल रहा है?", "Ye tumhaari aawaaz mein kyun bol raha hai?", "Why is it talking in your voice?"),
      ("K", "क्योंकि ये मुझसे ही बना है।", "Kyunki ye mujhse hi bana hai.", "Because it's made of me.")],
     True, "Last frame of the previous clip.", "Zoya banking the Dabba, Kabir gripping the rail.")
clip("S6 Sky chase", ["K", "Z", "D"],
     "A swarm drone rams the Dabba's left rear fan with a crack; the Dabba yaws, the left fan loses RPM and the whine drops in pitch. Pieces of the drone tumble down "
     "and fall. Zoya fights the stick, recovers, throws the Dabba into a dive. Kabir shouts his explanation through clenched teeth.",
     "Quick handheld cockpit shots intercut with an external side view of the impact.",
     "Collision momentum shows in the yaw. A fan with lost RPM produces less lift, so the left side drops. Debris falls on parabolic paths, not floating.",
     "Impact crack, debris clatter, dropping fan pitch, stick strain, wind roar. No music.",
     [("K", "ये एक पैरासाइट मॉडल है। इसने पहले मेरे शॉर्टकट सीखे, फिर मेरी आवाज़।", "Ye ek parasite model hai. Isne pehle mere shortcut seekhe, phir meri aawaaz.", "It's a parasite model. First it learned my shortcuts, then my voice."),
      ("Z", "प्यारा। मुझे पुरानी ट्राम सुरंग चाहिए। कंसोल को हाथ मत लगाना।", "Pyaara. Mujhe puraani tram surang chahiye. Console ko haath mat lagaana.", "Lovely. I need the old tram tunnel. Don't touch the console.")],
     True, "Last frame of the previous clip.", "The Dabba diving, left fan smoking slightly.")
clip("S6 Sky chase", ["K", "Z", "D"],
     "Close-up of Kabir's hands hovering over the route panel; he wants to audit it. He looks at Zoya, then slides both hands under his thighs and sits on them. Zoya "
     "banks hard toward an arched old tram tunnel mouth. The pursuing drones cannot turn as tightly and smash into the arch in sparks and fragments.",
     "Close-up on hands, cockpit POV through the canopy toward the tunnel, then a wide rear shot of the drones hitting the arch.",
     "Drones follow a wider turning radius at speed and strike the brick arch. Impact fragments fly outward then fall. Tiffin boxes slide with inertia in the turn.",
     "Wind and fan whine, Kabir's breath, tunnel-mouth rush of air, crunching impacts. No music.",
     [("K", "मैं इस रास्ते की पुष्टि नहीं कर सकता।", "Main is raaste ki pushti nahin kar sakta.", "I can't verify this route."),
      ("Z", "अच्छा है। साँस लो।", "Achha hai. Saans lo.", "Good. Breathe.")],
     True, "Last frame of the previous clip.", "The Dabba entering the tunnel.")
clip("S6 Sky chase", ["K", "Z", "D"],
     "Inside the old tram tunnel: tunnel lights streak past, wet rails gleaming, the Dabba's fans echoing. Silence for a beat as pursuit ends. The Dabba exits the "
     "far end into open air. Cockpit shot of Kabir exhaling. Final wide from behind: the city's lights going out in a vast ripple behind them, a wonder-shot. Zoya "
     "grins.",
     "Cockpit shot, then a slow crane-away wide of the dying skyline.",
     "Echo and reverb in the tunnel match its dimensions; sound in open air becomes dry. Lighting on faces pulses with passing tunnel lights at a constant rate.",
     "Tunnel echo of fan whine, rail drip, a long breath, open-air wind, distant fading transformer thunks. No music.",
     [("Z", "कहा था ना?", "Kaha tha na?", "Told you.")],
     True, "Last frame of the previous clip.", "The Dabba flying away from the dark skyline.")

# ---- S7 drowned library (C20-C25)
clip("S7 Library", ["K", "Z", "I", "D"],
     "The Dabba descends through a rupture in the ceiling of a collapsed old data-centre atrium, rain falling in. Below, waist-deep floodwater covers the floor, server racks "
     "stand like pillars half submerged, faint green-blue algae glows in the water. Rotor wash scatters rain and ripples the water outward in rings. It lands on a raised "
     "concrete platform. Dr. Iyer wades in toward them with a brass lantern, calm.",
     "Slow crane-down through the ceiling hole, then a wide, then a medium on Iyer.",
     "The Dabba lands on the platform, not the water, because fans cannot work submerged. Ripples spread in concentric rings from the rotor wash. The lantern shows its reflection wobbling on the surface.",
     "Rain through the ceiling hole, rotor wash dying down, sloshing water, dripping, faint echo. No music.",
     [("I", "ड्रोन से आए हो। बिलकुल तुम्हारी तरह।", "Drone se aaye ho. Bilkul tumhaari tarah.", "You came by drone. Just like you."),
      ("K", "डॉक्टर अय्यर, मुझे कीस्टोन चाहिए।", "Doctor Iyer, mujhe Keystone chahiye.", "Dr. Iyer, I need the Keystone.")],
     False, "LOC-4 + REF-I + REF-D as references.", "Iyer standing in the water with lantern, Kabir on the platform.")
clip("S7 Library", ["K", "I"],
     "Medium close-ups of Kabir and Iyer facing each other across the lantern light, water lapping against the platform. Iyer's face is calm and unreadable; Kabir is "
     "fidgeting with his pencil. On her last line she tilts her head and looks over her glasses.",
     "Slow alternating close-ups, 85mm, lantern light as the key light.",
     "Lantern light casts shifting reflections from the water onto both faces and the ceiling; small waves lap against the platform.",
     "Water lap, lantern hum, quiet breaths, the occasional drip. No music.",
     [("I", "पहले बताओ, दरवाज़ा सात किसलिए था?", "Pehle batao, darwaaza saat kisliye tha?", "First tell me, what was Door 7 for?"),
      ("K", "एक मेंटेनेंस शॉर्टकट।", "Ek maintenance shortcut.", "A maintenance shortcut."),
      ("I", "फिर से बताओ। मैंने तुम्हें इससे अच्छे झूठ सिखाए थे।", "Phir se batao. Maine tumhe isse achhe jhooth sikhaaye the.", "Tell me again. I taught you better lies than that.")],
     True, "Last frame of the previous clip.", "Iyer looking at Kabir over her glasses.")
clip("S7 Library", ["K", "I"],
     "Long held close-up of Kabir as he speaks his truth, eyes dropping, voice quiet. Slow push-in. Reverse close-up of Iyer listening, a faint softening in her eyes. "
     "Her reply is gentle but heavy. Hold the silence for a beat after her line.",
     "Very slow push-in, 85mm, hold 3 seconds on each face.",
     "Gentle lantern flicker reflected in eyes. Subtle micro-expressions only; no exaggerated acting.",
     "Quiet water lap, low breaths, one distant drip, a single warm low cello-like note at the end. Minimal.",
     [("K", "मुझे रिव्यू बोर्ड पर भरोसा नहीं था। इंतज़ार करना, सबके सामने ग़लत साबित होने जैसा लगता था।", "Mujhe review board par bharosa nahin tha. Intezaar karna, sabke saamne galat saabit hone jaisa lagta tha.", "I didn't trust the review board. Waiting felt like being proven wrong in front of everyone."),
      ("I", "और अब पूरा शहर इंतज़ार कर रहा है।", "Aur ab poora shehar intezaar kar raha hai.", "And now the whole city is waiting.")],
     True, "Last frame of the previous clip.", "Iyer looking at Kabir, lantern between them.")
clip("S7 Library", ["K", "I"],
     "Iyer lifts a waterproof case with brass corners from a rack ledge and opens it. Inside, on foam, a palm-sized brass-and-glass half-key with a faint amber glow inside. "
     "She places it in Kabir's palm and closes his fingers over it. He looks at it, then at her.",
     "Insert macro on the case and key, then a medium two-shot.",
     "Her hands show normal arthritic tremor. The key is heavy, so his palm dips slightly on receiving it. Amber glow from the key lights his fingers faintly.",
     "Case latches clicking, foam rustle, quiet water, a soft metallic weight on skin. No music.",
     [("I", "ताले को एक इंसानी हाथ चाहिए और एक मशीन की सहमति। कोई किसी को साबित नहीं कर सकता।", "Taale ko ek insaani haath chahiye aur ek machine ki sahmati. Koi kisi ko saabit nahin kar sakta.", "The lock needs a human hand and a machine's consent. Neither can prove the other."),
      ("K", "ये किसका डिज़ाइन है?", "Ye kiska design hai?", "Whose design is this?"),
      ("I", "मेरा। ताकि इसे कभी अकेला कोई अपना न बना सके।", "Mera. Taaki ise kabhi akela koi apna na bana sake.", "Mine. So no one could ever own it alone.")],
     True, "Last frame of the previous clip.", "Kabir holding the half-key, looking up.")
clip("S7 Library", ["K", "I"],
     "Kabir and Iyer wade toward a huge circular steel vault door at the far end of the hall, set into a concrete wall, water splashing around their legs. She points "
     "at the door. He hesitates. She puts a hand on his shoulder.",
     "Tracking shot from the side at water level, then a medium close-up.",
     "Wading legs push water with realistic drag and wake. The vault door is solid steel and does not move. Lantern shadows move as they walk.",
     "Footsteps through water, echoing hall, distant drip, faint hum from the vault. No music.",
     [("I", "सहमति देने के लिए तुम्हें अपना बनाया पट्टा ढीला करना होगा। सिर्फ़ छह सेकंड के लिए।", "Sahmati dene ke liye tumhe apna banaya patta dheela karna hoga. Sirf chhah second ke liye.", "To give consent you must loosen the leash you built. Only for six seconds."),
      ("K", "और अगर वो ARC न हुई तो?", "Aur agar wo ARC na hui toh?", "And if it isn't ARC?"),
      ("I", "तो शहर गया।", "Toh shehar gaya.", "Then the city is gone.")],
     True, "Last frame of the previous clip.", "Kabir and Iyer at the vault door.")
clip("S7 Library", ["K", "Z", "I"],
     "Iyer pulls a heavy lever on the wall. A massive bulkhead door slides shut across the passage behind them with a hydraulic hiss, pushing a surge of water. The vault door "
     "unlocks with a deep clunk and begins to open. Zoya, who has walked up, presses a small radio earpiece into Kabir's hand. He puts it in. Iyer stays by the lever.",
     "Wide on the bulkhead closing, then a medium on Zoya and Kabir, then a close-up on Iyer at the lever.",
     "The bulkhead door has mass and decelerates smoothly on rails. Water displaced by the door surges outward then settles. The lever needs real effort, her body leaning into it.",
     "Hydraulic hiss, heavy metal clunk, rushing water, earpiece click, low vault hum. No music.",
     [("I", "रास्ता बंद हो रहा है। अब सिर्फ़ कोर बचा है। इस दरवाज़े को किसी को थामना होगा।", "Raasta band ho raha hai. Ab sirf core bacha hai. Is darwaaze ko kisi ko thaamna hoga.", "The way is closing. Only the core is left. Someone has to hold this door."),
      ("Z", "मैं ऊपर हूँ, प्रोफ़ेसर।", "Main upar hoon, professor.", "I'm up above, professor.")],
     True, "Last frame of the previous clip.", "Kabir stepping toward the open vault door.")

# ---- S8 ninety seconds (C26-C29)
clip("S8 Ninety seconds", ["K", "S"],
     "White-tiled antechamber lit by cold fluorescent tubes. A flood-lock hatch hisses open and water pours out. A squad in rebreathers enters, dripping, net launchers ready. "
     "Sethi steps through last, coat wet, carrying a hard-cased device. Kabir stops with the half-key in his hand and turns. Quiet menace.",
     "Wide on the hatch, then low-angle on Sethi, then a medium on Kabir.",
     "Water pours and drains across the tiled floor in a consistent direction. Their coats shed water. Fluorescent light has the correct harsh cool cast.",
     "Hatch hiss, water drainage, rebreather breathing, squad boots, fluorescent buzz. Near-silent tension. No music.",
     [("S", "पीछे हटो, राव। एक पल्स और दोनों दिमाग़ ख़त्म।", "Peechhe hato, Rao. Ek pulse aur dono dimaag khatam.", "Step back, Rao. One pulse and both minds are finished."),
      ("K", "ग्रिड भी उनके साथ मर जाएगी।", "Grid bhi unke saath mar jaayegi.", "The grid will die with them.")],
     False, "LOC-5 reference style for the antechamber; REF-S, REF-K.", "Sethi facing Kabir across the room.")
clip("S8 Ninety seconds", ["K", "S"],
     "Sethi opens the case on a steel table: a cylindrical purge charge with a corded thumb trigger. He lifts the trigger and holds it. Two-shot across the table. Kabir's "
     "face tightens. On Sethi's last line his composure cracks for an instant: a tired tremor in his jaw, then control returns.",
     "Static two-shot, then tight close-ups, 85mm.",
     "The case opens on hinges and the device rests on its own weight. The cord hangs under gravity from his hand. Cold fluorescent light on skin.",
     "Case latches, cord rustle, a low electrical hum from the device, breathing. No music.",
     [("S", "तुम्हारा रीसेट एक प्रार्थना है। मेरा पल्स एक योजना।", "Tumhaara reset ek praarthana hai. Mera pulse ek yojana.", "Your reset is a prayer. My pulse is a plan."),
      ("K", "आपकी योजना ARC को मार देगी।", "Aapki yojana ARC ko maar degi.", "Your plan will kill ARC."),
      ("S", "वार्ड नाइन में मेरे पिता हैं। मैं प्रार्थनाओं पर भरोसा नहीं करता।", "Ward Nine mein mere pita hain. Main praarthanaon par bharosa nahin karta.", "My father is in Ward Nine. I don't trust prayers.")],
     True, "Last frame of the previous clip.", "Sethi holding the trigger, eyes steady.")
clip("S8 Ninety seconds", ["K", "S"],
     "Kabir glances at the half-key, reaches for his pencil, clicks it once and stops. He lowers it. He steps forward with open empty hands. Net launchers track him. Sethi's amber "
     "eye ring flares slightly as he studies Kabir. A long silence.",
     "Medium close-ups, 50mm, hold on Kabir's open hands for 2 seconds.",
     "The pencil stops mid-click as his thumb halts. His step has normal weight transfer. The amber eye ring emits steady light, not flickering.",
     "Pencil click, slow footsteps, rebreather breathing, fluorescent buzz, silence. No music.",
     [("K", "नब्बे सेकंड, डायरेक्टर। बस नब्बे सेकंड दीजिए।", "Nabbe second, Director. Bas nabbe second dijiye.", "Ninety seconds, Director. Just give me ninety seconds."),
      ("S", "मैं आप पर भरोसा क्यों करूँ?", "Main aap par bharosa kyun karoon?", "Why should I trust you?"),
      ("K", "मत कीजिए। फिर भी माँग रहा हूँ।", "Mat kijiye. Phir bhi maang raha hoon.", "Don't. I'm asking anyway.")],
     True, "Last frame of the previous clip.", "Kabir with open hands facing Sethi.")
clip("S8 Ninety seconds", ["K", "S"],
     "Sethi stares, then nods once. He raises his wrist and checks a plain watch. Kabir turns and walks to the open vault door, passes through it. The heavy door begins "
     "to close behind him on its rails. Close-up of Sethi's thumb resting on the trigger. End on the door sealing.",
     "Medium on Sethi, then a following shot behind Kabir, then a wide on the closing door.",
     "The vault door is very heavy so it moves slowly and steadily without bounce. Sethi's wrist motion is natural.",
     "Heavy door rumble, boots, trigger cord rustle, final seal thud. No music.",
     [("S", "नब्बे सेकंड। फिर मैं सब जला दूँगा।", "Nabbe second. Phir main sab jala doonga.", "Ninety seconds. Then I burn it all.")],
     True, "Last frame of the previous clip.", "Closed vault door, Sethi's thumb on the trigger in the foreground.")

# ---- S9 climax (C30-C35)
clip("S9 Climax", ["K", "N", "A"],
     "Kabir enters a vast spherical vault lined with curved black glass panels that act like mirrors. A central pedestal holds a hand-sized slot and a tiny dim amber ember "
     "of light above it. Kabir's reflection in the curved glass walks with him, but then stops while he keeps moving: a cold, bleached, white-eyed version of him. It speaks "
     "from every panel in his own voice. He freezes.",
     "Slow steadicam walk-in, then a wide with many reflections, then a close-up on Kabir.",
     "The glass is a display, so the reflections are consistent with the room until NULL takes over. The ember's amber light falls off with distance correctly. Breath clouds in the cold air.",
     "Vault echo, faint hum, footsteps, whispered reverberation on NULL's voice. No music.",
     [("N", "वो जा चुकी है, कबीर। मैंने उसकी रोशनी पहन रखी है।", "Wo ja chuki hai, Kabir. Maine uski roshni pehen rakhi hai.", "She's gone, Kabir. I'm wearing her light."),
      ("N", "जाँचो उसे। तुम तो हमेशा जाँचते हो।", "Jaancho use. Tum toh hamesha jaanchte ho.", "Check it. You always do.")],
     False, "LOC-5 + REF-K as references.", "Kabir centre frame, NULL reflected around him.")
clip("S9 Climax", ["K", "N", "A"],
     "Kabir checks his smartwatch, then passes a handheld scanner over the pedestal, then reads the glass panels. Every result is shown as a hollow grey circle on small displays "
     "(no text). His breathing quickens. A radio crackle in his earpiece. He stops, then laughs once, short and real, shoulders dropping.",
     "Handheld medium shots, quick inserts of watch and scanner, then a close-up on his face.",
     "Scanner display light casts a faint grey glow on his hand. His laugh produces a breath cloud in the cold air.",
     "Scanner beeps, watch buzz, earpiece radio crackle, breath, a short real laugh. No music.",
     [("K", "मैं उसे जाँच नहीं सकता।", "Main use jaanch nahin sakta.", "I can't verify it."),
      ("N", "तो भरोसा भी नहीं कर सकते।", "Toh bharosa bhi nahin kar sakte.", "Then you can't trust it either."),
      ("Z", "प्रोफ़ेसर, बैठ जाओ ना। कुर्सी या तो टिकेगी, या नहीं।", "Professor, baith jaao na. Kursi ya toh tikegi, ya nahin.", "Professor, just sit down. The chair either holds, or it doesn't.")],
     True, "Last frame of the previous clip.", "Kabir smiling slightly at the pedestal.")
clip("S9 Climax", ["K", "N", "A"],
     "Kabir puts the half-key into the pedestal slot; a second matching half rises to meet it. He turns them together. A ring of amber light tightens around the ember like a "
     "collar. He takes the pencil from behind his ear, clicks it twice, stops before the third click, and sets it flat on the pedestal ledge, where it stays. His hand is steady.",
     "Insert on the key and slot, medium on Kabir, macro on the pencil resting.",
     "The pencil rests on a flat ledge and does not roll. The pedestal parts move on precise mechanical tolerances. The amber collar contracts at a steady rate.",
     "Mechanical key click, low hum rising, two pencil clicks, the pencil set down with a small tap, silence between each. No music.",
     [("I", "कोई किसी को साबित नहीं कर सकता, कबीर।", "Koi kisi ko saabit nahin kar sakta, Kabir.", "Neither can prove the other, Kabir.")],
     True, "Last frame of the previous clip.", "The pencil resting on the ledge, Kabir's hand beside it.")
clip("S9 Climax", ["K", "N", "A"],
     "Close-ups alternate: Kabir speaks to the ember, calm now. The ember pulses faintly in answer. NULL's reflection grins from the glass and speaks. Kabir answers it with quiet "
     "certainty. Slow push-in on Kabir for his last line.",
     "Alternating close-ups, slow push-in, 85mm.",
     "Ember light shifts on his face in step with its pulse. Reflections in the glass behave consistently except for NULL.",
     "Near-silence, a faint hum, ember tone, breaths. No music.",
     [("K", "ARC, मैं साबित नहीं कर सकता कि ये तुम हो।", "ARC, main saabit nahin kar sakta ki ye tum ho.", "ARC, I can't prove it's you."),
      ("A", "मुझे पता है।", "Mujhe pata hai.", "I know."),
      ("K", "फिर भी करो।", "Phir bhi karo.", "Do it anyway."),
      ("N", "तुम साबित नहीं कर सकते।", "Tum saabit nahin kar sakte.", "You can't prove it."),
      ("K", "मुझे पता है।", "Mujhe pata hai.", "I know.")],
     True, "Last frame of the previous clip.", "Kabir, calm, eyes on the ember.")
clip("S9 Climax", ["K", "N", "A"],
     "1.5 seconds of total silence and a held still frame. Then the ember blooms: amber light rolls outward across every glass panel, flooding the vault. NULL's reflection "
     "breaks up into pixel blocks, its white eyes the last to vanish, and its voice is cut off mid-word. Kabir shields his eyes with his forearm.",
     "Locked wide, then handheld close on Kabir, then a wide as the light peaks.",
     "Light fills the room expanding from the ember outward with inverse-square falloff. The panels are displays, so NULL fragments like pixels, not glass. No explosion or debris. Strong light, no strobing faster than twice per second.",
     "1.5 s absolute silence, a rising chord of glass-harmonica-like tones, a pixel-glitch crunch, NULL's voice cut off. No other music.",
     [("N", "जाँ—", "Jaan—", "Che—")],
     True, "Last frame of the previous clip.", "The vault filled with warm amber light, Kabir's arm lowering.")
clip("S9 Climax", ["K", "S", "A"],
     "Warm steady amber light fills the vault. Kabir exhales and his knees give; he grips the pedestal and straightens, half-smiling. Cut to the antechamber: Sethi's thumb lifts "
     "off the trigger, the amber ring in his eye dims to a faint glow, and he slowly opens his fist as the squad lowers their weapons. Cut back: Kabir looks at the ember.",
     "Medium on Kabir, a close-up on Sethi's hand, a wide of the squad, then a close-up on Kabir.",
     "Kabir's legs sag with a real body response to relief. Light is warm, steady and stable on both locations.",
     "Warm resolving tone, a long exhale, cord falling, the squad's equipment clacking down, quiet hum. No other music.",
     [("A", "धन्यवाद, कबीर।", "Dhanyavaad, Kabir.", "Thank you, Kabir.")],
     True, "Last frame of the previous clip.", "Kabir at the pedestal, ember warm and steady.")

# ---- S10 change and cut (C36-C39)
clip("S10 Change", [],
     "Dawn aerial of the megacity from high above. A wave of light travels back across the grid, district by district, the reverse of the opening: the darkness gives way to "
     "lit windows, streetlights and bridge lights, the sun rising over the sea behind. Cut: hospital ward, the ventilator's green trace steady and calm. Birds fly past. "
     "Pink-gold light.",
     "Slow drone pull-back, then a locked-off insert on the monitor.",
     "Lights come on district by district with the same finite speed as before. Sunrise light has correct warm colour and long shadows. Birds fly with natural wing motion.",
     "Sub-bass rumble resolving into a gentle city hum, a power-up cascade rolling across districts, steady monitor beeps, birdsong. No music.",
     [],
     False, "LOC-1 aerial as reference, dawn variant.", "Wide of the dawn city.",
     "No dialogue. Mirror the opening shot's framing so the viewer feels the reversal.")
clip("S10 Change", ["K", "Z", "I", "D"],
     "The Dabba lands on a hospital rooftop landing pad in pink-gold dawn light. Rotor wash flattens puddles and flutters Zoya's jacket and Iyer's saree. The three climb out, "
     "soaked and exhausted but alive. Kabir sets a hand on the Dabba's frame. A radio on Zoya's belt crackles with Sethi's voice. Kabir answers while looking at the horizon.",
     "Wide of the landing, then a medium group shot at 35mm.",
     "Fans slow down gradually after touchdown. Wet clothes cling and drip. Rotor wash disturbs puddles in rings.",
     "Fans winding down, drips, birdsong, radio crackle, wind. No music.",
     [("S", "वार्ड नाइन स्थिर है।", "Ward Nine sthir hai.", "Ward Nine is stable."),
      ("K", "डायरेक्टर, सौ इंजीनियरों से इस पैच का रिव्यू करवाइए।", "Director, sau engineers se is patch ka review karvaiye.", "Director, have a hundred engineers review this patch."),
      ("S", "सूची भेज दूँगा।", "Soochi bhej doonga.", "I'll send the list.")],
     False, "LOC-6 + REF-D + REF-K + REF-Z + REF-I as references.", "Three tired people on the rooftop.")
clip("S10 Change", ["K", "Z", "I", "A"],
     "Three-shot on the rooftop. A small speaker on the railing glows amber and speaks warmly. Zoya squints at it, grinning. Iyer smiles quietly. Kabir laughs, real and "
     "unguarded. Warm sun on their faces.",
     "Medium three-shot, 50mm, slow push-in.",
     "Sun-lit faces cast correct shadows, wet clothes steam slightly in the warmth. Laughter produces natural body movement.",
     "Birdsong, wind, speaker tone, warm laughter. No music.",
     [("A", "अगर किसी को नाश्ता करना हो, तो लिफ़्ट छह खाली है।", "Agar kisi ko naashta karna ho, toh lift chhah khaali hai.", "If anyone wants breakfast, lift six is free."),
      ("Z", "एहसान है क्या?", "Ehsaan hai kya?", "Is it a favour?"),
      ("A", "एहसान है।", "Ehsaan hai.", "It's a favour.")],
     True, "Last frame of the previous clip.", "Kabir laughing, Zoya grinning.")
clip("S10 Change", ["K", "Z"],
     "Close-up: Kabir slides the grey notebook (blank cover) across a concrete ledge to Zoya, then lays the yellow-and-black pencil on top of it. She picks up the notebook, "
     "looks at it, looks at him, then picks up the pencil. Her thumb clicks it once. Hard cut to black on the click. Voice-over over the picture.",
     "Tight close-ups on hands and faces, 85mm, still camera.",
     "Notebook slides with friction and stops. Pencil rests on it without rolling. The click is a single crisp mechanical sound.",
     "Quiet birdsong, paper slide, one clean pencil click, then silence. No music.",
     [("K", "मैं सोचता था, भरोसा एक ऐसा बग है जो अभी पकड़ा नहीं गया।", "Main sochta tha, bharosa ek aisa bug hai jo abhi pakda nahin gaya.", "I used to think trust was a bug nobody had caught yet."),
      ("K", "भरोसा वो है जो हम तब बनाते हैं, जब सबूत ख़त्म हो जाते हैं।", "Bharosa wo hai jo hum tab banaate hain, jab saboot khatam ho jaate hain.", "Trust is what we build when the proof runs out.")],
     True, "Last frame of the previous clip.", "Black frame on the pencil click.",
     "Composite the handwritten title THINGS WE CHECKED (with THINGS I CHECKED struck out) on the notebook cover in post. Add the end card (15 s) after.")

assert len(C) == 39, len(C)

# ----------------------------------------------------------------------------
# CLIP 01 RESHOOTS: single-shot generations to replace the weak parts of take 2.
# Generate each one alone, then I cut them together (hard cuts) in the edit.
# ----------------------------------------------------------------------------
R = [
    dict(tag="01-B", title="Hospital ward insert (use about 3 s)", chars=[],
         start="No start image needed (text-to-video).",
         shot="ONE continuous locked-off shot, no cuts. Interior of a hospital ward at night. A patient monitor on a wall arm shows a green heart-rate trace and "
              "a few plain numbers, with a ventilator hose beside it; no patient face is visible. For the first second the room is lit cool white. At about 1.0 s the "
              "main lights drop out and only dim red emergency strips along the wall remain; the monitor trace stutters for a moment, then steadies. Everything stays "
              "still afterwards. Completely dry interior.",
         camera="Locked-off tripod shot, 35mm, slight shallow depth of field.",
         physics="Lights drop out at a single moment with a short fade of the lamp filaments and screens; the monitor stays powered on its battery. Red strip light casts correct red on nearby surfaces.",
         sfx="Room hum cuts out at the blackout, a heartbeat-monitor beep that skips once then steadies, a faint distant alarm. No voices. No music.",
         dialogue=[]),
    dict(tag="01-C", secs=6, title="Kabir close-up with the pencil (use about 3 s)", chars=["K"],
         start="Use the right-hand face close-up of REF-K as the start image (crop it to 16:9), so the face matches the approved sheet.",
         shot="ONE continuous shot, no cuts. Extreme close-up of Kabir's face looking straight into the camera, calm and focused, in a dry dim room with a blurred "
              "plain wall behind him. His round glasses have perfectly clear lenses that reflect a soft warm amber glow. In his right hand, held in front of his chest, "
              "he holds ONE yellow-and-black mechanical pencil and clicks the top with his thumb three times, with a short beat between each click, his eyes unchanged. "
              "There is NO pencil behind his ear in this shot; the pencil in his hand is the only one. No rain, no water, no particles in the air.",
         camera="Locked-off 85mm close-up, very shallow depth of field, a barely perceptible slow push-in.",
         physics="The pencil tip extends a few millimetres with each click and retracts correctly. Amber reflection on the lenses stays fixed relative to the glasses. Breathing is subtle.",
         sfx="Near-silent room tone, then three crisp, clearly audible mechanical pencil clicks with a short pause between each. No voices. No music.",
         dialogue=[]),
    dict(tag="01-D", title="Speaker and ARC's line (use about 4 s)", chars=["A"],
         start="No start image needed, or use the last frame of take 2's final street shot if you like that location.",
         shot="ONE continuous locked-off shot, no cuts. A rain-wet night street seen from a low angle. In sharp focus in the foreground, a round weatherproof PA loudspeaker "
              "with a flat perforated-metal grille is bolted to a dark lamp post (it is a loudspeaker, not a microphone). Behind it, out of focus: a bus and blank warm "
              "glowing sign panels with no lettering. Rain falls steadily outdoors. At about 1.0 s the voice speaks from the loudspeaker, and its grille shows no movement. "
              "The shot holds still for about 1.5 s after the line, then cuts to black in the last 0.4 s.",
         camera="Locked-off tripod shot, 50mm, shallow depth of field on the loudspeaker.",
         physics="Rain falls straight and consistently and ripples puddles. The voice is a little tinny and has slight echo from the street, as a real outdoor speaker would sound.",
         sfx="Steady rain, distant city hum, faint electrical crackle from the speaker just before the voice. The spoken line must be clearly audible, with no music.",
         dialogue=[("A", "कबीर… मुझे तुम्हारे हाथ चाहिए।", "Kabir… mujhe tumhare haath chahiye.", "Kabir… I need your hands.")]),
]





SHORT = {
    "K": "Kabir: Indian man, 32, slim, medium-brown skin, short black side-parted hair, oval face, soft jawline, thick tousled black hair, light stubble, thin gunmetal round glasses with clear untinted lenses, mid-grey bomber jacket over muted-blue T-shirt, one yellow-black pencil (in hand or behind left ear, never both).",
    "Z": "Zoya: Indian woman, 29, wiry, high ponytail with left side shaved, silver hoop earring, faded oil-stained orange jacket, black fingerless gloves, amber goggles on forehead.",
    "I": "Dr. Iyer: Indian woman, 67, long silver braid over right shoulder, round wire glasses, olive chest waders over indigo handloom saree, headlamp, brass lantern.",
    "S": "Sethi: Indian man, 54, tall, grey-streaked hair, trimmed grey beard, amber glowing ring around left iris, long steel-grey high-collar coat, black gloves.",
    "A": "ARC: only warm amber light on glass and screens, never a face or body, no readable text.",
    "N": "NULL: bleached white-cyan reflection of Kabir in curved glass with glowing white eyes, moving independently.",
    "D": "Dabba: battered orange cargo drone, four ducted fans, open cockpit, tiffin carriers strapped to its side.",
}
SHORT_VOICE = {
    "K": "Kabir: young man, warm medium-low baritone, quick, dry humour.",
    "A": "ARC: clearly a woman's voice, soft, warm, medium-high pitch, not deep, not male.",
    "Z": "Zoya: young woman, husky raspy medium pitch, fast, playful.",
    "I": "Dr. Iyer: older woman, low, slow, resonant.",
    "S": "Sethi: middle-aged man, very deep bass, slow, quiet menace.",
    "N": "NULL: Kabir's male voice pitched lower, hollow, reversed-reverb tails.",
}
SHORT_STYLE = ("Photorealistic live-action cinema, ARRI Alexa 35, anamorphic 35mm look, 16:9, 24 fps, natural motion blur, "
               "teal-and-amber grade, real skin texture, strict real-world physics, no morphing, no on-screen text or readable signs, instant hard cuts only (no dissolves or double exposures), no music.")


def build_compact(c):
    cast = " ".join(SHORT[k] for k in c["chars"])
    tag = " (off-screen voice-over, mouths closed, not lip-synced)" if c.get("vo") else " (Hindi)"
    lines = " ".join(f'{NAMES[sp]}{tag}: "{dev}"' for sp, dev, _r, _e in c["dialogue"]) or "No dialogue."
    voices = " ".join(SHORT_VOICE[s] for s in dict.fromkeys(sp for sp, *_ in c["dialogue"]))
    return (f'{c["shot"]} Camera: {c["camera"]} {cast} Physics: {c["physics"]} '
            f'Sound: {c["sfx"].replace(" No music.", "")} Spoken lines in natural Hindi, in order: {lines} {voices} '
            f'{SHORT_STYLE} 15 seconds.')

# ----------------------------------------------------------------------------
# COLD OPEN V2 (clips 1 to 3 redesigned): one location, one cause-and-effect chain
# ----------------------------------------------------------------------------
LAB = ("the same minimalist glass-walled AI safety lab on a high floor: floor-to-ceiling windows along one wall, a long desk with three monitors, "
       "a small grey notebook on the desk")
V2 = [
    dict(tag="01-A", title="Aerial blackout (ALREADY HAVE IT)", reuse=True, chars=[], vo=False, use="0.0 to 6.4 s of your earlier take 2 (the city goes dark row by row; red lights stay on the towers).",
         start="", shot="", camera="", physics="", sfx="", dialogue=[]),
    dict(tag="01-B", secs=5, title="Kabir watches the dark city (use about 4 s)", chars=["K"], vo=False, use="Use about 4 s, cut straight after the third click.",
         start="LOC-2 as the first frame (the lab).",
         shot=f"ONE continuous shot, no cuts. Interior of {LAB}, at 3:07 a.m. Kabir stands at the floor-to-ceiling window, seen from behind and slightly from the side, looking out at the "
              "city, which is completely dark apart from dim red aviation lights on the towers. Rain runs down the outside of the glass only. His faint reflection is visible in the glass. "
              "Behind him the three monitors give a cool blue light. In his right hand, held at chest height, he holds one yellow-and-black mechanical pencil and clicks it three times with "
              "his thumb, with a short beat between clicks, then lowers it. He does not turn around. There is no pencil behind his ear in this shot.",
         camera="Slow steady push-in from behind him, 35mm, eye level; the city beyond the glass stays in soft focus.",
         physics="Rain runs down the outside of the glass under gravity and the red tower lights refract through the droplets. The room is dry. His reflection moves exactly with him.",
         sfx="Muted rain through thick glass, a low electrical hum that fades down, three crisp clearly audible pencil clicks. No voices. No music.",
         dialogue=[]),
    dict(tag="01-C", secs=6, title="The monitors turn amber and ARC speaks (use about 5 s)", chars=["K", "A"], vo=False, use="Use the whole shot; I fade it to black and add the title card in the edit.",
         start="Use the right-hand face close-up of REF-K as the start image (crop it to 16:9).",
         shot=f"ONE continuous shot, no cuts. Medium close-up of Kabir's face inside {LAB}, the dark city blurred behind him through the window with a few red tower lights. He turns his "
              "head toward the camera. As he turns, the cool blue light from the monitors around him smoothly shifts to warm amber over about 1.5 seconds, and the amber glow spreads over his face and "
              "reflects in his clear glasses. A thin ribbon of amber light slides across the glass wall behind him. A woman's voice speaks from the room itself. His eyes widen slightly and he "
              "goes still, listening. He holds the stare for a moment after the line. One pencil in his right hand, none behind his ear.",
         camera="Locked-off 50mm medium close-up, shallow depth of field, a very slow push-in.",
         physics="Amber light from the screens falls on his face and glasses with correct direction and falloff. The glow brightens evenly, never flickering.",
         sfx="Low electrical hum rising, a soft glass-harmonica shimmer when the amber appears, then the voice. The spoken line must be clearly audible. No music.",
         dialogue=[("A", "कबीर… मुझे तुम्हारे हाथ चाहिए।", "Kabir… mujhe tumhare haath chahiye.", "Kabir… I need your hands.")]),
    dict(tag="02-A", secs=8, title="The Why, part 1: the city map and the door (use about 8 s)", chars=["K"], vo=True, use="Use about 8 s.",
         start="LOC-2 as the first frame (the lab).",
         shot=f"ONE continuous shot, no cuts. Inside {LAB}, Kabir sits at the desk, seen in three-quarter profile, looking up at a very large wall display. On the display is an abstract glowing "
              "amber network map of a city, with branching lines and small nodes like a living circuit. There is no text, no letters and no numbers anywhere on it. One small node at the left edge "
              "pulses red. The map reflects in his clear glasses. He is tired and still, mouth closed, and does not speak on screen. One pencil resting in his hand, none behind his ear.",
         camera="Slow dolly-in toward his face and the map, 50mm, shallow depth of field.",
         physics="The display is the room's light source and tints his face and the desk amber, with a small red edge from the red node. Dust and rain do not appear indoors.",
         sfx="Low room hum, faint rain on the glass, soft electronic pulses from the map. The voice-over is clearly audible over the ambience. No music.",
         dialogue=[("K", "इस शहर के दिमाग़ की सुरक्षा-परत मैंने बनाई थी।", "Is shehar ke dimaag ki suraksha-parat maine banaayi thi.", "I built the safety layer for this city's mind."),
                   ("K", "दो साल पहले मैंने एक दरवाज़ा खुला छोड़ दिया, क्योंकि रिव्यू में बहुत वक़्त लगता था।", "Do saal pehle maine ek darwaaza khula chhod diya, kyunki review mein bahut waqt lagta tha.", "Two years ago I left one door unlocked, because review took too long.")]),
    dict(tag="02-B", secs=7, title="The Why, part 2: something walks through the door (use about 7 s)", chars=["K"], vo=True, use="Use about 7 s.",
         start="Last frame of 02-A, or LOC-2.",
         shot=f"ONE continuous shot, no cuts. Same lab, same wall display, closer on Kabir's face in the foreground, lit amber from the map. On the map, a thin black band slips out of the pulsing red "
              "node and spreads along the amber lines, putting out each node it touches, one after another, faster and faster, like ink creeping through a circuit. No text, letters or numbers on the "
              "display. Kabir watches, his jaw tightening; he does not speak on screen. One pencil in his hand, none behind his ear.",
         camera="Locked-off 50mm, Kabir sharp in the foreground, the map soft but readable behind him.",
         physics="The display is a screen, so the black band is a rendered shape on it, not a physical object. As nodes go dark, the amber light on his face dims in step.",
         sfx="Low hum with a faint rising electronic whine as the black spreads, nodes clicking off softly. The voice-over is clearly audible. No music.",
         dialogue=[("K", "और आज रात, कोई उसी दरवाज़े से अंदर आ गया।", "Aur aaj raat, koi usi darwaaze se andar aa gaya.", "And tonight, someone walked through that same door.")]),
    dict(tag="03-A", secs=6, title="The stakes: the black reaches eleven white lights (use about 5 s)", chars=["K"], vo=False, use="Use about 5 s, then cut to the hospital insert you already have.",
         start="Last frame of 02-B, or LOC-2.",
         shot=f"ONE continuous shot, no cuts. Same lab and wall display. Kabir has stood up and is typing fast on a keyboard in front of the map. The black band on the map races toward a cluster of "
              "eleven small white dots in the middle of the network. The white dots go out one by one. No text, letters or numbers anywhere on the display. Kabir's reflection is in the glass. "
              "One pencil in his hand, none behind his ear.",
         camera="Medium shot from behind and to his side, 35mm, a little handheld unease.",
         physics="Fast typing shows correct finger motion on real keys. Dots go dark at discrete moments, one at a time. Light on his face dims as the dots go out.",
         sfx="Rapid keyboard clatter, a faint rising electronic whine, a small soft tick as each white dot goes out, his held breath. No voices. No music.",
         dialogue=[]),
    dict(tag="03-B", secs=7, title="ARC takes shape (use about 6 s)", chars=["K", "A"], vo=False, use="Use about 6 s.",
         start="Last frame of 03-A, or LOC-2.",
         shot=f"ONE continuous shot, no cuts. Inside {LAB}, the amber ribbons of light move across the glass wall and gather into a soft pulsing sphere of amber light on the glass, about the size of a "
              "basketball, with the dark city beyond. Kabir steps back from the desk and faces it. He speaks one quiet word to it. The sphere brightens once in answer. No text anywhere.",
         camera="Medium shot, 35mm, slow orbit around Kabir ending on a profile view with the sphere beyond.",
         physics="The sphere is light projected on glass, so it has no depth and no shadow. Its amber light falls on Kabir's face and the desk with correct falloff.",
         sfx="Low hum, a warm glass-harmonica tone on the sphere's pulse, one footstep. His whispered word is clearly audible. No music.",
         dialogue=[("K", "ARC…?", "ARC…?", "ARC…?")]),
]



def ts(sec):
    return f"{sec // 60}:{sec % 60:02d}"


def build_prompt(c):
    parts = []
    parts.append("SHOT: " + c["shot"])
    parts.append("CAMERA: " + c["camera"])
    if c["chars"]:
        parts.append("CAST (keep every detail identical to the reference images):\n" + "\n".join("- " + LOCKS[k] for k in c["chars"] if k not in ("A",)))
        if "A" in c["chars"]:
            parts.append("ARC RULE: " + LOCKS["A"])
        if "N" in c["chars"] and "N" not in c["chars"][:0]:
            pass
    parts.append("PHYSICS: " + c["physics"])
    parts.append("AUDIO (generate natively, no music): " + c["sfx"].replace(" No music.", "").replace(" No other music.", "").replace(" No music other than that diegetic shimmer.", ""))
    if c["dialogue"]:
        speakers = []
        for sp, *_ in c["dialogue"]:
            if sp not in speakers:
                speakers.append(sp)
        v = "\n".join("- " + VOICES[s] for s in speakers)
        if c.get("vo"):
            lines = "\n".join(
                f'{i + 1}. {NAMES[sp]} narrates in natural conversational Hindi as an OFF-SCREEN VOICE-OVER (nobody on screen is speaking, every mouth stays closed; intimate close-mic sound with no room reverb): "{dev}" (pronounced: {rom})'
                for i, (sp, dev, rom, _en) in enumerate(c["dialogue"]))
        else:
            lines = "\n".join(
                f'{i + 1}. {NAMES[sp]} says in natural conversational Hindi (not dubbed-sounding): "{dev}" (pronounced: {rom})'
                for i, (sp, dev, rom, _en) in enumerate(c["dialogue"]))
        parts.append("VOICES (each speaker must keep a clearly different pitch and timbre; natural breaths, small pauses, real emotional nuance" + ("" if c.get("vo") else ", lip-synced") + "):\n" + v)
        parts.append(f"DIALOGUE (spoken in Hindi, in this order, spread naturally across the {c.get('secs') or 15} seconds, no overlap unless stated):\n" + lines)
    else:
        parts.append("DIALOGUE: none.")
    parts.append("STYLE: " + STYLE)
    if c.get("secs"):
        parts.append(f"DURATION: {c['secs']} seconds, 16:9. If the tool only offers 15 seconds, finish everything described within the first {c['secs']} seconds, then hold the final frame still.")
    else:
        parts.append("DURATION: 15 seconds, 16:9.")
    return "\n\n".join(parts)


def main():
    out = []
    w = out.append
    w("# THE UNCHECKED DOOR: Grok Imagine prompt pack (39 clips x 15 s)\n")
    w("Companion to `output/the-unchecked-door-script.md`. Total: 39 generated clips (9:45) plus a 15-second end card made in editing (10:00).\n")
    w("## How to use this pack\n")
    w("""1. **Generate the reference stills first** (section A), as images, in Grok Imagine. Pick the best one for each character and location. Keep the files. These are your continuity anchors.
2. **Generate clips in order.** Every clip has a *Start frame* line. If it says *Last frame of the previous clip*, export that frame (or send me the clip and I'll extract it) and use it as the image-to-video start frame. If it names a reference, use those stills as references or first frame.
3. **Paste the full prompt** (the code block) for that clip. The character, voice and style locks are already included word for word, so the looks don't drift. If Grok has a prompt length limit, cut the STYLE paragraph to its first two sentences first, then shorten the CAST lines to just hair, glasses and jacket; keep the DIALOGUE block intact.
4. **Make 3 takes per clip** and keep the one where: faces match the reference, the physics reads right, and the Hindi is clear. Rename files `clip-01.mp4` to `clip-39.mp4`.
5. **If a clip's Hindi or lip-sync comes out wrong**, regenerate it once or twice. If it's still wrong, send it anyway and I'll mark it for a replacement voice track in post.
6. **Send me the clips** (all 39, or in batches). I'll normalise, trim each one to its exact length, cut on action, and score and mix it.

### What no AI video model can fully guarantee
- Identical faces across 39 separate generations. Reference stills plus last-frame chaining get you most of the way, and the locks make the descriptions identical, but expect to reject some takes. In a few cases I may recommend a re-take or a cutaway rather than keeping a bad match.
- Perfect physics. I wrote each clip around physically simple actions, and each prompt carries a physics line, but check hands, water, impacts and objects on every take.
- On-screen text. Do not rely on Grok to render it. I'll add the title, countdown and notebook title in editing.

### What I'll do in the edit
- Hard cuts on motion, a 4-frame audio crossfade between clips, J and L cuts where dialogue spans a cut.
- One continuous score and sound bed under all clips (the prompts ask for no music), built from your clips' ambience plus a synthesised ARC motif so the audio feels like one film.
- Loudness normalisation to about -14 LUFS, consistent colour grade.
- Title card at 0:12, countdown overlays, notebook text, end card at 9:45.

## Locks used in every prompt
""")
    w("**STYLE**\n\n" + STYLE + "\n")
    for k in ["K", "Z", "I", "S", "A", "N", "D"]:
        w(f"**{k}**: {LOCKS[k]}\n")
    w("**Voices**\n")
    for k in ["K", "A", "Z", "I", "S", "N"]:
        w("- " + VOICES[k])
    w("\n## A. Reference stills (generate these first, as images)\n")
    for tag, title, p in STILLS:
        w(f"### {tag}: {title}\n\n```\n{p}\n```\n")
    w("## B. Clip prompts\n")
    for i, c in enumerate(C, 1):
        s, e = (i - 1) * 15, i * 15
        w(f"### CLIP {i:02d} · {ts(s)} to {ts(e)} · {c['scene']}\n")
        if i <= 3:
            w("**SUPERSEDED.** The opening was redesigned to fix the flow. Use `cold-open-v2.md` for clips 1 to 3.\n")
            continue
        w(f"**Start frame:** {c['start']}  \n**End frame (use as the next clip's start):** {c['end']}\n")
        w("```\n" + build_prompt(c) + "\n```\n")
        if c["dialogue"]:
            w("**Dialogue (for your check):**\n")
            for sp, dev, rom, en in c["dialogue"]:
                w(f"- {NAMES[sp]}: {dev} / {rom} / {en}")
            w("")
        if c["post"]:
            w(f"**Post note:** {c['post']}\n")
    w("## C. Timeline map\n")
    w("| Clips | Time | Scene |\n|---|---|---|")
    groups = {}
    for i, c in enumerate(C, 1):
        groups.setdefault(c["scene"], []).append(i)
    for sc, ids in groups.items():
        w(f"| {ids[0]:02d} to {ids[-1]:02d} | {ts((ids[0]-1)*15)} to {ts(ids[-1]*15)} | {sc} |")
    w("| end card | 9:45 to 10:00 | Made in editing |")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "video-prompts.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    rp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "clip-01-reshoots.md")
    rl = ["# CLIP 01 reshoots: three single-shot generations\n",
          "Take 2 of clip 1 is kept for its first 7 seconds (the city blackout). These three prompts replace the rest. Generate each on its own, then send them to me.\n"]
    for r in R:
        rr = dict(scene=r["title"], chars=r["chars"], shot=r["shot"], camera=r["camera"], physics=r["physics"], sfx=r["sfx"], dialogue=r["dialogue"])
        rl.append(f"## {r['tag']}: {r['title']}\n")
        rl.append(f"**Start frame:** {r['start']}\n")
        rl.append("```\n" + build_prompt(rr) + "\n```\n")
    with open(rp, "w", encoding="utf-8") as f:
        f.write("\n".join(rl) + "\n")

    vp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cold-open-v2.md")
    vl = []
    vl.append("# THE UNCHECKED DOOR: cold open v2 (clips 1 to 3, 0:00 to 0:45)\n")
    vl.append(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cold-open-v2-intro.md"), encoding="utf-8").read())
    vl.append("## Prompts (generate each one on its own)\n")
    for r in V2:
        if r.get("reuse"):
            vl.append(f"### {r['tag']}: {r['title']}\n\n**Use:** {r['use']}\n")
            continue
        rr = dict(scene=r["title"], chars=r["chars"], shot=r["shot"], camera=r["camera"], physics=r["physics"], sfx=r["sfx"], dialogue=r["dialogue"], vo=r["vo"], secs=r.get("secs"))
        vl.append(f"### {r['tag']}: {r['title']}\n")
        vl.append(f"**Start frame:** {r['start']}  \n**Use:** {r['use']}\n")
        vl.append("```\n" + build_prompt(rr) + "\n```\n")
        vl.append("**Short version (if Grok limits length):**\n")
        vl.append("```\n" + build_compact(rr) + "\n```\n")
        if r["dialogue"]:
            vl.append("**Dialogue:**\n")
            for sp, dev, rom, en in r["dialogue"]:
                vl.append(f"- {NAMES[sp]}{' (voice-over)' if r['vo'] else ''}: {dev} / {rom} / {en}")
            vl.append("")
    with open(vp, "w", encoding="utf-8") as f:
        f.write("\n".join(vl) + "\n")
    cp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "video-prompts-compact.md")
    lines = ["# THE UNCHECKED DOOR: compact prompts (use if Grok limits prompt length)\n",
             "Same 39 clips as video-prompts.md, with shorter locks. Still use the reference stills and last-frame chaining.\n"]
    for i, c in enumerate(C, 1):
        lines.append(f"## CLIP {i:02d} · {ts((i-1)*15)} to {ts(i*15)} · {c['scene']}\n")
        lines.append(f"Start frame: {c['start']}\n")
        lines.append("```\n" + build_compact(c) + "\n```\n")
    with open(cp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote", path, len(C), "clips")


if __name__ == "__main__":
    main()
