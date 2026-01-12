## 2026-01-12 - Reusable Loading State Pattern
**Learning:** The app uses a global `post` helper for interactions but previously lacked consistent loading states, which could lead to double-submissions and user uncertainty.
**Action:** Enhanced `post` to accept a button reference `this` from call sites. The helper now automatically disables the button and updates text to "Đang xử lý..." during the transaction. Future implementations should follow this `onclick="handler(this)"` -> `post(..., btn)` pattern.
