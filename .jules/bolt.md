## 2024-05-23 - Date Formatting Performance
**Learning:** `toLocaleString` with locale arguments (e.g. `vi-VN`) is extremely expensive (50x slower) compared to reusing an `Intl.DateTimeFormat` instance.
**Action:** Always hoist `Intl.DateTimeFormat` instances to the top scope and reuse them in loops, rather than calling `toLocaleString` repeatedly.
