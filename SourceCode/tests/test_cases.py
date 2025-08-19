import re

import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
#from SourceCode.tests.test_cases import test_has_title, test_get_started_link
def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

@pytest.fixture
def a():
    return 10
def test_maths(a):
    b = 10
    assert a == b


with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1500)  # actions will be displayed on UI
        page = browser.new_page()
        #test_has_title(page)
        #test_get_started_link(page)
        #test_maths(a)

