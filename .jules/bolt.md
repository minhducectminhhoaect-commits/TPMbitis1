## 2024-10-27 - Client-Side Filtering vs Server Fetching
**Learning:** The dashboard fetched the entire dataset from the server every time the "Filter" button was clicked, even though filtering logic is entirely client-side. This caused unnecessary network latency and server load.
**Action:** When implementing filters on client-side data, always ensure the data fetching is decoupled from the filtering action. Use a cache (variable) to store the raw data and only re-fetch when explicitly requested or necessary.
