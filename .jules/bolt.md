## 2024-05-22 - Date Parsing in Loops
**Learning:** The application frequently parses ISO date strings using `new Date()` inside tight loops (filtering and aggregation). This is expensive (O(N*M)) when the reference dates (start/end filter) are invariant.
**Action:** Hoist `new Date()` for invariant values outside of loops. Cache parsed Date objects if they are reused within the same iteration (e.g., used for both Downtime and MTTR calculations).
