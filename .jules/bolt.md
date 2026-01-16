# Bolt's Journal

## 2024-05-22 - Dashboard Date Parsing Optimization
**Learning:** Parsing `new Date()` inside a `filter` or `forEach` loop is expensive (O(N)), especially when comparing against constant start/end dates. Combining filtering and aggregation into a single pass avoids intermediate array allocation.
**Action:** Always hoist invariant object creation (like date boundaries) out of loops. Prefer single-pass iteration for simultaneous filtering and aggregation.
