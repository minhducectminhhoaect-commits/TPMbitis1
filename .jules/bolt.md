## 2026-01-04 - Hoisting Date Parsing in Loops
**Learning:** `new Date()` is surprisingly expensive when called thousands of times in a loop. Hoisting constant dates out of filters and caching parsed dates in loops yielded ~4x speedup.
**Action:** Always check for `new Date()` inside loops and hoist or cache if possible. Use `.getTime()` for comparisons.
