## 2024-05-24 - Orphaned Labels
**Learning:** Many form inputs were relying on placeholders or unassociated text, making them inaccessible to screen readers and harder to click.
**Action:** Use Python scripts (BeautifulSoup) to audit and fix `index.html` by ensuring every `<input>` has a corresponding `<label>` with a `for` attribute, using the `.input-label` class for consistency.
