# Palette's Journal

This journal tracks critical UX and accessibility learnings.

## 2024-05-22 - Legacy Modal Accessibility
**Learning:** The application uses plain `div` elements for modals without ARIA roles, making them invisible or confusing to screen readers.
**Action:** Always add `role="dialog"` and `aria-modal="true"` to custom modal containers. Ensure close buttons have accessible labels.
