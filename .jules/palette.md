# Palette's Journal

## 2024-05-22 - [Starting]
**Learning:** Initial setup.
**Action:** none

## 2024-05-22 - [Centralized Loading States]
**Learning:** This app uses a central `post` wrapper for API calls. This allowed me to implement "Loading..." states for *all* buttons by modifying just one function, instead of touching every click handler individually (mostly).
**Action:** Always check for central utility functions before implementing repetitive UI logic.

## 2024-05-22 - [Modal Accessibility]
**Learning:** Legacy apps often implement modals as simple hidden `div`s. Adding `role="dialog"`, `aria-modal="true"`, and linking `aria-labelledby` to the modal title is a low-effort, high-impact a11y win.
**Action:** Standardize modal markup in future designs to include these by default.
