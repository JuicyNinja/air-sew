# Card
A square-cornered project or service item: image on top, mono label, one-line title. In Logbook most lists are rows or registers, not cards; use cards only for photo-led items (projects, style tiles).

**Consumer provides:** an image in `.as-card__media` (4:3, real work), a mono label in `.as-eyebrow` (e.g. "[Year] A36 Bonanza"), an `h3` title, and at most one `.as-card__link`.

- Border 1px `ink`, radius `radius-lg` (2px), image corners 0. No hover lift; links underline on hover.
- Grids are 3-up desktop, 1-up or swipe rows on mobile with 20px gutters.
- Empty media falls back to `linen` — replace with a photo before launch.

Don't: add shadows, colored borders, icons in circles, or more than one link per card.
