## 2026-01-16 - [Minified HTML & Accessibility]
**Learning:** Retrofitting accessibility (ARIA labels, semantic tags) into heavily minified or single-line HTML structures is error-prone and requires large, risky diffs or fragile regex replacements.
**Action:** When creating new components, break long lines logically. For legacy maintenance, prioritize converting target sections to multi-line format before applying attributes to ensure targeted, safe patches.
