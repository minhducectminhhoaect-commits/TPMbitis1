# Bolt's Journal ⚡

## 2024-05-23 - Date Parsing Overhead
**Learning:** Parsing date strings (`new Date()`) inside loops is significantly expensive. Hoisting invariant dates and caching parsed dates for reuse in the same iteration can yield >20% performance gains.
**Action:** Always check loops for redundant `new Date()` calls, especially when comparing against static range boundaries or using the same date field multiple times.
