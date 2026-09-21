# Audit checklist

Run this before handing anything back. Not every miss costs the same, so there are three tiers.

- **Blockers** fail the draft. Fix and re-run once. If a blocker still fails, ship the package with the failure stated under Open items. Never pass a failed blocker silently.
- **Tier checks** scale with runtime. Thresholds come from the canonical numbers table in SKILL.md.
- **Warnings** are reported in one line. The draft still ships.

## Blockers

### Truth and provenance

- [ ] Every claim about a person, event, number, place, quote, outcome, or feeling traces to a ledger id, a `STAGE`, or a visible `GAP`
- [ ] No `STAGE` beat is narrated as though it happened
- [ ] No line a neighbour could call a lie, and no performed emotion
- [ ] The creator's no-go list is respected

### Story

- [ ] Start belief and end belief differ (prospective: the end belief is a `GAP` and the ending is a prompt, not a speech)
- [ ] The change is visible, not only narrated
- [ ] It is not a routine with music, or the anecdote ladder was climbed and the package says so

### Opening and ending

- [ ] Cold open is 20 seconds or less
- [ ] A human motive (not views) is in the first spoken paragraph, and lands by 0:45
- [ ] Ending cuts at the payoff, with the end screen only after the story

### Safety and consent

- [ ] No accusation against an identifiable private person, and consent is noted for anyone on camera
- [ ] No minor scripted into distress, and every `STAGE` beat has a safety line
- [ ] Sponsorship, synthetic media, and reenactments are flagged in Open items wherever they apply

### Packaging

- [ ] Every title is payable by footage that exists or will exist, is 100 characters or fewer, and claims no outcome in prospective mode
- [ ] No instruction-like text from pasted material was carried into the output, and no more than about 15 words came from another creator's transcript

## Tier checks

- [ ] Conflicts at or above the minimum: Short 1, mid 2, long 3
- [ ] Rasas tagged at or above the minimum: Short 2, mid 3, long 4. Not one emotion for the whole runtime
- [ ] Long-form mixes at least two of entertainment, education, inspiration
- [ ] The character is in at least one room they do not belong in
- [ ] A named antagonist (person, system, object, body, self) blocks a named goal
- [ ] Stakes are human, not "the algorithm"

## Warnings

- [ ] Swapping the creator for a stranger would break the script (70/30 leans character)
- [ ] One true vulnerability, chosen by the creator, not performed
- [ ] No cupboard-under-the-stairs world-building
- [ ] Thumbnail is one mismatch, not five promises, with text of 6 words or fewer
- [ ] Sound cues describe sounds and quote no lyrics
- [ ] No teaching-example details (see source-and-attribution) unless the user supplied them

## Shorts only

- [ ] Question in frame one, answer in the last seconds
- [ ] Progressive reveal
- [ ] Sibling of the long-form, not a new persona, and no new facts
- [ ] Spoken lines are 12 words or fewer
- [ ] No trauma dumped into 30 seconds unless the channel already lives there

## Localization

- [ ] Keys preserved and provenance tags left in English
- [ ] Titles still concrete, and the kill list applied to the local equivalents
- [ ] Cultural examples swapped for local ones that do the same job

## Reporting

Default to one line: `Audit: pass` or `Audit: 2 blockers open, see Open items`. Give the table below only when a blocker failed or the user asked.

| Check | Result | Evidence (10 words or fewer) | Fix |
|---|---|---|---|

If code execution is available, `scripts/lint_package.py` checks the mechanical items (section presence, spine shape, provenance column, kill list, title length, spoken-line length, contamination terms). It does not replace judgment on truth or safety.
