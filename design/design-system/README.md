Air Sew builds and restores aircraft interiors. The visual direction is **Logbook**: the precision of aviation paperwork applied to a craft business. White pages, ink hairlines, data plates and registers, a wide grotesk for headlines and a monospace face for the numbers owners care about. It should feel like a shop that documents everything, because it does.

## Principles

- **Show the record.** Tail numbers, seat counts, burn standards, sign-off dates and work orders are the proof. Set them as data (plates, registers, the job file), not as marketing claims.
- **One signature per page.** Each page gets one moment that breaks the grid: the tail-number lookup, the full-width before/after wiper, the job file. Everything around it stays quiet.
- **Ink carries, red acts.** `ink` and `navy` do all the structural work. `needle` red is reserved for the primary action and nothing else.
- **The work is the hero.** Real cabins, real hands, same-angle before/after pairs. Photos are square-cornered and run full-bleed when they matter.

## Content fundamentals

- Voice: a master craftsman talking to an owner-pilot. Direct, specific, calm. "We" for Air Sew, "you" and "your aircraft" for the reader.
- Sentence case everywhere. Headings end with a period. No uppercase labels, no arrows on links or buttons, no emoji, no exclamation marks.
- Name aircraft by make and model ("Beechcraft A36 Bonanza"). Numbers as numerals, in the mono face.
- Never publish downtime numbers or ranges: the completion date is set after the design session, written into the quote and tracked in the client portal.
- Aviation vernacular where it's honest: squawk list, work order, signed off, records packet.

## Color

- Page ground is `surface`. `draft` is the only tint, for alternating bands; never two in a row. `navy-deep` is used once per page for the closing call-to-action band.
- Text is `ink`; secondary text and mono labels `ink-muted`.
- Plates and the 1.5px section rules are `ink`. Inside plates and tables, hairlines are `line`; list dividers are `rule`. Form controls use `line-strong` or `ink` (3:1 minimum).
- `needle` only on the primary action of the page (it may repeat for the same action, e.g. Find my aircraft in the hero and closing band). `success` for Registration valid, Sent, Signed off, always with words.

## Typography

- **Archivo** (Google Fonts, variable width). Headlines at weight 500 and width 112 (`font-variation-settings: 'wdth' 112`), tight tracking; body at width 100. Styles `display`, `h1`, `h2`, `h3`, `lead`, `body`, `body-sm`, `button`.
- **IBM Plex Mono** for data only: tail numbers, serials, seat counts, dates, prices, plate labels, step numbers. Styles `label`, `data`, `data-lg`. Always tabular figures.
- Sizes: display 76/78 (mobile 42/44), h2 44/50 (mobile 30/34), body 17/28, nothing below 14px except mono labels at 13px.
- Keep running text to 680px (`measure`).

## Signature components

- **Data plate.** 1px ink border, 2px radius, a header row with the tail number in `data-lg` and a status in mono, then a two-column `dl` of label and value with `line` hairlines. Optional seat plan below. Used in the hero, Start flow, model spec and job file.
- **Tail field.** Fixed "N" prefix on `draft`, 24px mono input, 1.5px ink border; paired with the needle button.
- **Seat plan.** Top-down line drawing (ink 1px, seat backs 3px), Club / Standard segmented toggle, mono annotations. Not to scale, says so.
- **Wiper.** Full-width before/after with a 2px white seam and a round grip; native range input underneath for keyboard and screen readers; mono "Before / After" tags. One per page. Numbered pins may annotate the after image.
- **Register.** Table with mono column heads, 1.5px ink rule under the head, hairline rows. Used for aircraft lists, variants, squawk lists.
- **Job file.** Work-order table with stage, status and signed-off date; the one plate per page that gets `shadow-soft` (an offset draft block).
- **Step rail.** Six labeled segments with mono step numbers; the active step is ink, upcoming ones `ink-muted`.

## Spacing and layout

- 4px base. Feature sections `space-4xl` (120px) desktop, supporting sections 88px, mobile 56px.
- `container` 1232px with 32px side padding (20px on mobile) on a 12-column grid; the hero shows the grid as faint `line` columns.
- Left-align everything. Asymmetric splits (7/5, 6/5, 4/8) instead of centered stacks.

## Shape, depth, motion

- Radii: 4px controls, 2px plates, 0 on photos and the wiper.
- Depth comes from ink borders, not shadows. `shadow-soft` (offset block) once per page; `shadow-lift` on the wiper grip only.
- Motion only where it answers an action or tells the story: the data plate resolves in 400ms after a lookup; the wiper follows the drag; the Process and case-study pages pin one image while steps scroll. No fade-up on every section, no parallax, no counters. Everything has a static state under `prefers-reduced-motion`.
- Focus: 2px solid `navy` outline, 3px offset, on every interactive element.

## Logo

- Use the Logos asset as supplied, on `surface` or `draft` only. Minimum height 32px on screen; clear space on every side equal to the height of the "A".
- Header logo height: 36px desktop, 28px mobile.
- Don't recolor, stretch, outline, add effects, or place it on photos or navy. A one-color white version for dark grounds still needs to be produced from the vector source.

## Imagery

Real cabins in daylight or soft hangar light, close crops, no grading. Before/after pairs must share the angle. Square corners; full-bleed for the wiper and hero-level images, 4:3 in grids, captions in mono `label`. No airline or OEM logos, tail numbers or registration marks in generated images.

## Iconography

The Icons group is Air Sew's own set: 32 hairline icons drawn on a 24-unit grid, exported at 48px with a 1.2px navy (`#18335f`) stroke, round caps and joins. Each icon carries at most one accent in `needle` (`#b71c1c`): a dashed running stitch on craft icons, and the one meaningful detail elsewhere — the check, the clock hand, the window shade, the before/after divide. Contact and UI icons are navy only.

- Interiors: `seat`, `divan`, `sidewall`, `headliner`, `cabin-window`, `carpet`, `cabinetry`, `embroidery`, `leather`, `foam`, `refinish`, `stitch`.
- Process and trust: `inspect`, `measure`, `logbook`, `certified`, `turnaround`, `calendar`, `before-after`, `quote`.
- Aviation: `aircraft`, `hangar`.
- Contact and UI: `phone`, `mail`, `location`, `check`, `arrow-right`, `external`, `chevron-down`, `plus`, `menu`, `close`.
- Hairlines need room: 24px minimum, 32px beside headings and in cards, 48px as feature icons. Never below 24px; never thicken the stroke.
- Use on `surface` and `draft`. On `navy-deep` (closing band), inline the SVG and set both strokes to `on-navy`.
- Icons support a label; they never stand alone without an accessible name, and never sit in colored circles or tiles.
- New icons: same grid and stroke, one red accent at most, the dashed stitch only for things we sew or upholster.

## Components

`Header`, `Hero`, `Button`, `Card`, `FormField`, plus `.as-plate`, `.as-tail` and `.as-mono` in `components/bundle.css`, wrapped in an `.as-root` element. The full page mockups (Logbook) live on the Air Sew Website Mockups canvas.
