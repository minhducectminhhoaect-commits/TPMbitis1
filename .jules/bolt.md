## 2024-05-22 - Hoisting Date Object Creation
**Learning:** Creating `new Date()` objects inside a `filter` or `forEach` loop is a significant performance bottleneck, especially when parsing strings.
**Action:** Hoist invariant Date objects (like start/end range filters) outside the loop. This can improve filtering performance by ~4x for large datasets.
