## 2024-05-23 - Accessibility Patterns in Legacy Single-File Apps
**Learning:** In "single file" apps where modals are just `div`s, standard accessibility features (focus trapping, ARIA roles) are almost always missing. Users relying on screen readers often get lost because the "modal" is just a div at the end of the DOM, not a true dialog.
**Action:** Always add `role="dialog"`, `aria-modal="true"`, and `aria-label`/`aria-labelledby` to these `div` structures. Ensure close buttons have `aria-label` especially if they are icon-only or generic text like "X".
