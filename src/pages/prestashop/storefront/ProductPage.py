from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect


class ProductPage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.product = page.locator("#main")
        self.add_to_cart_button = page.locator("[data-button-action='add-to-cart']")

    def verify_loaded(self):
        super().verify_loaded()
        expect(self.product).to_be_visible()
        return self

    def add_to_cart(self):
        self.add_to_cart_button.click()
        return self
