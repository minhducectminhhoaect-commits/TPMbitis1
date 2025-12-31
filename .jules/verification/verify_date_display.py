from playwright.sync_api import sync_playwright
import json
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Inject login
        page.add_init_script("""
            localStorage.setItem('tpm_user', JSON.stringify({
                fullname: 'Leader Test',
                role: 'leader'
            }));
        """)

        # Mock API
        def handle_route(route):
            req = route.request
            post_data = req.post_data
            if req.method == 'POST' and post_data and 'get_history' in post_data:
                # Mock history data
                mock_data = {
                    "data": [
                        {
                            "id": "1",
                            "status": "Done",
                            "chuyen": "May 1",
                            "ma_so": "M001",
                            "gio_hu": "2023-10-27T10:00:00",
                            "gio_den": "2023-10-27T10:15:00",
                            "gio_xong": "2023-10-27T10:30:00",
                            "gio_chay_lai": "2023-10-27T10:35:00",
                            "nguoi_tao": "Test User",
                            "ten_bao_tri": "Tech 1"
                        }
                    ]
                }
                route.fulfill(status=200, body=json.dumps(mock_data))
            else:
                try:
                    route.continue_()
                except:
                    pass

        page.route('**/*', handle_route)

        page.goto('http://localhost:8080/index.html')

        # Click History tab (Tab 4)
        # We need to make sure the element is visible. Tab 4 is "Lịch Sử"
        page.click('text=4. Lịch Sử')

        # Wait for the list to populate
        page.wait_for_selector('.ticket-item')

        content = page.text_content('#l-history-list')
        print(f"Content found: {content}")

        # Screenshot
        page.screenshot(path='.jules/verification/history_tab.png')

        browser.close()

if __name__ == "__main__":
    run()
