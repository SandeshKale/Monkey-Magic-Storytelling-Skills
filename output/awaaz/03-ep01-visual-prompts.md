# AWAAZ Episode 1: contact sheets and location prompts

Generate these first, in Grok image mode. A contact sheet is one image with nine frames of the same person (angles, expressions, full body). It is the identity anchor for every video clip. Keep the best sheet for each person, then crop single frames out of it when a clip needs a start image.

## How to use
1. Generate each sheet 2 to 4 times. Keep the one where the nine faces are clearly the same person and the outfit is identical in every frame.
2. If one frame is bad but the rest are good, regenerate with "same as the reference image, change only the bottom-right frame".
3. Name the files `CS-KABIR`, `CS-SUSHMA`, `CS-RIYA`, `LOC-PUNE`, `LOC-BLR`, `PROP-STAGE`.
4. Kabir and Riya already have reference sheets from before. If you prefer to keep those, skip the Kabir and Riya sheets and use the old ones as references. The new sheets add expressions, which the micro-drama needs.

## Style for all sheets
`Photorealistic, neutral mid-grey seamless studio background, soft even key light with gentle fill, 85mm lens, natural skin with pores and fine detail, real fabric texture, no text, no captions, no watermarks, no logos. Contact sheet layout: a clean 3 by 3 grid, thin dark gutters, every frame the same person in the same outfit.`

---

## Characters

### CS-KABIR: Kabir Rao (reuse the approved face)
Attach your existing `REF-K` as a reference.
```
Photorealistic contact sheet, a clean 3 by 3 grid on a neutral mid-grey studio background, thin dark gutters, nine frames of the SAME man in the SAME outfit in every frame. KABIR RAO: Indian man, 32 years old, 178 cm, lean slim build, medium-brown skin, oval face with a soft jawline, thick black hair short at the sides and slightly tousled on top with a side parting, light stubble, thin round gunmetal wire-frame glasses with perfectly clear untinted lenses, mid-grey bomber jacket over a muted-blue crew-neck T-shirt, dark navy chinos, black leather sneakers with white soles, black smartwatch on his left wrist, one yellow-and-black mechanical pencil. Row 1 (head and shoulders): neutral facing the camera; three-quarter left; profile facing right. Row 2 (head and shoulders, expressions): tired and focused on a screen, mouth set; flat and avoiding, eyes sliding away; sudden alarm, eyes wide, hand over his mouth. Row 3 (full body): standing front view holding the pencil at chest height; back view; mid-stride running, jacket flying. Soft even key light, 85mm lens, natural skin with pores, real fabric texture. No text, no captions, no watermarks.
```

### CS-SUSHMA: Sushma Rao
```
Photorealistic contact sheet, a clean 3 by 3 grid on a neutral mid-grey studio background, thin dark gutters, nine frames of the SAME woman in the SAME outfit in every frame. SUSHMA RAO: Indian woman, 58 years old, 155 cm, medium build, wheatish skin with deep smile lines and a few age spots, greying black hair in a loose low bun with silver streaks, a small round red bindi on her forehead, round tortoiseshell reading glasses (sometimes pushed up on her head), a small gold nose stud, small gold earrings, a sage-green cotton saree with a thin printed border worn simply over a deep teal blouse, a thin gold bangle on each wrist, flour on both hands and a smudge on her forearm, worn rubber slippers. Row 1 (head and shoulders): neutral facing the camera; three-quarter left; profile facing right. Row 2 (head and shoulders, expressions): ordinary and calm, about to answer a phone; sudden fear, eyes wide, hand to her chest; tearful and begging, lips trembling, glasses on her nose. Row 3 (full body): standing front view with floury hands held slightly out; back view; seated at a table leaning forward, shoulders tight. Soft even key light, 85mm lens, natural skin with pores and fine detail, real fabric texture. No text, no captions, no watermarks.
```

