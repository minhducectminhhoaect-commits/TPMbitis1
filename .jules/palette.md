## 2024-05-23 - [Form Accessibility in SPA]
**Learning:** In a legacy SPA where forms are just `div`s with `onclick` handlers, adding `required` attributes to inputs is not enough for validation. The browser's native constraint validation doesn't trigger automatically on button click.
**Action:** When adding `required` attributes for accessibility/visual cues, always ensure the corresponding JavaScript handler explicitly checks these fields (e.g. `if (!val) ...`) to enforce the constraint. Also, use `input-label` class for consistent styling.
