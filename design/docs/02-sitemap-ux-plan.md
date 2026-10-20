# Air Sew Website — Sitemap & UX Plan

Oct 19, 2026 · @Tad

## Goal

The site has one job: make an owner believe Air Sew is the best shop for their aircraft, then get them into Start Your Design. Every page ends on that path.

- **Marketing site** (air-sew.com): proof, depth, and the design flow. Public, fast, airy.
- **Client portal** (app.air-sew.com): existing customers log in. Linked from the header as "Client login", nothing else from the portal lives here.
- **Back office**: every Start Your Design submission and contact form is pushed in as a new lead with aircraft data, survey answers, photos and the AI concept attached.

Three jobs on every page, in order: show we know *their* aircraft, prove we've done the work, make the next step effortless.

## Sitemap

&#91;embedded content: air-sew.com sitemap · 5 primary sections\]

Primary nav: Services, Aircraft, Capabilities, Portfolio, and Start Your Design as the highlighted button. Client login sits top right and leaves for the portal; supporting pages live in the footer.

## Services

One hub page plus a page per service, grouped the way an owner thinks about the airplane: inside the cabin, then outside.

| Group | Page | URL | Icon |
| --- | --- | --- | --- |
| Cabin | Seats & upholstery | /services/seats | seat |
| Cabin | Divans & club seating | /services/divans | divan |
| Cabin | Sidewalls & panels | /services/sidewalls | sidewall |
| Cabin | Headliners | /services/headliners | headliner |
| Cabin | Carpet & flooring | /services/carpet | carpet |
| Cabin | Cabinetry & galleys | /services/cabinetry | cabinetry |
| Cabin | Windows, shades & reveals | /services/windows | cabin-window |
| Cabin | Plastics & trim refinishing | /services/plastics | refinish |
| Cabin | Soft goods & embroidery | /services/soft-goods | embroidery |
| Cabin | Seat belts & restraints | /services/restraints | stitch |
| Exterior | Cowl plugs & inlet covers | /services/cowl-plugs | aircraft |
| Exterior | Aircraft covers (canopy, wing, engine) | /services/covers | hangar |

**Hub page (/services):** hero, then the two groups as icon cards, a strip of before/after images, "Full interiors" band explaining whole-cabin refits, and the Start Your Design CTA.

**Service page template, top to bottom:**

1. Hero: service name, one-line promise, hero image, primary CTA "Start your design".
2. What we do: 3–5 short blocks with icons (strip, rebuild, materials, finish, documentation).
3. Materials & options: leather, fabric, foam, thread, colors — with swatch images.
4. Gallery: 6–9 images, before/after slider first.
5. Aircraft we do this on: links into the matching Aircraft pages.
6. Related capabilities: e.g. seats → CNC cutting, burn-certified materials.
7. FAQ: 4–6 questions (turnaround, downtime, cost drivers, certification paperwork).
8. CTA band: "Start your design" + phone.

Cowl plugs and covers can also be a fast, priced product line later (order online by model). Worth keeping in mind for the template.

## Aircraft

Build Aircraft as three levels — manufacturer, model family, variant — with Certified and Experimental as two doors into the same tree. This is the section that wins search and makes an owner feel "they know my airplane."

**Structure**

