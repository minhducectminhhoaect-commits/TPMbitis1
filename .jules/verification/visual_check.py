from playwright.sync_api import sync_playwright

def verify_visuals():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000/index.html")

        # Mock ticketCache to avoid errors if any scripts try to access it
        page.evaluate("window.ticketCache = {}")

        # Unhide modal detail to screenshot it
        # We also need to populate it with some content to make it look realistic
        page.evaluate("""
            const modal = document.getElementById('modal-detail');
            modal.classList.remove('hidden');
            document.getElementById('detail-content').innerHTML = '<div style="padding:10px">Sample Content</div>';
        """)

        page.screenshot(path=".jules/verification/modal_detail.png")
        print("Screenshot saved to .jules/verification/modal_detail.png")

        browser.close()

if __name__ == "__main__":
    verify_visuals()
