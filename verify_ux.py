from playwright.sync_api import sync_playwright
import json
import os
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Inject leader user
        user = {
            "fullname": "Leader Test",
            "role": "leader"
        }

        # Navigate to the file
        # Since we are local, we can open the file directly if we serve it or just open it.
        # But we need local storage before load? Or set it after?
        # The app checks localStorage on DOMContentLoaded.
        # So we need to set it before.

        # We can use a simple script to set localStorage before load? No, localStorage is origin bound.
        # We should load the page, then set localStorage, then reload.

        # Start a simple http server in the background to serve the current directory
        # This is better than file:// because of localStorage security in some browsers, though file:// might work.
        # Let's assume file:// works for now or use the python http.server running in background.

        # Assuming we can just access via file protocol for simplicity or localhost:8000
        # Let's rely on the memory that says "The application can be served locally for testing using python3 -m http.server"

        page.goto("http://localhost:8000/index.html")

        # Inject user
        page.evaluate(f"localStorage.setItem('tpm_user', '{json.dumps(user)}');")
        page.reload()

        # Wait for "Báo Hư" tab to be visible
        # It is tab 1, so it should be visible by default for leader
        page.wait_for_selector("#l-tab-1")

        print("Checking for labels in #l-tab-1...")

        # Check for labels for l-chuyen and l-msts
        # Using evaluate to check DOM structure specifically
        labels_exist = page.evaluate("""() => {
            const chuyenLabel = document.querySelector('label[for="l-chuyen"]');
            const mstsLabel = document.querySelector('label[for="l-msts"]');
            const chuyenRequired = document.getElementById('l-chuyen').hasAttribute('required');
            const mstsRequired = document.getElementById('l-msts').hasAttribute('required');
            const closeBtnLabel = document.querySelector('#modal-detail button.secondary').getAttribute('aria-label');

            return {
                chuyenLabel: !!chuyenLabel,
                mstsLabel: !!mstsLabel,
                chuyenRequired: chuyenRequired,
                mstsRequired: mstsRequired,
                closeBtnLabel: closeBtnLabel
            };
        }""")

        print(f"Labels status: {labels_exist}")

        # Take screenshot
        os.makedirs(".jules/verification", exist_ok=True)
        page.screenshot(path=".jules/verification/before_changes.png")

        browser.close()

if __name__ == "__main__":
    run()
