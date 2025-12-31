## 2024-05-23 - [Form Accessibility Pattern]
**Learning:** Inputs relying solely on `placeholder` attributes create significant accessibility barriers and usability issues (context loss when typing).
**Action:** Always wrap form inputs with explicit `<label>` elements using `for` attributes and `.input-label` class, and use `required` attribute for native validation.
