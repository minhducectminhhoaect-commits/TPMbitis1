from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the local index.html
        page.goto(f"file://{os.path.abspath('index.html')}")

        # Test 1: Check ShowToast
        print("Testing ShowToast...")

        # Mock the function if needed, but it's defined in global scope so we can just call it.
        # Call showToast with success
        page.evaluate("showToast('Test Success', 'success')")

        # Check if the toast element exists and has role="status"
        toast = page.locator(".toast.success").first
        toast.wait_for()

        role = toast.get_attribute("role")
        aria_live = toast.get_attribute("aria-live")

        print(f"Success Toast Role: {role}")
        print(f"Success Toast Aria-Live: {aria_live}")

        if role == "status" and aria_live == "polite":
            print("✅ Success Toast Attributes Correct")
        else:
            print("❌ Success Toast Attributes Incorrect (Expected role=status, aria-live=polite)")

        # Call showToast with error
        page.evaluate("showToast('Test Error', 'error')")

        # Check if the toast element exists and has role="alert"
        toast_err = page.locator(".toast.error").first
        toast_err.wait_for()

        role_err = toast_err.get_attribute("role")
        aria_live_err = toast_err.get_attribute("aria-live")

        print(f"Error Toast Role: {role_err}")
        print(f"Error Toast Aria-Live: {aria_live_err}")

        if role_err == "alert" and aria_live_err == "assertive":
            print("✅ Error Toast Attributes Correct")
        else:
            print("❌ Error Toast Attributes Incorrect (Expected role=alert, aria-live=assertive)")

        # Test 2: Check Modal Close Button Aria Label
        # The button is in #modal-detail header
        # <button class="secondary" ...>X</button>

        # We find the button by its text content "X" inside #modal-detail
        close_btn = page.locator("#modal-detail button.secondary").filter(has_text="X").first
        aria_label = close_btn.get_attribute("aria-label")

        print(f"Modal Close Button Aria-Label: {aria_label}")

        if aria_label == "Đóng":
            print("✅ Modal Close Button Aria-Label Correct")
        else:
            print("❌ Modal Close Button Aria-Label Incorrect (Expected 'Đóng')")

        browser.close()

if __name__ == "__main__":
    run()
