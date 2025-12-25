## 2024-05-24 - [Client-side Large Dataset Filtering]
**Learning:** The application downloads the entire dataset and filters it on the client side. This causes performance degradation as the dataset grows, specifically due to heavy operations like `Date` parsing inside the filter loop.
**Action:** When working on `loadDashboardData` or similar functions, ensure expensive operations (date parsing, map lookups) are lifted out of loops. For long-term scalability, recommend moving filtering logic to the backend.
