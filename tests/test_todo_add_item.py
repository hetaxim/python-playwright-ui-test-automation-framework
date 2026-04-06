import re
#2. import playwright
from playwright.sync_api import sync_playwright, expect



#1. define the function (enhanced in step 3 is latest)
def test_todo_add_item():
    with (sync_playwright() as p):
        # step 1- browser launch.
        browser = p.chromium.launch(headless=False)
        # step 2 - open a tab.
        page = browser.new_page()
        #step 3 - navigate to website
        page.goto("https://demo.playwright.dev/todomvc/")
        #step 4 - type text and submit using locator - placeholder
        todo_input = page.get_by_placeholder("What needs to be done?")
        #step 5 - type buy milk
        todo_input.fill("Buy milk")
        #type 7 - enter.
        todo_input.press("Enter")
        #checkpoint 1 - verify the item appears/exist on the page (test 1)
        item = page.get_by_role("listitem").filter(has_text='Buy milk')
        expect(item).to_be_visible()
        # checkpoint 2 - verify counter shows item left (test 2)
       # counter=page.locator(".todo-count")
        #expect(counter).to_contain_text("1 item left")
        #checkpoint 3 - verify checking the todo mark is as completed.

        #3.1 - action to check the toggle
        toggle = item.locator("input.toggle")
        toggle.check()

        #3.2 - verify checkbox is checked.
        expect(toggle).to_be_checked()
        #3.3 - verify item has completed class
        expect(item).to_have_class(re.compile(r".*\bcompleted\b.*"))

        browser.close()



