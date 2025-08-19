#def test_open_google():

from playwright.sync_api import sync_playwright
def test_playwright ():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1500) #actions will be displayed on UI
        page = browser.new_page()
        page.goto("https://playwright.dev/")


        #docs_button = page.get_by_role('link', name="Community")
        getstarted_button = page.get_by_role('link',name = "GET STARTED")
        #locating by name
        getstarted_button.click()
       # browser.close()
        print (page.url) # current URL

test_playwright()