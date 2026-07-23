from pages.BasePage import BasePage
from playwright.sync_api import expect


class BaseBackofficePage(BasePage):
    BASE_URL = "http://localhost:8090/admin-dev/"

    def open(self, path=""):
        self.page.goto(f"{self.BASE_URL}{path}")
        return self

    def verify_loaded(self):
        expect(self.page.locator("body")).to_be_visible()
        return self
