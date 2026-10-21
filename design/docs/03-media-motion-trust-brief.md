# Air Sew Website — Media, Motion & Trust Brief

Oct 19, 2026 · @Tad

## What this brief does

Every photo, video, graphic and motion effect on the site has one job: make an owner confident handing Air Sew their airplane. Beauty sells the transformation; proof earns the trust. This brief says what goes where, page by page, keyed to the section numbers on the wireframes canvas (01 · Hero, 02 · Trust strip…).

The trust thesis: an owner is about to give a stranger a six- or seven-figure asset for weeks. They trust what they can **see** — real hands, real work, real paperwork, a real person who answers, and a clear view of their airplane while it's gone. So the site shows, it doesn't claim.

## Trust principles

Seven rules. Any image or effect that doesn't serve at least one of them comes out.

1. **Show the hands.** People trust craft they can watch: needles, stitching, foam being cut, a hand smoothing leather. Faces and hands beat empty, perfect cabins.
2. **Show the person.** The owner appears on Home, About, How it works and the thank-you screen — same person, same name. A boutique shop is trusted because there's a someone.
3. **Show the paperwork.** Burn certs, logbook entries, the records packet and the repair station certificate are photographed and shown, not just mentioned. For turboprop and jet owners, paperwork is the product.
4. **Show it while it's gone.** The client portal is demonstrated live (animated screen recordings), because the fear is losing sight of the airplane for weeks.
5. **Show before and after, same angle.** Every transformation claim has a matched pair. Mismatched angles read as staged.
6. **Name the aircraft.** Every photo, quote and project names the make and model. Specific is credible; generic is stock.
7. **Calm, not flashy.** Motion is slow and quiet, like a well-run hangar. Fast, bouncy or showy effects read as a startup, not a craftsman. No parallax, no autoplay audio, no carousels that move on their own.

## Effect library

Ten named effects, built once and reused everywhere. Page tables below refer to them by code. Nothing else gets invented page by page.

| Code | Effect | Behavior | Trust job | Use limit |
| --- | --- | --- | --- | --- |
| E1 | Soft reveal | Content fades up 16px as it enters view, 400ms, children stagger 60ms | Calm, considered pacing | Default for every section; once per element |
| E2 | Before/after slider | Drag handle across a matched pair; keyboard arrows move it; starts at 50% | Proves the transformation | Any page with a real pair |
| E3 | Scroll transformation | Section pins; as you scroll, the worn cabin dissolves into the finished one in 3–4 stages (strip → foam → cover → finished) | Shows the work between before and after | Max one per page; Home hero band, Services hub, case studies |
| E4 | Stitch line | A dashed needle-red line draws itself along a path as the section enters (600ms) | Brand signature: hand-made | Max twice per page; connecting process steps, under a key heading |
| E5 | Sticky step rail | Step list stays pinned; current step highlights as its detail scrolls past | Process clarity: no surprises | How it works, capability process strips |
| E6 | Count-up | Real numbers count up once on entry (800ms) | Track record | Only verified numbers; never estimates |
| E7 | Slow drift | Hero still image scales 100→104% over 20s | Quiet luxury | Hero stills only |
| E8 | Silent loop | 6–12s muted video, poster frame first, pauses when off-screen, play/pause control | Shows the hands at work | One per section, max three per page |
| E9 | Card lift | Hover: card rises 2px with the lift shadow, 180ms | Clickable, responsive | All cards |
| E10 | Portal demo | Looping screen recording of the real portal: a photo posting, an approval tapped, the timeline advancing | Visibility while the airplane is gone | Home 06, How it works 05, About |

Every effect has a static fallback for reduced motion (E1, E4, E6, E7 show the end state; E3 shows a before/after slider; E8 and E10 show the poster frame with a play button).

## Photography and AI imagery

One look across both sources so they sit side by side: daylight or soft hangar light, warm neutrals, shallow depth of field on details, clean backgrounds, no lens flare or heavy filters. Shoot and generate in 3:2 at minimum 3000px wide; crop to 4:3, 16:9 and 21:9 from there.

**In-house photography is the proof.** It carries anything that says "we did this": portfolio, case studies, before/after, wear points on model pages, the people, the shop and the paperwork.

**AI imagery is the vision.** It carries heroes, style tiles in Start Your Design, service overviews, and model pages that don't have a project yet. Prompt for materials and light, not airplanes: leather grain, stitch rows, a seat back in window light. No real airline or manufacturer logos, tail numbers or recognizable people.

**Every image names its aircraft** in its caption or alt text ("1998 Beechcraft A36, club seats, cognac leather").

### In-house shot list

One full shoot day at the hangar, then a standing habit on every job.

