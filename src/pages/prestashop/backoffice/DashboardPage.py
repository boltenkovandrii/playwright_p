from pages.prestashop.backoffice.BaseBackofficePage import BaseBackofficePage
from playwright.sync_api import expect


class DashboardPage(BaseBackofficePage):
    def __init__(self, page):
        super().__init__(page)
        self.dashboard = page.locator("#content")

    def verify_loaded(self):
        super().verify_loaded()
        expect(self.dashboard).to_be_visible()
        return self
