
import re
from playwright.sync_api import sync_playwright, expect


def _add_todo(page, text: str):
    todo_input = page.get_by_placeholder("What needs to be done?")
    todo_input.fill(text)
    todo_input.press("Enter")
    return page.get_by_role("listitem").filter(has_text=text)


def test_checkpoint1_add_item_visible():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc/")

        item = _add_todo(page, "Buy milk")
        expect(item).to_be_visible()

        browser.close()


def test_checkpoint2_counter_updates():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc/")

        _add_todo(page, "Buy milk")
        counter = page.locator(".todo-count")
        expect(counter).to_contain_text("1 item left")

        browser.close()


def test_checkpoint3_mark_completed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc/")

        item = _add_todo(page, "Buy milk")

        toggle = item.locator("input.toggle")
        toggle.check()
        expect(toggle).to_be_checked()

        # Verify completed class (Python expects string/regex, not lambda)
        expect(item).to_have_class(re.compile(r".*\bcompleted\b.*"))

        browser.close()
