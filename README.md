# Air Sew — website redesign

Static, dependency-free site for **Air Sew · Aviation Upholstery and Interiors** (Sky Park Airport, Woods Cross, UT).

## Structure

```
index.html                 Home (video hero, heritage, services, before/after, horizontal restorations, fleet, materials, process, location)
restorations.html          Recent Restorations gallery with filters + Citation CJ2 spotlight
services.html              Service catalogue
about.html                 Heritage & history
contact.html               Project inquiry form + map
piper-archer.html          Aircraft model pages (one per model, generated from build.py)
piper-aerostar.html
piper-comanche.html
cessna-172.html
cessna-182.html
cessna-206.html
pilatus-pc12.html
pilatus-pc24.html
citation.html
phenom-300.html
privacy.html / terms.html  Legal stubs
assets/css/main.css        Design system + layout + motion primitives
assets/js/main.js          GSAP ScrollTrigger + Lenis motion layer, nav, before/after, filters, form
assets/img/full/           Web-sized photos (1920px). /real = actual shop photos from the old site
assets/img/thumb/          800px thumbnails (menus, cards)
assets/img/orig-2k/        Original 2K AI renders (not referenced by the site; safe to delete)
assets/video/              Hero & B-roll loops (MP4, 5s)
build.py                   Page generator. Edit content/nav here, then run `python build.py`
```

## Editing content

All navigation, aircraft data (specs, copy, FAQ), and page sections live in `build.py`.
Run `python build.py` after any change to regenerate every page with a consistent header and footer.

To add an aircraft model: append a `dict(...)` to `AIRCRAFT`, drop a 16:9 image in `assets/img/full/` and `assets/img/thumb/`, and add its slug to the relevant `NAV` submenu.

## Preview locally

```
python -m http.server 8765
```
then open http://localhost:8765

## Notes

- Photos in `assets/img/full/real/` are Air Sew's own project photos (recovered from the previous site). All other photography and the video loops were generated with Runware (Seedream 4.0 stills, Kling 2.5 image-to-video) as design studies; the Restorations gallery labels them "Design study" vs "Shop photo".
- The contact form opens the visitor's email client pre-filled (no backend). Swap the `<form>` for Formspree/Netlify Forms if you want server-side delivery.
- Fonts (Playfair Display, Manrope) load from Google Fonts; GSAP from cdnjs; Lenis from jsDelivr.
- Deploy by uploading the whole folder to any static host (Netlify, Cloudflare Pages, S3, cPanel).
