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
        self.page_list = page.locator("nav.pagination ul.page-list")

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

    def check_displayed_results_count(self, count):
        expect(self.product_grid.cards).to_have_count(count)
        return self

    def verify_products_match(self, term):
        for card in self.product_grid.cards.all():
            expect(
                card
                .locator(".product-title a")
                .filter(has_text=re.compile(re.escape(term), re.IGNORECASE))
            ).to_be_visible()
        return self

    def check_pagination_visible(self, visible):
        if visible:
            expect(self.page_list).to_be_visible()
        else:
            expect(self.page_list).not_to_be_visible()
        return self

    def go_to_page_number(self, index):
        self.page_list.get_by_role("link", name=str(index), exact=True).click()
        return SearchResultsPage(self.page).verify_loaded()