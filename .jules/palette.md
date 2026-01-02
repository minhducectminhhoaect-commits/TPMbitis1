## 2024-05-23 - Accessibility of Single-Line Forms
**Learning:** Using placeholder text as the only label is a common pattern in legacy code that hurts accessibility and usability. Adding explicit `<label>` elements and `required` attributes provides immediate structure and screen reader support without needing complex CSS changes.
**Action:** Always check if inputs have associated labels, even if the design seems "cleaner" without them. Use `for` attribute to link label and input.
