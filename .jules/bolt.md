## 2026-01-14 - Date Parsing in Loops
**Learning:** Instantiating `new Date()` inside a large loop (e.g., 10k items) for filtering logic is a significant performance bottleneck (100ms+ overhead).
**Action:** Always hoist constant date parsing (filters) outside the loop. For row data, parse once and store in a variable if reused for multiple calculations.
