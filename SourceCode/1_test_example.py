from asyncio import wait_for

from playwright.sync_api import sync_playwright

#def test_open_google():
with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500) #actions will be displayed on UI
        page = browser.new_page()
        page.goto("https://google.com")
        page.screenshot(path="google.png")
       # api_context = p.request.n ew_context()
        #response = api_context.get("https://google.com")
       # print(response.json())
       # browser.close()


#test_open_google()