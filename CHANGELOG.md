# Changelog

## 1.2 — hardening

### Fixed (contradictions in 1.1)
- The Why deadline was stated as 30 seconds, 30–45 seconds, by 0:45, and (in the time map) up to 1:15. It is now one rule: first spoken paragraph, aim 0:30, hard limit 0:45, with a cold open of 0:00–0:20.
- Shorts spoken-line cap was 12 words in one file and 18 in another. Shorts are 12, video-model shots are 18.
- Conflict and rasa minimums ignored runtime. They now scale by tier (Short, mid, long). Extrapolated values are labeled as such.
- The retention target is labeled a course heuristic, not a platform guarantee.
- README said "13-lesson" while the repo encodes 12 lessons plus an invitation.

### Added
- **Provenance:** a fact ledger and `FACT` / `STAGE` / `GAP` tags, so "truth first" is checkable instead of aspirational. A prospective mode for shoots that have not happened, where the ending is a prompt rather than an invented speech.
- **Safety and consent** reference: real people, minors, physical and legal risk, sensitive topics, money and health claims, sponsorship, synthetic media, music.
- **Untrusted input** handling: pasted notes and transcripts are data, not instructions.
- **Edge cases:** scope gate and light mode for tutorials and news, an anecdote ladder instead of refusal, non-interactive runs, faceless channels, pushing past a line.
- **Tiered audit** (blockers, tier checks, warnings) with a reporting format and a rule against passing a failed audit silently.
- Worked examples: a passing package, a Shorts sibling, and a deliberately failing draft.
- `scripts/lint_package.py` and `scripts/validate_skill.py` (standard library only), 17 evals, and a CI workflow.
- `assets/intake.md`, Devanagari rasa names, a contamination list for teaching examples, and new glossary keys.

### Changed
- Intake asks only for what the user alone can supply, once, and states defaults for the rest.
- "Invent mismatch" became "find or stage a real mismatch". The vlog vulnerability prompt no longer asks creators for what they "would rather hide"; the creator chooses and is never pressed.
- Rasa notes now distinguish rasa (audience experience) from bhava, and note that the Natyashastra names eight rasas with Shanta added later.
- The anecdote rule is a ladder, not "rewrite or refuse".

## 1.1
- Declared the skill LLM-agnostic.

## 1.0
- Lessons 1–12, canvases, glossary, templates, translation guide, video-model pipeline, attribution.