- **/aircraft** — search box ("Find your aircraft"), two big doors: Certified and Experimental, plus a size filter (2-seat, 4–6 seat, twins, turboprops, light & midsize jets).
- **/aircraft/certified** and **/aircraft/experimental** — manufacturer grids. Experimental lists kit makers (Van's, Lancair, Kitfox, Glasair…).
- **/aircraft/beechcraft** — manufacturer page: logo-free brand intro, model families as cards.
- **/aircraft/beechcraft/bonanza** — model family page. This is the money page.
- Variants (A36, G36, V35B) are sections and anchors on the family page, not their own pages, unless their cabins genuinely differ (e.g. Piper Malibu vs M600, King Air C90 vs 350).

Why family pages, not one page per variant: hundreds of near-identical pages trigger Google's scaled-content filters and look thin to buyers. Fewer, deeper pages rank better and convert better.

**Model family page template**

1. Hero: "Beechcraft Bonanza interiors", model photo, CTA "Start your Bonanza design" (pre-fills the aircraft in the form).
2. Cabin at a glance: seat count, standard layouts (club, forward-facing), cabin dimensions, which burn standard applies.
3. What wears out on this airplane: model-specific (e.g. seat-back plastics cracking, headliner sag, sun-faded sidewalls) — written from shop experience.
4. What we do on it: links to the relevant Services, each with a line specific to this model.
5. Options & upgrades: popular materials, stitch patterns, lighting, USB/power, sound deadening.
6. Our work on this model: Portfolio projects filtered to this family (hidden until one exists; AI concept images until then).
7. Variants we cover: list with years.
8. FAQ: downtime, ferry or pickup, typical cost range, paperwork (337 / logbook entries).
9. CTA band.

**Unique data per page:** pull a registered-fleet count from the FAA registry ("\[count\] Bonanzas on the US register", refreshed monthly) and model-specific notes. That makes each page different from every competitor's.

**Rollout waves**

| Wave | Scope | Pages |
| --- | --- | --- |
| 1 — launch | Highest-volume pistons and the turboprops/jets you're targeting: Cessna 172/182/206/210, Piper PA-28/32/34/46, Beechcraft Bonanza/Baron/King Air, Cirrus SR20/22, Mooney M20, Pilatus PC-12, Daher TBM, Cessna Citation CJ, Embraer Phenom, Van's RV | \~25 families |
| 2 — month 2–3 | Remaining common pistons, Diamond, Grumman, Commander, more light jets, top kit planes | \~30 |
| 3 — ongoing | Long tail as projects and leads come in | as needed |

Pages live in a CMS collection (manufacturer, family, variants, category, seats, size class, burn standard, wear notes, images) so adding a model is data entry, not design.

## Capabilities

Capabilities are the "how" behind the services: proof that Air Sew is a modern shop, not a guy with a sewing machine. Four pages under one hub.

| Page | URL | What it proves | Page's star asset |
| --- | --- | --- | --- |
| CNC sewing & cutting | /capabilities/cnc | Repeatable, factory-precise patterns and stitching; digital patterns kept on file for every aircraft | Video: CNC head running a quilted pattern |
| 3D printing | /capabilities/3d-printing | Out-of-production trim, bezels and brackets reproduced instead of hunted | Before/after of a remade part |
| Plastic repair & restoration | /capabilities/plastics | Cracked, faded panels brought back without replacement cost | Before/after slider |
| Burn-certified materials | /capabilities/burn-certified | Every material meets the applicable FAR flammability standard (Part 23 / Part 25 §25.853), with paperwork delivered | Sample of the certification packet |

**Capability page template:** hero with motion (short silent video loop), "what it means for your aircraft" in 3 points, process strip (scan → pattern → cut → sew / print → finish), equipment and specs, gallery, services that use it, CTA.

The burn-certified page doubles as the trust page for turboprop and jet owners and their maintenance directors — write it for them: standards, test method, what paperwork they receive, sample documents.

## Portfolio

Featured Projects is a filterable grid of case studies; each project is a story, not just photos.

- **/portfolio** — 3-up grid of project cards, filters for aircraft size class, manufacturer and service. Featured projects pinned at the top with a large lead image.
- **/portfolio/\[project\]** — case study page.

**Case study template**

1. Hero: aircraft (make, model, year), one-line result, full-width finished-cabin image.
2. The brief: what the owner wanted, in their words if possible.
3. Before / after slider.
4. What we did: services and capabilities used, each linked.
5. Materials: leather, fabric, thread, stitch pattern, color names with swatches.
6. Detail gallery: 8–12 close-ups.
7. Numbers: seats, downtime in weeks, parts remade.
8. Owner quote with name and aircraft.
9. CTA: "Start a design like this" (pre-fills aircraft type and style answers in the form).

Every case study is tagged to its Aircraft family and Services, so it automatically appears on those pages. One strong project lights up three or four pages at once.

## Start Your Design

A six-step guided flow at /start that turns a visitor into a fully qualified lead and gives them something exciting back: a concept render of *their* cabin. One question per screen, progress bar on top, back button always available, nothing longer than a minute per step.

1. **You and your aircraft.** Name, phone, email and tail number (N-number) — all four required; no tail number, no next step. The lead is created in the back office the moment this step is submitted, so an abandoned flow is still a lead to call.
2. **"Is this your aircraft?"** We look up the N-number and show a confirm card: make, model, series, year, serial number, seats, engines, category (standard/experimental). Owner confirms or edits. If the tail number isn't on the FAA register, the flow stops there with "We couldn't find N12345 — check the number or call us," and the contact still lands in the back office as a lead.
3. **The survey.** 8–10 tap-to-answer questions, mostly picture tiles and icons:
   - Scope: which areas (seats, sidewalls, headliner, carpet, cabinetry, plastics, covers…)
   - How the aircraft is used: personal, family, business, charter
   - Style direction: classic, modern, executive, sport (image tiles)
   - Color palette: light, warm neutral, dark, two-tone (swatches)
   - Materials: leather, synthetic leather, fabric, combination
   - Stitch and detail: diamond, channel, perforated inserts, piping, embroidered logo
   - Extras: headrests, lighting, power/USB, sound deadening
   - Timing: when the aircraft can be down
   - Budget range (bands, including "not sure yet")
   - Home airport
4. **Show us your cabin.** Upload 1–6 photos of the current interior (phone camera opens directly on mobile). Optional, but needed for the render.
5. **Your concept.** AI renders their photo restyled from a prompt built from their answers. Shown as a "concept render" with the answers summarized beside it; up to two regenerations; download and share.
6. **Thank you.** "Air Sew will contact you shortly" with a named person, photo, and expected response time. Email confirmation with the concept attached. Buttons: explore their Aircraft page, see Portfolio.

**Tail number lookup.** The FAA publishes its full registry as a free download, refreshed daily ([FAA Releasable Aircraft Database](https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download/)). Load it nightly into our own database and query it by N-number — faster and more reliable than scraping the FAA's search page, which can change or block us. The make/model reference file in the same download also gives seats and engine count. Some owners have their name and address withheld from public release, so never depend on owner data being there.

**Lead handoff to the back office.** One record per submission, updated as they progress: contact, N-number, full registry data, every survey answer, photos, render(s), step reached, source page and campaign. Instant alert to sales for every completed flow; a follow-up task for abandoned ones after 24 hours. Pre-fills: arriving from an Aircraft or Portfolio page carries the model (and style) into the form.

## Conversion and trust

One action everywhere — "Start your design" — backed by proof on every page, so the decision feels safe before the owner ever calls.

- **One CTA, everywhere.** Header button on every page, a sticky bottom bar on mobile, a closing CTA band at the end of every page. Phone number in the header for the owners who'd rather call.
- **Speak to their airplane.** Site search "Find your aircraft" in the hero; Aircraft and Portfolio pages pre-fill the form.
- **Trust strip** under every hero: repair station certification, burn-certified materials with paperwork, insured, years in business, aircraft completed.
- **How it works** (/process): 5 steps from design to delivery, with downtime expectations, pickup/ferry options and what paperwork they get back. This answers the big unspoken question for first-timers.
- **People.** Name and face of who will call them, on the thank-you screen and the About page.
- **Reviews and owner quotes** on service, aircraft and case study pages, always with the aircraft named.
- **Speed.** Respond to completed designs within one business day; say it on the site and keep it.

**Pages to add to your sitemap:** About (/about), How it works (/process), FAQ (/faq), Contact (/contact), plus Privacy and Terms (needed for the form, AI renders and photo uploads).

## Where this may not work, and decisions for Tad

1. **Contact first with a required tail number filters hard.** Expect drop-off at step 1; the trade is that every starter is a real owner with a real aircraft. Keep the step feeling quick: four fields, the N-number formatted as they type, and one line under it saying why we ask ("so we can pull your aircraft's specs"). Shoppers without a tail number get the phone number and Contact page.
2. **The render sets expectations.** Owners will treat it as a promise. Label it "Concept render", keep it on the photo they uploaded, and say a designer finalizes materials and layout on the call.
3. **Aircraft pages are a writing job.** \~25 strong family pages at launch is real work: model-specific wear notes and options have to come from you. Plan one sitting per manufacturer; the CMS does the rest.
4. **Certification claims must match reality.** With the shop relocating, everything the site says about the repair station certificate, location and capabilities has to match the current certificate on launch day.
5. **Thin portfolio at launch.** Launch with whatever finished projects you have, even three. Aircraft and Services pages carry AI concepts until real projects are tagged in.
6. **Render cost and abuse.** Limit renders per email and per day, and only render after step 1 is complete.

**Decisions needed**

- [ ] Step order: decided — contact first, tail number required
- [ ] Back-office tool name and how it accepts leads (API or webhook) — needed to spec the handoff
- [ ] Launch list of aircraft families for Wave 1
- [ ] Who appears as the contact person on the thank-you screen
- [ ] Cowl plugs and covers: quote-only, or priced and orderable online later
