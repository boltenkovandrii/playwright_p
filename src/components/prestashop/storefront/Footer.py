from playwright.sync_api import expect


class Footer:
    def __init__(self, page):
        self.container = page.locator("#footer")

    def verify_loaded(self):
        expect(self.container).to_be_visible()
        return self
