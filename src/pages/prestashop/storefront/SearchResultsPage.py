import re

from components.prestashop.storefront.ProductGrid import ProductGrid
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from resources.translations import UI_TEXT
from utils.allure_reporting import attach_screenshot


class SearchResultsPage(BaseStorefrontPage):
    def __init__(self, page, locale="en"):
        super().__init__(page, locale)
        self.heading = page.locator("#js-product-list-header")
        self.product_grid = ProductGrid(page.locator("#js-product-list"))
        self.page_list = page.locator("nav.pagination ul.page-list")
        self.no_matches_message = page.get_by_test_id("product-search-no-matches")
        self.search_results_header = page.get_by_test_id("js-product-list-header")

    def verify_loaded(self):
        attach_screenshot(self.page, "Search results page")
        super().verify_loaded()
        expect(self.heading).to_be_visible()
        return self

    def verify_current_language(self, locale):
        super().verify_current_language(locale)
        expect(self.search_results_header).to_contain_text(UI_TEXT[self.locale]["search_results_header"])
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking search results page structure")
        super().check_structure()
        expect(self.heading).to_be_visible()
        if not self.no_matches_message.is_visible():
            self.product_grid.check_structure()
        return self

    def check_displayed_results_count(self, count):
        attach_screenshot(self.page, "Checking displayed results count")
        expect(self.product_grid.cards).to_have_count(count)
        return self

    def check_no_matches_message(self):
        attach_screenshot(self.page, "Checking no matches message")
        expect(self.no_matches_message).to_be_visible()
        expect(self.no_matches_message).to_contain_text(UI_TEXT[self.locale]["search_no_matches_message"])
        return self

    def verify_products_match(self, term):
        attach_screenshot(self.page, f"Verifying products match: {term}")
        for card in self.product_grid.cards.all():
            expect(
                card
                .locator(".product-title a")
                .filter(has_text=re.compile(re.escape(term), re.IGNORECASE))
            ).to_be_visible()
        return self

    def check_pagination_visible(self, visible):
        attach_screenshot(self.page, "Checking pagination visibility")
        if visible:
            expect(self.page_list).to_be_visible()
        else:
            expect(self.page_list).not_to_be_visible()
        return self

    def go_to_page_number(self, index):
        attach_screenshot(self.page, f"Going to page number: {index}")

        link = self.page_list.get_by_role("link", name=str(index), exact=True)
        link.click()

        # PrestaShop's pagination is configured using workaround - with resultsPerPage in the test URL to provide enough results for pagination testing.
        # In headed mode, some viewport configurations occasionally require a second click before the pagination navigation takes effect.
        # Retry only when the expected page state was not reached.
        current_page = self.page.locator("nav.pagination ul.page-list li.current a")
        try:
            expect(current_page).to_have_text(str(index), timeout=1000)
        except AssertionError:
            attach_screenshot(self.page,f"Retrying click for page number: {index}")
            link.click()

        return SearchResultsPage(self.page, self.locale).verify_loaded()

