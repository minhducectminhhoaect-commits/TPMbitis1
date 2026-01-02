## 2024-05-23 - Date Parsing Performance
**Learning:** `new Date().toLocaleString()` with options creates a new `Intl.DateTimeFormat` instance every time, which is very expensive in loops.
**Action:** Reuse `Intl.DateTimeFormat` instances or use `Intl.DateTimeFormat().format()` directly when formatting dates in loops.

## 2024-05-23 - Hoisting Invariants in Loops
**Learning:** Creating new `Date` objects for static comparison values (like start/end range) inside a `filter` loop adds significant overhead (allocations + parsing) when iterating over large arrays.
**Action:** Always hoist invariant object creation (like date ranges) outside of `filter`, `map`, or `forEach` loops.
