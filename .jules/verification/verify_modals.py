from playwright.sync_api import sync_playwright
import time

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000/index.html")

        # Check modal detail
        modal_detail = page.locator("#modal-detail")

        # Check if modal-detail exists (it might be hidden)
        print(f"Modal detail exists: {modal_detail.count() > 0}")

        # Check for role=dialog
        role = modal_detail.get_attribute("role")
        print(f"Modal detail role: {role}")

        # Check for close button in modal detail header
        close_btn = modal_detail.locator(".header button")
        print(f"Close button exists: {close_btn.count() > 0}")

        aria_label = close_btn.get_attribute("aria-label")
        print(f"Close button aria-label: {aria_label}")

        # Check input l-msts label
        msts_input = page.locator("#l-msts")
        # Check if there is a label with for="l-msts"
        label_msts = page.locator("label[for='l-msts']")
        print(f"Label for l-msts exists: {label_msts.count() > 0}")

        # Check input l-time label
        label_time = page.locator("label[for='l-time']")
        print(f"Label for l-time exists: {label_time.count() > 0}")

        browser.close()

if __name__ == "__main__":
    verify()
