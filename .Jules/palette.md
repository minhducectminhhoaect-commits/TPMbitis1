# Palette's Journal - Critical UX/A11y Learnings

## 2024-05-23 - Login Accessibility & Feedback
**Learning:** Single-page apps with custom inline scripts often lack standard form behaviors (like button disabling on submit) which confuses users and allows double-submission errors.
**Action:** Always wrap async actions with disable/enable states on the trigger button, and provide explicit "Processing" text.

**Learning:** Minimalist "Card" designs often skip labels in favor of placeholders, hurting accessibility.
**Action:** Reintroduce labels with `input-label` styling that complements the clean design rather than cluttering it.
