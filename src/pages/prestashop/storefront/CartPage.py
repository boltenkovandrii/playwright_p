from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class CartPage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.cart = page.locator(".cart-grid")

    def verify_loaded(self):
        super().verify_loaded()
        expect(self.cart).to_be_visible()
        return self

    def check_structure(self, profile):
        attach_screenshot(self.page, "Checking cart page structure")
        super().check_structure(profile)
        expect(self.cart).to_be_visible()
        expect(self.page.locator(".cart-overview")).to_be_visible()
        expect(self.page.locator(".cart-detailed-totals")).to_be_visible()
        return self
