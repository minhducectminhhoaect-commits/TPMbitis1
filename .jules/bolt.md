## 2024-05-22 - Dashboard Date Logic Optimization
**Learning:** Hoisting invariant `Date` object creation out of the `filter` loop and caching `getTime()` results significantly improved performance (from ~60ms to ~19ms for 10k items, ~3x gain).
**Action:** When filtering or aggregating large datasets, always hoist constants (like date ranges) and cache parsed values (timestamps) to avoid repeated `new Date()` overhead.
