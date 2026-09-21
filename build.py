# -*- coding: utf-8 -*-
"""
Air Sew static site generator.
Run:  python build.py
Generates index.html, restorations.html, services.html, about.html, contact.html
and one page per aircraft model, all sharing the same header / footer / scripts.
"""
import os, html, time
ASSET_V = str(int(time.time()))

OUT = os.path.dirname(os.path.abspath(__file__))
PHONE = "(385) 595-6002"
PHONE_TEL = "tel:+13855956002"
EMAIL = "info@air-sew.com"
ADDRESS = "2124 Thunderbird Dr, Hangar 27, Woods Cross, UT 84087"

# ---------------------------------------------------------------------------
# Icons
# ---------------------------------------------------------------------------
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARROW_UP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>'
PLUS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
DRAG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6-6 6 6 6M15 6l6 6-6 6"/></svg>'

ICONS = {
    "seat": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M14 8h12a4 4 0 0 1 4 4v14H12V12a2 2 0 0 1 2-4Z"/><path d="M10 26h24a4 4 0 0 1 4 4v6H8v-6a4 4 0 0 1 2-4Z"/><path d="M12 36v5M36 36v5M18 14h8M18 19h8"/></svg>',
    "cabin": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 24c0-9 9-16 18-16s18 7 18 16-9 16-18 16S6 33 6 24Z"/><path d="M6 24h36M16 10v28M32 10v28"/></svg>',
    "headliner": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 30C6 18 14 10 24 10s18 8 18 20"/><path d="M6 30h36M12 30v8M24 30v8M36 30v8"/></svg>',
    "floor": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="m8 30 16-10 16 10-16 10Z"/><path d="m8 22 16-10 16 10M8 30v6l16 10 16-10v-6"/></svg>',
    "panel": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="10" width="32" height="28" rx="4"/><path d="M8 22h32M20 10v28M14 16h2M14 30h2"/></svg>',
    "embroidery": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M8 36c6-6 8-18 20-18s8 12 12 18"/><path d="M12 12c4 0 6 6 6 6M30 8l4 6M36 22l-6-2"/><circle cx="24" cy="30" r="3"/></svg>',
}

# ---------------------------------------------------------------------------
# Navigation & fleet data
# ---------------------------------------------------------------------------
AIRCRAFT = [
    # slug, make, model, designation, category(s), hero image, card image
    dict(slug="piper-archer", make="Piper", model="Archer", designation="PA-28-181", cats="piper single",
         img="piper-archer.jpg", seats="4", timeline="2–3 weeks", price="From $6,500", tagline="The contemporary Cherokee, dressed for another forty years.",
         intro=[
             "The Archer is the most-flown Cherokee variant in the country, and the one we see most often on the Sky Park ramp. Whether yours is a 1970s PA-28-181 with the original crushed velour or a late-model Archer LX, the cabin is compact, the seat frames are straightforward, and a full interior can be turned around in a couple of weeks.",
             "We rebuild every seat from the frame out: new high-density foam carved to the original profile, new covers in leather, synthetic leather, or FAR 25.853-rated fabric, and the sidewalls, headliner, and carpet to match. Embroidered headrests with the Piper logo or your tail number are standard options.",
         ],
         faq=[
             ("How long does an Archer interior take?", "A seats-only refresh is typically 1–2 weeks. A full cabin (seats, side panels, headliner, carpet, plastics) usually runs 2–3 weeks. Fly in, leave the airplane with us at Sky Park, and we call you when it's ready."),
             ("Can you match the original Piper colors?", "Yes. We keep samples and specifications for most classic Piper interior schemes from the 1960s through the 1980s, including burnt orange, avocado, and the tan/brown combinations, and we can reproduce original patterns for vintage restorations."),
             ("Is the material FAA compliant?", "Every fabric, leather, and foam we install carries burn certification for its application. Documentation is included with your logbook entry."),
         ]),
    dict(slug="piper-aerostar", make="Piper", model="Aerostar", designation="PA-60 · 600 / 601 / 602P / 700P", cats="piper twin",
         img="piper-aerostar.jpg", seats="6", timeline="4–6 weeks", price="From $18,000", tagline="The fastest piston twin ever built deserves a cabin that keeps up.",
         intro=[
             "Ted Smith's Aerostar is a pilot's airplane, and most owners have already spent generously on engines and avionics. The cabin is often the last piece left untouched. We specialize in bringing Aerostar interiors up to the standard of the rest of the airframe: six-place club seating rebuilt with new foam, full-hide leather or Ultraleather, refinished side ledges, new carpet, and a headliner that finally fits.",
             "Aerostar cabins are tight and the seat mechanisms are particular. Our team has the templates and the patience to make everything line up the first time.",
         ],
         faq=[
             ("Do you handle pressurized Aerostar models?", "Yes. The 601P, 602P, and 700P cabins add sealed-door hardware and pressure-vessel considerations. We remove and reinstall trim without disturbing seals and document everything for your IA."),
             ("Can you update the side ledges and cabinetry?", "We refinish or re-veneer side ledges and armrest tops and can integrate USB power, LED reading lights, and cup holders during the rebuild."),
             ("What is a realistic budget?", "Most full Aerostar interiors land between $18,000 and $40,000 depending on material choice. We quote a fixed price after a design appointment, with no surprises."),
         ]),
    dict(slug="piper-comanche", make="Piper", model="Comanche", designation="PA-24 · 180 / 250 / 260 / 400", cats="piper single vintage",
         img="piper-comanche.jpg", seats="4–6", timeline="3–4 weeks", price="From $9,500", tagline="Period-correct or fully modern. Your Comanche, your call.",
         intro=[
             "Comanche owners are a loyal bunch, and many want an interior that honors the airplane's 1958–1972 heritage. We can reproduce original Piper patterns and colors from our sample library, or reinterpret the cabin with modern leather, diamond stitching, and LED lighting while keeping the classic lines.",
             "Every Comanche interior we do includes new seat foam, refurbished seat frames and tracks, new side panels and armrests, headliner, carpet, and paint-matched plastics.",
         ],
         faq=[
             ("Can you reproduce the original 1960s pattern?", "Yes. We keep samples and specs for most classic Piper schemes and can match the original pleats, colors, and piping for a period-correct restoration."),
             ("What about the six-place PA-24-260C?", "We handle the 5th and 6th seat installations and the extended cabin trim. Timeline is slightly longer, typically 4 weeks."),
             ("Do you repair the seat frames?", "We inspect every frame, repair cracks and loose joints, and rebuild adjustment mechanisms before the new upholstery goes on."),
         ]),
    dict(slug="cessna-172", make="Cessna", model="172 Skyhawk", designation="172 · 172RG · 172S", cats="cessna single",
         img="cessna-172.jpg", seats="4", timeline="2–3 weeks", price="From $6,000", tagline="The most-produced airplane in history, made yours.",
         intro=[
             "From 1956 Skyhawks to new 172S trainers, we've restored every generation of the type. The 172 is the airplane that taught most of us to fly, and it's also the one most often flown with a forty-year-old interior. A new cabin transforms the experience for a fraction of what an avionics upgrade costs.",
             "Our typical 172 package: four rebuilt seats with new foam and embroidered Cessna headrests, new side panels and door panels, headliner, carpet, and paint-matched plastics. Flight schools ask us for durable synthetic leather; owners usually go for full hide.",
         ],
         faq=[
             ("What does a Cessna 172 interior cost?", "A full interior for a small Cessna generally ranges from $15,000 to $30,000 with premium materials. Seats-only packages start around $6,000. Every job is quoted as a fixed price after a design appointment."),
             ("How long will my airplane be down?", "Typically 2–3 weeks for a full cabin. Fly in to Sky Park, and we handle removal and installation on the field."),
             ("Can you do the embroidered headrests I've seen on your Instagram?", "Yes. Cessna logos, tail numbers, and custom artwork are all embroidered in-house."),
         ]),
    dict(slug="cessna-182", make="Cessna", model="182 Skylane", designation="182 · 182RG · T182T", cats="cessna single",
         img="cessna-182.jpg", seats="4", timeline="2–3 weeks", price="From $6,500", tagline="More airplane, more cabin, more reasons to do it right.",
         intro=[
             "The Skylane is the family and cross-country airplane of choice, and it's one we know well. Our own shop Skylane project set the template for the two-tone leather, embroidered headrest, and new headliner combination we install most often.",
             "We rebuild the front and rear seats, replace the headliner and window trim, install new carpet and sidewalls, and paint-match all interior plastics to the new scheme.",
         ],
         faq=[
             ("Do you handle the newer T182T with the glass panel?", "Yes. Late-model Skylanes with G1000 panels have different plastics and trim. We have the templates and take care not to disturb the avionics."),
             ("What is the most popular 182 scheme?", "Two-tone gray or stone leather with charcoal accents and contrast stitching, embroidered Cessna headrests, and a light gray headliner. It photographs beautifully and hides wear well."),
             ("Can you rebuild the seat mechanisms?", "We inspect and repair seat rails, stops, and recline mechanisms while the seats are out of the airplane."),
         ]),
    dict(slug="cessna-206", make="Cessna", model="206 Stationair", designation="U206 · TU206 · T206H", cats="cessna single utility",
         img="cessna-206.jpg", seats="6", timeline="3–4 weeks", price="From $9,500", tagline="A utility cabin built to work, finished to impress.",
         intro=[
             "Stationairs live hard lives: backcountry strips, floats, skydiving, and cargo. We build 206 interiors that can take it, with heavy-gauge synthetic leather or full hide, reinforced seams, and durable loop-pile carpet, without giving up the finish you'd expect in an executive cabin.",
             "Six-place club or forward-facing configurations, quick-release rear seats, and cargo-door trim are all in our wheelhouse.",
         ],
         faq=[
             ("Which materials hold up best for backcountry use?", "Marine-grade synthetic leather with reinforced stitching and solution-dyed carpet resist UV, dirt, and moisture better than anything else we install."),
             ("Can you set the airplane up for quick seat removal?", "Yes. We refurbish the quick-release hardware and keep the rear seat covers free of anything that snags on the tracks."),
             ("How long does a 206 interior take?", "Plan on 3–4 weeks for a full six-place cabin."),
         ]),
    dict(slug="pilatus-pc12", make="Pilatus", model="PC-12", designation="PC-12 · PC-12/45 · PC-12/47 · NG · NGX", cats="pilatus turboprop",
         img="pilatus-pc12.jpg", seats="6–9", timeline="5–8 weeks", price="From $25,000", tagline="The world's favorite turboprop, refreshed to executive standard.",
         intro=[
             "The PC-12 cabin is large, and owners use it for everything from executive shuttle to family hauling to medevac. We do complete cabin refurbishments: executive seats rebuilt with new foam and full-hide leather, refinished side ledges and cabinetry, new headliner and window panels, new carpet, and updated LED lighting.",
             "PC-12 restoration budgets range widely because the scope does. A leather-and-carpet refresh looks like one number; a full cabin with cabinetry, veneer, and lighting looks like another. We walk you through the options at a design appointment and quote a fixed price.",
         ],
         faq=[
             ("What does a PC-12 interior cost?", "Refreshes start around $25,000. Full executive cabin refurbishments with veneer, cabinetry, and lighting can exceed $100,000. The single biggest factor is scope, and we help you decide what's worth doing."),
             ("Do you work on the NG and NGX models?", "Yes. Newer cabins with the BMW Designworks interior have different seat structures and trim. We have experience with all generations."),
             ("Can I fly in for the work?", "Absolutely. Sky Park is a 1,100 ft-elevation field with a 4,000 ft runway and ample ramp space for a PC-12. We also service aircraft at South Valley and Salt Lake City International."),
         ]),
    dict(slug="pilatus-pc24", make="Pilatus", model="PC-24", designation="Super Versatile Jet", cats="pilatus jet",
         img="pilatus-pc24.jpg", seats="6–8", timeline="6–8 weeks", price="From $35,000", tagline="A light jet cabin as versatile as the airplane around it.",
         intro=[
             "The PC-24's flat-floor cabin and oversize cargo door invite reconfiguration, and many operators want the interior to reflect how they actually use the airplane. We refurbish and re-cover executive seats, rebuild divans, refinish side ledges, and replace carpet and headliner to the standard the airframe deserves.",
             "As with all jet work, we coordinate with your maintenance provider on removal and reinstallation and document every material's burn certification.",
         ],
         faq=[
             ("Do you offer diamond-stitched or perforated leather for the PC-24?", "Yes. Diamond quilting, perforation, and contrast piping are all done in-house on full-hide leather."),
             ("How do you handle jet certification paperwork?", "Every material is burn-certified for its application, and we provide the documentation package your DOM or IA needs for the logbook entry."),
             ("Can you work at my home base?", "For jet projects along the Wasatch Front we can perform removal and reinstallation at Salt Lake City International or South Valley. Cabin work is done in our shop at Sky Park."),
         ]),
    dict(slug="citation", make="Cessna", model="Citation", designation="CJ · CJ1 · CJ2 · CJ3 · CJ4 · M2 · XLS", cats="jet cessna",
         img="citation.jpg", seats="6–9", timeline="5–8 weeks", price="From $30,000", tagline="Light-jet cabins, rebuilt seat by seat.",
         intro=[
             "Our most recent jet project was a 2003 Citation CJ2 out of Salt Lake International: new floors, new front seats, and new rear seats, all rebuilt in tan full-hide leather with new foam and new carpet. It's typical of the Citation work we do, which ranges from a single seat re-cover to a complete cabin.",
             "Citation seats are complex assemblies with tracking, swivel, and recline mechanisms. We disassemble, inspect, and rebuild each one before it's re-covered, so the seat works as well as it looks.",
         ],
         faq=[
             ("Which Citation models do you service?", "CitationJet, CJ1 through CJ4, M2, Bravo, Encore, Ultra, and XLS. If it's a Citation, we've probably had a seat from one on the bench."),
             ("Can you replace only the carpet and seats?", "Yes. Floors and seats are the highest-wear items and are often the most cost-effective refresh. Side panels and headliners can follow later."),
             ("Where is the work done?", "Removal and reinstallation can be done at Salt Lake City International or South Valley with your maintenance provider. Cabin components come to our shop at Sky Park."),
         ]),
    dict(slug="phenom-300", make="Embraer", model="Phenom 300", designation="Phenom 300 · 300E", cats="jet embraer",
         img="phenom-300.jpg", seats="6–10", timeline="6–8 weeks", price="From $35,000", tagline="The best-selling light jet, with a cabin to match.",
         intro=[
             "The Phenom 300's Oval Lite cabin is one of the most comfortable in the class, and it responds beautifully to a refresh. We rebuild the executive seats with new foam and leather, replace carpet and headliner, refinish side ledges, and can integrate updated lighting.",
             "Embraer interiors use a lot of sculpted, wrapped surfaces. Our team has the experience to re-wrap complex panels without wrinkles or seams in the wrong places.",
         ],
         faq=[
             ("Can you re-cover Phenom seats without replacing the foam?", "We can, but we rarely recommend it. Seat foam loses its shape after a decade, and new foam is the difference between a re-cover and a restoration."),
             ("What leathers do you offer for jets?", "Full-hide aviation leathers from the major mills in dozens of colors, plus Ultraleather and Tapis for high-wear applications. All burn-certified."),
             ("How long is the airplane down?", "Typically 6–8 weeks for a full cabin. We coordinate with your maintenance schedule to overlap with inspections where possible."),
         ]),
]
BY_SLUG = {a["slug"]: a for a in AIRCRAFT}

