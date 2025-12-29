## 2024-05-23 - Client-side Filtering Performance
**Learning:** In loops processing large datasets (e.g., dashboard filtering), creating new `Date` objects inside the loop is a massive bottleneck. Additionally, ordering checks from cheapest (string comparison) to most expensive (Date parsing) provides significant speedups.
**Action:** Always hoist invariant object creations out of loops and order conditional checks by cost.
