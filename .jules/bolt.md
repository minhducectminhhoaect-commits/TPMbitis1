## 2026-01-02 - Hoisting Date Creation and Caching Formatters
**Learning:** `new Date().toLocaleString()` is extremely expensive in loops (up to 40x slower than `Intl.DateTimeFormat`). Similarly, repeatedly creating `new Date(string)` inside a `filter` loop for invariant comparison values kills performance.
**Action:** Always hoist `new Date()` creation for loop invariants. Use a global/cached `Intl.DateTimeFormat` instance for date formatting in lists.
