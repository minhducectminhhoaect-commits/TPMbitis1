## 2024-05-22 - Hoisting Date Parsing
**Learning:** In loops processing date strings, repeatedly calling `new Date()` on invariant comparison dates creates significant O(N) overhead.
**Action:** Hoist invariant `Date` object creation outside loops. Benchmark showed ~33% improvement.
