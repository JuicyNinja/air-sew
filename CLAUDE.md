# Air Sew website: build instructions for Claude Code

You are building the new Air Sew marketing site from the approved design package in `/design`. Tad (owner) and Claude designed it together; your job is to turn it into a production site that matches it closely.

## What this site is

- A marketing site for Air Sew, an owner-operated aircraft interior shop. Its job is to turn a worn-out, tired cabin into a one-of-a-kind, comfortable, personal flying experience, and to make owners trust a boutique shop with a big-ticket job.
- One conversion path everywhere: **Start your design** (a 6-step flow that captures a lead with a verified tail number).
- The client portal at https://app.air-sew.com is a separate app (repo `JuicyNinja/airsew-app`). This site only links to it ("Client login").

## Read these first, in this order

1. `design/docs/01-build-handoff.md`: the build spec (pages, URLs, content model, components, Start flow, integrations, SEO, launch checklist). **This is the source of truth.**
2. `design/screenshots/`: a rendered image of every page. Look at these before writing a page.
3. `design/mockups/*.dc.html`: full-design source for each page (layout, exact copy, spacing, interactions). See "Reading the mockups" below.
4. `design/design-system/`: tokens (`tokens.json`), component specs, icon rules, logo.
5. `design/docs/04-design-audit-and-directions.md`: the audit and three visual directions (`ConceptA/B/C` mockups). **Wait for Tad to pick a direction before styling pages**; the structure, content and flows above don't change.
6. `design/docs/02-sitemap-ux-plan.md` and `03-media-motion-trust-brief.md`: background on structure, media and motion. Where they disagree with the handoff or mockups, **the handoff and mockups win** (they are newer).
7. `design/wireframes/`: gray wireframes. Use them only for pages that have no full-design mockup: manufacturer page, Certified/Experimental category pages, Privacy/Terms, and 404.

## Reading the mockups

Each `*.dc.html` file is one page. Inside `<x-dc>` is plain HTML with inline styles. Values in `{{double braces}}` are filled by the `renderVals()` method in the `<script data-dc-script>` at the bottom of the file, and `onClick="{{fn}}"` / `onInput="{{fn}}"` are event handlers defined there. That script is how each interaction is meant to behave (before/after slider, seat-map toggle, accordions, filters, Start-flow state).

To view a mockup in a browser: `cd design && python3 -m http.server 8765`, then open `http://localhost:8765/mockups/Main.dc.html`. The `support.js` next to the files is a small preview shim; it is not part of the product.

| Mockup file | Page |
| --- | --- |
| Main | Home (desktop) |
| HomeM | Home (mobile, 390px) |
| ModelBonanza / BonanzaM | Aircraft model template, filled for the Beechcraft Bonanza (desktop / mobile) |
| Services | Services hub |
| ServiceSeats | Service template, filled for Seats & upholstery |
| Aircraft | Aircraft hub |
| Capabilities | Capabilities hub |
| Capability | Capability template, filled for CNC sewing & cutting |
| Portfolio | Portfolio |
| CaseStudy | Case study template |
| Process | How it works |
| About, Faq, Contact | Those pages |
| Start1–Start6 / StartM1–StartM6 | Start Your Design flow (desktop / mobile) |
| ConceptA / B / C (+M for mobile) | Visual directions under review: Logbook, Atelier, Altitude |

Rebuild these as real, reusable components. Don't copy the inline styles verbatim; use the design tokens.

## Stack (recommended; Tad can override)

- **Astro** with content collections for the CMS model in the handoff (manufacturers, model families, services, capabilities, projects, testimonials, FAQs). Static pages, so they're fast and good for SEO.
- **Serverless API routes** for the Start flow: FAA tail-number lookup, AI render, and lead create/update/push.
- **Supabase** for lead records and private photo/render storage.
- **Vercel** for hosting.
- Keep JS light: vanilla or small islands for the slider, toggles, filters and the Start flow.

## Non-negotiable rules

- **Tail number required.** The Start flow can't move past step 1 without a tail number that is found on the FAA registry. Create the lead record at step 1, so a drop-off is still a lead.
- **No downtime numbers or ranges anywhere.** Tad's rule. The copy is: the completion date is set after the design session, written into the quote, and tracked in the client portal. This overrides any older doc that mentions typical weeks or a downtime table.
- **No invented facts.** Anything in `[square brackets]` in the mockups is a placeholder that Tad will fill: name, phone, certificate number, address, counts, quotes. Keep it as a visible placeholder or a CMS field. Never make up a value.
- **Location is not final.** The shop is relocating. Don't hard-code an airport or address (not KBMC, not Sky Park); use a single config value.
- **Images are placeholders.** Everything in `design/assets/img/` was AI-generated for layout. Tad will swap in real photos. `assets/img/full/real/` (from the old site) holds real Air Sew shop photos; prefer those wherever one fits.
- **Accessibility:** WCAG 2.2 AA, native inputs for the slider and toggles, visible focus, and honor `prefers-reduced-motion`.
- **One red (needle) call-to-action per page.** Everything else in the UI is navy.

## The existing site in this repo

The root `*.html`, `assets/` and `build.py` files are the **previous** redesign (static, GSAP). The new site replaces it. Don't delete the old files until the new build is ready to deploy. Plan 301 redirects from the old URLs (for example `cessna-182.html` → `/aircraft/cessna/182`).

## Working with Tad

Tad is direct and wants momentum. Build in vertical slices and show progress:

1. Tokens, layout, header and footer
2. Home
3. Model template
4. Start flow
5. The rest

Flag anything that won't work as designed rather than silently changing it. Open decisions are listed at the end of the handoff doc.
