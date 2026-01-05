from playwright.sync_api import sync_playwright

def verify_accessibility(page):
    page.goto("http://localhost:8000/index.html")

    # Override the global post function to mock backend calls
    # Note: data might be null if it's an auto-login check or similar that doesn't send data?
    # Actually, checkAutoLogin calls restoreSession which calls loadLeaderOpen which calls post({action:'leader_get_open'})
    # But wait, document.addEventListener('DOMContentLoaded', () => { checkAutoLogin(); });
    # checkAutoLogin reads localStorage.
    # If localStorage is empty (which it is), it does nothing.

    # However, handleLogin does post.

    # The error was: TypeError: Cannot read properties of null (reading 'action')
    # This implies 'data' was null in window.post.

    page.evaluate("""
        window.post = function(data, cb) {
            console.log('Mock post called with:', data);
            if (!data) return; // Prevent crash if data is null

            if (data.action === 'leader_get_open') {
                cb({data: []});
            } else if (data.action === 'get_dashboard') {
                cb({data: []});
            } else if (data.action === 'tech_get_jobs') {
                cb({data: {myJobs: [], alertJobs: []}});
            } else {
                cb({data: []});
            }
        };
    """)

    # Verify attributes on modals
    modal_ids = ["modal-detail", "modal-history", "modal-assign", "modal-finish", "modal-action"]
    for mid in modal_ids:
        locator = page.locator(f"#{mid}")
        role = locator.get_attribute("role")
        aria_modal = locator.get_attribute("aria-modal")
        aria_labelledby = locator.get_attribute("aria-labelledby")

        print(f"Checking #{mid}: role={role}, aria-modal={aria_modal}, aria-labelledby={aria_labelledby}")
        assert role == "dialog"
        assert aria_modal == "true"
        assert aria_labelledby is not None

    # Open a modal to visualize it
    # We'll use JS to remove 'hidden' class from one modal to take a screenshot
    page.evaluate("document.getElementById('modal-detail').classList.remove('hidden')")

    # Check the close button in the modal
    close_btn = page.locator("#modal-detail button.secondary").first
    aria_label = close_btn.get_attribute("aria-label")
    print(f"Checking Close Button in #modal-detail: aria-label={aria_label}")
    assert aria_label == "Đóng"

    page.screenshot(path=".jules/verification/modal_accessibility.png")
    print("Verification complete. Screenshot saved.")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_accessibility(page)
        finally:
            browser.close()
