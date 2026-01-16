import os
from playwright.sync_api import sync_playwright

def verify_accessibility_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        page.add_init_script("""
            window.localStorage.setItem('tpm_user', JSON.stringify({fullname: 'Test Leader', role: 'leader'}));
            window.post = (data, cb) => {
                if(data.action === 'leader_get_open') cb({data: []});
                if(data.action === 'leader_get_actionable') cb({data: []});
                if(data.action === 'get_history') cb({data: []});
                if(data.action === 'get_dashboard') cb({data: []});
            };
        """)

        page.reload()

        print("Verifying Leader Screen Labels...")
        page.locator("#l-tab-1").wait_for(state="visible")

        labels = [("l-chuyen", "Chuyền sản xuất"), ("l-msts", "Mã số tài sản"), ("l-time", "Thời điểm hư")]
        for id_val, text in labels:
            l = page.locator(f"label[for='{id_val}']")
            if l.count() > 0 and text in l.inner_text():
                print(f"PASS: Label for {id_val} found.")
            else:
                print(f"FAIL: Label for {id_val} incorrect or missing.")

        page.screenshot(path="/home/jules/verification/leader_screen.png")

        print("\nVerifying Modals...")
        def check_modal(id_name, has_header_close=False):
            modal = page.locator(f"#{id_name}")
            role = modal.get_attribute("role")
            if role == "dialog" and modal.get_attribute("aria-modal") == "true":
                 print(f"PASS: Modal {id_name} has correct ARIA attributes.")
            else:
                 print(f"FAIL: Modal {id_name} missing attributes.")

            if has_header_close:
                close_btn = modal.locator("button.secondary").first
                if close_btn.get_attribute("aria-label") == "Đóng":
                     print(f"PASS: Modal {id_name} close button has aria-label.")
                else:
                     print(f"FAIL: Modal {id_name} close button missing aria-label.")

        check_modal("modal-detail", has_header_close=True)
        check_modal("modal-assign")
        check_modal("modal-finish")
        check_modal("modal-action")

        print("\nVerifying Dashboard Filters...")
        page.evaluate("showDashboard(true)")
        d_vsm = page.locator("#d-vsm")
        if d_vsm.get_attribute("aria-label") == "Lọc theo VSM":
            print("PASS: #d-vsm has aria-label")
        else:
             print("FAIL: #d-vsm missing aria-label")

        print("\nVerifying Toasts...")
        page.evaluate("showToast('Error Msg', 'error')")
        t = page.locator(".toast.error")
        t.wait_for()
        if t.get_attribute("role") == "alert":
            print("PASS: Error toast has role='alert'")
        else:
            print("FAIL: Error toast missing role")

        browser.close()

if __name__ == "__main__":
    verify_accessibility_changes()
