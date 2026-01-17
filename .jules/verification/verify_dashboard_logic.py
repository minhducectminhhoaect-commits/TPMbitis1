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

        # Mock localStorage for auto-login
        page.add_init_script("""
            localStorage.setItem('tpm_user', JSON.stringify({
                fullname: 'Test Leader',
                role: 'leader'
            }));
        """)

        # Track network requests
        requests = []
        def handle_route(route):
            # print(f"Intercepted request: {route.request.post_data}")
            requests.append(route.request.post_data)
            try:
                data = json.loads(route.request.post_data)
                if data.get('action') == 'get_dashboard':
                    route.fulfill(
                        status=200,
                        content_type="application/json",
                        body='{"data": [{"chuyen": "May 1", "gio_hu": "2023-10-27T10:00:00.000Z", "ten_bao_tri": "Thợ 1"}]}'
                    )
                else:
                    route.fulfill(status=200, content_type="application/json", body='{"data": [], "message": "ok"}')
            except:
                route.fulfill(status=200, content_type="application/json", body='{"data": [], "message": "error"}')

        page.route(f"**{API_URL_PART}", handle_route)

        print("Loading page...")
        page.goto(HTML_PATH)
        page.wait_for_selector("#screen-leader:not(.hidden)")

        # 1. Open Dashboard
        requests.clear()
        print("1. Opening Dashboard...")
        page.click("#screen-leader button[onclick='showDashboard(true)']")
        page.wait_for_timeout(1000)

        req_count = len([r for r in requests if 'get_dashboard' in r])
        print(f"   Requests: {req_count}")
        if req_count != 1:
            print("   FAIL: Expected 1 request.")
            return

        # 2. Filter Data
        requests.clear()
        print("2. Clicking Filter...")
        page.click("#screen-dashboard button[onclick='loadDashboardData()']")
        page.wait_for_timeout(1000)

        req_count = len([r for r in requests if 'get_dashboard' in r])
        print(f"   Requests: {req_count}")
        if req_count != 0:
            print("   FAIL: Expected 0 requests (Cached).")
            return

        # 3. Go Back
        print("3. Going Back...")
        page.click("button[onclick='goBack()']")
        page.wait_for_timeout(1000)

        # 4. Open Dashboard Again
        requests.clear()
        print("4. Opening Dashboard Again (Should refresh)...")
        page.click("#screen-leader button[onclick='showDashboard(true)']")
        page.wait_for_timeout(1000)

        req_count = len([r for r in requests if 'get_dashboard' in r])
        print(f"   Requests: {req_count}")
        if req_count != 1:
            print("   FAIL: Expected 1 request (Force Refresh).")
            return

        print("SUCCESS: Caching logic works as expected.")
        browser.close()

if __name__ == "__main__":
    run()
