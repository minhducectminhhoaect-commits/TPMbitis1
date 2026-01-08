# Bolt's Journal

This journal tracks critical performance learnings.

## Format
## YYYY-MM-DD - [Title]
**Learning:** [Insight]
**Action:** [How to apply next time]

## 2024-05-23 - Date Parsing in Loops
**Learning:** Creating `new Date()` objects inside a loop (especially filter+map chains) is significantly expensive.
**Action:** Hoist invariant Date parsing outside loops. Combine filter and aggregation into a single pass to avoid iterating twice.
