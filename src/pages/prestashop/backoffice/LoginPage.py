from pages.prestashop.backoffice.BaseBackofficePage import BaseBackofficePage
from playwright.sync_api import expect


class LoginPage(BaseBackofficePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_form = page.locator("form")

    def open(self):
        return super().open()

    def verify_loaded(self):
        super().verify_loaded()
        expect(self.login_form).to_be_visible()
        return self
