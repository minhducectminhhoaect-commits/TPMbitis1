## 2024-05-22 - [Loop Invariant Hoisting in Dashboard Filter]
**Learning:** Parsing dates (`new Date()`) inside a filter loop for every item significantly degrades performance (found ~3.9x slowdown).
**Action:** Always hoist loop-invariant Date object creation (and other expensive initializations) outside of `filter`, `map`, or `forEach` loops. Use local variables to store the pre-calculated values.
