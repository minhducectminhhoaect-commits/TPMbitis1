import json
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Mock user to bypass login
        mock_user = {
            "fullname": "Test Leader",
            "role": "leader"
        }

        # Inject user into localStorage before navigation
        page.add_init_script(f"""
            localStorage.setItem('tpm_user', '{json.dumps(mock_user)}');
        """)

        # Navigate
        page.goto("http://localhost:8000/index.html")

        # Wait for dashboard/leader screen to appear
        page.wait_for_selector("#screen-leader")
        print("Logged in as Leader.")

        # Check Modal Roles
        modals = ["modal-detail", "modal-history", "modal-assign", "modal-finish", "modal-action"]
        missing_roles = []
        for mid in modals:
            role = page.eval_on_selector(f"#{mid}", "el => el.getAttribute('role')")
            aria_modal = page.eval_on_selector(f"#{mid}", "el => el.getAttribute('aria-modal')")
            if role != "dialog":
                missing_roles.append(f"{mid}: role={role}")
            if aria_modal != "true":
                missing_roles.append(f"{mid}: aria-modal={aria_modal}")

        if missing_roles:
            print(f"FAILED: Modals missing accessibility attributes:\n" + "\n".join(missing_roles))
        else:
            print("SUCCESS: All modals have correct attributes.")

        # Test Escape Key
        # First, open a modal. Let's try to open modal-history directly by removing hidden class
        print("Opening modal-history...")
        page.evaluate("document.getElementById('modal-history').classList.remove('hidden')")

        # Check visibility
        is_visible = page.is_visible("#modal-history")
        if not is_visible:
            print("Error: Could not open modal for testing.")
            browser.close()
            return

        # Press Escape
        print("Pressing Escape...")
        page.keyboard.press("Escape")

        # Check if hidden again
        is_hidden = page.eval_on_selector("#modal-history", "el => el.classList.contains('hidden')")
        if is_hidden:
            print("SUCCESS: Escape key closed the modal.")
        else:
            print("FAILED: Escape key did NOT close the modal.")

        browser.close()

if __name__ == "__main__":
    verify()
