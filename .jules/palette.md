## 2024-05-23 - Retrofitting Accessibility in Legacy Minified Code
**Learning:** When adding accessibility to a legacy, semi-minified HTML file (mixed HTML/CSS/JS in one file), full parsing/rewriting (like `BeautifulSoup`) can cause massive diffs due to attribute reordering and whitespace normalization, making code reviews impossible.
**Action:** Use targeted regex or strict string replacement scripts (like Python `replace` or `re.sub`) to surgically inject `aria-*` attributes and `<label>` tags without disturbing the surrounding structure or whitespace.
