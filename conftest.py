import pytest
from playwright.sync_api import Page, expect, Browser, Playwright


# @pytest.fixture()
# def main_url(page:Page):
#     page.goto('https://www.wikipedia.org/')

@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page

# @pytest.fixture(scope="function")
# def setup_browser(playwright: Playwright) -> Page:
#
#     print("\n--- Setting up browser for test ---")
#
#     browser: Browser = playwright.chromium.launch(headless=False, slow_mo=500) # slow_mo adds a delay between actions
#     page: Page = browser.new_page()
#
#     # You could perform login or other setup here before the test starts
#     # Example: page.goto("login_url"); page.fill("#username", "testuser"); page.click("button[type='submit']")
#
#     yield page  # The test function will run here
#
#     browser.close()

