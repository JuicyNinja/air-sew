# FormField
A stacked label, input and help line: `.as-field` wrapping `.as-label`, `.as-input` and `.as-help`. The tail-number field is its own pattern, `.as-tail` (fixed "N" prefix on `draft`, 24px mono).

**Consumer provides:** a visible label tied to the input with `for`/`id`, an optional placeholder example, and help text; on error add `.as-field--error`, `aria-invalid="true"`, and a help line that says how to fix it.

- Inputs sit on `surface`; borders `line-strong` (3:1) or `ink`. Height 52px, radius `radius-sm` (4px), label-to-input gap 8px, fields 20px apart.
- Errors use `needle` for the border and message, always with words.

Don't: rely on placeholder as the label, or mark errors by color alone.
