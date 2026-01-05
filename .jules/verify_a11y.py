from bs4 import BeautifulSoup
import sys
import os

def check_accessibility():
    if not os.path.exists("index.html"):
        print("index.html not found!")
        return False

    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    errors = []

    # 1. Check Modals for role="dialog" and aria-modal="true"
    modal_ids = ["modal-detail", "modal-history", "modal-assign", "modal-finish", "modal-action"]
    for mid in modal_ids:
        modal = soup.find(id=mid)
        if modal:
            if modal.get("role") != "dialog":
                errors.append(f"Modal #{mid} missing role='dialog'")
            if modal.get("aria-modal") != "true":
                errors.append(f"Modal #{mid} missing aria-modal='true'")

    # 2. Check Close Buttons for aria-label
    # Searching for buttons that likely function as close buttons inside modals
    # They usually have onclick that hides the modal
    for mid in modal_ids:
        modal = soup.find(id=mid)
        if modal:
            # Find buttons inside the header or with "secondary" class that hide the modal
            buttons = modal.find_all("button")
            for btn in buttons:
                onclick = btn.get("onclick", "")
                text = btn.get_text().strip()
                if "hidden" in onclick and (text == "X" or text == "Đóng"):
                    # This is likely a close button
                    if not btn.get("aria-label"):
                        errors.append(f"Close button in #{mid} ('{text}') missing aria-label")

    # 3. Check specific unassociated label in #l-tab-1
    # <label style="font-size:12px">Thời điểm hư:</label><input type="datetime-local" id="l-time">
    l_tab_1 = soup.find(id="l-tab-1")
    if l_tab_1:
        labels = l_tab_1.find_all("label")
        for label in labels:
            if "Thời điểm hư" in label.get_text():
                if not label.get("for"):
                    errors.append("Label 'Thời điểm hư' in #l-tab-1 missing 'for' attribute")

    if errors:
        print("Accessibility Issues Found:")
        for e in errors:
            print(f"- {e}")
        return False
    else:
        print("All Checked Accessibility Improvements Present!")
        return True

if __name__ == "__main__":
    if not check_accessibility():
        sys.exit(1)
