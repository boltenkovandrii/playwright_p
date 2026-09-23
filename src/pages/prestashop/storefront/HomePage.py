from urllib.parse import urlencode

from components.prestashop.storefront.ProductGrid import ProductGrid
from pages.prestashop.storefront.CatalogPage import CatalogPage
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from pages.prestashop.storefront.ProductPage import ProductPage
from playwright.sync_api import expect

from pages.prestashop.storefront.SearchResultsPage import SearchResultsPage
from resources.translations import UI_TEXT
from utils.allure_reporting import attach_screenshot


class HomePage(BaseStorefrontPage):
    def __init__(self, page, locale="en"):
        super().__init__(page, locale)
        self.carousel = page.get_by_test_id("carousel")
        self.featured_products_heading = page.get_by_role("heading", name=UI_TEXT[self.locale]["featured_products_heading"])
        self.featured_products = ProductGrid(page.locator(".featured-products"))

    def open(self, path=""):
        super().open(path)
        return self

    def verify_loaded(self):
        attach_screenshot(self.page, "Home page")
        super().verify_loaded()
        expect(self.carousel).to_be_visible()
        self.featured_products.verify_loaded()
        return self

    def verify_current_language(self, locale):
        super().verify_current_language(locale)
        expect(self.featured_products_heading).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking home page structure")
        super().check_structure()
        expect(self.carousel).to_be_visible()
        self.featured_products.check_structure()
        return self

    def search(self, query):
        attach_screenshot(self.page, f"Performing search by query: {query}")
        self.header.search(query)
        return SearchResultsPage(self.page, self.locale).verify_loaded()

    def open_search_results(self, query, results_per_page=None, page=None):
        attach_screenshot(self.page, f"Opening search results for query: {query} and results_per_page: {results_per_page} using direct URL")
        params = {"search_query": query}
        if results_per_page is not None:
            params["resultsPerPage"] = str(results_per_page)
        if page is not None:
            params["page"] = str(page)

        self.page.goto(self._localized_url(f"search?{urlencode(params)}"))
        return SearchResultsPage(self.page, self.locale).verify_loaded()

    def open_category(self, name):
        attach_screenshot(self.page, f"Opening category: {name}")
        self.header.click_category(name)
        return CatalogPage(self.page, self.locale).verify_loaded()

    def open_featured_product(self, index=0):
        attach_screenshot(self.page, f"Opening featured product at index: {index}")
        self.featured_products.product_at(index).open_product()
        return ProductPage(self.page, self.locale).verify_loaded()

    def get_featured_product_name(self, index=0):
        attach_screenshot(self.page, f"Getting featured product name at index: {index}")
        return self.featured_products.product_at(index).get_name()

    def open_featured_product_by_name(self, name):
        attach_screenshot(self.page, f"Opening featured product by name: {name}")
        self.featured_products.open_product_by_name(name)
        return ProductPage(self.page, self.locale).verify_loaded()


    def verify_header_cart_count(self, expected_count):
        self.header.verify_cart_count(expected_count)
        return self
