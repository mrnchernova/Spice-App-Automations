# import pytest
# from playwright.sync_api import Page, expect, Browser, Playwright


# @pytest.fixture()
# def main_url(page:Page):
#     page.goto('https://www.wikipedia.org/')

# @pytest.fixture()
# def page(context):
#     page: Page = context.new_page()
#     page.set_viewport_size({'height': 1080, 'width': 1920})
#     yield page

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


import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from typing import Generator


@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,   # 👈 запуск без окна браузера
            args=["--disable-notifications"]
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser) -> Generator[Page, None, None]:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def test_example(page: Page):
    page.goto("https://example.com")
    assert "Example Domain" in page.title()
