## 2026-01-18 - Split Fetch and Render for Client-Side Filtering
**Learning:** In this single-file app, `loadDashboardData` coupled data fetching with local filtering, causing redundant network requests on every filter change.
**Action:** Always separate `fetchData` (updates cache) from `renderData` (filters and draws). This allows instant client-side filtering using cached data.
