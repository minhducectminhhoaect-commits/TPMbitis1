## 2026-01-07 - [Loading States for Async Actions]
**Learning:** Refactoring a central helper (like `post`) to handle UI state (loading/disabled) is cleaner and more reliable than repeating logic in every handler. However, it requires careful cleanup of existing manual handling to avoid conflicts.
**Action:** When implementing cross-cutting UX concerns like loading states, look for central utility functions to augment first. Ensure `finally` blocks are used to restore state reliably even on errors.
