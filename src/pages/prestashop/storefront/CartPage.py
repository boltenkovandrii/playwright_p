import re

from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class CartPage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.cart = page.locator(".cart-grid")
        self.cart_items = page.locator(".cart-items .cart-item")
        self.cart_item_product_names = self.cart_items.locator(".product-line-info a.label")
        self.cart_item_product_prices = self.cart_items.locator(".current-price .price")
        self.cart_products_subtotal_value = page.locator("#cart-subtotal-products .value")
        self.cart_total_value = page.locator(".cart-summary-line.cart-total .value")

    def verify_loaded(self):
        attach_screenshot(self.page, "Cart page")
        super().verify_loaded()
        expect(self.cart).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking cart page structure")
        super().check_structure()
        expect(self.cart).to_be_visible()
        expect(self.page.locator(".cart-overview")).to_be_visible()
        expect(self.page.locator(".cart-detailed-totals")).to_be_visible()
        return self

    def verify_product_count(self, expected_count):
        expect(self.cart_items).to_have_count(expected_count)
        return self

    def verify_product_name(self, expected_name):
        product_name = self.cart_item_product_names.filter(
            has_text=re.compile(rf"^\s*{re.escape(expected_name)}\s*$")
        )
        expect(product_name).to_have_count(1)
        expect(product_name.first).to_be_visible()
        return self

    def verify_product_price(self, expected_price):
        expect(self.cart_item_product_prices.first).to_be_visible()
        expect(self.cart_item_product_prices.first).to_have_text(f"€{expected_price}")
        return self

    def verify_products_subtotal(self, expected_subtotal):
        expect(self.cart_products_subtotal_value).to_have_text(f"€{expected_subtotal}")
        return self

    def verify_total(self, expected_total):
        expect(self.cart_total_value).to_have_text(f"€{expected_total}")
        return self

