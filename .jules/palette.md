## 2024-05-23 - Accessibility Updates to Legacy Modals
**Learning:** Legacy `div`-based modals without semantic markup are invisible to screen readers as dialogs. Simply adding `role="dialog"` and `aria-modal="true"` is a high-impact, low-effort fix that doesn't break existing CSS layouts.
**Action:** Always check `div.hidden` toggles for missing ARIA attributes and add them during micro-UX passes.

## 2024-05-23 - Visual Label Consistency
**Learning:** Mixing placeholders with inline styled labels creates a disjointed UI. Using a shared CSS class (`.input-label`) for all form inputs not only improves consistency but allows for global accessibility styling updates later.
**Action:** Replace inline label styles with `.input-label` and ensure every input has a corresponding `<label for="...">`.
