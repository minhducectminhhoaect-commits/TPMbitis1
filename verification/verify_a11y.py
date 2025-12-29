from playwright.sync_api import sync_playwright

def verify_accessibility_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the app
        page.goto("http://localhost:8080/index.html")

        # Bypass login by injecting user into localStorage
        page.evaluate("""
            localStorage.setItem('tpm_user', JSON.stringify({
                fullname: 'Test Leader',
                role: 'leader'
            }));
            location.reload();
        """)

        # Wait for Leader screen to load
        page.wait_for_selector("#screen-leader:not(.hidden)")

        # Take a screenshot of the Leader screen (Create Ticket tab)
        page.screenshot(path="verification/leader_screen.png")
        print("Screenshot saved to verification/leader_screen.png")

        # Verify labels exist and are associated correctly
        # 1. Check 'l-chuyen'
        label_chuyen = page.locator("label[for='l-chuyen']")
        if label_chuyen.count() > 0:
            print("PASS: Label for 'l-chuyen' found.")
        else:
            print("FAIL: Label for 'l-chuyen' NOT found.")

        # 2. Check 'l-msts'
        label_msts = page.locator("label[for='l-msts']")
        if label_msts.count() > 0:
            print("PASS: Label for 'l-msts' found.")
        else:
            print("FAIL: Label for 'l-msts' NOT found.")

        # 3. Check 'l-time'
        label_time = page.locator("label[for='l-time']")
        if label_time.count() > 0:
            print("PASS: Label for 'l-time' found.")
        else:
            print("FAIL: Label for 'l-time' NOT found.")

        # Open Modal Assign (simulate)
        # We need to mock the ticket data or just force show the modal
        page.evaluate("""
            document.getElementById('modal-assign').classList.remove('hidden');
        """)
        page.screenshot(path="verification/modal_assign.png")
        print("Screenshot saved to verification/modal_assign.png")

        # Verify modal labels
        if page.locator("label[for='a-tech']").count() > 0:
             print("PASS: Label for 'a-tech' found.")
        else:
             print("FAIL: Label for 'a-tech' NOT found.")

        if page.locator("label[for='a-time']").count() > 0:
             print("PASS: Label for 'a-time' found.")
        else:
             print("FAIL: Label for 'a-time' NOT found.")

        browser.close()

if __name__ == "__main__":
    verify_accessibility_changes()
