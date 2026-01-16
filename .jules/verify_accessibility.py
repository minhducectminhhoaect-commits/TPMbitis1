from bs4 import BeautifulSoup
import sys

def check_accessibility(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    issues = []

    # Check 1: Inputs/Selects/Textareas without labels
    form_elements = soup.find_all(['input', 'select', 'textarea'])
    for el in form_elements:
        if el.get('type') == 'hidden':
            continue

        el_id = el.get('id')
        if not el_id:
            continue

        # Check for associated label
        label = soup.find('label', attrs={'for': el_id})
        aria_label = el.get('aria-label')
        aria_labelledby = el.get('aria-labelledby')

        if not label and not aria_label and not aria_labelledby:
            # Check if implicit label (parent is label)
            if el.find_parent('label'):
                continue
            issues.append(f"Missing label for element: <{el.name} id='{el_id}'>")

    # Check 2: Icon-only buttons (simplified check: buttons with little text or known class)
    buttons = soup.find_all('button')
    for btn in buttons:
        text = btn.get_text(strip=True)
        if len(text) <= 1 and not btn.get('aria-label'):
            issues.append(f"Button with little/no text needs aria-label: <button ...>{text}</button>")

    # Check 3: Modals without roles
    modals = soup.find_all('div', id=lambda x: x and x.startswith('modal-'))
    for modal in modals:
        if not modal.get('role'):
             issues.append(f"Modal div needs role='dialog': <div id='{modal.get('id')}'>")

    return issues

if __name__ == "__main__":
    issues = check_accessibility('index.html')
    if issues:
        print("Accessibility Issues Found:")
        for i in issues:
            print(f"- {i}")
    else:
        print("No accessibility issues found (by this simple check).")
