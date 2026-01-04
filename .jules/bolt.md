## 2026-01-04 - [Invariant Date Object Hoisting]
**Learning:** `new Date()` creation inside high-frequency loops (like `filter`) significantly degrades performance. In this app, filtering dashboard data created 2 new Date objects per item per iteration, causing a 3.25x slowdown.
**Action:** Always hoist invariant Date creations outside of loops. Pre-calculate timestamps (numeric) if possible for even faster comparison.
