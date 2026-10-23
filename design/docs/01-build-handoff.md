# Air Sew Website — Build Handoff

> **Update, Oct 20, 2026:** the visual direction is Logbook. Colors, type and component styling in the "Design system" section below are superseded by `design/design-system/` (Archivo + IBM Plex Mono, ink plates, needle red only on the primary action). Step 1 of the Start flow now leads with the tail number and an instant FAA match, with contact fields on the same screen. Everything else in this doc stands.

Oct 20, 2026 · @Tad

## Overview

Build the Air Sew marketing site so it turns a visitor into a qualified lead with a tail number and pushes that lead into the back office. The client portal at [app.air-sew.com](https://app.air-sew.com/) is a separate app; this site only links to it.

The site's job: make an owner believe Air Sew can turn a worn-out cabin into a one-of-a-kind, comfortable, personal one, and trust a small owner-run shop with their airplane.

**Source files (build from these, in this order of authority):**

| File | What it is | Use it for |
| --- | --- | --- |
| [Air Sew Design System](../design-system/) | Tokens, type, components, icon rules | Every visual value |
| [Website Mockups canvas](../mockups/) | Full-design pages, desktop + mobile, clickable | Layout, copy, interactions |
| [Website Wireframes canvas](../wireframes/) | Every page and template in gray, numbered sections | Pages not yet in full design (manufacturer, category, legal, 404) |
| Sitemap & UX Plan (doc) | Page tree, flows, decisions | Navigation and URL intent |
| Media, Motion & Trust Brief (doc) | Photo, video, scroll and motion plan per page | Media and animation |

**Principles:** airy layouts, generous spacing, one clear action per screen, every claim backed by proof. All images are placeholders generated for layout; Air Sew swaps in real photos before launch.

## Design system

Use the design system artifact's tokens as CSS custom properties; never hard-code a value the system already names. The core set:

| Token | Value | Use |
| --- | --- | --- |
| surface | #ffffff | Default page and card background |
| paper | #f8f7f4 | Alternating section band (never two in a row) |
| sky | #eef3f9 | Hero backdrop, feature bands, closing CTA |
| line | #e3e7ed | Hairline borders and dividers |
| line-strong | #8590a2 | Form control borders |
| ink | #14243d | Body text and headings |
| ink-muted | #566174 | Secondary text, captions |
| navy | #18335f | Primary buttons, links, active nav, focus ring |
| navy-deep | #10264a | Hover and pressed states |
| needle | #b71c1c | One key CTA per page, eyebrow tick, error marks |

**Type:** Fraunces (300/400) for display and headings, Manrope (400/500/600) for everything else, both from Google Fonts.

| Style | Desktop | Mobile |
| --- | --- | --- |
| Hero headline | 64/68 Fraunces 300 | 40/44 |
| Page title (h1) | 60/64 Fraunces 300 | 40/44 |
| Section heading (h2) | 36/44 Fraunces 400 | 28/34 |
| Card title (h3) | 22–24/30–32 Fraunces 400 | 20/28 |
| Lead | 20/32 Manrope | 17/27 |
| Body | 17/28 Manrope | 16/26 |
| Eyebrow | 13 Manrope 600, uppercase, 0.12em, red tick | 12 |

**Layout:** 1200 px content width, 24 px gutters (20 on mobile), section padding 96 px desktop / 64 px mobile, radii 16 cards / 10 buttons / 999 pills, buttons at least 48 px tall (52 on mobile).

**Icons:** hairline style, navy strokes at 0.6–0.9 weight with one needle-red detail per icon. The SVGs are in the mockups; export them as one icon set.

**Imagery:** real cabins, real hands, daylight, no stock smiles. Before/after pairs shot from the same angle. Every image needs meaningful alt text.

**Accessibility target:** WCAG 2.2 AA. All token pairs above already pass contrast; keep visible focus rings (navy, 2 px) and never rely on color alone.

## Page inventory and URLs

The site is 10 static pages, the Start Your Design flow and 7 CMS templates. The templates generate every aircraft, service, capability and project page; build each template once.

| Page | URL | Type | Mockup (design/mockups/*.dc.html) |
| --- | --- | --- | --- |
| Home | / | Static | LBHome, LBHomeM |
| Services hub | /services | Static | LBServices |
| Service | /services/{slug} | CMS template | LBService |
| Aircraft hub | /aircraft | Static | LBAircraft |
| Category | /aircraft/certified, /aircraft/experimental | CMS template | LBCategory, LBCategoryExp |
| Manufacturer | /aircraft/{maker} | CMS template | LBManufacturer |
| Model family | /aircraft/{maker}/{model} | CMS template | LBModel, LBModelM |
| Capabilities hub | /capabilities | Static | LBCapabilities |
| Capability | /capabilities/{slug} | CMS template | LBCapability |
| Portfolio | /portfolio | Static + CMS grid | LBPortfolio |
| Case study | /portfolio/{slug} | CMS template | LBCaseStudy |
| How it works | /how-it-works | Static | LBProcess |
| About | /about | Static | LBAbout |
| FAQ | /faq | Static + CMS FAQs | LBFaq |
| Contact | /contact | Static | LBContact |
| Start your design | /start (steps 1–6) | App flow | LBStart1–6, LBStartM1–6 |
| Privacy, Terms | /privacy, /terms | CMS template | LBLegal |
| 404 | — | Static | LB404 |

Main navigation: Services · Aircraft · Capabilities · Portfolio, with Client login (to app.air-sew.com) and the Start your design button on the right. The footer adds About, How it works, FAQ, Contact, Privacy and Terms.

Mobile: every page is responsive at 390 px. Every page has a dedicated mobile mockup (the LB…M files) (stacked sections, horizontal swipe rows, pinned bottom action bar).

## CMS content model

Seven collections drive the templates. Relations matter more than fields: a model links to its services, projects and FAQs, so one new case study shows up on the right model, service and portfolio pages automatically.

| Collection | Key fields | Relations |
| --- | --- | --- |
| Manufacturer | name, slug, logo (optional), intro, category (certified / experimental / both) | has many Model families |
| Model family | name, slug, size class (2-seat, 4–6 seat single, twin, turboprop, light/midsize jet), category, hero image, promise line, seats, layouts, cabin dimensions, burn standard (Part 23 / 25), fleet count (from FAA data, refreshed monthly), seat-map variant (standard / club), wear points (image, title, fix; 3), popular options (tags), variants (name, seats, cabin note), popular flag | Manufacturer; Services; Projects; FAQs; related models |
| Service | name, slug, icon, short line, hero image, quick facts, steps (number, title, text; 3–5), options (tags), material swatches (image, label) | Capabilities; Models; Projects; FAQs |
| Capability | name, slug, icon, tagline, hero video + poster, owner benefits (3), process steps (3–5), proof block (rich text + 2 stats), gallery | Services |
| Project (case study) | title, slug, one-line result, aircraft (year + model), scope, style, delivered (month + year), hero image, before/after pair (same angle), brief, what we did (per area), materials (label + value), detail gallery (8–12), featured flag | Model family; Services; Testimonial |
| Testimonial | quote, owner name, aircraft, home airport, portrait, permission on file (yes/no) | Project |
| FAQ | question, answer, group (quotes, downtime, materials and paperwork, working with us) | Models; Services; shown on FAQ page by group |

**Empty states:** a model with no projects shows three AI concept cabins labelled “Concept”. A testimonial only publishes when its permission field is yes.

**No downtime numbers:** there is deliberately no downtime field. Copy everywhere says the completion date is set after the design session, written into the quote and tracked in the portal.

## Components and interactions

Every interaction below is already working in the mockups; click through them on the canvas before building.

| Component | Where | Behavior |
| --- | --- | --- |
| Header | All pages | Desktop: logo, 4 nav links, Client login, Start your design button; active page underlined in needle red. Mobile: logo, Log in, menu button. |
| Mobile menu | All pages, mobile | Drops down under the header: 7 links, then Start your design (red) and Call. Closes on link tap, Escape, or second tap; focus trapped while open. |
| Pinned action bar | Home, model pages, mobile | Start your design + call icon, fixed to the bottom, respects the safe area. Hide while the on-screen keyboard is open. |
| Before/after slider | Home hero, model, service, case study | Two same-angle images; the before image is clipped from the right by the slider value. Native range input, so keyboard and screen readers work; start at 50%. |
| Seat map toggle | Model pages | Club / Standard switch redraws the top-down seat map (SVG). Horizontal on desktop, nose-up on mobile. Seat backs marked red where the layout changes. |
| In-page jump nav | Model pages | Sticks under the header; desktop links plus a Start button, mobile a swipe row of chips. Highlights the section in view. |
| Accordion FAQ | Model, service, How it works, FAQ | Button with aria-expanded; first item open; one open at a time. |
| Portfolio filters | Portfolio | Sticky chip row: All, Pistons, Twins, Turboprops, Jets, Experimental; filters the grid without a reload and updates the count. |
| Swipe rows | Mobile sections | Horizontal scroll with snap; cards 78% wide so the next one peeks in. |
| Step rail | How it works | Sticky list of the 5 steps; the active step follows scroll. |
| Closing CTA band | Every page | Sky band, headline that names the model when known, red Start button + Call. |
| Footer | Every page | Logo, location, 3 link columns, legal line. |

**Motion:** subtle and optional. Sections fade up 8 px on first view (200 ms, ease-out); capability heroes use muted, looping video with a poster and a pause control. Honor prefers-reduced-motion by turning all of it off. Detailed per-page motion is in the Media, Motion & Trust Brief.

## Start Your Design flow

Six steps, contact details first, and no tail number means no lead: the flow cannot continue past step 1 without a valid US registration. Save the lead after step 1 so a drop-off later still reaches the back office.

| Step | Screen | What happens | Rules and states |
| --- | --- | --- | --- |
| 1 | You and your aircraft | Full name, phone, email, tail number (N prefix fixed, uppercase), consent line | All four required. Tail number validated against the FAA registry before moving on. Lead record created here with status “started”. |
| 2 | Confirm your aircraft | Card with year, make, model, serial, seats, engines, category, burn standard from the registry | “Yes, that’s my aircraft” continues. “Not my aircraft” returns to step 1 with the field focused. Not found: inline error, offer to call. Deregistered or expired: same error. |
| 3 | Survey | About 10 one-tap questions, one per screen (scope, use, style with 4 image tiles, colors, materials, timing…); answers summarised in a side panel on desktop | Tapping an answer advances. Progress saves after every answer; a resume link goes out by email. |
| 4 | Cabin photos | Camera-first upload, up to 6 photos (JPG, PNG, HEIC, 20 MB each); first photo marked “For render” | “Skip, no render” jumps to step 6 and still submits the lead. Strip location metadata on upload. |
| 5 | Concept | AI render built from the photo + answers; Before / Concept toggle; “Try another version” (3 renders total); Download | Show a progress state while rendering. Label it a concept made by AI; final design is set with Air Sew. On failure: apologise, keep the lead, continue to step 6. |
| 6 | Thank you | “Thanks, \[First name\]. Your design is with us.” Owner card with direct line; “Air Sew will contact you within one business day.” | Lead status “submitted”; confirmation email with render and answers; links to the model page and portfolio. |

**Entry points:** every Start button. From a model page, the model is pre-filled and step 2 confirms it. From a case study, the style is pre-selected.

**Survey questions** are content, not code: keep them in the CMS so Air Sew can edit wording and options. The final list is still to be confirmed with Air Sew.

## Integrations and data flow

The site owns one thing: a clean lead record with a verified tail number. Everything after that lives in the back office and the client portal.

```
Aircraft owner -> Start Your Design (site)
                    |-- tail number ------> FAA registry (lookup)
                    |-- photo + answers --> AI render service
                    '-> Lead record (site DB) -> Back office -> (job won) -> Client portal (app.air-sew.com)
                                     '-> Email + SMS (owner and Air Sew)
```

The owner talks only to the Start flow; the site calls the FAA registry and the render service, writes one lead record, and hands it to the back office.

| Integration | What it does | Notes |
| --- | --- | --- |
| FAA aircraft registry | Looks up the tail number at step 1; returns year, make, model, serial, seats, engines, category | Use the FAA’s public registry data. Cache lookups. Burn standard (Part 23 / 25) is derived from category, not returned by the FAA. |
| AI render service | Restyles the cabin photo from the survey answers | Runware is used for placeholders today; final service and prompt template to be chosen. Keep the prompt server-side. Up to 3 renders per lead. |
| Lead record (site database) | Stores contact, aircraft, answers, photos, renders, status (started, submitted), source page | Created at step 1, updated each step. Photos and renders in private storage. |
| Back office | Receives each lead as a new project | Push on submit and on abandon (after 24 h at status started). Tool and API still to be confirmed by Air Sew. |
| Email and SMS | Owner: confirmation with render and answers, resume link. Air Sew: new-lead alert with everything above. | Transactional sender with SPF/DKIM on air-sew.com. |
| Client portal | Separate app at app.air-sew.com | Linked from the header, footer, portal section and Contact. No shared login with the marketing site. |

**Analytics events:** start\_design\_click (with page), step\_completed (1–6), tail\_lookup\_failed, photo\_uploaded, render\_requested, render\_failed, lead\_submitted, call\_click, client\_login\_click. Use them to see where owners drop out of the flow.

## SEO, performance, accessibility and launch

The model pages are the SEO engine: one well-built page per aircraft family, answering what owners search (“Bonanza interior”, “PC-12 seats”), is worth more than any blog.

**SEO**

- Unique title and meta description per page; templates build them from fields (“{Make} {Model} interiors | Air Sew”).
- Schema: LocalBusiness on every page, Service on service pages, FAQPage on FAQ blocks, BreadcrumbList on all interior pages.
- Clean URLs as listed above; XML sitemap generated from the CMS; canonical tags on filtered portfolio views.
- Every image gets descriptive alt text from the CMS, never the file name.

**Performance targets** (mobile, 4G)

| Metric | Target |
| --- | --- |
| Largest Contentful Paint | under 2.5 s |
| Interaction to Next Paint | under 200 ms |
| Cumulative Layout Shift | under 0.1 |

- Images in AVIF/WebP with explicit width and height; hero image preloaded, everything else lazy.
- Video: muted loops under 2 MB, poster image first, never autoplay with sound.
- Two font families, subset, font-display swap.

**Accessibility**

- WCAG 2.2 AA; keyboard reachable everything; visible navy focus ring.
- Sliders, toggles and accordions use native inputs or correct ARIA (already modelled in the mockups).
- Form errors in words, next to the field, announced to screen readers.

**Launch checklist**

- [ ] Real photos swapped in for every placeholder
- [ ] Tail number lookup tested with valid, invalid and deregistered numbers
- [ ] Lead reaches the back office and the alert reaches Air Sew
- [ ] Confirmation email and SMS tested on phone
- [ ] Analytics events firing
- [ ] 301 redirects from every current air-sew.com URL
- [ ] Privacy policy covers photo uploads and AI rendering

## Still needed from Air Sew

The build can start now; these items fill the brackets in the mockups and can land during development.

**Content**

- [ ] White logo variant (dark backgrounds, video heroes)
- [ ] Shop location, address and airport ID (About, Contact, footer)
- [ ] Repair-station status at Sky Park (certificate number, or who signs logbook entries) and insurance details (About, Certified category). Until confirmed, the site makes no Part 145 claim.
- [ ] Real photos: owner portrait, shop and hangar, team, before/after pairs
- [ ] Cabins delivered count; CNC tolerance figure (or drop the claim)
- [ ] Equipment models: cutting table, 3D printer, paint and repair setup
- [ ] Phone, email, owner name and title; typical reply time on Contact
- [ ] Final survey questions and answer options for step 3
- [ ] Portfolio projects and owner testimonials, with permission (added after launch)

**Decisions**

| Decision | Options | Needed by |
| --- | --- | --- |
| Back-office tool and how leads arrive | API, webhook, or email-to-project | Before the Start flow is wired |
| AI render service | Keep Runware or choose another; prompt template | Before step 5 is built |
| CMS / platform | Developer’s recommendation; must support the relations in the content model | Kick-off |
| Which aircraft get pages at launch | Start with the 9 popular models, add more from the CMS | Before content entry |
