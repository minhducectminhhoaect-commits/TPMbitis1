# Bolt's Journal ⚡

## 2023-10-27 - Hoisting Invariant Date Parsing
**Learning:** `new Date()` creation inside array methods (like `filter`) is significantly expensive (O(N)).
**Action:** Always hoist invariant date parsing (e.g., filter boundaries) outside the loop.