NAV = [
    ("Recent Restorations", "restorations.html", None),
    # A dict value = grouped mega menu (make -> model slugs); a list = flat card menu
    ("Light Planes", None, {
        "Piper": ["piper-archer", "piper-aerostar", "piper-comanche"],
        "Cessna": ["cessna-172", "cessna-182", "cessna-206"],
        "Pilatus": ["pilatus-pc12", "pilatus-pc24"],
    }),
    ("Business Jets", None, ["citation", "pilatus-pc24", "phenom-300"]),
    ("Experimental", "experimental.html", None),
    ("Services", "services.html", None),
    ("About", "about.html", None),
]

# ---------------------------------------------------------------------------
# Shared chrome
# ---------------------------------------------------------------------------
def head(title, desc, extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#0a0d12">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="assets/img/full/hero-cabin.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/main.css?v={ASSET_V}">
{extra}
</head>
<body>
<div class="cursor" aria-hidden="true"></div>
"""

def preloader():
    return """<div class="preloader" aria-hidden="true">
  <div class="preloader__inner">
    <img class="preloader__logo" src="assets/img/logo.png" alt="">
    <div class="preloader__line"><i></i></div>
    <div class="preloader__label">Aviation Upholstery &amp; Interiors</div>
  </div>
</div>
"""

def mega_card(slug):
    a = BY_SLUG[slug]
    return f"""<a class="mega__card" href="{a['slug']}.html">
  <img src="assets/img/thumb/{a['img']}" alt="{a['make']} {a['model']} interior" loading="lazy">
  <div class="mega__meta"><b>{a['model'] if a['make'] != 'Embraer' else 'Phenom 300'}</b><small>{a['make']} · {a['designation'].split(' · ')[0]}</small></div>
</a>"""

def header(active=""):
    items = []
    for label, href, subs in NAV:
        if isinstance(subs, dict):
            cols = []
            for make, slugs in subs.items():
                rows = "".join(f"""<a class="mega__row" href="{BY_SLUG[x]['slug']}.html"><img src="assets/img/thumb/{BY_SLUG[x]['img']}" alt="" loading="lazy"><span><b>{BY_SLUG[x]['model']}</b><small>{BY_SLUG[x]['designation'].split(' · ')[0]}</small></span></a>""" for x in slugs)
                cols.append(f'<div class="mega__group"><h5>{make}</h5>{rows}</div>')
            items.append(f"""<li class="nav__item">
  <a class="nav__link{' is-active' if active == label else ''}" href="#" aria-haspopup="true">{label} {CHEV}</a>
  <div class="mega mega--groups">
    <div class="mega__groups">{''.join(cols)}</div>
    <div class="mega__foot"><span>Single-engine and twin piston, plus turboprops · fly-in / fly-out at Sky Park</span><a class="link-arrow" href="index.html#aircraft"><span>All aircraft</span>{ARROW_UP}</a></div>
  </div>
</li>""")
        elif subs:
            cards = "\n".join(mega_card(s) for s in subs)
            foot_link = "restorations.html" if label == "Business Jets" else "services.html"
            items.append(f"""<li class="nav__item">
  <a class="nav__link{' is-active' if active == label else ''}" href="#" aria-haspopup="true">{label} {CHEV}</a>
  <div class="mega" style="--cols:{len(subs)}">
    <div class="mega__grid">{cards}</div>
    <div class="mega__foot"><span>{label} interiors · fly-in / fly-out at Sky Park</span><a class="link-arrow" href="contact.html"><span>Start a project</span>{ARROW_UP}</a></div>
  </div>
</li>""")
        else:
            items.append(f'<li class="nav__item"><a class="nav__link{" is-active" if active == label else ""}" href="{href}">{label}</a></li>')
    # drawer
    ditems = []
    for label, href, subs in NAV:
        if isinstance(subs, dict):
            sub = ""
            for make, slugs in subs.items():
                sub += f'<li class="drawer__group">{make}</li>' + "".join(f'<li><a href="{BY_SLUG[x]["slug"]}.html">{BY_SLUG[x]["model"]}<small>{BY_SLUG[x]["designation"].split(" · ")[0]}</small></a></li>' for x in slugs)
            ditems.append(f'<li class="drawer__item drawer__item--sub"><button class="drawer__link" type="button">{label} {CHEV}</button><ul class="drawer__sub">{sub}</ul></li>')
        elif subs:
            sub = "".join(f'<li><a href="{BY_SLUG[s]["slug"]}.html">{BY_SLUG[s]["make"]} {BY_SLUG[s]["model"]}<small>{BY_SLUG[s]["designation"].split(" · ")[0]}</small></a></li>' for s in subs)
            ditems.append(f'<li class="drawer__item drawer__item--sub"><button class="drawer__link" type="button">{label} {CHEV}</button><ul class="drawer__sub">{sub}</ul></li>')
        else:
            ditems.append(f'<li class="drawer__item"><a class="drawer__link" href="{href}">{label} {ARROW_UP}</a></li>')
    ditems.append(f'<li class="drawer__item"><a class="drawer__link" href="contact.html">Contact {ARROW_UP}</a></li>')
    return f"""<header class="header">
  <div class="container header__inner">
    <a class="brand" href="index.html" aria-label="Air Sew home"><img src="assets/img/logo.png" alt="Air Sew"></a>
    <nav class="nav" aria-label="Primary"><ul class="nav" style="list-style:none;margin:0;padding:0">{''.join(items)}</ul></nav>
    <div class="header__cta">
      <a class="header__phone" href="{PHONE_TEL}">{PHONE}</a>
      <a class="btn btn--sm" href="contact.html">Start a project {ARROW}</a>
      <button class="burger" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="drawer" aria-label="Mobile navigation">
  <ul class="drawer__list">{''.join(ditems)}</ul>
  <div class="drawer__foot">
    <a class="btn btn--blue" href="contact.html">Start a project {ARROW}</a>
    <a href="{PHONE_TEL}">{PHONE}</a>
    <span class="small">{ADDRESS}</span>
  </div>
</div>
"""

def footer():
    fleet = "".join(f'<li><a href="{a["slug"]}.html">{a["make"]} {a["model"]}</a></li>' for a in AIRCRAFT)
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="assets/img/logo.png" alt="Air Sew">
        <p>Third-generation upholstery craftsmanship from Bogotá, brought to the skies of northern Utah. FAA-compliant aircraft interiors with fixed pricing and fly-in / fly-out convenience.</p>
        <p style="margin-top:14px"><a href="{PHONE_TEL}"><b>{PHONE}</b></a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <h4>Aircraft</h4>
        <ul>{fleet}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="restorations.html">Recent Restorations</a></li>
          <li><a href="experimental.html">Experimental</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="about.html">About &amp; Heritage</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="contact.html#appointment">Design Appointment</a></li>
          <li><a href="https://air-sew.printful.me/" target="_blank" rel="noopener">Air Sew Shop</a></li>
        </ul>
      </div>
      <div>
        <h4>Visit</h4>
        <ul>
          <li><a href="https://maps.google.com/?q=2124+Thunderbird+Dr+Woods+Cross+UT" target="_blank" rel="noopener">Sky Park Airport (KBTF)<br>2124 Thunderbird Dr, Hangar 27<br>Woods Cross, UT 84087</a></li>
          <li><span class="small muted">Also serving South Valley Regional (U42) and Salt Lake City International (KSLC)</span></li>
          <li><span class="small muted">Mon–Fri 8am–5pm · Fly-ins by appointment</span></li>
        </ul>
      </div>
    </div>
    <div class="footer__big" aria-hidden="true">Old planes. New tricks.</div>
    <div class="footer__bottom">
      <span>© 2026 Air Sew · Aviation Upholstery and Interiors · Woods Cross, Utah</span>
      <span><a href="privacy.html">Privacy</a> &nbsp;·&nbsp; <a href="terms.html">Terms</a></span>
    </div>
  </div>
</footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js"></script>
<script src="assets/js/main.js?v={ASSET_V}"></script>
</body>
</html>
"""

def cta_band(video="hero-cabin", title="Ready to reimagine your cabin?", sub="Schedule a design appointment, fly in to Sky Park, and fly out with an interior that finally matches the airplane."):
    return f"""<section class="cta-band">
  <div class="cta-band__media">
    <video data-lazy data-src="assets/video/{video}.mp4" poster="assets/img/full/{video}.jpg" muted loop playsinline preload="none"></video>
  </div>
  <div class="cta-band__inner">
    <div class="eyebrow reveal" style="justify-content:center">Start your project</div>
    <h2 class="display-lg" data-split>{title}</h2>
    <p class="lead reveal" style="max-width:56ch;margin-inline:auto">{sub}</p>
    <div class="cta-band__actions reveal">
      <a class="btn btn--blue" href="contact.html">Tell us about your project {ARROW}</a>
      <a class="btn btn--ghost" href="{PHONE_TEL}">Call {PHONE}</a>
    </div>
  </div>
</section>
"""

def page_hero(eyebrow, title, lead, img, crumbs, short=False, actions=True):
    crumb_html = " ".join(f'<a href="{h}">{t}</a>' if h else f"<span>{t}</span>" for t, h in crumbs)
    act = f"""<div class="hero__actions"><a class="btn btn--blue" href="contact.html">Start a project {ARROW}</a><a class="btn btn--ghost" href="{PHONE_TEL}">{PHONE}</a></div>""" if actions else ""
    return f"""<section class="page-hero{' page-hero--short' if short else ''}">
  <div class="page-hero__media"><img src="assets/img/full/{img}" alt=""></div>
  <div class="container page-hero__content">
    <div class="crumbs">{crumb_html}</div>
    <div class="eyebrow">{eyebrow}</div>
    <h1 class="display-lg">{title}</h1>
    <p class="lead" style="max-width:56ch;margin-top:22px">{lead}</p>
    {act}
  </div>
</section>
"""

def fleet_card(a):
    label = a["model"] if a["make"] != "Embraer" else "Phenom 300"
    return f"""<a class="fleet-card reveal" href="{a['slug']}.html" data-cat="{a['cats']}">
  <img src="assets/img/thumb/{a['img']}" alt="{a['make']} {a['model']} interior" loading="lazy">
  <div class="fleet-card__meta"><div><small>{a['make']} · {a['designation'].split(' · ')[0]}</small><b>{label}</b></div><span class="fleet-card__arrow">{ARROW_UP}</span></div>
</a>"""

# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
def build_index():
    services = [
        ("seat", "Seat Restoration", "Frames inspected and repaired, new high-density foam carved to profile, then re-covered in leather, synthetic leather, or certified fabric."),
        ("cabin", "Full Interior Restoration", "Seats, side and door panels, headliner, carpet, and plastics, designed as one scheme and installed on the field."),
        ("headliner", "Headliners", "Sagging, stained, or brittle headliners replaced with new material that fits tight and stays put."),
        ("floor", "Floors & Carpet", "Aviation-grade carpet, bound edges, and refurbished floor panels for a cabin that feels new underfoot."),
        ("panel", "Panels & Plastics", "Side panels re-wrapped, interior plastics repaired and paint-matched to the new scheme."),
        ("embroidery", "Embroidery & Personalization", "Logos, tail numbers, and custom artwork stitched in-house. Lighting, USB power, and modern touches on request."),
    ]
    svc_html = "".join(f"""<article class="service reveal">
  <span class="service__num">0{i+1}</span>
  <a class="service__more" href="services.html" aria-label="More about {t}">{ARROW_UP}</a>
  <div class="service__icon">{ICONS[k]}</div>
  <h3>{t}</h3><p>{d}</p>
</article>""" for i, (k, t, d) in enumerate(services))

    projects = [
        ("real/citation-cj2-seat.jpg", "Business Jet", "Citation CJ2", "Full seat and floor restoration · KSLC", "tall"),
        ("real/cessna-182-headliner.jpg", "Cessna", "182 Skylane", "Headliner, headrests, and two-tone seats", "wide"),
        ("real/cessna-172-embroidered-seats.jpg", "Cessna", "172 Skyhawk", "Embroidered gray leather seats", "wide"),
        ("real/kodiak-diamond-seat.jpg", "Utility", "Quest Kodiak", "Navy and red diamond-stitched seat", "tall"),
        ("real/eagle-embroidery-seats.jpg", "Personalized", "Custom embroidery", "Eagle motif with patterned inserts", "wide"),
        ("real/rear-bench-two-tone.jpg", "Cessna", "Rear bench", "Two-tone gray with contrast panels", "wide"),
    ]
    proj_html = "".join(f"""<article class="hcard hcard--{sz}">
  <div class="hcard__img"><img src="assets/img/full/{img}" alt="{title}" loading="lazy"></div>
  <div class="hcard__meta"><small>{cat}</small><b>{title}</b><span>{desc}</span></div>
</article>""" for img, cat, title, desc, sz in projects)

    fleet_html = "".join(fleet_card(a) for a in AIRCRAFT)

    swatches = [
        ("#1d2a4a", "Navy full hide", 0.55), ("#8a5a2b", "Cognac full hide", 0.5), ("#5a1e1e", "Oxblood", 0.5),
        ("#3a3d42", "Charcoal", 0.5), ("#e6dcc6", "Cream", 0.35), ("#7a8590", "Stone gray", 0.45),
    ]
    sw_html = "".join(f'<button class="swatch{" is-active" if i == 0 else ""}" type="button" style="background:{c}" data-color="{c}" data-tint="{t}" data-name="{n}"><span class="swatch__name">{n.split(" ")[0]}</span></button>' for i, (c, n, t) in enumerate(swatches))

    why = [
        ("Fly-in / Fly-out", "Land at Sky Park, taxi to Hangar 27, and leave the airplane with us. Removal and installation happen on the field."),
        ("Fixed Cost", "One quote after your design appointment. No hourly surprises, no change orders you didn't ask for."),
        ("Proven Skills", "Three generations of leatherwork and upholstery, refined on aircraft from Cubs to Citations."),
        ("On Schedule", "Reliable timelines and minimal downtime, coordinated with your maintenance calendar."),
        ("Clear Communication", "Progress photos and updates through every stage of the build."),
        ("Airport Partnerships", "Service at Sky Park, South Valley Regional, and Salt Lake City International."),
        ("1,000+ Design Options", "Leather, synthetic leather, vinyl, and FAR-rated fabrics in hundreds of colors and textures."),
        ("FAA Compliant", "Every material burn-certified for its application, with documentation for your logbook."),
        ("Financing Available", "Flexible financing options to fit the project into your budget. Ask for details."),
    ]
    why_html = "".join(f'<div class="why__item reveal"><i></i><b>{t}</b><p>{d}</p></div>' for t, d in why)

    body = f"""
<section class="hero">
  <div class="hero__media">
    <video autoplay muted loop playsinline poster="assets/video/hero-hangar-poster.jpg"><source src="assets/video/hero-hangar.mp4" type="video/mp4"></video>
  </div>
  <div class="container hero__content">
    <div class="eyebrow">Sky Park Airport · Woods Cross, Utah</div>
    <h1 class="hero__title display-xl">Old planes. New tricks.</h1>
    <p class="hero__sub lead">Aviation upholstery and complete interior restoration for Piper, Cessna, Pilatus, and business jets. Three generations of craftsmanship, FAA-compliant materials, fixed pricing, and fly-in / fly-out convenience.</p>
    <div class="hero__actions">
      <a class="btn btn--blue" href="contact.html">Tell us about your project {ARROW}</a>
      <a class="btn btn--ghost" href="restorations.html">See recent restorations</a>
    </div>
    <div class="hero__stats">
      <div class="stat"><b><span data-count="250">0</span><sup>+</sup></b><span>Interiors completed</span></div>
      <div class="stat"><b><span data-count="1000">0</span><sup>+</sup></b><span>Design options</span></div>
      <div class="stat"><b><span data-count="3">0</span></b><span>Generations of craft</span></div>
      <div class="stat"><b><span data-count="3">0</span></b><span>Partner airports</span></div>
    </div>
  </div>
  <div class="hero__scroll"><span>Scroll</span><i></i></div>
</section>

<div class="marquee" aria-hidden="true">
  <div class="marquee__track">
    {''.join(f'<span class="marquee__item">{m}<i></i></span>' for m in ["Piper","Cessna","Pilatus","Beechcraft","Cirrus","Mooney","Citation","Embraer","Daher","Diamond","Eclipse","Experimental"]*2)}
  </div>
</div>

<section class="section">
  <div class="container split split--narrow">
    <div>
      <div class="media-stack">
        <div class="media media--4x5 media--reveal media--parallax"><img src="assets/img/full/craft-stitch.jpg" alt="Stitching cognac leather on an industrial sewing machine"></div>
        <div class="media media--4x3"><video data-lazy data-src="assets/video/craft-stitch.mp4" poster="assets/img/thumb/craft-stitch.jpg" muted loop playsinline preload="none"></video></div>
      </div>
    </div>
    <div>
      <div class="eyebrow reveal">Heritage</div>
      <h2 class="big-statement">Three generations of leatherwork from Bogotá, brought to the skies of northern Utah. Every stitch carries the legacy of the workshops where our family learned the craft.</h2>
      <p class="lead reveal mt-2">Air Sew was built on the principle that an aircraft interior is more than seats and carpet. It's the space you spend your best hours in. We treat it that way, with premium materials, industrial design, and craftsmanship that takes its time.</p>
      <a class="link-arrow reveal" href="about.html"><span>Our story</span>{ARROW_UP}</a>
    </div>
  </div>
</section>

<section class="section section--tight bg-2" id="services">
  <div class="container">
    <div class="sec-head">
      <div><div class="eyebrow reveal">What we do</div><h2 class="display-lg" data-split>Every surface in the cabin, done as one design.</h2></div>
      <a class="link-arrow reveal" href="services.html"><span>All services</span>{ARROW_UP}</a>
    </div>
    <div class="services">{svc_html}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head">
      <div><div class="eyebrow reveal">Before &amp; after</div><h2 class="display-lg" data-split>Drag to see what forty years and three weeks look like.</h2></div>
      <p class="muted reveal" style="max-width:36ch">A worn 1970s cabin versus a period-correct restoration in saddle tan and cream. Same airplane family, different century.</p>
    </div>
    <div class="ba reveal-fade" aria-label="Before and after comparison, drag to compare">
      <img class="ba__before" src="assets/img/full/before-worn.jpg" alt="Worn 1970s aircraft interior before restoration">
      <img class="ba__after" src="assets/img/full/piper-comanche.jpg" alt="Restored vintage Piper cabin after restoration">
      <div class="ba__handle"><i>{DRAG}</i></div>
      <span class="ba__tag ba__tag--before">Before</span><span class="ba__tag ba__tag--after">After</span>
    </div>
  </div>
</section>

<section class="hscroll bg-2" id="restorations">
  <div class="hscroll__pin">
    <div class="hscroll__track">
      <div class="hcard hcard--intro">
        <div class="eyebrow">Recent restorations</div>
        <h2 class="display-md">Real airplanes. Real seats. Straight from Hangar 27.</h2>
        <p class="muted mt-1">A few of the projects that have rolled out of the shop lately. Every photo here is our own work.</p>
        <a class="link-arrow mt-1" href="restorations.html"><span>View the full gallery</span>{ARROW_UP}</a>
      </div>
      {proj_html}
      <a class="hcard hcard--cta" href="restorations.html"><div><div class="display-sm">See all projects</div><p class="muted small mt-1">Jets, singles, twins, helicopters, and experimentals</p><span class="btn btn--ghost btn--sm mt-1">Open gallery {ARROW}</span></div></a>
    </div>
  </div>
</section>

<section class="section" id="aircraft">
  <div class="container">
    <div class="sec-head">
      <div><div class="eyebrow reveal">Aircraft we service</div><h2 class="display-lg" data-split>From Archers to Phenoms, we know the cabin.</h2></div>
      <p class="muted reveal" style="max-width:36ch">Pick your airplane for model-specific scope, timelines, and pricing. Don't see yours? We service most certified and experimental types.</p>
    </div>
    <div class="fleet-tabs reveal" data-filter-group="#fleet">
      <button class="fleet-tab is-active" type="button" data-filter="all">All</button>
      <button class="fleet-tab" type="button" data-filter="piper">Piper</button>
      <button class="fleet-tab" type="button" data-filter="cessna">Cessna</button>
      <button class="fleet-tab" type="button" data-filter="pilatus">Pilatus</button>
      <button class="fleet-tab" type="button" data-filter="jet">Business Jets</button>
    </div>
    <div class="fleet-grid" id="fleet">{fleet_html}</div>
  </div>
</section>

<section class="section bg-2" id="materials">
  <div class="container materials">
    <div class="materials__media">
      <div class="media media--4x3 media--reveal"><img src="assets/img/full/materials.jpg" alt="Leather, fabric, and thread samples"><div class="materials__tint"></div></div>
    </div>
    <div>
      <div class="eyebrow reveal">Materials &amp; design</div>
      <h2 class="display-md" data-split>Over a thousand FAR-rated options. One that's yours.</h2>
      <p class="lead reveal mt-1">Full-hide aviation leather, Ultraleather, marine vinyl, wool, and technical fabrics, in every color you can name and a few you can't. Selected with you at a design appointment, in the airplane.</p>
      <div class="swatches reveal">{sw_html}</div>
      <p class="small muted mt-1">Selected: <span class="material-name">Navy full hide</span></p>
      <ul class="material-list reveal">
        <li><span>Full-hide leather</span><span>Premium · burn-certified</span></li>
        <li><span>Synthetic leather / Ultraleather</span><span>Durable · trainers &amp; utility</span></li>
        <li><span>Fabric &amp; wool blends</span><span>FAR 25.853 rated</span></li>
        <li><span>Carpet &amp; flooring</span><span>Bound edges · solution dyed</span></li>
        <li><span>Diamond stitch, perforation, piping</span><span>In-house</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head">
      <div><div class="eyebrow reveal">The process</div><h2 class="display-lg" data-split>Fly in. Fly out. Everything between is handled.</h2></div>
    </div>
    <div class="process">
      <div class="step"><div class="step__num">01</div><h3>Design appointment</h3><p>Sit in your airplane with our designer. Choose materials, colors, stitching, and personalization. Leave with a fixed quote.</p></div>
      <div class="step"><div class="step__num">02</div><h3>Fly in to Sky Park</h3><p>Taxi to Hangar 27. We remove seats, panels, headliner, and carpet on the field and photograph everything.</p></div>
      <div class="step"><div class="step__num">03</div><h3>Craft</h3><p>Frames repaired, foam rebuilt, covers patterned and sewn, panels wrapped, plastics paint-matched. Progress photos along the way.</p></div>
      <div class="step"><div class="step__num">04</div><h3>Install &amp; fly out</h3><p>Everything reinstalled, inspected, and documented for your logbook. Then you take a very different airplane home.</p></div>
    </div>
  </div>
</section>

<section class="section section--tight bg-2">
  <div class="container">
    <div class="sec-head">
      <div><div class="eyebrow reveal">Why Air Sew</div><h2 class="display-md" data-split>The advantages owners keep coming back for.</h2></div>
    </div>
    <div class="why">{why_html}</div>
  </div>
</section>

<section class="section">
  <div class="container split split--wide">
    <div class="media media--16x9 media--reveal media--parallax"><img src="assets/img/full/ramp-skypark.jpg" alt="Aircraft on the ramp with the Wasatch mountains behind"></div>
    <div>
      <div class="eyebrow reveal">Where to find us</div>
      <h2 class="display-md" data-split>Based at Sky Park. Serving the Wasatch Front.</h2>
      <p class="lead reveal mt-1">Our shop is in Hangar 27 at Sky Park Airport in Woods Cross, ten minutes north of downtown Salt Lake City. Jet and turboprop work can also be coordinated at South Valley Regional and Salt Lake City International.</p>
      <div class="airports reveal">
        <div class="airport"><span class="airport__code">BTF</span><div><b>Sky Park Airport</b><span>Woods Cross, UT · Home base · Hangar 27</span></div><small>Fly-in</small></div>
        <div class="airport"><span class="airport__code">U42</span><div><b>South Valley Regional</b><span>West Jordan, UT · Partner airport</span></div><small>On-site</small></div>
        <div class="airport"><span class="airport__code">SLC</span><div><b>Salt Lake City International</b><span>Salt Lake City, UT · Jet &amp; turboprop</span></div><small>On-site</small></div>
      </div>
      <a class="btn btn--ghost mt-2 reveal" href="contact.html">Directions &amp; contact {ARROW}</a>
    </div>
  </div>
</section>

{cta_band()}
"""
    return head("Air Sew · Aviation Upholstery & Aircraft Interior Restoration · Woods Cross, Utah",
                "Air Sew restores aircraft interiors for Piper, Cessna, Pilatus, and business jets from Sky Park Airport in Woods Cross, Utah. FAA-compliant materials, fixed pricing, fly-in / fly-out.") + preloader() + header("Home") + body + footer()

# ---------------------------------------------------------------------------
# Recent Restorations
# ---------------------------------------------------------------------------
def build_restorations():
    tiles = [
        ("real/citation-cj2-seat.jpg", "jet", "Business Jet", "Citation CJ2 · 2003", "New floors, front and rear seats in tan full hide", True),
        ("real/cessna-182-headliner.jpg", "cessna", "Cessna", "182 Skylane", "New headliner, embroidered headrests, two-tone seats", True),
        ("real/cessna-172-embroidered-seats.jpg", "cessna", "Cessna", "172 Skyhawk", "Gray leather with embroidered Cessna headrests", True),
        ("real/kodiak-diamond-seat.jpg", "utility", "Utility", "Quest Kodiak", "Navy with red diamond-stitched inserts", True),
        ("real/eagle-embroidery-seats.jpg", "personalized", "Personalized", "Custom embroidery", "Eagle motif on gray with patterned fabric inserts", True),
        ("real/rear-bench-two-tone.jpg", "cessna", "Cessna", "Rear bench", "Two-tone gray with contrast center panels", True),
        ("piper-archer.jpg", "piper", "Piper", "Archer PA-28", "Gray and tan leather with contrast stitching", False),
        ("pilatus-pc12.jpg", "pilatus", "Pilatus", "PC-12 executive cabin", "Cream club seats and walnut ledges", False),
        ("piper-comanche.jpg", "piper", "Piper", "Comanche PA-24", "Period-correct saddle tan and cream", False),
        ("cessna-206.jpg", "cessna utility", "Cessna", "206 Stationair", "Tan and charcoal six-place utility cabin", False),
        ("phenom-300.jpg", "jet", "Business Jet", "Phenom 300", "Charcoal and ivory executive seats", False),
        ("piper-aerostar.jpg", "piper", "Piper", "Aerostar", "Six-place cream leather club cabin", False),
        ("stitch-macro.jpg", "personalized", "Detail", "Diamond stitching", "Navy leather, red contrast thread", False),
        ("cessna-182.jpg", "cessna", "Cessna", "182 Skylane", "Navy and stone leather with new headliner", False),
        ("citation.jpg", "jet", "Business Jet", "Citation CJ series", "Tan full-hide club seats, new carpet", False),
    ]
    tiles_html = "".join(f"""<figure class="tile reveal" data-cat="{cat}">
  <img src="assets/img/full/{img}" alt="{title} interior restoration" loading="lazy">
  {'<span class="tile__badge">Shop photo</span>' if real else '<span class="tile__badge" style="background:rgba(46,143,216,0.85)">Design study</span>'}
  <figcaption class="tile__meta"><small>{cat_label}</small><b>{title}</b><span>{desc}</span></figcaption>
</figure>""" for img, cat, cat_label, title, desc, real in tiles)

    body = page_hero("Recent restorations", "Work that just rolled out of Hangar 27.",
                     "Jets, singles, twins, utility airplanes, and one-off personalization projects. Shop photos are our own completed work. Design studies show the schemes we're building next.",
                     "hero-cabin.jpg", [("Home", "index.html"), ("Recent Restorations", None)]) + f"""
<section class="section section--tight">
  <div class="container">
    <div class="spotlight reveal">
      <div class="media media--4x3 media--reveal"><img src="assets/img/full/real/citation-cj2-seat.jpg" alt="Restored Citation CJ2 seat in tan leather"></div>
      <div class="spotlight__text">
        <div class="eyebrow">Project spotlight</div>
        <h2 class="display-md">Citation CJ2 seat and floor restoration</h2>
        <p class="muted mt-1">Restoring the floors and seats in a 2003 Citation CJ2 jet based at Salt Lake City International. Every seat came off the airplane, was stripped to the frame, rebuilt with new foam, and re-covered in tan full-hide leather.</p>
        <ul class="spotlight__list">
          <li>New carpet and floor panels throughout the cabin</li>
          <li>New front crew seats, rebuilt mechanisms</li>
          <li>New rear executive seats in full-hide leather</li>
          <li>Removal and reinstallation coordinated at KSLC</li>
        </ul>
        <a class="link-arrow mt-2" href="citation.html"><span>Citation interiors</span>{ARROW_UP}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="filters reveal" data-filter-group="#gallery">
      <button class="fleet-tab is-active" type="button" data-filter="all">All</button>
      <button class="fleet-tab" type="button" data-filter="jet">Business Jets</button>
      <button class="fleet-tab" type="button" data-filter="pilatus">Pilatus</button>
      <button class="fleet-tab" type="button" data-filter="cessna">Cessna</button>
      <button class="fleet-tab" type="button" data-filter="piper">Piper</button>
      <button class="fleet-tab" type="button" data-filter="utility">Utility</button>
      <button class="fleet-tab" type="button" data-filter="personalized">Personalized</button>
    </div>
    <div class="masonry" id="gallery">{tiles_html}</div>
  </div>
</section>
""" + cta_band("hero-hangar", "Your airplane could be next.", "Book a design appointment and we'll build a scheme around how you actually fly.")
    return head("Recent Restorations · Air Sew", "A gallery of recent aircraft interior restorations by Air Sew: Citation, Cessna, Piper, Pilatus, Kodiak, and custom embroidery projects.") + preloader() + header("Recent Restorations") + body + footer()

# ---------------------------------------------------------------------------
# Aircraft model pages
# ---------------------------------------------------------------------------
def build_aircraft(a):
    label = f"{a['make']} {a['model']}"
    scope = [
        ("seat", "Seats", "Frames inspected and repaired, new high-density foam, new covers with your choice of stitching and piping."),
        ("panel", "Side & door panels", "Re-wrapped in matching material, armrests rebuilt, map pockets and trim replaced."),
        ("headliner", "Headliner & window trim", "New headliner fitted tight, window reveals re-covered or replaced."),
        ("floor", "Carpet & floors", "Aviation-grade carpet, bound edges, refurbished floor panels and sill plates."),
        ("cabin", "Plastics & trim", "Interior plastics repaired and paint-matched to the scheme, or replaced with new."),
        ("embroidery", "Personalization", "Embroidered headrests, tail numbers, logos, LED lighting, USB power."),
    ]
    scope_html = "".join(f'<div class="scope__item reveal"><i>{ICONS[k]}</i><div><b>{t}</b><p>{d}</p></div></div>' for k, t, d in scope)
    faq_html = "".join(f'<div class="faq__item"><button class="faq__q" type="button">{q}<i>{PLUS}</i></button><div class="faq__a"><p>{ans}</p></div></div>' for q, ans in a["faq"])
    # gallery: page image + relevant real photos + others
    gal = [a["img"], "stitch-macro.jpg", "craft-fitting.jpg", "materials.jpg", "workshop.jpg"]
    if a["make"] == "Cessna" and "Citation" not in a["model"]:
        gal = [a["img"], "real/cessna-172-embroidered-seats.jpg", "real/cessna-182-headliner.jpg", "real/rear-bench-two-tone.jpg", "stitch-macro.jpg"]
    if a["slug"] == "citation":
        gal = [a["img"], "real/citation-cj2-seat.jpg", "stitch-macro.jpg", "craft-fitting.jpg", "materials.jpg"]
    gal_html = "".join(f'<div class="media media--reveal"><img src="assets/img/full/{g}" alt="{label} interior detail" loading="lazy"></div>' for g in gal)
    related = [x for x in AIRCRAFT if x["slug"] != a["slug"] and (x["make"] == a["make"] or ("jet" in a["cats"] and "jet" in x["cats"]))][:3]
    if len(related) < 3:
        related += [x for x in AIRCRAFT if x not in related and x["slug"] != a["slug"]][: 3 - len(related)]
    rel_html = "".join(fleet_card(x) for x in related)
    intro_html = "".join(f"<p class=\"lead reveal\">{p}</p>" for p in a["intro"])

    body = page_hero(f"{a['make']} interiors · {a['designation']}", f"{label}", a["tagline"], a["img"],
                     [("Home", "index.html"), (a["make"], "index.html#aircraft"), (a["model"], None)]) + f"""
<section class="section section--tight">
  <div class="container">
    <div class="spec-strip reveal">
      <div class="spec"><small>Seats</small><b>{a['seats']}</b></div>
      <div class="spec"><small>Typical timeline</small><b>{a['timeline']}</b></div>
      <div class="spec"><small>Full interior</small><b>{a['price']}</b></div>
      <div class="spec"><small>Materials</small><b>FAA compliant</b></div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container split split--wide">
    <div>
      <div class="eyebrow reveal">About the {a['model']}</div>
      <h2 class="display-md" data-split>What we do for the {label}.</h2>
      <div class="mt-2">{intro_html}</div>
      <div class="pricing-note reveal mt-2"><b>Fixed-price quotes</b><p>Every {a['model']} project is quoted as a fixed price after a design appointment in your airplane. Financing is available. Ask for details.</p></div>
    </div>
    <div class="media media--4x5 media--reveal media--parallax"><img src="assets/img/full/{a['img']}" alt="{label} restored interior"></div>
  </div>
</section>

<section class="section section--tight bg-2">
  <div class="container">
    <div class="sec-head"><div><div class="eyebrow reveal">Scope</div><h2 class="display-md" data-split>Everything in the cabin, or just the parts that need it.</h2></div><p class="muted reveal" style="max-width:36ch">Most owners start with seats and carpet. Many come back for the rest. Either order works.</p></div>
    <div class="scope">{scope_html}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="sec-head"><div><div class="eyebrow reveal">Gallery</div><h2 class="display-md" data-split>Details from the bench.</h2></div></div>
    <div class="gallery">{gal_html}</div>
  </div>
</section>

<section class="section section--tight bg-2">
  <div class="container grid-2">
    <div><div class="eyebrow reveal">FAQ</div><h2 class="display-md" data-split>{a['model']} questions, answered.</h2><p class="muted reveal mt-1">Anything else? Call {PHONE} or <a href="contact.html" style="text-decoration:underline">send us the details</a>.</p></div>
    <div class="faq reveal">{faq_html}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="sec-head"><div><div class="eyebrow reveal">Related</div><h2 class="display-md" data-split>Other aircraft we service.</h2></div><a class="link-arrow reveal" href="index.html#aircraft"><span>All aircraft</span>{ARROW_UP}</a></div>
    <div class="related">{rel_html}</div>
  </div>
</section>
""" + cta_band("hero-cabin", f"Let's talk about your {a['model']}.", "Schedule a design appointment at Sky Park and leave with a fixed quote.")
    return head(f"{label} Interior Restoration & Upholstery · Air Sew", f"{label} ({a['designation']}) interior restoration and upholstery from Air Sew in Woods Cross, Utah. Seats, headliner, carpet, panels, and personalization. Fixed pricing, fly-in / fly-out.") + preloader() + header("Light Planes" if a["make"] in ("Piper", "Cessna", "Pilatus") else "Business Jets") + body + footer()

# ---------------------------------------------------------------------------
# Experimental
# ---------------------------------------------------------------------------
def build_experimental():
    types = [
        ("Van's RV series", "RV-4 through RV-14 and the RV-10. Sport seats, side panels, carpet, and baggage-area trim built light and tough."),
        ("Lancair & Glasair", "Composite cabins with sculpted panels. We wrap complex curves cleanly and keep the weight down."),
        ("Kitfox, Cub clones & backcountry", "Rugged synthetic leather, reinforced seams, and simple, serviceable interiors for airplanes that work."),
        ("Sling, Sonex & light sport", "Weight-conscious interiors where every ounce counts, without giving up comfort on long legs."),
        ("Warbird replicas & scratch-builds", "One-off cabins and cockpits patterned from your airframe, not a template."),
        ("Helicopters & gyros", "Robinson, Bell, Rotorway, and gyroplane seats and panels, built for vibration and sun."),
    ]
    types_html = "".join(f'<div class="why__item reveal"><i></i><b>{t}</b><p>{d}</p></div>' for t, d in types)
    faq = [
        ("Do experimental interiors need certified materials?", "There is no FAA requirement for burn-certified fabrics in an experimental amateur-built aircraft, but we recommend and stock them anyway. They cost little more, they are safer, and they hold their value at resale."),
        ("Can you work from my drawings or a template?", "Yes. Bring the seat frames, panels, or a cardboard mock-up, and we pattern from the real parts. For airplanes still under construction we can build covers to your foam and frame before the cabin closes up."),
        ("How light can you go?", "Lightweight foams, thin-hide leather, and minimal backing can save several pounds over a conventional interior. Tell us your weight budget at the design appointment and we design to it."),
        ("Do you offer embroidery and custom colors?", "All of it. Builder's logos, N-numbers, tail art, diamond stitching, and any color in our library, in-house."),
    ]
    faq_html = "".join(f'<div class="faq__item"><button class="faq__q" type="button">{q}<i>{PLUS}</i></button><div class="faq__a"><p>{a}</p></div></div>' for q, a in faq)
    body = page_hero("Experimental &amp; homebuilt", "Experimental aircraft interiors.", "Builders spend years getting the airframe right. We make sure the cabin lives up to it, with lightweight, personalized interiors for RVs, Lancairs, Kitfoxes, light sport, and one-off designs.",
                     "experimental.jpg", [("Home", "index.html"), ("Experimental", None)]) + f"""
<section class="section section--tight">
  <div class="container">
    <div class="spec-strip reveal">
      <div class="spec"><small>Seats only</small><b>1–2 weeks</b></div>
      <div class="spec"><small>Full cabin</small><b>2–4 weeks</b></div>
      <div class="spec"><small>Seats from</small><b>$3,500</b></div>
      <div class="spec"><small>Materials</small><b>Weight-conscious</b></div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container split split--wide">
    <div>
      <div class="eyebrow reveal">Built for builders</div>
      <h2 class="display-md" data-split>Your airplane is one of a kind. The interior should be too.</h2>
      <p class="lead reveal mt-2">Experimental aircraft give us a freedom certified airplanes don't: no STC, no approved-parts list, and an owner who already knows every rivet. We use that freedom to build interiors that are lighter, more personal, and often more comfortable than anything in a production cabin.</p>
      <p class="lead reveal">Sport-style seats with bolsters and perforated inserts, carbon-look or leather-wrapped panels, custom embroidery, LED lighting, and carpet cut to your floor. Patterned from your actual frames and panels at Sky Park, or from parts you ship to us.</p>
      <div class="pricing-note reveal mt-2"><b>Still under construction? Start early.</b><p>The best time to design the interior is before the cabin closes up. Bring the project in or send photos and we will build covers to your frames and foam so everything drops in at final assembly.</p></div>
    </div>
    <div class="media media--4x5 media--reveal media--parallax"><img src="assets/img/full/experimental.jpg" alt="Experimental aircraft sport seats in charcoal leather with red stitching"></div>
  </div>
</section>

<section class="section section--tight bg-2">
  <div class="container">
    <div class="sec-head"><div><div class="eyebrow reveal">What we see on the ramp</div><h2 class="display-md" data-split>From RVs to rotorcraft.</h2></div></div>
    <div class="why">{types_html}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="sec-head"><div><div class="eyebrow reveal">Gallery</div><h2 class="display-md" data-split>Details from the bench.</h2></div></div>
    <div class="gallery">
      <div class="media media--reveal"><img src="assets/img/full/experimental.jpg" alt="Experimental cabin" loading="lazy"></div>
      <div class="media media--reveal"><img src="assets/img/full/stitch-macro.jpg" alt="Diamond stitching detail" loading="lazy"></div>
      <div class="media media--reveal"><img src="assets/img/full/real/kodiak-diamond-seat.jpg" alt="Navy and red diamond seat" loading="lazy"></div>
      <div class="media media--reveal"><img src="assets/img/full/real/eagle-embroidery-seats.jpg" alt="Custom eagle embroidery" loading="lazy"></div>
      <div class="media media--reveal"><img src="assets/img/full/craft-fitting.jpg" alt="Fitting a seat cover" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section section--tight bg-2">
  <div class="container grid-2">
    <div><div class="eyebrow reveal">FAQ</div><h2 class="display-md" data-split>Experimental questions, answered.</h2><p class="muted reveal mt-1">Anything else? Call {PHONE} or <a href="contact.html" style="text-decoration:underline">send us the details</a>.</p></div>
    <div class="faq reveal">{faq_html}</div>
  </div>
</section>
""" + cta_band("hero-hangar", "Let's finish the airplane.", "Bring the project to Sky Park, or send photos of the frames and panels, and we'll quote a fixed price.")
    return head("Experimental Aircraft Interiors & Upholstery · Air Sew", "Lightweight, personalized interiors for experimental and homebuilt aircraft: Van's RV, Lancair, Glasair, Kitfox, light sport, and helicopters. Air Sew, Woods Cross, Utah.") + preloader() + header("Experimental") + body + footer()

# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------
def build_services():
    rows = [
        ("Aircraft seat restoration", "We carefully remove the existing upholstery with the frame intact, inspect and repair cracks, loose joints, and worn mechanisms, replace the foam with new high-density material carved to the original profile, and re-cover in leather, synthetic leather, or certified fabric.", "craft-fitting.jpg"),
        ("Full interior restoration", "Seats, side and door panels, headliner, carpet, plastics, and trim designed as one scheme and installed together. This is the transformation most owners are after, and the one that adds the most value to the airplane.", "hero-cabin.jpg"),
        ("Headliners", "Sagging, stained, or brittle headliners replaced with new material fitted tight to the airframe. Window reveals and overhead trim re-covered to match.", "cessna-182.jpg"),
        ("Floors & carpet", "Aviation-grade carpet with bound edges, refurbished floor panels, new sill plates, and durable solution-dyed options for utility airplanes.", "citation.jpg"),
        ("Side panels & plastics", "Side and door panels re-wrapped, armrests rebuilt, and interior plastics repaired and paint-matched to the overall theme, or replaced with new lightweight parts.", "piper-archer.jpg"),
        ("Custom design, stitching & embroidery", "Diamond quilting, perforation, contrast piping, and in-house embroidery of logos, tail numbers, and artwork. Lighting, USB power, and modern touches integrated during the rebuild.", "stitch-macro.jpg"),
        ("Private jet & turboprop interiors", "Executive seats, divans, veneer and cabinetry refinishing, lighting, and complete cabin refurbishment for Citation, Phenom, PC-12, PC-24, King Air, and Kodiak operators.", "pilatus-pc12.jpg"),
        ("Helicopter & experimental", "Robinson, Bell, and Airbus helicopter interiors, plus experimental and light-sport aircraft where weight and creativity both matter.", "workshop.jpg"),
    ]
    rows_html = "".join(f"""<div class="service-row reveal">
  <span class="service-row__num">0{i+1}</span>
  <h3>{t}</h3>
  <p>{d}</p>
  <div class="media"><img src="assets/img/thumb/{img}" alt="{t}" loading="lazy"></div>
</div>""" for i, (t, d, img) in enumerate(rows))
    body = page_hero("Services", "Every surface in the cabin. One shop.", "From a single re-covered seat to a complete executive cabin, every project gets the same materials, the same craftsmanship, and the same fixed quote.",
                     "workshop.jpg", [("Home", "index.html"), ("Services", None)]) + f"""
<section class="section section--tight">
  <div class="container"><div class="service-rows">{rows_html}</div></div>
</section>
<section class="section bg-2">
  <div class="container split">
    <div>
      <div class="eyebrow reveal">Materials</div>
      <h2 class="display-md" data-split>Premium, certified, and chosen in your airplane.</h2>
      <p class="lead reveal mt-1">Full-hide leather, Ultraleather, marine vinyl, wool, and technical fabrics, all burn-certified for their application. We bring the samples to the design appointment so you can see them in your cabin's light.</p>
      <ul class="checks reveal">
        <li>{CHECK}<span>Fabric, vinyl, synthetic leather, and full-hide leather</span></li>
        <li>{CHECK}<span>Over 1,000 FAR-rated design and personalization options</span></li>
        <li>{CHECK}<span>Lighting and modernization packages</span></li>
        <li>{CHECK}<span>Documentation for your logbook with every install</span></li>
      </ul>
    </div>
    <div class="media media--4x3 media--reveal media--parallax"><img src="assets/img/full/materials.jpg" alt="Material samples"></div>
  </div>
</section>
""" + cta_band()
    return head("Aircraft Interior Services · Air Sew", "Seat restoration, full interior restoration, headliners, floors, panels, embroidery, jet and helicopter interiors from Air Sew in Woods Cross, Utah.") + preloader() + header("Services") + body + footer()

# ---------------------------------------------------------------------------
# About
# ---------------------------------------------------------------------------
def build_about():
    body = page_hero("Heritage & history", "A family craft, three generations deep.", "Nestled in the heart of Bogotá, Colombia, where leatherwork and upholstery are revered traditions, Air Sew's story begins with the skilled hands of our forebears.",
                     "craft-stitch.jpg", [("Home", "index.html"), ("About", None)], actions=False) + f"""
<section class="section">
  <div class="container split split--narrow">
    <div class="media media--4x5 media--reveal media--parallax"><img src="assets/img/full/craft-fitting.jpg" alt="Craftsman fitting a leather seat cover"></div>
    <div>
      <div class="eyebrow reveal">Our story</div>
      <h2 class="big-statement">In the workshops of our grandparents in Bogotá, the hum of sewing machines and the scent of leather became symbols of our family's dedication to their craft.</h2>
      <p class="lead reveal mt-2">Three generations ago, our family embarked on a journey of craftsmanship, mastering the art of transforming leather and fabric into work of beauty and durability. Our parents expanded on that legacy, embracing innovation while honoring tradition. Today, at Air Sew, we bring that heritage to the skies of Utah.</p>
      <p class="reveal muted">Our commitment goes beyond crafting seats and interiors. It's about creating an experience that pays homage to our past while soaring toward the future. Each stitch we make, each design we conceive, carries the legacy of our forebears.</p>
    </div>
  </div>
</section>

<section class="section section--tight bg-2">
  <div class="container">
    <div class="sec-head"><div><div class="eyebrow reveal">Timeline</div><h2 class="display-md" data-split>From Bogotá to Sky Park.</h2></div></div>
    <div class="timeline">
      <div class="tl reveal"><b>Gen. 1</b><div><h3>The Bogotá workshops</h3><p>Our grandparents master leatherwork and upholstery, building a reputation on hard work, exceptional skill, and an unwavering commitment to quality.</p></div></div>
      <div class="tl reveal"><b>Gen. 2</b><div><h3>Tradition meets innovation</h3><p>Our parents expand the family business, adopting new materials and techniques while preserving the old ways that make the work last.</p></div></div>
      <div class="tl reveal"><b>Gen. 3</b><div><h3>Air Sew takes flight</h3><p>The craft moves to aviation. Air Sew opens at Sky Park Airport in Woods Cross, Utah, specializing in aircraft interiors for private owners, flight schools, and business aviation.</p></div></div>
      <div class="tl reveal"><b>Today</b><div><h3>Hangar 27</h3><p>Fly-in / fly-out service from Sky Park, partnerships at South Valley and Salt Lake City International, and a growing list of Citations, Skylanes, Archers, and Kodiaks that leave looking brand new.</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head"><div><div class="eyebrow reveal">Values</div><h2 class="display-md" data-split>What we promise every owner.</h2></div></div>
    <div class="values">
      <div class="value reveal"><b>01</b><h3>Fixed cost</h3><p>Transparent pricing with no hidden fees. The quote you approve is the invoice you get.</p></div>
      <div class="value reveal"><b>02</b><h3>Client communication</h3><p>Consistent, clear updates throughout the process, with photos from the bench.</p></div>
      <div class="value reveal"><b>03</b><h3>Reputation</h3><p>A legacy of excellence and customer satisfaction, built one interior at a time.</p></div>
    </div>
  </div>
</section>

<section class="section section--flush">
  <div class="media media--21x9 media--reveal media--parallax" style="border-radius:0"><img src="assets/img/full/workshop.jpg" alt="Air Sew workshop"></div>
</section>

<section class="section bg-2">
  <div class="container split">
    <div>
      <div class="eyebrow reveal">Community</div>
      <h2 class="display-md" data-split>We show up where pilots gather.</h2>
      <p class="lead reveal mt-1">From the Sky Park Aviation Festival to fly-ins across the Wasatch Front, we try to join our fellow aviation enthusiasts as often as we can. Come find the booth, sit in a seat, and bring your questions.</p>
      <a class="btn btn--ghost reveal mt-1" href="contact.html">Get in touch {ARROW}</a>
    </div>
    <div class="media media--4x3 media--reveal"><img src="assets/img/full/ramp-skypark.jpg" alt="Aircraft on the Sky Park ramp"></div>
  </div>
</section>
""" + cta_band("hero-hangar", "Come see the shop.", "Fly in to Sky Park or drive up from Salt Lake. We'll show you the bench, the samples, and what's on the stands.")
    return head("About Air Sew · Heritage & History", "Air Sew's story: three generations of leatherwork and upholstery from Bogotá, Colombia, now specializing in aircraft interiors at Sky Park Airport in Woods Cross, Utah.") + preloader() + header("About") + body + footer()

# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------
def build_contact():
    options = "".join(f'<option>{a["make"]} {a["model"]}</option>' for a in AIRCRAFT) + "<option>Beechcraft</option><option>Cirrus</option><option>Mooney</option><option>Daher / Kodiak</option><option>Helicopter</option><option>Experimental / homebuilt</option><option>Other</option>"
    body = page_hero("Contact", "Tell us about your project.", "Send the details and we'll follow up to schedule a design appointment. Prefer the phone? Call " + PHONE + " during shop hours.",
                     "ramp-skypark.jpg", [("Home", "index.html"), ("Contact", None)], short=True, actions=False) + f"""
<section class="section section--tight" id="appointment">
  <div class="container contact">
    <div>
      <div class="eyebrow reveal">Project inquiry</div>
      <h2 class="display-md" data-split>Schedule a design appointment.</h2>
      <form class="form mt-2 reveal" id="project-form" data-to="{EMAIL}" novalidate>
        <div class="form__row">
          <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" type="text" required placeholder="Your name"></div>
          <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" placeholder="(555) 555-5555"></div>
        </div>
        <div class="form__row">
          <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" required placeholder="you@example.com"></div>
          <div class="field"><label for="f-aircraft">Aircraft</label><select id="f-aircraft" name="aircraft">{options}</select></div>
        </div>
        <div class="form__row">
          <div class="field"><label for="f-tail">Tail number (optional)</label><input id="f-tail" name="tail" type="text" placeholder="N12345"></div>
          <div class="field"><label for="f-scope">Scope</label><select id="f-scope" name="scope"><option>Full interior</option><option>Seats only</option><option>Seats and carpet</option><option>Headliner</option><option>Panels and plastics</option><option>Embroidery / personalization</option><option>Not sure yet</option></select></div>
        </div>
        <div class="field"><label for="f-msg">Tell us about the airplane</label><textarea id="f-msg" name="message" placeholder="Year, current interior condition, what you have in mind, and where the airplane is based."></textarea></div>
        <div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">
          <button class="btn btn--blue" type="submit">Send inquiry {ARROW}</button>
          <span class="form__note">Opens your email client with the details pre-filled.</span>
        </div>
        <p class="form__success" hidden style="color:var(--blue-2)">Thanks. Your email client should now be open with the inquiry. We'll be in touch shortly.</p>
      </form>
    </div>
    <div>
      <div class="contact-card reveal">
        <h3>Call the shop</h3>
        <a class="big" href="{PHONE_TEL}">{PHONE}</a>
        <p>Monday to Friday, 8am to 5pm Mountain. Fly-ins by appointment.</p>
      </div>
      <div class="contact-card reveal">
        <h3>Visit Hangar 27</h3>
        <p><b>Sky Park Airport (KBTF)</b><br>2124 Thunderbird Dr, Hangar 27<br>Woods Cross, UT 84087</p>
        <p class="mt-1"><a class="link-arrow" href="https://maps.google.com/?q=2124+Thunderbird+Dr+Woods+Cross+UT" target="_blank" rel="noopener"><span>Get directions</span>{ARROW_UP}</a></p>
      </div>
      <div class="contact-card reveal">
        <h3>Partner airports</h3>
        <p>South Valley Regional (U42), West Jordan<br>Salt Lake City International (KSLC)</p>
      </div>
      <div class="contact-card reveal">
        <h3>Email</h3>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="map reveal-fade"><iframe title="Map to Air Sew at Sky Park Airport" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=2124+Thunderbird+Dr+Woods+Cross+UT+84087&output=embed"></iframe></div>
  </div>
</section>
"""
    return head("Contact Air Sew · Schedule a Design Appointment", "Contact Air Sew at Sky Park Airport, Woods Cross, Utah. Call (385) 595-6002 or send your aircraft interior project details to schedule a design appointment.") + preloader() + header("Contact") + body + footer()

# ---------------------------------------------------------------------------
# Legal stubs
# ---------------------------------------------------------------------------
def build_legal(title, slug, text):
    body = page_hero("Legal", title, "", "workshop.jpg", [("Home", "index.html"), (title, None)], short=True, actions=False) + f"""
<section class="section section--tight"><div class="container" style="max-width:800px"><div class="muted">{text}</div></div></section>"""
    return head(f"{title} · Air Sew", f"Air Sew {title.lower()}.") + preloader() + header("") + body + footer()

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0a0d12"/><path d="M32 10 20 40h6l6-16 6 16h6L32 10Z" fill="#2e8fd8"/><path d="M8 44h48v4H8z" fill="#e5322d"/><circle cx="24" cy="54" r="4" fill="#e5322d"/><circle cx="40" cy="54" r="4" fill="#e5322d"/></svg>"""

def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name, len(content) // 1024, "KB")

if __name__ == "__main__":
    write("index.html", build_index())
    write("restorations.html", build_restorations())
    write("experimental.html", build_experimental())
    write("services.html", build_services())
    write("about.html", build_about())
    write("contact.html", build_contact())
    for a in AIRCRAFT:
        write(a["slug"] + ".html", build_aircraft(a))
    write("privacy.html", build_legal("Privacy Policy", "privacy", "<p>Air Sew collects only the information you choose to send us through the contact form, by email, or by phone, and uses it solely to respond to your inquiry and deliver our services. We do not sell or share personal information with third parties for marketing. This site uses no tracking cookies. Contact us at " + EMAIL + " with any questions.</p>"))
    write("terms.html", build_legal("Terms & Conditions", "terms", "<p>All quotes are fixed-price and valid for 30 days from the date issued. Work begins upon receipt of a signed quote and deposit. Materials are certified for their intended aviation application and documentation is provided with each installation. Timelines are estimates and may be affected by material availability. Air Sew is not responsible for airframe conditions discovered during removal that are outside the quoted scope; these will be communicated and quoted separately before any additional work is performed.</p>"))
    with open(os.path.join(OUT, "assets", "img", "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(FAVICON)
    print("done")
