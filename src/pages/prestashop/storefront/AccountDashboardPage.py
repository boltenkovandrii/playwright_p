
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from resources.translations import UI_TEXT
from utils.allure_reporting import attach_screenshot


class AccountDashboardPage(BaseStorefrontPage):
    def __init__(self, page, locale="en"):
        super().__init__(page, locale)
        self.heading = page.get_by_role("heading", name=UI_TEXT[self.locale]["account_heading"])
        self.account_links = page.locator(".links .link-item")

    def open(self, path="my-account"):
        super().open(path)
        return self

    def verify_loaded(self):
        attach_screenshot(self.page, "Account dashboard page")
        super().verify_loaded()
        expect(self.heading).to_be_visible()
        return self

    def verify_current_language(self, locale):
        super().verify_current_language(locale)
        expect(self.heading).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking account dashboard structure")
        super().check_structure()
        expect(self.heading).to_be_visible()
        expect(self.account_links).to_have_count(7)
        return self
