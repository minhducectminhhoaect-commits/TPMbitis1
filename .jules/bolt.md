## 2025-12-26 - [Loop Invariant Code Motion in Filtering]
**Learning:** Parsing `new Date()` inside a loop (especially for constant comparison values) is extremely expensive in JS. Lifting these out yielded a ~46% speedup.
**Action:** Always check loop bodies for object instantiations that depend only on external variables.
