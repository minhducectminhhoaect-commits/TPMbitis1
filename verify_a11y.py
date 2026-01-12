import bs4
import sys

def verify_a11y(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')

    errors = []

    # Helper to check input labeling
    def check_label(input_id, element_type='input'):
        el = soup.find(element_type, id=input_id)
        if not el:
            errors.append(f"Element #{input_id} not found.")
            return

        # Check for aria-label or aria-labelledby
        if el.get('aria-label') or el.get('aria-labelledby'):
            return

        # Check for explicit label with for attribute
        labels = soup.find_all('label', attrs={'for': input_id})
        if labels:
            return

        # Check for implicit label (wrapped) - unlikely in this codebase but good to check
        parent = el.find_parent('label')
        if parent:
            return

        errors.append(f"Element #{input_id} ({element_type}) is missing a label (for='{input_id}' or aria-label).")

    # 1. Leader Tab 1 inputs
    check_label('l-chuyen', 'select')
    check_label('l-msts', 'input')
    check_label('l-time', 'input')

    # 2. Assign Modal inputs
    check_label('a-tech', 'select')
    check_label('a-time', 'input')

    # 3. Finish Modal inputs
    check_label('f-nhomloi', 'input')
    check_label('f-bienphap', 'textarea')
    check_label('f-time', 'input')

    # 4. Action/Swap Modal inputs
    check_label('c-new-msts', 'input')
    check_label('c-time-swap', 'input')
    check_label('c-time-confirm', 'input')

    # 5. Modals role="dialog"
    modals = ['modal-detail', 'modal-history', 'modal-assign', 'modal-finish', 'modal-action']
    for mid in modals:
        m = soup.find('div', id=mid)
        if not m:
            errors.append(f"Modal #{mid} not found.")
            continue
        if m.get('role') != 'dialog':
            errors.append(f"Modal #{mid} missing role='dialog'.")
        if m.get('aria-modal') != 'true':
            errors.append(f"Modal #{mid} missing aria-modal='true'.")

    if errors:
        print("Accessibility Verification FAILED:")
        for e in errors:
            print(f"- {e}")
        sys.exit(1)
    else:
        print("Accessibility Verification PASSED!")
        sys.exit(0)

if __name__ == "__main__":
    verify_a11y('index.html')
