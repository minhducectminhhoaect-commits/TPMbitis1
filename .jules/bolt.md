## 2024-05-23 - Loop Invariant Code Motion in Data Filtering
**Learning:** Hoisting repetitive `Date` object creation and manipulation out of large data filtering loops significantly improves performance. In the `loadDashboardData` function, creating `start` and `end` date objects inside the loop for every record caused a ~50% performance penalty.
**Action:** Always inspect array methods (`filter`, `map`, `reduce`) used on large datasets for invariant calculations or object instantiations that can be moved to the outer scope.
