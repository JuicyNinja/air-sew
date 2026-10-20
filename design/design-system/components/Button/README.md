# Button
A link or button styled as `.as-btn` plus one variant: `--primary`, `--secondary`, `--accent` or `--text`.

**Consumer provides:** an `<a>` (navigates) or `<button>` (submits/acts) with a sentence-case verb label; add `--sm` for compact rows.

- `--primary` (navy fill, `on-navy` text) is the default action. One or two per section.
- `--secondary` (navy outline) sits beside a primary as the alternative.
- `--accent` (`needle` fill) is the single most important call-to-action on a page — use it at most once.
- `--text` is for inline "learn more" moves; its hover underline is `needle`.
- Minimum height 48px (40px for `--sm`). Gap between buttons: `space-sm`.

Don't: stack three filled buttons, use `--accent` for routine actions, or write labels in all caps.
