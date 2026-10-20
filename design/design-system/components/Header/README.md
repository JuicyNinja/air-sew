# Header
The site header: logo left, at most five nav links, one primary button right, on `surface` with a `line` hairline below.

**Consumer provides:** the logo `<img>` (the Logos asset, 40px tall), nav `<a>` links with `aria-current="page"` on the active one, and one `as-btn--primary as-btn--sm`.

- Height is `header-height` (80px desktop, 64px mobile). Sticky on scroll; add `shadow-lift` once the page has scrolled.
- Active link: `navy` text with a 2px `needle` underline.
- Mobile: collapse links into a menu button; keep the quote button visible.

Don't: add a top utility bar, put more than five links, or place the header on navy (the logo is made for light grounds).
