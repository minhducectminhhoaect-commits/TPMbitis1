from playwright.sync_api import sync_playwright
import time

def verify_dashboard(page):
    page.on("console", lambda msg: print(f"PAGE LOG: {msg.text}"))
    page.goto('http://localhost:8000/index.html')

    # Bypass login
    page.evaluate("""
        localStorage.setItem('tpm_user', JSON.stringify({role: 'leader', fullname: 'Test Leader'}));
    """)
    page.reload()

    # Wait for dashboard button
    page.wait_for_selector('button:has-text("Xem Dashboard Chi Tiết")')

    # Mock post ensuring it overrides existing function
    page.evaluate("""
        window.mockDashboardData = {
            data: [
                {chuyen: 'May 1', gio_hu: new Date(Date.now() - 86400000).toISOString(), ma_so: 'M1-001', ten_bao_tri: 'Tech A', gio_xong: new Date().toISOString()},
                {chuyen: 'May 2', gio_hu: new Date(Date.now() - 172800000).toISOString(), ma_so: 'M2-002', ten_bao_tri: 'Tech B', gio_xong: new Date().toISOString()},
                {chuyen: 'May 3', gio_hu: new Date(Date.now() - 259200000).toISOString(), ma_so: 'M3-003', ten_bao_tri: 'Tech C', gio_xong: new Date().toISOString()}
            ]
        };
        window.post = function(data, cb) {
            console.log("Mock post called with: " + JSON.stringify(data));
            if (data && data.action === 'get_dashboard') {
                cb(window.mockDashboardData);
            }
        };
    """)

    # Navigate to Dashboard
    page.click('button:has-text("Xem Dashboard Chi Tiết")')

    # Wait for dashboard
    page.wait_for_selector('#screen-dashboard:not(.hidden)')

    # Check initial load
    time.sleep(1)
    initial_total = page.text_content('#kpi-total')
    print(f"Initial Total: {initial_total}")

    # Set filters
    page.fill('#d-start', '2020-01-01')
    page.fill('#d-end', '2030-12-31')

    # Click Filter
    page.click('button:has-text("Lọc Dữ Liệu")')

    # Wait
    time.sleep(1)

    # Verify
    final_total = page.text_content('#kpi-total')
    print(f"Final Total (filtered): {final_total}")

    if final_total == '3':
        print("SUCCESS: Dashboard loaded and filtered correctly.")
    else:
        print(f"FAILURE: Expected 3, got {final_total}")

    page.screenshot(path='.jules/verification/dashboard_opt.png')

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            verify_dashboard(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
