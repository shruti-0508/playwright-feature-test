from playwright.sync_api import sync_playwright
from SourceCode.tests.test_cases import test_has_title, test_get_started_link

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1500)  # actions will be displayed on UI
        page = browser.new_page().goto("https://playwright.dev/")
        test_has_title()
        test_get_started_link()

