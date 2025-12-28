## 2024-05-22 - [Accessibility] Legacy Div-Button Pattern
**Learning:** The application heavily relies on `div` elements with `onclick` handlers for interactive elements (tabs, lists) instead of semantic `<button>` or `<a>` tags. This completely breaks keyboard navigation.
**Action:** Instead of rewriting all HTML to semantic tags (which might break CSS layouts relying on specific structures), apply `role="button/tab"`, `tabindex="0"`, and `onkeydown` handlers to retrofit accessibility while preserving visual layout.

## 2024-05-22 - [Accessibility] Implicit Labels
**Learning:** Many inputs rely solely on `placeholder` text or adjacent text nodes without explicit `<label for="...">` associations.
**Action:** Systematically wrap text in `<label class="input-label" for="...">` to ensure screen reader support and hit-area usability.
