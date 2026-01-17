# Palette's Journal

## 2024-05-22 - Async Button Feedback
**Learning:** Users lack immediate visual feedback when clicking "Submit" on form modals (like 'Gửi Báo Cáo'). This leads to confusion on whether the action was registered, especially with potential network latency.
**Action:** Implement a generic "loading" state in the global `post` utility that disables the triggering button and changes its text (e.g., "Đang xử lý...") to provide immediate feedback and prevent double-submissions.
