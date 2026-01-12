
import os
from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Load the local index.html
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Mock the API
        page.route("**/exec", lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"status":"success", "message":"Done", "data":[]}'
        ))

        # We need to simulate being logged in as Leader to access Leader Create
        page.evaluate("""() => {
            localStorage.setItem('tpm_user', JSON.stringify({fullname: 'Test Leader', role: 'leader'}));
            checkAutoLogin();
        }""")

        # Wait for Leader screen
        page.wait_for_selector("#screen-leader:not(.hidden)")

        # Fill required fields
        page.select_option("#l-chuyen", "May 1")
        page.fill("#l-msts", "M-001")

        # CSS selector (without playwright extensions like :has-text which are not valid in document.querySelector)
        # We know it's the only button in that tab div for now, or the last one.
        # Structure: <div id="l-tab-1" ...> ... <button ...>Gửi Báo Cáo</button> </div>
        # It is the last child button.

        js_selector = "#l-tab-1 button:last-of-type"

        # Verify initial state
        is_disabled_initial = page.evaluate(f"document.querySelector('{js_selector}').disabled")
        print(f"Initial disabled state: {is_disabled_initial}")

        # Trigger click via evaluate to ensure we can check state immediately without waiting for nav/fetch
        page.evaluate(f"document.querySelector('{js_selector}').click()")

        # Check state immediately
        is_disabled_after = page.evaluate(f"document.querySelector('{js_selector}').disabled")
        btn_text = page.evaluate(f"document.querySelector('{js_selector}').innerText")

        print(f"Disabled state after click: {is_disabled_after}")
        print(f"Button text after click: {btn_text}")

        if is_disabled_after and btn_text == "Đang xử lý...":
            print("SUCCESS: Button is disabled and text changed.")
        else:
            print("FAILURE: Button state did not update correctly.")

        browser.close()

if __name__ == "__main__":
    run()
