## 2025-12-30 - Date Object Hoisting in Filter Loops
**Learning:** Creating `new Date()` inside a `filter` or `forEach` loop for invariant comparison values (like start/end range) is a significant performance killer, causing O(N) object allocations instead of O(1).
**Action:** Always hoist invariant Date creation outside the loop. For variant dates (like row data), parse once and reuse within the loop scope if accessed multiple times.
