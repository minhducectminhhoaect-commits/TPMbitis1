## 2024-05-22 - Accessibility in Modal Dialogs
**Learning:** Adding `role="dialog"` and `aria-modal="true"` to simple `div` overlays significantly improves screen reader behavior, but requires explicit `aria-labelledby` referencing a title element to contextually describe the modal.
**Action:** Always pair `role="dialog"` with an `aria-labelledby` pointing to the modal's heading element (adding an ID to the heading if missing).

## 2024-05-22 - Label Association in Legacy Forms
**Learning:** Implicit visual labeling (text next to input) is insufficient for screen readers. Explicit `<label for="id">` is the gold standard, but `aria-label` is a valid fallback for compact UIs or when refactoring HTML structure is risky.
**Action:** Prioritize `for` attributes when a visible label exists; use `aria-label` for inputs with no visible label or placeholder-only labels.
