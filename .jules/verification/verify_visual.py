import os
import json
from playwright.sync_api import sync_playwright

CWD = os.getcwd()
HTML_PATH = f"file://{CWD}/index.html"
API_URL_PART = "/exec"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Mock localStorage
        page.add_init_script("""
            localStorage.setItem('tpm_user', JSON.stringify({
                fullname: 'Visual Test Leader',
                role: 'leader'
            }));
        """)

        # Mock API
        def handle_route(route):
            try:
                data = json.loads(route.request.post_data)
                if data.get('action') == 'get_dashboard':
                    # Return sample data
                    body_data = {
                        "data": [
                            {"chuyen": "May 1", "gio_hu": "2023-10-27T08:00:00.000Z", "gio_chay_lai": "2023-10-27T09:00:00.000Z", "gio_xong": "2023-10-27T08:30:00.000Z", "ten_bao_tri": "Thợ A"},
                            {"chuyen": "May 2", "gio_hu": "2023-10-27T10:00:00.000Z", "ten_bao_tri": "Thợ B"}
                        ]
                    }
                    route.fulfill(status=200, content_type="application/json", body=json.dumps(body_data))
                else:
                    route.fulfill(status=200, content_type="application/json", body='{"data": [], "message": "ok"}')
            except:
                route.fulfill(status=200, content_type="application/json", body='{"data": [], "message": "error"}')

        page.route(f"**{API_URL_PART}", handle_route)

        page.goto(HTML_PATH)
        page.wait_for_selector("#screen-leader:not(.hidden)")

        # Open Dashboard
        page.click("#screen-leader button[onclick='showDashboard(true)']")

        # Wait for data to render (charts or KPIs)
        page.wait_for_timeout(2000)

        # Screenshot
        screenshot_path = ".jules/verification/dashboard_visual.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
