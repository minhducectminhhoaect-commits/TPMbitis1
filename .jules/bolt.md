## 2024-05-22 - Date Parsing in Loops
**Learning:** `new Date()` is expensive. Hoisting parsing out of `filter` and caching it in `forEach` yielded a 2x speedup in dashboard data processing.
**Action:** Always look for Date parsing inside loops as a primary optimization target in data-heavy client-side logic.
