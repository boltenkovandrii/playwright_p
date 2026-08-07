import re

from components.prestashop.storefront.ProductGrid import ProductGrid
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class SearchResultsPage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.heading = page.locator("#js-product-list-header")
        self.product_grid = ProductGrid(page.locator("#js-product-list"))

    def verify_loaded(self):
        attach_screenshot(self.page, "Search results page")
        super().verify_loaded()
        expect(self.heading).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking search results page structure")
        super().check_structure()
        expect(self.heading).to_be_visible()
        self.product_grid.check_structure()
        return self

    def get_displayed_results_count(self):
        return self.product_grid.cards.count()

    def verify_products_contain(self, *terms):
        for term in terms:
            expect(
                self.product_grid.cards
                .locator(".product-title a")
                .filter(has_text=re.compile(term, re.IGNORECASE))
                .first
            ).to_be_visible()
        return self
