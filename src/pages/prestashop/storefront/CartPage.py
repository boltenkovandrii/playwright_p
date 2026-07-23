from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect


class CartPage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.cart = page.locator(".cart-grid")

    def verify_loaded(self):
        super().verify_loaded()
        expect(self.cart).to_be_visible()
        return self
