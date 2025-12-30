from playwright.sync_api import sync_playwright

def verify_modals(page):
    page.goto("http://localhost:8080/index.html")

    # Check modal-detail attributes
    modal = page.locator("#modal-detail")

    # We can't easily check 'role' and 'aria-modal' via standard expect matchers directly without get_attribute
    # But we can assert they exist
    role = modal.get_attribute("role")
    aria_modal = modal.get_attribute("aria-modal")

    print(f"modal-detail role: {role}")
    print(f"modal-detail aria-modal: {aria_modal}")

    if role != "dialog":
        print("FAIL: modal-detail role is not dialog")
    if aria_modal != "true":
        print("FAIL: modal-detail aria-modal is not true")

    # Check Close button in modal-detail
    close_btn = modal.locator("button.secondary").first
    aria_label = close_btn.get_attribute("aria-label")
    print(f"modal-detail close button aria-label: {aria_label}")

    if aria_label != "Đóng":
        print("FAIL: modal-detail close button missing aria-label='Đóng'")

    # Check modal-assign label associations
    page.evaluate("document.getElementById('modal-assign').classList.remove('hidden')")
    page.wait_for_selector("#modal-assign", state="visible")

    # Take screenshot of open modal
    page.screenshot(path=".jules/verification/modal_assign.png")

    # Verify label for
    label_tech = page.locator("#modal-assign label[for='a-tech']")
    if label_tech.count() == 0:
        print("FAIL: No label for='a-tech' found in modal-assign")
    else:
        print("PASS: Label for='a-tech' exists")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            verify_modals(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
