from playwright.sync_api import expect
class MainPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto('https://www.wikipedia.org/')

    def check_link_visible(self):
        link = self.page.get_by_role('link', name='English')
        expect(link).to_be_visible()