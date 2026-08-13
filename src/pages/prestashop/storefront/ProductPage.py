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
        self.product_information = page.locator(".product-information")

        self.cover_image = page.locator(".product-cover .img-fluid")
        self.price = page.locator(".current-price .current-price-value")
        self.regular_price = page.locator(".product-discount .regular-price")
        self.description_short = page.locator("div[id*='product-description-short-'] p")

        self.description_tab = page.get_by_role("tab", name="Description")
        self.description_tab_panel = page.get_by_test_id("description")
        self.description_full = page.locator(".tab-content .product-description")

        self.product_details_tab = page.get_by_role("tab", name="Product Details")
        self.product_details_tab_panel = page.get_by_test_id("product-details")
        self.in_stock = page.locator(".product-quantities span")




        self.short_description = self.product_information.locator("p").filter(has_text=re.compile(r"\S")).first


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
        expect(self.cover_image).to_be_visible()
        expect(self.product_information).to_be_visible()
        expect(self.short_description).to_be_visible()
        expect(self.description_tab).to_be_visible()
        expect(self.product_details_tab).to_be_visible()
        expect(self.add_to_cart_button).to_be_visible()
        return self

    def verify_product_name(self, expected_name):
        attach_screenshot(self.page, "Verifying product name")
        expect(self.product_name).to_contain_text(
            re.compile(re.escape(expected_name), re.IGNORECASE)
        )
        return self

    def verify_regular_price(self, expected_price):
        expect(self.regular_price).to_have_text(f"€{expected_price}")
        return self

    def verify_price(self, expected_price):
        expect(self.price).to_have_text(f"€{expected_price}")
        return self

    def verify_short_description(self, expected_text):
        expect(self.description_short).to_contain_text(expected_text)
        return self

    def verify_full_description(self, expected_text):
        self._open_description_tab()
        expect(self.description_full).to_be_visible()
        expect(self.description_full).to_contain_text(expected_text)
        return self

    def verify_in_stock_count(self, count):
        self._open_product_details_tab()
        expect(self.in_stock).to_be_visible()
        expect(self.in_stock).to_have_text(f"{count} Items")
        return self

    def _open_description_tab(self):
        self.description_tab.click()
        expect(self.description_tab_panel).to_be_visible()
        return self

    def _open_product_details_tab(self):
        self.product_details_tab.click()
        expect(self.product_details_tab_panel).to_be_visible()
        return self

    def add_to_cart(self):
        attach_screenshot(self.page, "Adding product to cart")
        self.add_to_cart_button.click()
        expect(self.cart_modal).to_be_visible()
        attach_screenshot(self.page, "After adding item to a cart")
        return self

    def go_to_cart(self):
        attach_screenshot(self.page, "Going to cart")
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            self.cart_modal.locator("a[href*='cart']").click()
        attach_screenshot(self.page, "After navigating to the cart")
        return CartPage(self.page).verify_loaded()

    def go_to_category_from_breadcrumb(self, category_name):
        attach_screenshot(self.page, "Going to category from breadcrumb")
        from pages.prestashop.storefront.CatalogPage import CatalogPage
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            self.page.locator("nav.breadcrumb a").filter(has_text=category_name).click()
        return CatalogPage(self.page).verify_loaded()

