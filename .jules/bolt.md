## 2024-05-22 - Date Creation in Loops
**Learning:** Repeatedly creating Date objects (and other objects) inside loops, especially filtering loops, significantly impacts performance (3x slower in benchmarks).
**Action:** Hoist loop invariants (like start/end date objects) outside the loop. Cache parsed Date objects if used multiple times in the same iteration.
