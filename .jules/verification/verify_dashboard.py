
from playwright.sync_api import sync_playwright

def verify_dashboard(page):
    page.goto("http://localhost:3000/index.html")

    # Mock user login
    page.evaluate("""
        localStorage.setItem('tpm_user', JSON.stringify({
            fullname: 'Test User',
            role: 'leader',
            username: 'test'
        }));
    """)

    page.reload()

    # Intercept dashboard data request
    page.route("**/exec", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body='{"data": [{"gio_hu": "2023-10-27T10:00:00", "chuyen": "May 1", "ma_so": "M1-01"}, {"gio_hu": "2023-10-27T11:00:00", "chuyen": "May 2", "ma_so": "M2-01"}]}'
    ))

    # Navigate to dashboard
    page.evaluate("showDashboard(true)")

    # Wait for dashboard to load
    page.wait_for_selector("#screen-dashboard:not(.hidden)")

    # Set dates
    page.fill("#d-start", "2023-10-27")
    page.fill("#d-end", "2023-10-27")

    # Trigger filtering
    page.click("button:has-text('Lọc Dữ Liệu')")

    # Wait for processing
    page.wait_for_timeout(500)

    # Take screenshot
    page.screenshot(path=".jules/verification/dashboard_verified.png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    verify_dashboard(page)
    browser.close()
