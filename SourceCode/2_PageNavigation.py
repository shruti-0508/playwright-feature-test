from playwright.sync_api import sync_playwright

#def test_open_google():
def test_playwright ():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1500) #actions will be displayed on UI
        page = browser.new_page()
        page.goto("https://playwright.dev/")
       #select or locate link element with DOCS text

        #page.click("text=/log/i")
      #  page.click('a[href="/docs/intro"]'); #locating by link

        docs_button = page.get_by_role('link', name="Community") #locating by name
        docs_button.click()
       # browser.close()
        print (page.url) # current URL





#page.click('a[href="/docs/intro"]');

test_playwright ()
#test_open_google()