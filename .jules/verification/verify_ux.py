from playwright.sync_api import sync_playwright
import os
import json

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Mock API to avoid errors and hangs
        def handle_route(route):
            request = route.request
            if request.method == "POST":
                try:
                    post_data = request.post_data_json
                    action = post_data.get("action") if post_data else None

                    if action == "leader_get_open":
                        route.fulfill(
                            status=200,
                            content_type="application/json",
                            body=json.dumps({"data": []})
                        )
                        return
                except:
                    pass
            # Fulfill others with generic success to avoid hangs
            route.fulfill(
                status=200,
                content_type="application/json",
                body=json.dumps({"status": "success", "data": []})
            )

        page.route("**/*script.google.com*", handle_route)

        # Inject user login
        user = {
            "username": "leader1",
            "fullname": "Leader Test",
            "role": "leader"
        }

        url = f"file://{os.getcwd()}/index.html"
        page.goto(url)

        page.evaluate(f"localStorage.setItem('tpm_user', '{json.dumps(user)}');")
        page.reload()

        # Wait for the Leader screen to appear
        try:
            page.wait_for_selector("#screen-leader:not(.hidden)", timeout=5000)
            page.wait_for_selector("#l-tab-1:not(.hidden)", timeout=5000)
        except Exception as e:
            print(f"Error waiting for selectors: {e}")
            page.screenshot(path=".jules/verification/error.png")
            browser.close()
            return

        # Take screenshot of the form
        page.screenshot(path=".jules/verification/before_changes.png")

        # Check for labels
        has_label_msts = page.evaluate("document.querySelector('label[for=\"l-msts\"]') !== null")
        has_label_chuyen = page.evaluate("document.querySelector('label[for=\"l-chuyen\"]') !== null")

        print(f"Has label for l-msts: {has_label_msts}")
        print(f"Has label for l-chuyen: {has_label_chuyen}")

        browser.close()

if __name__ == "__main__":
    run()
