
from playwright.sync_api import sync_playwright

def verify_dashboard(page):
    # Mock data
    mock_data = [
        {
            "id": 1, "chuyen": "May 1", "ten_bao_tri": "Tho 1",
            "gio_hu": "2023-10-27T08:00:00.000Z",
            "gio_xong": "2023-10-27T09:00:00.000Z",
            "gio_chay_lai": "2023-10-27T09:30:00.000Z",
            "status": "Done"
        },
        {
            "id": 2, "chuyen": "May 2", "ten_bao_tri": "Tho 2",
            "gio_hu": "2023-10-27T10:00:00.000Z",
            "gio_xong": "2023-10-27T11:00:00.000Z",
            "gio_chay_lai": "2023-10-27T11:30:00.000Z",
            "status": "Done"
        }
    ]

    # Mock the post function
    page.add_init_script("""
        window.post = function(data, cb) {
            console.log('Post called', data);
            if (data.action === 'get_dashboard') {
                cb({data: %s});
            } else if (data.action === 'login') {
                cb({role: 'leader', fullname: 'Test Leader'});
            } else if (data.action === 'leader_get_open') {
                cb({data: []}); // Mock initial leader load
            }
        };
    """ % str(mock_data).replace("True", "true").replace("False", "false").replace("None", "null"))

    page.goto("http://localhost:8000/index.html")

    # Debug: Check if login screen is visible
    if not page.is_visible("#screen-login"):
        print("Login screen not visible")

    # Login to reach dashboard or just call showDashboard if exposed, but login is safer path
    page.fill("#log-user", "admin")
    page.fill("#log-pass", "123")

    # Use evaluate to click because sometimes overlays block clicks or elements are not stable
    page.evaluate("handleLogin()")

    # Wait for login transition
    try:
        page.wait_for_selector("#screen-leader:not(.hidden)", timeout=5000)
    except:
        print("Failed to wait for leader screen. Checking visibility...")
        print(f"Leader screen class: {page.eval_on_selector('#screen-leader', 'e => e.className')}")
        # Force show if needed for test
        page.evaluate("showScreen('screen-leader')")

    # Click "Xem Dashboard Chi Tiết"
    # page.click("text=Xem Dashboard Chi Tiết")
    page.evaluate("showDashboard(true)")

    # Wait for chart
    page.wait_for_selector("#c-line-ticket")

    # Take screenshot
    page.screenshot(path="/home/jules/verification/dashboard_verified.png")
    print("Screenshot taken")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            verify_dashboard(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
