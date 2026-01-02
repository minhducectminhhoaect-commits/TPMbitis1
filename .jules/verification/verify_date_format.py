
from playwright.sync_api import sync_playwright

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Mock user login to bypass login screen
        page.goto('http://localhost:8000')
        page.evaluate("""
            localStorage.setItem('tpm_user', JSON.stringify({
                fullname: 'Test Leader',
                role: 'leader',
                id: '123'
            }));
        """)

        # Reload to apply login
        page.goto('http://localhost:8000')

        # Mock the API response for 'get_history' which uses formatDate
        page.route('**/exec', lambda route: handle_route(route))

        # Open history tab (Tab 4)
        page.click('text=4. Lịch Sử')

        # Wait for the history list to load
        page.wait_for_selector('.ticket-item')

        # Take screenshot
        page.screenshot(path='.jules/verification/history_date_format.png')
        print("Screenshot taken at .jules/verification/history_date_format.png")

        browser.close()

def handle_route(route):
    # Parse request to check action
    post_data = route.request.post_data_json
    if post_data and post_data.get('action') == 'get_history':
        route.fulfill(
            status=200,
            content_type='application/json',
            body='{"data": [{"id": "t1", "chuyen": "May 1", "ma_so": "M1-001", "gio_hu": "2023-10-27T10:05:00.000Z", "status": "Done", "gio_xong": "2023-10-27T11:00:00.000Z"}]}'
        )
    else:
        # Default empty response for other calls
        route.fulfill(status=200, body='{"data": []}')

if __name__ == "__main__":
    verify_frontend()
