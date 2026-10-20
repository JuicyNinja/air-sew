# FormField
A stacked label, input and help line: `.as-field` wrapping `.as-label`, `.as-input` and `.as-help`.

**Consumer provides:** a visible label tied to the input with `for`/`id`, an optional placeholder example, and help text; on error add `.as-field--error`, `aria-invalid="true"`, and a help line that says how to fix it.

- Inputs sit on `surface` only — `line-strong` borders meet 3:1 there. On `sky` or `paper`, wrap the form in a white card.
- Height 48px, radius `radius-sm`, label-to-input gap `space-xs`, fields `space-lg` apart.
- Errors use `needle` for the border and message, always with words.

Don't: rely on placeholder as the label, or mark errors by color alone.
