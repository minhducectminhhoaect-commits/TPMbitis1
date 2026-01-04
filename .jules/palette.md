## 2024-05-24 - Accessibility Patterns for Legacy Apps
**Learning:** Legacy single-file apps with `div`-based modals and inline styles often lack basic ARIA semantics. Retrofitting `role="dialog"`, `aria-modal="true"`, and explicit `aria-labelledby` linked to header IDs is a high-impact, low-risk way to improve accessibility without breaking layout.
**Action:** When auditing modals, check for role, modal state, and label association. Use `aria-label` for icon-only close buttons if text is ambiguous.

## 2024-05-24 - Label Association in Forms
**Learning:** Inputs often have visual labels (text next to input) but lack semantic association (`for` attribute matching `id`). This breaks screen reader navigation.
**Action:** Systematically scan for `<label>` elements and ensure they have a `for` attribute corresponding to a valid input ID.
