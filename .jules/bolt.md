## 2024-05-24 - Hoisting Date Parsing in Filter Loops
**Learning:** In tight loops filtering thousands of items, repetitive `new Date()` calls (especially with string parsing) are a major bottleneck. Hoisting invariant date parsing (like start/end filter dates) outside the loop reduced execution time by ~3x (from ~16ms to ~5ms for 10k items).
**Action:** Always check loop invariants, especially object creation like `Date` or `RegExp`, and hoist them. Also cache parsed values if used multiple times within the loop body.
