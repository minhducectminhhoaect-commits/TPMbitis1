## 2026-01-01 - [Labeling Inputs]
**Learning:** Implicit labeling (via layout or placeholder) fails accessibility checks and is fragile. Explicit `<label for="...">` is required for screen readers and click-to-focus behavior.
**Action:** Always verify form inputs have a corresponding `<label>` with a matching `for` attribute, even if the visual layout implies a connection.
