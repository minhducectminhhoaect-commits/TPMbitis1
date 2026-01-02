from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load local index.html
        page.goto(f"file://{os.path.abspath('index.html')}")

        # Open modal-detail
        # Use JS to remove hidden class because the triggering button might not be visible in initial state without login
        # Actually, let's try to click a button if possible, but JS is safer for this visual check of the modal itself
        page.evaluate("document.getElementById('modal-detail').classList.remove('hidden')")

        # Wait for modal to be visible
        modal = page.locator("#modal-detail")
        modal.wait_for(state="visible")

        # Take screenshot of the modal
        page.screenshot(path=".jules/verification/modal_verification.png")
        print("Screenshot saved to .jules/verification/modal_verification.png")

        browser.close()

if __name__ == "__main__":
    run()
