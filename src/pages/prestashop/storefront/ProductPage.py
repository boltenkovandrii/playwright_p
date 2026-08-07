import re

from pages.prestashop.storefront.CartPage import CartPage
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class ProductPage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.product = page.locator("#main")
        self.product_name = page.locator("#main h1")
        self.add_to_cart_button = page.locator("[data-button-action='add-to-cart']")
        self.cart_modal = page.locator("#blockcart-modal")

    def verify_loaded(self):
        attach_screenshot(self.page, "Product page")
        super().verify_loaded()
        expect(self.product).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking product page structure")
        super().check_structure()
        expect(self.product).to_be_visible()
        expect(self.page.locator(".product-information")).to_be_visible()
        expect(self.page.locator(".product-cover img").first).to_be_visible()
        expect(self.add_to_cart_button).to_be_visible()
        return self

    def verify_product_name(self, expected_name):
        expect(self.product_name).to_contain_text(
            re.compile(re.escape(expected_name))
        )
        return self

    def add_to_cart(self):
        self.add_to_cart_button.click()
        expect(self.cart_modal).to_be_visible()
        attach_screenshot(self.page, "After adding item to a cart")
        return self

    def go_to_cart(self):
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            self.cart_modal.locator("a[href*='cart']").click()
        attach_screenshot(self.page, "After navigating to the cart")
        return CartPage(self.page).verify_loaded()