| Shot | Where it's used | Notes |
| --- | --- | --- |
| Owner portrait at the sewing table, natural light | About 01, Home 06, thank-you screen | Same person everywhere; also a candid version mid-work |
| Owner shaking hands with a client beside an airplane | About 02, How it works 03 | The moment of handover |
| Hands: needle through leather, CNC head moving, foam cut, leather smoothed | Capabilities, service pages 03, Home 05 | Tight crops, 1/250s or faster; these become E8 loops too |
| Team at work (each person) | About 04 | Name and role on every portrait |
| Shop wide: hangar with an aircraft inside, doors open | About 05, Contact | Golden hour, exterior and interior |
| Materials wall: leathers, threads, foam | About 05, service pages 04 | Shows choice and quality |
| Paperwork flat-lay: burn cert, logbook entry, records packet, repair station certificate | Burn-certified capability page, About 06, How it works 04 | Real documents with private details blurred |
| Before / after pairs, same angle, same lens | Every portfolio item, service galleries, model pages | Tripod marks on the hangar floor so every job matches |
| Wear points by model (cracked plastics, sagging headliners) | Model pages 04 | Shot at intake on every job |
| Stage sign-off photos | Portal, case studies | Already required by the portal spec; flag the best as marketing-usable |

**Standing rule:** every job gets intake, mid-build and delivery photos from the marked angles. That's where the portfolio comes from in year two.

## Video

Short, silent, real. Loops (E8) are 6–12 seconds, muted, 1080p, under 3 MB as MP4/WebM, with a poster frame. One longer film with sound is the exception: the owner's story, only ever played by the visitor.

| Video | Length | Where | What it shows |
| --- | --- | --- | --- |
| CNC quilting loop | 8s | Home 05, CNC capability hero | The CNC head running a quilted seat back |
| Hands loop | 10s | Capabilities hub 01, service heroes | Needle, leather, foam: three cuts stitched together |
| Transformation time-lapse | 12s | Home 01 (optional), Services hub 04 | One seat from stripped frame to finished, locked-off camera |
| Portal demo (E10) | 10s | Home 06, How it works 05 | Screen recording: photo posts, approval tapped, timeline moves |
| 3D print time-lapse | 8s | 3D printing capability | A discontinued bezel printing, then next to the original |
| Owner's story (with sound, click to play) | 60–90s | About 02 | Why Air Sew exists, filmed in the shop. Captions burned in and as a track |
| Delivery moment | 8s loop + 30s cut | How it works 02 step 05, case studies | Owner opening the door to the finished cabin |

## Graphics and illustration

Line drawings in the icon style: navy hairline with one needle-red accent, nothing filled, nothing cartoonish.

- **Cabin layout diagrams** (Model pages 03): top-down seat maps per model family, toggling standard and club layouts. Built as SVG from one template; data per model. This is the single most "they know my airplane" graphic on the site.
- **Aircraft silhouettes** (Aircraft hub 03): one per size class, side view, hairline.
- **Stitch-pattern swatches** (service pages 04): diamond, channel, perforated, piping, drawn as hairline tiles, then replaced by real macro photos once shot.
- **Process diagram** (How it works): the five steps connected by an E4 stitch line.
- **Certification graphic** (Burn-certified page): Part 23 vs Part 25 side by side, which materials pass which test, what document you get.
- **Icon set**: the Air Sew hairline set from the design system, never mixed with another set.
- **No stock illustration, no 3D renders of jets, no infographics with invented numbers.**

## Motion rules

- **Timing:** 150–200ms for hover and taps, 400ms for reveals, 600ms for the stitch line. Ease-out on entry, never bounce or spring.
- **One thing moves at a time** in any viewport. If a loop is playing, nothing else animates beside it.
- **Reduced motion:** honor the system setting; every effect has the static fallback in the effect library. Videos never autoplay for those users.
- **Accessibility:** every loop has a pause control; the before/after slider works with arrow keys and announces its position; alt text names the aircraft and the change shown.
- **Performance budget per page:** largest image in view under 250 KB (AVIF/WebP), total page weight under 3 MB before scroll, first content visible under 2.5s on 4G. Loops load only when scrolled near; hero video never blocks the headline.
- **Mobile:** E3 becomes a before/after slider; sticky rails (E5) become a progress bar at the top; loops play only on Wi-Fi or tap.

## Per page: core pages

### Home

The first 10 seconds must answer "can these people be trusted with my airplane?" before the visitor scrolls far.

