## 2024-05-23 - [Date Parsing Hoisting]
**Learning:** Parsing dates inside a loop (especially `new Date(string)`) is surprisingly expensive. Hoisting invariant date parsing out of the filter callback yielded a ~35% speedup.
**Action:** Always check for `new Date()` calls inside `filter`, `map`, or `forEach` loops and hoist them if the input doesn't change.
