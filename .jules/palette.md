## 2024-05-23 - Missing Labels in Legacy Forms
**Learning:** Found that legacy forms (e.g., "Báo Hư") relied solely on placeholders or unassociated text for labels. This fails accessibility checks and makes screen readers unusable.
**Action:** Always verify forms have explicit `<label for="id">` elements, even if "it looks okay" visually. Use the `.input-label` class for consistency.
