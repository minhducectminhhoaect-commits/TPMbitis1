## 2024-05-23 - Custom Modal Accessibility
**Learning:** For custom modals implemented as `div` toggles without a framework, adding `role="dialog"`, `aria-modal="true"`, and a global `keydown` listener for the Escape key is a critical low-effort, high-impact accessibility improvement.
**Action:** When observing custom modals, always ensure they support Escape key closing and have proper ARIA roles.
