## 2024-05-23 - Date Parsing Bottleneck
**Learning:** In loops processing 100k+ items (like dashboard filters), repeatedly creating invariant Date objects (e.g., `new Date(filterInput)`) is a massive bottleneck. Hoisting them out reduces time by ~40%.
**Action:** Always check loop invariants in filter/map functions and hoist them. Also reuse parsed date objects if used multiple times in the same loop iteration.
