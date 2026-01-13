## 2024-05-23 - Date Parsing Overhead
**Learning:** `new Date()` creation in tight loops is a significant performance bottleneck (over 60% of loop time). Hoisting invariant dates and caching repeated parses improved dashboard calculation speed by 3x.
**Action:** Always hoist invariant Date parsing out of loops. If a Date field is accessed multiple times, parse it once and store the timestamp or object.
