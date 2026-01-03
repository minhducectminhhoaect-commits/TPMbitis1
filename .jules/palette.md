## 2026-01-03 - Modal Accessibility Patterns
**Learning:** Legacy `div`-based modals are completely invisible to screen readers as dialogs, and text-based close buttons like "X" are ambiguous without labels.
**Action:** Always wrap modals with `role="dialog"`, `aria-modal="true"`, and `aria-labelledby` pointing to a unique title ID. Ensure close buttons have descriptive `aria-label`.
