## 2024-05-23 - Date Parsing in Loops
**Learning:** Parsing dates with `new Date()` is expensive. In filtering loops, hoisting invariant date parsing (like start/end range dates) outside the loop reduced execution time by ~44% (from 4.2s to 2.3s for 10k items x 100 runs).
**Action:** Always hoist invariant `Date` object creation out of loops. Cache parsed dates if used multiple times in the same iteration.
