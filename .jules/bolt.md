## 2024-05-22 - Hoisting Date Object Creation
**Learning:** In loops filtering by date range, `new Date()` creation from input strings inside the loop is a significant bottleneck. Hoisting the boundary dates outside the loop reduced filtering time by ~50% in benchmarks.
**Action:** Always check loop invariants, especially object creation like `new Date()` or regex compilation, and move them out.
