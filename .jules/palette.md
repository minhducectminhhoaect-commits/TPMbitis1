## 2024-05-23 - Accessibility First Steps
**Learning:** This legacy codebase uses `onclick` on `div` elements for interactive controls (tabs) and modal dialogs without any ARIA attributes or keyboard support. This makes the application completely inaccessible to keyboard and screen reader users.
**Action:** When refactoring legacy "div-soup" applications, prioritize converting interactive divs to semantic buttons or adding full ARIA roles (`role="button"`, `role="tab"`) and keyboard event handlers (`keydown`). For modals, ensure focus management and Escape key support are added globally.