| Section | Media | Effect | Trust move |
| --- | --- | --- | --- |
| 01 Hero | Before/after of one real cabin, same angle; AI image only until the first real pair exists | E2 slider with a slow hint nudge on load; E7 on the still | The transformation, proven in one image |
| 02 Trust strip | Hairline icons; repair station certificate number links to the FAA's public record | E6 on cabins delivered (real count only) | Credentials before any sales talk |
| 03 Services | Icon cards; on hover, a small detail photo fades in behind the icon | E1, E9 | Breadth of craft |
| 04 Aircraft finder | Small cabin thumbnail per model card | E1; search suggests as you type | "They know my airplane" |
| 05 Capabilities | CNC quilting loop | E8; E4 stitch line linking the four capabilities | Modern shop, not a garage |
| 06 Client portal | Portal demo recording in a browser frame | E10 | Visibility while the airplane is gone |
| 07 Portfolio | Three real project cards, before photo swaps to after on hover | E9; hover swap | Real work, named aircraft |
| 08 Owner testimonial | Owner standing with their airplane, photo by us | E1 | A peer vouching, face and aircraft shown |
| 09 How it works | Five steps connected by a stitch line | E4 | No surprises |
| 10 Closing CTA | None; space and one sentence | E1 | Calm confidence |

### About

| Section | Media | Effect | Trust move |
| --- | --- | --- | --- |
| 01 Hero | Owner portrait at the sewing table | E7 | There's a someone |
| 02 Story | Owner's story film, click to play, captions | Play on click only | Hear the owner in their own words |
| 03 Beliefs | Hairline icons | E1 | Stated standards |
| 04 People | Real portraits, name and role | E1 stagger | Faces, not a logo |
| 05 The shop | Hangar, sewing room, materials wall | E1; lightbox | A real, well-kept place |
| 06 Certifications | Photo of the framed repair station certificate; links to the FAA record and a sample burn cert | E1 | Verifiable, not claimed |
| 07 Find us | Static map with the hangar pinned; aerial of the field | none | Real location, fly-in welcome |

### How it works

| Section | Media | Effect | Trust move |
| --- | --- | --- | --- |
| 01 Hero | None; headline only | E1 | Clarity |
| 02 Five steps | One photo or loop per step; the delivery-moment loop on step 05 | E5 sticky rail; E4 stitch line between steps | Every step visible in advance |
| 03 Downtime | Table, no imagery | E1 | Honest numbers |
| 04 What you get back | Paperwork flat-lay photo | E1 | The records an owner's mechanic will ask for |
| 05 Portal teaser | Portal demo on a phone | E10 | Visibility |
| 06 FAQ | Accordions | 200ms open | Objections answered |

### FAQ and Contact

- **FAQ:** no imagery except a small owner portrait beside "Still have a question? Talk to the owner directly." Accordions open in 200ms; deep links open the right answer.
- **Contact:** the owner's portrait and direct phone number at the top of the side column; click-to-call on mobile; static map of the hangar. A one-line promise under the form: "We reply within one business day."

## Per page: Services and Aircraft

### Services hub

