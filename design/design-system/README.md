Air Sew builds and restores aircraft interiors. The brand is light, precise and hand-made: a lot of white space, a calm navy, one red needle. Every page should feel like a freshly finished cabin — clean, quiet, nothing extra.

## Principles

- **Air first.** White (`surface`) is the main material. Sections breathe at `space-4xl` (96px) top and bottom on desktop; when unsure, choose the bigger spacing step.
- **One idea per section.** A heading, a short paragraph, one action. Long pages are fine; crowded sections are not.
- **Navy carries, red points.** `navy` does the work (buttons, links, headings that need weight). `needle` appears only where the eye should land — one key CTA, the eyebrow tick, the active-link underline.
- **The work is the hero.** Photography of seats, stitching and finished cabins does the selling — in-house photos of real work wherever we have them, AI imagery to show the class of cabin we're building toward. No stock photos of jets or smiling pilots.

## Content fundamentals

- Voice: a master craftsman talking to an owner-pilot — direct, specific, calm. "We" for Air Sew, "you" and "your aircraft" for the reader.
- Sentence case everywhere: headings, buttons, nav. Uppercase only in the `eyebrow` style.
- Lead with the material and the result: "New foam, Italian leather, original stitch pattern" beats "premium quality solutions".
- Name aircraft by make and model ("Beechcraft Baron 58"). Numbers as numerals (3–5 weeks, 6 seats).
- No emoji, no exclamation marks, no superlatives we can't prove.
- Example lines: "Cabins worth flying in." · "Every seat comes off, gets stripped to the frame and rebuilt." · "Request a quote".

## Color

- Page ground is `surface`. Alternate full-width bands with `paper` (warm) or `sky` (cool) — never the same tint twice in a row, and at most one `linen` band per page for craft/materials content.
- Text is `ink`; secondary text `ink-muted`. Both pass 4.5:1 on every light ground.
- Links and primary buttons: `navy` with `on-navy` text; hover `navy-deep`.
- `needle` is the accent. Never use it for body text or large fills. Errors also use `needle`, always with words.
- The footer may sit on `navy-deep` with `on-navy` text; nothing else goes dark.
- Hairlines (`line`) separate; `line-strong` outlines inputs on `surface` only.

## Typography

- Headings: Fraunces (light 300 / regular 400), a soft, crafted serif that echoes the script logo without competing with it. Styles `display`, `h1`, `h2`, `h3`.
- Everything else: Manrope — open, highly legible. Styles `lead`, `body`, `body-sm`, `eyebrow`, `button`, `caption`.
- Body is 17px on 28px. Keep text blocks to the `measure` token (680px, ~70 characters).
- Put an `eyebrow` (navy, with the short needle tick) above every h1/h2; `space-xs` between them, `space-lg` from heading to copy.
- Never set the brand name in Fraunces as a logo substitute — use the logo.
- Both faces load from Google Fonts (`components/bundle.css` imports them).

## Spacing and layout

- 4px base scale `space-2xs` … `space-5xl`. Section padding `space-4xl` desktop / `space-3xl` mobile; hero `space-5xl`.
- Content max width `container` (1200px), 12-column grid with `space-lg` gutters; card grids are 3-up desktop, 2-up tablet, 1-up mobile.
- Left-align text. Center only a short closing CTA band.

## Shape, depth, motion

- Radii: `radius-sm` inputs, `radius-md` buttons, `radius-lg` cards and photos. Nothing sharper, nothing bubblier.
- Depth is quiet: borders first; `shadow-soft` for resting cards on white, `shadow-lift` on hover and for the scrolled header.
- Motion: 150–200ms ease on color, shadow and a 2px lift. No parallax, no auto-playing carousels.
- Focus: a 2px solid `navy` outline offset 3px on every interactive element (12:1 on white).

## Logo

- Use the Logos asset as supplied, on `surface`, `paper` or `sky` only. Minimum height 32px on screen; clear space on every side equal to the height of the "A".
- Header logo height: 40px.
- Don't recolor, stretch, outline, add effects, or place it on photos or navy. A one-color white version for dark grounds still needs to be produced from the vector source.

## Imagery

The library mixes two sources. Both follow the same look so they sit side by side: daylight or soft hangar light, neutral and warm materials, close crops, clean backgrounds, no lens flare or heavy grading.

Mix in-house photography of real work (stitching close-ups, foam and frames, the shop at work, before/after pairs, finished cabins) with AI imagery of the larger cabins we build toward (club seating, divans, cabinetry, sidewalls). Detail and material shots — leather grain, stitch rows, a seat back in light — carry the brand best from either source.

- No real airline or OEM logos, tail numbers or registration marks in generated images.
- Frame photos at `radius-lg`; 4:3 in cards, 3:2 or 16:9 in bands. Caption in `caption` style, `ink-muted`.

## Iconography

The Icons group is Air Sew's own set: 32 hairline icons drawn on a 24-unit grid, exported at 48px with a 1.2px navy (`#18335f`) stroke, round caps and joins. Each icon carries at most one accent in `needle` (`#b71c1c`): a dashed running stitch on craft icons, and the one meaningful detail elsewhere — the check, the clock hand, the window shade, the before/after divide. Contact and UI icons are navy only.

- Interiors: `seat`, `divan`, `sidewall`, `headliner`, `cabin-window`, `carpet`, `cabinetry`, `embroidery`, `leather`, `foam`, `refinish`, `stitch`.
- Process and trust: `inspect`, `measure`, `logbook`, `certified`, `turnaround`, `calendar`, `before-after`, `quote`.
- Aviation: `aircraft`, `hangar`.
- Contact and UI: `phone`, `mail`, `location`, `check`, `arrow-right`, `external`, `chevron-down`, `plus`, `menu`, `close`.
- Hairlines need room: 24px minimum, 32px beside headings and in cards, 48px as feature icons. Never below 24px; never thicken the stroke.
- Use on light grounds (`surface`, `paper`, `sky`, `linen`). On `navy-deep` (footer), inline the SVG and set both strokes to `on-navy`.
- Icons support a label; they never stand alone without an accessible name, and never sit in colored circles or tiles.
- New icons: same grid and stroke, one red accent at most, the dashed stitch only for things we sew or upholster.

## Components

`Header`, `Hero`, `Button`, `Card`, `FormField` — CSS classes prefixed `as-` in `components/bundle.css`, wrapped in an `.as-root` element. See each component's guidelines.
