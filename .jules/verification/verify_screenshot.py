from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the local index.html
        page.goto(f"file://{os.path.abspath('index.html')}")

        # Trigger a Success Toast
        page.evaluate("showToast('Success Toast', 'success')")

        # Trigger an Error Toast
        page.evaluate("showToast('Error Toast', 'error')")

        # Open Modal Detail to see the close button
        page.evaluate("document.getElementById('modal-detail').classList.remove('hidden')")

        # Wait a bit for animations
        page.wait_for_timeout(1000)

        # Take screenshot
        page.screenshot(path=".jules/verification/ux_verification.png")

        browser.close()

if __name__ == "__main__":
    run()
