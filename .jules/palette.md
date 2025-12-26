## 2024-05-23 - Accessibility of Modal Dialogs
**Learning:** Using standard `div` elements for modals without ARIA roles (dialog, modal) and focus management creates a significant barrier for screen reader and keyboard users.
**Action:** Always implement `role="dialog"`, `aria-modal="true"`, and a global Escape key listener to close modals, even in legacy codebases where full focus trapping might be complex. This provides a baseline of accessibility.
