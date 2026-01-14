## 2023-10-27 - Date Parsing Optimization
**Learning:** Hoisting `new Date()` parsing out of loops and caching parsed date objects inside loops reduced execution time by ~6x (from ~190ms to ~30ms for 10k items) in the dashboard calculation logic.
**Action:** Always check for repeated object instantiation (especially `Date`) inside hot loops and hoist/cache where possible.
