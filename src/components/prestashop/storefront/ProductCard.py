import re

from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class ProductCard:
    def __init__(self, container):
        self.container = container
        self.product_link = container.locator(".product-title a")
        self.price = container.locator(".price")

    def get_name(self):
        return self.product_link.inner_text().strip()

    def get_price(self):
        price_text = self.price.inner_text().strip()
        return float(re.sub(r"[^\d,.]", "", price_text).replace(",", "."))

    def open_product(self):
        with self.container.page.expect_navigation(wait_until="domcontentloaded"):
            self.product_link.click()
        return self

    def check_structure(self):
        attach_screenshot(self.container, "Checking product card structure", False)
        expect(self.container).to_be_visible()
        expect(self.product_link).to_be_visible()
        expect(self.price).to_be_visible()
        return self
