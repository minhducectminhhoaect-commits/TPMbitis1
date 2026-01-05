## 2024-05-20 - [Date Parsing Optimization]
**Learning:** Reusing `Intl.DateTimeFormat` is significantly faster (100x) than calling `toLocaleString` repeatedly. Hoisting date parsing out of loops (2x speedup) is a simple but effective win for large datasets.
**Action:** Always look for `new Date()` or `toLocaleString()` inside loops and try to hoist or cache them.
