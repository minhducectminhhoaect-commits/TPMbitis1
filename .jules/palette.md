## 2024-10-27 - Accessibility in Legacy Modals
**Learning:** Legacy `div`-based modals often lack semantic roles, making them invisible to screen readers despite being visually obvious.
**Action:** Always retro-fit `role="dialog"` and `aria-modal="true"` to existing modal containers before attempting complex focus trapping logic.