### CS-RIYA: Riya Menon (reuse or regenerate)
Attach your existing `REF-R` as a reference if you have it.
```
Photorealistic contact sheet, a clean 3 by 3 grid on a neutral mid-grey studio background, thin dark gutters, nine frames of the SAME woman in the SAME outfit in every frame. RIYA MENON: Indian woman, 24 years old, 162 cm, slim, wheatish skin, round friendly face with soft cheeks, large dark expressive eyes, shoulder-length straight black hair tied in a low ponytail with a few loose strands, small silver stud earrings, an olive-green cotton kurta over blue jeans, a company lanyard with a plain white card, white canvas sneakers, no glasses. Row 1 (head and shoulders): neutral facing the camera; three-quarter left; profile facing right. Row 2 (head and shoulders, expressions): curious, head tilted, noticing something; worried, brow drawn, lips pressed; dawning realisation, eyes widening, a slow breath in. Row 3 (full body): standing front view holding a coffee mug; back view with a laptop under one arm; walking briskly mid-stride with the laptop. Soft even key light, 85mm lens, natural skin with pores, real fabric texture. No text, no captions, no watermarks.
```

### The cloned voice (no image)
It is never seen. In every clip it is heard through a phone speaker only. Do not generate a face for it.

---

## Locations
Each location sheet is one image with six vertical (9:16) panels in a 3 by 2 grid showing the same place from different camera positions, all at the same time of day with the same props. These are for you to pick start angles from.

### LOC-PUNE: the Rao flat (kitchen and dining nook), night
```
Photorealistic location contact sheet, a clean 3 by 2 grid of six vertical 9:16 panels with thin dark gutters, all showing the SAME small middle-class Indian flat in Pune at night, warm tungsten ceiling light and a yellow bulb over the stove, a slightly worn lived-in look, no people. Panel 1: wide of the kitchen, a steel kitchen counter with a rolling steel plate of dough, a stack of steel containers, a gas stove with a steel pot, an exhaust fan, a calendar on the wall. Panel 2: close on the counter with flour dusted on the steel, a steel plate with dough, a rolling pin, a phone lying face-up. Panel 3: a small wooden dining table with a plastic table runner, two chairs, an unfinished dinner on a steel thali, a water jug. Panel 4: close on the dining table surface with a phone laid beside the thali, reading glasses folded next to it. Panel 5: a wall shelf in the hall with a framed photo of a young man in a graduation robe (face not in focus), a small brass diya, a clock. Panel 6: a doorway between the kitchen and the hall, a ceiling fan turning above, a steel almirah visible. Teal-and-amber grade, shallow depth of field, real textures, no text, no readable calendar, no signs.
```

### LOC-BLR: SparkMind office, Bengaluru, night
```
Photorealistic location contact sheet, a clean 3 by 2 grid of six vertical 9:16 panels with thin dark gutters, all showing the SAME open-plan tech startup office at night, mostly dark with a few lit desks, cool blue light, rain on the windows, no people. Panel 1: wide of the floor with rows of desks and dark monitors, one lit desk in the middle. Panel 2: a single lit desk with two monitors showing blurred, illegible code, a half-drunk cup of chai, a desk lamp, headphones, a phone lying face-up. Panel 3: a long aisle between desks leading toward a glass-walled meeting room and an exit, empty chairs, overhead strip lights half on. Panel 4: a tall rain-streaked window with a blurred city and a few lights behind it, a desk chair in the foreground. Panel 5: a neighbouring desk with a laptop open, a plain white mug, a lanyard hung on the monitor. Panel 6: a whiteboard with illegible scribbles and a coffee machine in a corner. Cool teal shadows with warm lamplight, shallow depth of field, real textures, no text, no logos, no readable screens.
```

### PROP-STAGE: Kabir's talk on a conference stage (for the laptop screen)
Attach `CS-KABIR` as a reference.
```
Photorealistic 16:9 still of KABIR RAO (Indian man, 32, oval face, thick tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, wearing a black blazer over a muted-blue T-shirt, a headset microphone at his cheek, a conference lanyard) speaking on a modern tech conference stage at a lectern, mid-sentence, one hand raised with the palm up, a large screen behind him showing only an abstract audio waveform with no text, an audience of blurred shapes in the dark foreground, stage lighting. Natural skin with pores, shallow depth of field. No text, no logos, no captions.
```
