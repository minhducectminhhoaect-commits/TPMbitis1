## 2026-01-07 - Date Parsing Bottleneck
**Learning:** `new Date()` inside loops is a major bottleneck (O(N) or O(N^2)). Especially when parsing string dates repeatedly for filtering and aggregation.
**Action:** Always hoist Date parsing for invariant boundaries outside loops. Cache parsed timestamps (using `getTime()`) inside loops if the same field is accessed multiple times. Use `getTime()` for arithmetic instead of Date object subtraction when possible.
