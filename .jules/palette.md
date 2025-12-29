## 2024-05-22 - Form Accessibility & Labeling
**Learning:** Legacy forms often rely on visual proximity or placeholders rather than explicit `for` attributes, which fails accessibility checks and screen readers. Overwriting large blocks is sometimes necessary to fix this in single-file apps with long lines.
**Action:** Always check for `label` association when seeing inputs. If modifying legacy code, ensure `.input-label` or similar utility classes are consistently applied for both visual and semantic correctness.
