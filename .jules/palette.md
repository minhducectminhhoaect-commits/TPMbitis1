## 2024-05-22 - Standardized Async Loading States
**Learning:** Centralizing loading state logic (disable button + change text) in the global `post` wrapper ensures consistent feedback across all forms without repetitive boilerplate code in every handler.
**Action:** When adding new forms or actions, simply pass the submit button reference (`this`) to the handler and forward it to `post()`. No manual DOM manipulation needed.
