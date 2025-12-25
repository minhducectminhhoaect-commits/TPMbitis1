## 2024-05-22 - [Keyboard Accessible Tabs]
**Learning:** High-impact navigation elements (Tabs) implemented as `div`s with `onclick` are invisible to keyboard users. Adding `role="tab"`, `tabindex="0"`, and `onkeydown` handlers restores access without breaking the existing layout or requiring a full rewrite.
**Action:** Always check `onclick` elements for keyboard accessibility. If it clicks, it should focus and act on Enter/Space.
