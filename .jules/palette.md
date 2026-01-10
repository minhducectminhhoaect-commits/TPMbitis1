## 2024-05-22 - [Manual Modal A11y]
**Learning:** Modals are implemented as simple `div` toggles without semantic structure. `index.html` whitespace is inconsistent, breaking standard diff tools.
**Action:** Use Python scripts for reliable patching. Always manually add `role="dialog"` and `aria-modal="true"` to new modals.
