import json
from playwright.sync_api import sync_playwright

def verify_visuals():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Mock user to bypass login
        mock_user = {
            "fullname": "Test Leader",
            "role": "leader"
        }

        # Inject user into localStorage before navigation
        page.add_init_script(f"""
            localStorage.setItem('tpm_user', '{json.dumps(mock_user)}');
        """)

        # Navigate
        page.goto("http://localhost:8000/index.html")
        page.wait_for_selector("#screen-leader")

        # 1. Take screenshot of Leader Screen showing form labels
        # Especially l-msts which we added a label for
        page.locator("#l-tab-1").screenshot(path=".jules/verification/leader_form_labels.png")
        print("Screenshot saved: leader_form_labels.png")

        # 2. Open a modal and take screenshot
        page.evaluate("document.getElementById('modal-history').classList.remove('hidden')")
        page.wait_for_selector("#modal-history")
        page.locator("#modal-history").screenshot(path=".jules/verification/modal_history.png")
        print("Screenshot saved: modal_history.png")

        browser.close()

if __name__ == "__main__":
    verify_visuals()
