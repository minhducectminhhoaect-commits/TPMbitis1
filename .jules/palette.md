## 2024-05-24 - Accessibility Patterns in Single File Apps
**Learning:** In a single-file application with inline styles and scripts, accessibility attributes often get overlooked because semantic structure is traded for compactness.
**Action:** When adding accessibility, prioritize `role="dialog"` and `aria-label` for interactive elements that lack text content, as these are the highest impact fixes for screen readers in such constrained environments.
