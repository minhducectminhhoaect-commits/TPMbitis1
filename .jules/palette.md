## 2024-05-22 - Accessibility Improvements for Modals
**Learning:** Adding `role="dialog"` and `aria-modal="true"` transforms `div` overlays into accessible dialogs, but keyboard support (Escape key) must be manually implemented as `div`s don't handle it natively like `<dialog>` elements.
**Action:** Always pair ARIA modal attributes with a global `keydown` listener for Escape to ensure keyboard accessibility.
