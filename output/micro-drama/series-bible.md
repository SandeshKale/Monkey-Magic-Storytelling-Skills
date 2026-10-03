# TEMPORARY (अस्थायी): series bible

A reel-style micro-drama series, built with the Monkey Magic method. Replaces the 10-minute sci-fi film, which is shelved.

## Assumptions used (correct any of these)
- **Genre:** grounded, real-life workplace drama. No sci-fi. Kabir stays an AI engineer, so the original brief (smart, early 30s, AI engineer, 3 to 4 other characters) still holds.
- **Format:** 9:16 vertical, about 75 seconds per episode (five 15-second clips), 8 episodes.
- **Language:** Hindi with English tech words (Hinglish), written in Devanagari for the video model, with a pronunciation line.
- **Production:** Grok Imagine, one clip per 15-second generation, lip-synced, real movement. At most two speakers per clip, always one man and one woman, so Grok gives them different voices.
- **Mode:** fiction (authored). Everything below is canon of this invented series, not a claim about real people.

## Logline
An AI engineer skipped one review to make a deadline. His loan-approval model has since rejected 31 people from one neighbourhood. One of them is standing in his lobby, begging for a human, and his promotion is on Friday.

## Spine (Monkey Magic)
When **Kabir** wants his promotion at Friday's investor demo but a review he skipped has been quietly rejecting real people, he hides it, then fights to fix it, and leaves believing that being wrong in public is the price of being right for the person on the other end.

- **Start belief:** waiting for review means being wrong in public, so I do it alone and ship.
- **Event:** the shortcut he called temporary hurts a woman paying for her mother's operation.
- **End belief:** being reviewed is not weakness. It is how a mistake gets caught before it lands on someone.

## Why (human, not views)
Kabir's father needs dialysis, and the promotion pays for it. Sunita, the applicant, needs the loan for her mother's operation. Two children paying for a parent's treatment, on opposite sides of one decision. Revealed on screen in episode 1 through a phone insert, and said aloud in episode 3.

## Cast (four others)
| Character | Who | Look | Voice (for Grok) |
|---|---|---|---|
| **Kabir Rao**, 32 | Lead ML engineer at the startup. Clicks a pencil three times before a risk. | Use the approved sheet (`REF-K`): oval face, thick tousled black hair, light stubble, thin round gunmetal glasses with clear lenses, mid-grey bomber over a muted-blue T-shirt. | Young man, warm medium-low baritone, quick, dry, tightens under stress. |
| **Riya Menon**, 24 | Junior engineer. Honest, a little scared, sharper than she lets on. | Slim, shoulder-length black hair in a low ponytail, round face, small silver stud earrings, olive kurta over jeans, lanyard, white sneakers. | Young woman, clear mid-high voice, quick, uncertain then firm. |
| **Meera Kapoor**, 44 | Founder and CEO. Warm in public, ruthless in private. | Sharp bob with a grey streak, tailored charcoal blazer over a white shirt, minimalist gold watch, still posture. | Mature woman, low-mid, calm, assertive, never raises her voice. |
| **Sunita Kulkarni**, 45 | Loan applicant. Her mother's operation is tomorrow. | Dark-brown hair in a bun with a few greys, cotton saree in faded maroon, cardigan, a plastic folder held to her chest, worn chappals. | Woman in her mid-40s, slightly raspy, tired, emotional but dignified. |

Minor roles: **Mr. Verma**, 35, lobby receptionist (a man, so his voice differs from Sunita's); **Papa** (Ramesh Rao), 62, Kabir's father, in episodes 3, 4 and 8.

## Locations
1. **Open-plan startup office** at night: glass partitions, rows of monitors, rain on a window, a few lights on.
2. **Glass meeting room and corridor** by day.
3. **Kabir's one-room rented flat**: laptop on a desk, a small shelf, a lamp.
4. **Office lobby** by day: reception desk, a sofa, a glass door.
5. **Auditorium stage** for the demo.

## Episode map
| Ep | Title | What happens | Ends on |
|---|---|---|---|
| 1 | **31** | Riya shows Kabir the pattern. Meera warns him off. He finds his own shortcut. Sunita turns up in the lobby. | Sunita says the operation is tomorrow, and the demo moves to tomorrow too. |
| 2 | **Kal subah** | Kabir tries to fix it quietly overnight. Riya catches him and gives him an ultimatum: get it reviewed, or she will. | Meera arrives and asks for his laptop. |
| 3 | **Papa** | Kabir's father calls about the dialysis fee. Meera offers a promotion and shares if he stays quiet, and reveals she saw the warning two weeks ago. | Sunita's number appears on his phone. |
| 4 | **Number 14** | He meets Sunita secretly and finds the pattern: the neighbourhood, used as a proxy. He can approve her by hand, but it will leave a log. | Meera is reading the log. |
| 5 | **Demo day** | On stage, an investor asks about fairness testing. Kabir has the slide, and the room is waiting. | He taps the microphone: "Ek baat batani hai." |
| 6 | **Public** | He confesses. The investor walks out. Meera fires him. Riya stays. | Sunita's decision is still pending. |
| 7 | **Review** | Kabir and Riya rebuild it with proper review, and invite outside reviewers. One finds a second shortcut in Meera's other product. | "Ek aur darwaza hai." |
| 8 | **Approved** | A human reviewer approves Sunita's loan after a proper check. Kabir asks Riya to review his own code, and does not click the pencil. | Riya: "Kal subah, sir." Cut. |

## Rules for writing the episodes
- **Frame one is a question,** readable with sound off. Each episode has one question that is answered only in the last seconds, or deliberately left open as a cliffhanger.
- **Spoken lines are 12 words or fewer.** One speaker per line. Interruptions only as a cut-off line ("..."), never overlapping speech, which Grok handles badly.
- **Subtext over statement.** Characters talk about the surface (Friday, a pin code, a file) and mean the deeper thing. No one says "I feel guilty." They click a pencil, look away, or change the subject.
- **Every 2 to 3 lines, something moves:** a hand, a door, a step, a glance. No static talking heads.
- **Text is added in post,** not by Grok: captions, phone messages, code lines, episode titles.
- **Pencil:** Kabir's pencil is his tell. Three clicks before a risk. In episode 8 he sets it down and does not click.

## Production notes for Grok
- Make reference stills first (image mode) for Riya, Meera, Sunita and Mr. Verma, plus the five locations, all in 9:16. Reuse `REF-K` for Kabir.
- One 15-second clip is one shot or two, with real movement. Start each clip from a still of the first frame to hold faces.
- Prompts: I write them per clip after you approve the script.
