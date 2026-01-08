## 2024-05-23 - [JavaScript Date Performance]
**Learning:** Instantiating `new Date()` inside tight loops (like filtering or aggregation over thousands of items) is surprisingly expensive in JavaScript.
**Action:** Always hoist Date creation for loop invariants (like start/end filters) and cache parsed Date objects (or better yet, their numeric timestamps) if they are accessed multiple times within the loop. In this case, hoisting and caching reduced execution time by ~75% (from ~100ms to ~25ms for 10k items).
