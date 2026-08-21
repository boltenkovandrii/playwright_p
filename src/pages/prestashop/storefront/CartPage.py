import re

from helpers.prestashop.ProductSpec import ProductSpec
from pages.prestashop.storefront.CheckoutPage import CheckoutPage
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
        self.empty_cart_message = page.locator(".no-items")
        self.continue_shopping_link = page.get_by_role("link", name="Continue shopping")
        self.proceed_to_checkout_link = self.page.locator(".checkout a, .checkout button").first

    def verify_loaded(self):
        attach_screenshot(self.page, "Cart page")
        super().verify_loaded()
        expect(self.page.locator("#cart")).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking cart page structure")
        super().check_structure()
        expect(self.cart).to_be_visible()
        expect(self.page.locator(".cart-overview")).to_be_visible()
        expect(self.page.locator(".cart-detailed-totals")).to_be_visible()
        return self

    def check_empty_structure(self):
        attach_screenshot(self.page, "Checking empty cart structure")
        super().check_structure()
        expect(self.empty_cart_message).to_be_visible()
        expect(self.empty_cart_message).to_contain_text("There are no more items in your cart")
        return self

    def verify_product_count(self, expected_count):
        expect(self.cart_items).to_have_count(expected_count)
        return self

    def verify_product_with_name_present(self, expected_name, expected_count=1):
        product_name = self.cart_item_product_names.filter(
            has_text=re.compile(rf"^\s*{re.escape(expected_name)}\s*$")
        )
        expect(product_name).to_have_count(expected_count)
        expect(product_name.first).to_be_visible()
        return self

    def verify_product_price(self, product, expected_price):
        for item in self.cart_items.filter(has_text=product).all():
            price = item.locator(".current-price .price")
            expect(price).to_be_visible()
            expect(price).to_have_text(f"€{expected_price}")
        return self

    def set_product_quantity(self, product, quantity):
        attach_screenshot(self.page, f"Updating quantity for {product} to {quantity}")
        quantity_input = self._cart_item_by_product(product).locator("input.js-cart-line-product-quantity")
        expect(quantity_input).to_be_visible()
        quantity_input.fill(str(quantity))
        quantity_input.press("Tab")
        expect(quantity_input).to_have_value(str(quantity))
        return self

    def verify_product_quantity(self, product, expected_quantity):
        quantity_input = self._cart_item_by_product(product).locator("input.js-cart-line-product-quantity")
        expect(quantity_input).to_have_value(str(expected_quantity))
        return self

    def remove_product(self, product):
        attach_screenshot(self.page, f"Removing product from cart: {product}")
        product_item = self._cart_item_by_product(product)
        expect(product_item).to_be_visible()
        product_item.locator(".remove-from-cart").click()
        expect(self._cart_item_by_product(product)).to_have_count(0)
        return self

    def continue_shopping(self):
        attach_screenshot(self.page, "Continuing shopping from cart page")
        self.continue_shopping_link.click()
        # avoiding circular imports
        return self.as_home_page()

    def proceed_to_checkout(self):
        attach_screenshot(self.page, "Proceeding from cart to checkout")
        self.proceed_to_checkout_link.click()
        return CheckoutPage(self.page).verify_loaded()

    def verify_products_subtotal(self, expected_subtotal):
        expect(self.cart_products_subtotal_value).to_have_text(f"€{expected_subtotal}")
        return self

    def verify_total(self, expected_total):
        expect(self.cart_total_value).to_have_text(f"€{expected_total}")
        return self


    def _cart_item_by_product(self, product: ProductSpec):
        candidates = self.cart_items.filter(
            has=self.page.locator(".product-line-info a.label", has_text=re.compile(rf"^\s*{re.escape(product.name)}\s*$"))
        )

        for attribute, value in product.attributes.items():
            candidates = candidates.filter(has=self.page.locator( f".{attribute} .value", has_text=value))

        return candidates.first