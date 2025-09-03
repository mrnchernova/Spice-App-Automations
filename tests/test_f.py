from playwright.sync_api import Page, expect
import pytest
import time
from pages.main_page import MainPage

def test_wiki(page):
    # page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='English').click()
    expect(page.get_by_text('From today\'s featured article')).to_be_visible()
    time.sleep(5)

@pytest.mark.smoke
def test_wiki2(page):
    main_page = MainPage(page)
    main_page.open()
    main_page.check_link_visible()
    page.get_by_role('link', name='English').click()
    expect(page.get_by_text('From today\'s featured article')).to_be_visible()
    page.get_by_role('link', name='Talk').click()
    expect(page.locator('#talkheader')).to_contain_text('Welcome! This page is for discussing the contents of the English Wikipedia\'s Main Page.')
    time.sleep(5)