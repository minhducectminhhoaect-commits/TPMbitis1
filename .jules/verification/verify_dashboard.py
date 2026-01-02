
from playwright.sync_api import sync_playwright, expect
import json

def verify_dashboard(page):
    # Mock the API response for the dashboard
    def handle_route(route):
        request = route.request
        # Check if post_data is not None before accessing it
        if request.post_data and "action" in request.post_data:
            try:
                data = json.loads(request.post_data)
                if data["action"] == "get_dashboard":
                    route.fulfill(
                        status=200,
                        content_type="application/json",
                        body=json.dumps({
                            "data": [
                                {"gio_hu": "2023-10-27T08:00:00", "gio_chay_lai": "2023-10-27T10:00:00", "chuyen": "May 1", "ten_bao_tri": "Tech A", "gio_xong": "2023-10-27T09:30:00"},
                                {"gio_hu": "2023-10-27T11:00:00", "gio_chay_lai": "2023-10-27T12:00:00", "chuyen": "May 2", "ten_bao_tri": "Tech B", "gio_xong": "2023-10-27T11:45:00"},
                                {"gio_hu": "2023-10-27T14:00:00", "gio_chay_lai": "2023-10-27T14:30:00", "chuyen": "May 1", "ten_bao_tri": "Tech A", "gio_xong": "2023-10-27T14:15:00"}
                            ]
                        })
                    )
                elif data["action"] == "login":
                    route.fulfill(
                        status=200,
                        content_type="application/json",
                        body=json.dumps({
                            "fullname": "Test User",
                            "role": "leader"
                        })
                    )
                else:
                    route.continue_()
            except json.JSONDecodeError:
                route.continue_()
        else:
            route.continue_()

    # Intercept network requests
    page.route("**/*", handle_route)

    # 1. Load the app
    page.goto("http://localhost:8000/index.html")

    # 2. Login
    page.fill("#log-user", "admin")
    page.fill("#log-pass", "123")
    page.click("button:text('Đăng Nhập')")

    # 3. Wait for leader screen
    page.wait_for_selector("#screen-leader:not(.hidden)")

    # 4. Go to Dashboard
    page.click("button:text('Xem Dashboard Chi Tiết')")
    page.wait_for_selector("#screen-dashboard:not(.hidden)")

    # 5. Set Filters and Click "Lọc Dữ Liệu" (Filter Data)
    # Using 2023-10-27 which matches mock data
    page.fill("#d-start", "2023-10-01")
    page.fill("#d-end", "2023-11-01")
    page.click("button:text('Lọc Dữ Liệu')")

    # 6. Verify KPI numbers update (Mock data has 3 records)
    # If the filter logic (optimized) works, it should show 3 records.
    # If it was broken by optimization, it might show 0 or throw error.
    expect(page.locator("#kpi-total")).to_have_text("3")

    # 7. Take screenshot
    page.screenshot(path=".jules/verification/dashboard_verified.png")
    print("Verification successful, screenshot saved.")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_dashboard(page)
        finally:
            browser.close()
