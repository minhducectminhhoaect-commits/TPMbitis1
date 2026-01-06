## 2024-05-23 - Accessibility Patterns for Legacy Apps
**Learning:** Legacy apps often use `div` elements for notifications without roles, making them invisible to screen readers.
**Action:** Always check `showToast` or similar global notification functions. Adding `role="alert"` (for errors) and `role="status"` (for info) is a high-impact, low-risk change that immediately benefits screen reader users. Also check for "X" buttons on modals - they are prime candidates for `aria-label`.
