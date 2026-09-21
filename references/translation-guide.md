# Translation guide

This skill is written so an LLM can emit a second-language twin without rewriting the method.

## What stays in English (keys)

Story, Anecdote, Change, Drama, Conflict, Goal, Stakes, Protagonist, Antagonist, Plot, Character, 70/30, Vulnerability, Character arc, Idle world, Inciting incident, Point of no return, Climax, Resolution, Why, Rasa, Navras, Bhava, Hasya, Raudra, Vibhatsa, Bhayanaka, Shringara, Vira, Karuna, Adbhuta, Shanta, EEI, CTR, Retention, Engagement, Hook, Hybrid, Truth.

The mechanical labels also stay in English so a video model and a human checker can find them in any language pack: FACT, STAGE, GAP, `F1`-style ledger ids, Src, Open items, Opening contract, and the `meta.*` field names.

When speaking to a local audience, put the local word first and the key in parentheses the first time.

Example, Hindi — "कहानी (Story) तब बनती है जब किरदार का सोच-तरीका बदलता है।"

## What translates freely

- Spoken script
- Titles
- Thumbnail text
- Why sentence
- Vulnerability lines
- CTA

## Title rules by script

- Keep the concrete noun.
- Keep the number or duration.
- Do not replace a dramatic verb with a soft local idiom that hides the mismatch.
- Do not add "vlog" or "must watch" in any language.

## Voice

Match the market's oral register, not literary translation. The source course is conversational Hindi. A Tamil, Spanish, or Japanese package should sound like a person on a platform, not a subtitle file.

Do not carry Indian cultural examples into a market where they do no work. Replace Lagaan with a local epic the audience already believes, then apply the same test (change, mismatch, stacked conflict, several rasas).

## Dual package

When asked to translate, deliver

1. Language-pack glossary (key → local gloss)
2. Beat sheet with bilingual labels
3. Spoken script in the target language
4. Title pack in the target language
5. English spine kept as the control so a video model can stay aligned

## Rasa names in Devanagari

For Hindi, Marathi, and other Sanskrit-derived languages, use these as the local word and keep the English key in parentheses the first time: Hasya (हास्य), Raudra (रौद्र), Vibhatsa (वीभत्स), Bhayanaka (भयानक), Shringara (शृंगार), Vira (वीर), Karuna (करुण), Adbhuta (अद्भुत), Shanta (शांत). For other languages, use the local word for the emotion and keep the key.

## Provenance survives translation

Translating a script must not add or remove facts. Re-run the audit on the translated script. A translated line that sharpens a number, adds a feeling, or hardens a claim is a new invention. Leave `[GAP: …]` placeholders in place, and translate only their descriptions.

## Kill list in every language

The title kill list (vlog, must watch, you won't believe, part 1) applies to the local equivalents as well. Check the transliterated forms too, such as व्लॉग.

## Numbers, dates, and names in TTS

Write numbers and dates the way the market speaks them. Mark proper names, brands, and place names so they are not translated or mangled. Record the language code (for example `hi-IN`, `mr-IN`, `ta-IN`) in `meta.language`.

## Video-model language

If a video generator will speak the lines, write short clauses. Avoid idioms that collapse in TTS. Mark proper names in the source script so they are not translated.
