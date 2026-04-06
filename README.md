# python-playwright-ui-test-automation-framework

## Python UI Automation 

This repository includes  UI automated test scripts. Reliable automation starts with simple, well-written tests.


### Basic Playwright + pytest Setup
- Installed Playwright and pytest
- Installed Playwright browsers

```bash
pip install playwright pytest
playwright install
```

### Tool Stack

- **Language:** Python 3.11
- **UI Automation:** Playwright (sync API)
- **Test Runner:** pytest
- **Browser:** Chromium (default)
- **IDE:** PyCharm

### Project Structure: (So far directory folder only, framework - In progress)
├── tests/
│   └── test_example.py


### Test scripting approach:
- Verified tests can run locally
- Scripted tests
- Used locators
  - get_by_role
  - get_by_text
  - get_by_label
- Used Auto-Waits using 'expect' instead of time.sleep(x)

### List of actions and checkpoints
#### Action : Add items todo list

  - Checkpoint 1 - Verify the item exists and visible
  - Checkpoint 2 - Verify the counter counts the items in the todo list
  - Checkpoint 3 - Verify marked completed when clicked on toggle.


