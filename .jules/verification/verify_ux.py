from playwright.sync_api import sync_playwright

def verify_a11y(page):
    page.goto("http://localhost:3000/index.html")

    # 1. Login to access Leader screen
    # We can inject local storage to bypass login or just login
    # Injecting local storage is faster and more reliable
    user_data = '{"fullname": "Test Leader", "role": "leader"}'
    page.add_init_script(f"localStorage.setItem('tpm_user', '{user_data}')")
    page.reload()

    # 2. Verify Labels in Leader Screen (Tab 1)
    # Check for "Chuyền / Khu vực" label
    label_chuyen = page.locator("label[for='l-chuyen']")
    if label_chuyen.is_visible() and label_chuyen.text_content() == "Chuyền / Khu vực":
        print("PASS: Label 'Chuyền / Khu vực' found.")
    else:
        print("FAIL: Label 'Chuyền / Khu vực' not found.")

    # Check for "Mã Số Tài Sản" label
    label_msts = page.locator("label[for='l-msts']")
    if label_msts.is_visible() and label_msts.text_content() == "Mã Số Tài Sản":
        print("PASS: Label 'Mã Số Tài Sản' found.")
    else:
        print("FAIL: Label 'Mã Số Tài Sản' not found.")

    # Check for "Thời điểm hư" label class
    label_time = page.locator("label[for='l-time']")
    if "input-label" in label_time.get_attribute("class"):
        print("PASS: Label 'Thời điểm hư' has class 'input-label'.")
    else:
        print("FAIL: Label 'Thời điểm hư' missing class 'input-label'.")

    # 3. Verify Modals Accessibility Attributes
    # Verify #modal-detail
    modal_detail = page.locator("#modal-detail")
    if modal_detail.get_attribute("role") == "dialog" and modal_detail.get_attribute("aria-modal") == "true":
        print("PASS: #modal-detail has correct ARIA attributes.")
    else:
        print("FAIL: #modal-detail missing ARIA attributes.")

    # Verify Close Button in #modal-detail
    close_btn = modal_detail.locator("button[aria-label='Đóng']")
    if close_btn.count() > 0:
        print("PASS: Close button with aria-label='Đóng' found in #modal-detail.")
    else:
        print("FAIL: Close button with aria-label='Đóng' not found in #modal-detail.")

    # Verify #modal-assign
    modal_assign = page.locator("#modal-assign")
    if modal_assign.get_attribute("role") == "dialog" and modal_assign.get_attribute("aria-modal") == "true":
        print("PASS: #modal-assign has correct ARIA attributes.")
    else:
        print("FAIL: #modal-assign missing ARIA attributes.")

    # Verify #modal-finish
    modal_finish = page.locator("#modal-finish")
    if modal_finish.get_attribute("role") == "dialog" and modal_finish.get_attribute("aria-modal") == "true":
        print("PASS: #modal-finish has correct ARIA attributes.")
    else:
        print("FAIL: #modal-finish missing ARIA attributes.")

    # Verify #modal-action
    modal_action = page.locator("#modal-action")
    if modal_action.get_attribute("role") == "dialog" and modal_action.get_attribute("aria-modal") == "true":
        print("PASS: #modal-action has correct ARIA attributes.")
    else:
        print("FAIL: #modal-action missing ARIA attributes.")

    # Take screenshot of Leader Screen
    page.screenshot(path=".jules/verification/leader_screen.png")

    # Open a modal to take screenshot (e.g., Assign modal)
    # We need to mock the data or just force show it
    page.evaluate("document.getElementById('modal-assign').classList.remove('hidden')")
    page.screenshot(path=".jules/verification/modal_assign.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            verify_a11y(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
