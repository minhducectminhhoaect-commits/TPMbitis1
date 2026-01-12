## 2024-05-22 - Hoisting Date Creation in Filters
**Learning:** Parsing dates inside a loop is expensive. Hoisting invariant date parsing (start/end filters) outside the `filter` loop reduced execution time by ~11x (110ms -> 10ms for 10k items) in Node.js benchmarks.
**Action:** Always hoist invariant calculations, especially `new Date()`, out of loops in client-side filtering logic.
