## 2024-05-22 - Centralized Loading States
**Learning:** In a vanilla JS/HTML app without a framework, wrapping the central `post` function to handle UI state (disable button, show loading text) is cleaner than scattering logic across all call sites, but requires consistent `this` passing.
**Action:** Always check if `this` is passed in `onclick` handlers when refactoring for loading states.

## 2024-05-22 - Modal Accessibility
**Learning:** Hidden `div` modals are invisible to screen readers unless `role="dialog"` and `aria-modal="true"` are added. Close buttons must have text or `aria-label`.
**Action:** Check all `class="hidden"` components for semantic roles.
