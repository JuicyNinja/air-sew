# Air Sew Website — Design Audit & Improvement Plan

Oct 20, 2026 · @Tad

## Verdict

The current design is clean, honest and on-brief for “airy”, but it reads as a template. Every section is the same kit (eyebrow, serif heading, gray lead, grid of identical rounded cards) on alternating pale bands, so nothing builds to a climax and the transformation, the one thing we sell, is staged at half width. The fix is not more decoration: it is rhythm, scale and one signature idea per page.

This audit used the frontend-design and design-critique skills plus an independent fresh-eyes review of all 52 screenshots. Mobbin could not be used: its connector returned “requires a paid plan”, so there are no Mobbin references in this round. Three directions are built and clickable on the mockups canvas under **Design directions — pick one**.

## Audit findings

Ranked by impact on trust and conversion.

| # | Finding | Where | Fix |
| --- | --- | --- | --- |
| 1 | Every section uses the same kit, so pages feel templated and monotonous | Sitewide | Cut eyebrow labels by about 70%; give each page one section that breaks the grid (full-bleed image, oversized quote, dark band); vary section heights on purpose |
| 2 | The transformation is staged small: a half-width slider whose track reads like a video scrubber, reused three times | Home hero, model, services | One full-bleed before/after per page with a real drag grip on the seam; different pairs on different pages |
| 3 | Needle red is on eyebrows, numerals, bullets, checks and nav, so the one red button no longer stands out | Sitewide | Red only on the primary CTA (and the seam mark if we adopt it); everything else navy or neutral |
| 4 | No people or proof where trust is decided; trust strip text is footer-sized | Home, model | Owner portrait and promise right after the hero; testimonial band; certificate shown as a real, legible badge |
| 5 | Text too small and too gray in many places (12–13 px card body, 9 px caps) | Sitewide | 16 px body minimum, 14 px meta, no tracked caps under 11 px, muted text at least #545e6c |
| 6 | How it works is about 3,500 px of five identical blocks, then a second numbered list | Process | Pinned scroll story: one image swaps as the steps scroll; fold “Your date” into step 02 |
| 7 | The concept render, the reward of the whole flow, is a modest card with a toggle | Start 5 | Near-full-width render, their photo vs concept on the same drag slider, a short reveal, send button directly under it |
| 8 | Step 1 asks for everything before giving anything back; consent checkbox missing on mobile | Start 1, StartM1 | Tail number first with an instant FAA match, then contact on the same screen (lead still created at step 1); add consent on mobile |
| 9 | Mobile scrollers start at the screen edge and clip; seat map eats a whole phone screen | HomeM, BonanzaM | 20 px gutter and scroll padding on every swipe row; cap the seat map height |
| 10 | Model pages don’t yet feel like they know the airplane: generic seat map, quiet variants table | Model template | Technical-plate seat plan drawn from the real fuselage; stronger variants table with tabular figures |

## Keep

- **The copy voice.** “Most shops go dark until the job is done. We don’t.” and “Your date, in writing” are specific and honest. Every direction keeps them.
- **The portal preview.** Progress by zone, findings with Approve, the records packet: it makes the visibility promise concrete. Make it bigger, not different.
- **The FAA confirmation card.** A real registration card is both trustworthy and satisfying; Direction A makes it the hero.
- **Mobile Start flow ergonomics.** Back / step / Call bar, thumb-zone buttons, large inputs, photo tiles.
- **The palette.** Navy and needle red from the logo are right; the problem is how often red is used, not the colors.

## Three directions

All three fix the findings above; they differ in personality. Each has a desktop and a mobile board on the canvas, and each is interactive.

