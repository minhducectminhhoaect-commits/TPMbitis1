## 2024-03-24 - [Automatic Loading State for Async Buttons]
**Learning:** Users lack feedback when submitting forms in SPA (Single Page Applications) without framework-level loading states. Implementing a pattern where the global `post`/fetch wrapper accepts the button element allows for automatic, consistent "Loading..." states and disabling of buttons across the app without repetitive logic in every handler.
**Action:** When working on "Vanilla JS" apps, always check if the central API utility can handle UI feedback states to reduce boilerplate and improve consistency.
