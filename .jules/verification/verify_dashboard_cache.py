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
            print(f"Intercepted request: {route.request.post_data}")
            requests.append(route.request.post_data)
            # Return dummy dashboard data
            # Check action
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

        # Wait for Leader screen to appear (auto-login)
        # Note: auto-login calls 'leader_get_open'
        page.wait_for_selector("#screen-leader:not(.hidden)")
        print("Leader screen loaded.")

        # Clear request log (ignore init requests)
        requests.clear()

        # Click 'Xem Dashboard Chi Tiết'
        print("Opening Dashboard...")
        page.click("#screen-leader button[onclick='showDashboard(true)']")

        # Wait for dashboard data request
        page.wait_for_timeout(2000)

        initial_req_count = len([r for r in requests if 'get_dashboard' in r])
        print(f"Requests (get_dashboard) after opening dashboard: {initial_req_count}")

        # Click 'Lọc Dữ Liệu'
        print("Clicking Filter button...")
        # Since button onclick is "loadDashboardData()", we click it.
        # It's inside #screen-dashboard .filter-group
        page.click("#screen-dashboard button[onclick='loadDashboardData()']")
        page.wait_for_timeout(2000)

        second_req_count = len([r for r in requests if 'get_dashboard' in r])
        print(f"Requests (get_dashboard) after clicking Filter: {second_req_count}")

        if second_req_count > initial_req_count:
            print("PERFORMANCE ISSUE: Filter button triggered a new network request.")
        else:
            print("OPTIMIZED: Filter button did NOT trigger a new network request.")

        browser.close()

if __name__ == "__main__":
    run()