|  | A · Logbook | B · Atelier | C · Altitude |
| --- | --- | --- | --- |
| Idea | The precision of aviation paperwork | The tactility of bespoke upholstery | A calmer, bigger version of what we have |
| Type | Archivo (wide) + IBM Plex Mono for tail numbers, serials, dimensions | Bodoni Moda (display) + Hanken Grotesk | Fraunces (soft, much larger) + Manrope |
| Hero | “Tell us your tail number” with a live FAA data plate and drawn seat plan | Full-screen before/after you drag, headline over the photo | Huge centered headline over a wide finished cabin |
| Signature | Registry plate, annotated before/after with numbered callouts, job file as a work-order table | Stitched seam line that sews itself in once, edge-to-edge material close-ups, dark portal band | Pinned scroll story: Arrives → Stripped → Built → Delivered, services as quiet lists |
| Motion | Data plate resolves after lookup | Seam draws across under the hero; drag grip | Image swaps as you scroll through stages |
| Feels like | An MRO you’d trust with a King Air | A tailor you’d trust with a Citation | A refined version of today |
| Risk | Can feel cold if photography is weak | Depends on great photography; serif is a bold change | Safest; least distinctive |

**Recommendation: B · Atelier as the base, borrowing A’s data plate for the Start flow and model pages.** The business is moving up-market to bigger, costlier jobs, and the emotional sell is the transformation of a space people sit in; Atelier sells that best. A’s registry plate and technical seat plan are the strongest trust devices we have, so they carry over where precision matters (tail lookup, model specs, records). C is the fallback if you want the least change from what’s built.

## Improvement plan

These apply whichever direction you pick.

**Spacing and rhythm**

- 8 px base scale; section padding 140 px desktop / 64 px mobile for feature sections, 96 / 48 for supporting ones, so pages breathe unevenly on purpose.
- One full-bleed moment per page; at most two tinted bands per page and never two in a row.
- Replace card grids with lists and edge-to-edge image strips where the content is a list (services, values, options).

**Typography**

- Display sizes up: hero 96–120 px desktop, 48–56 px mobile; section headings 52–64 px. Fewer, larger headings.
- Body 17–19 px desktop, 16 px mobile; meta never below 14 px; line length under 75 characters.
- Drop uppercase eyebrows except where they carry information; use tabular figures for numbers, tail numbers and specs.

**Flow**

- Home: hero (transformation) → owner and promise → craft close-ups → portal → proof (testimonial, projects) → process → CTA.
- Start flow: tail number first with an instant match, contact on the same step, then the survey; render step becomes the big reveal.
- One primary action per screen; secondary actions as text links.

**Motion and scroll** (each one only where it tells the story)

| Effect | Where | Rule |
| --- | --- | --- |
| Drag before/after with a grip | Hero, model, case study | Keyboard arrows move it; hint nudge once on load |
| Seam line draws once | Under the hero (Atelier) | 2.4 s, once per visit |
| Pinned scroll story | How it works, case study | Image pinned, text scrolls; becomes a stepper on mobile |
| Data plate resolves | Tail lookup, Start 2 | 400 ms reveal after the FAA match |
| Render reveal | Start 5 | Cross-fade from their photo to the concept |

No parallax, no fade-up on every card, no counters, no autoplaying carousels. Everything has a static version under prefers-reduced-motion.

**Responsiveness**

- Design at 390, 768, 1280 and 1440; fluid type with clamp() between them.
- 20 px gutters and scroll padding on every horizontal row; pinned bottom action bar on mobile only, hidden while typing.
- Touch targets at least 48 px; seat plan and tables reflow, never scroll sideways.

**Accessibility**

- WCAG 2.2 AA contrast for all text including on photos (scrim behind headlines over images).
- Native range input for sliders, real buttons for toggles, visible 2 px focus ring.
- Alt text names the aircraft and the change shown.

## Next steps

1. You pick a direction (or a mix) on the canvas.
2. I update the design system tokens and type to match, then redo Home, the model template and the Start flow in the chosen direction, desktop and mobile.
3. I push the updated design package to the repo branch so Claude Code builds from the new direction.
4. The remaining pages follow the same patterns.
