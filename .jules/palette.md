## 2024-05-23 - [Minimizing Diffs in Legacy HTML]
**Learning:** Using `BeautifulSoup` to modify `index.html` causes massive diffs because it normalizes whitespace and attributes, making reviews impossible.
**Action:** Use targeted Python string replacement for specific attribute injection in legacy files to preserve formatting and keep diffs minimal.
