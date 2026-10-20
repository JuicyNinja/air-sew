# Air Sew — design package

Everything Claude Code needs to build the new site. Start with `/CLAUDE.md` at the repo root. Direction: **Logbook** — the `LB*` mockups and screenshots are the ones to build.

| Folder | What's in it |
| --- | --- |
| `docs/` | 01 Build handoff (source of truth) · 02 Sitemap & UX plan · 03 Media, motion & trust brief |
| `screenshots/` | Rendered image of every mockup and wireframe |
| `mockups/` | Full-design pages, desktop + mobile (`*.dc.html`) |
| `wireframes/` | Gray wireframes for every page and template, incl. pages not yet in full design |
| `design-system/` | Tokens, component specs, icon rules, logo |
| `assets/img/` | Placeholder imagery used in the mockups (AI-generated; to be replaced with real photos) |
| `assets/logo/` | Air Sew logo (white version still to come) |

Preview locally: `python3 -m http.server 8765` from this folder, then open `/mockups/Main.dc.html`.
Screenshots of mobile pages show the pinned bottom bar mid-page; that's the sticky bar captured in a full-page shot, not a layout bug. Fonts fall back to Georgia in the screenshots; the real site loads Fraunces and Manrope.
