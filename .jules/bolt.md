## 2024-05-23 - Date Parsing in Loops
**Learning:** Parsing Dates (`new Date()`) inside a loop is surprisingly expensive, especially when the date string is constant (e.g., filter inputs).
**Action:** Always hoist invariant Date parsing out of loops. For `filter` or `map` operations involving date comparisons, parse the boundary dates once before the loop starts.