| Section | Media | Effect | Trust move |
| --- | --- | --- | --- |
| 01 Hero | Wide finished cabin, every surface done | E7 | The whole job, done well |
| 02 Cabin services | Icon cards with hover detail photo | E1, E9 | Breadth |
| 03 Exterior | Real photo of a plug or cover on an aircraft | E1 | Fit, shown on the airplane |
| 04 Full interiors | Seat transformation time-lapse, or a scroll transformation | E3 (the page's one) | The work between before and after |
| 05 Before/after strip | Three matched pairs | E2 each | Repeatable results |

### Service page template

| Section | Media | Effect | Trust move |
| --- | --- | --- | --- |
| 01 Hero | Close detail of the finished service (a stitched seat back, a reveal) | E7, or a hands loop | Craft up close |
| 02 Quick facts | Text only | E6 on downtime numbers only if verified | Plain answers up front |
| 03 What we do | One hands loop or step photo per step | E1; E4 joining steps | Process you can picture |
| 04 Materials & options | Macro photos of real leathers, fabrics and stitch patterns; tapping a color swaps the seat image | Swatch swap 200ms | Choice and quality |
| 05 Gallery | Matched before/after pair, then details | E2; lightbox | Proof per service |
| 06 Aircraft | Model chips with tiny thumbnails | E9 | Fits my airplane |
| 07 Related capabilities | Icons | E1 | The machines behind it |
| 08 FAQ | Accordions | 200ms | Objections answered |

### Aircraft hub, category and manufacturer

- **Hub 01:** search is the hero, no big image. Suggestions show a cabin thumbnail per result.
- **Hub 02 two doors:** real certified and experimental cabins, E9 lift with the image easing in 2%.
- **Hub 03 sizes:** hairline silhouettes per size class.
- **Category and manufacturer heroes:** a finished cabin from that category or brand; AI concept labeled "Concept" until a real one exists.
- **Manufacturer 03 projects:** hidden until a real project is tagged.

### Model family page template

The page that makes an owner think "they know my airplane." Trust here comes from specifics.

| Section | Media | Effect | Trust move |
| --- | --- | --- | --- |
| 01 Hero | Finished cabin of this model (real if possible; AI concept labeled) | E7; fleet count with E6 | Specific to my airplane |
| 02 In-page nav | Sticky bar | Active-section underline in needle red | Easy to scan |
| 03 Cabin at a glance | Cabin layout diagram, standard and club toggle | Seats re-arrange in 300ms on toggle | Knows the layout |
| 04 What wears out | Intake photos of real wear on this model | E1 | Shop-floor knowledge, honest about problems |
| 05 What we do | Service cards with a model-specific line | E9 | Tailored, not generic |
| 06 Options | Material and stitch montage | E1 | Personalization |
| 07 Our work | Before/after of this model, then projects | E2 | Done it before |
| 08 Variants | Table | none | Precision |
| 11 CTA | Model name in the button | none | Pre-filled, effortless |

## Per page: Capabilities, Portfolio and the rest

### Capabilities hub and capability template

| Section | Media | Effect | Trust move |
| --- | --- | --- | --- |
| Hub 01 | Full-width hands loop: CNC cutting → sewing → printing → finished seat | E8 | Real machines, real hands |
| Hub 02 | One photo or loop per capability, alternating sides | E1; E4 stitch line running down the page between them | One shop, connected process |
| Hub 03 Equipment | Photo of each machine with its name | E1 | Investment in the shop |
| Template 01 | Silent loop of that process | E8 | See it working |
| Template 03 Process strip | Step photos | E5 on desktop, swipe row on mobile | No black box |
| Template 04 Proof | CNC: machine and spec close-up. 3D printing: original part beside the printed one. Plastics: E2 slider. Burn-certified: paperwork flat-lay, Part 23 vs 25 graphic, sample document download | Varies | The evidence a maintenance director wants |

### Portfolio and case study

| Section | Media | Effect | Trust move |
| --- | --- | --- | --- |
| Portfolio 02 Featured | Full-width finished cabin | E2 on hover/drag | Best work first |
| Portfolio 04 Grid | Before photo swaps to after on hover | E9; 300ms crossfade | Every card is proof |
| Portfolio 05 Testimonials | Owner photo with aircraft per quote | E1 | Peers, named |
| Case 01 Hero | Full-width finished cabin | E7 | The result |
| Case 03 Brief | Intake photo of the cabin as it arrived | E1 | Honest starting point |
| Case 04 Before/after | Matched pair | E2 | The transformation |
| Case 05 What we did | Stage sign-off photos from the portal | E3 scroll transformation through the stages | You see what we'd show you during your job |
| Case 06 Materials | Macro swatches of the actual materials | E1 | Real choices |
| Case 07 Gallery | 8–12 details | Lightbox | Craft up close |
| Case 08 Quote | Owner with their airplane | E1 | A peer vouching |

### Utility pages

- **Legal:** no imagery; sticky contents, smooth anchor scroll.
- **404:** small hairline illustration of a loose thread; the stitch line (E4) draws a short dashed line under the headline. Search is the main action.

### Start Your Design flow

- **Step 1:** small owner portrait and "You'll hear from \[name\]" beside the form, so a person is attached from the first field.
- **Step 2:** aircraft confirm card resolves with a short 400ms reveal after lookup; a skeleton shimmer while it loads, never a spinner.
- **Step 3:** style tiles use AI imagery; the selected tile lifts (E9) and gets the navy ring.
- **Step 4:** uploaded photos appear as thumbnails instantly; the first is badged "For render".
- **Step 5:** while rendering, show the owner's photo with a slow stitch line (E4) tracing its edge and "Designing your cabin…"; the reveal is a crossfade from their photo to the concept, then the before/after toggle.
- **Step 6:** check mark draws in (400ms); the contact person's real photo and direct number.

## Production plan and decisions

Build the effects once, shoot once properly, then let every job feed the site.

1. **Effect library first.** Developers build E1–E10 as reusable components with their reduced-motion fallbacks before any page is assembled.
2. **AI image set.** Heroes, style tiles and model-page concepts, generated to the photo standard. Fills every page at launch.
3. **Shoot day at the hangar.** The in-house shot list plus the five short loops; a local videographer for one day, or a phone on a gimbal with locked-off tripods.
4. **Owner's story film.** Filmed the same day; edited to 60–90 seconds with captions.
5. **Graphics.** Cabin layout diagrams for the Wave 1 model families, silhouettes, certification graphic.
6. **Portal demo recording** once the portal shows real data.
7. **Swap AI for in-house** as each job is photographed at the marked angles.

**Decisions for you**

- [ ] Is the owner on camera (portrait, story film, thank-you screen)? The whole trust approach leans on a face and a name.
- [ ] Which real project becomes the Home hero before/after?
- [ ] Videographer for a day, or shoot in-house?
- [ ] Which three or four clients will give a quote and a photo with their airplane?
- [ ] Repair station certificate details for the new location, so the trust strip can link to the FAA record at launch.
