from urllib.parse import urlencode

from components.prestashop.storefront.ProductGrid import ProductGrid
from pages.prestashop.storefront.CatalogPage import CatalogPage
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from pages.prestashop.storefront.ProductPage import ProductPage
from playwright.sync_api import expect

from pages.prestashop.storefront.SearchResultsPage import SearchResultsPage
from utils.allure_reporting import attach_screenshot


class HomePage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.carousel = page.locator("#carousel")
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

    def check_structure(self):
        attach_screenshot(self.page, "Checking home page structure")
        super().check_structure()
        expect(self.carousel).to_be_visible()
        self.featured_products.check_structure()
        return self

    def search(self, query):
        attach_screenshot(self.page, f"Performing search by query: {query}")
        self.header.search(query)
        return SearchResultsPage(self.page).verify_loaded()

    def open_search_results(self, query, results_per_page=None, page=None):
        attach_screenshot(self.page, f"Opening search results for query: {query} and results_per_page: {results_per_page} using direct URL")
        params = {"search_query": query}
        if results_per_page is not None:
            params["resultsPerPage"] = str(results_per_page)
        if page is not None:
            params["page"] = str(page)

        self.page.goto(f"{self.BASE_URL}search?{urlencode(params)}")
        return SearchResultsPage(self.page).verify_loaded()

    def open_category(self, profile, name):
        attach_screenshot(self.page, f"Opening category: {name} for profile: {profile}")
        self.header.click_category(profile, name)
        return CatalogPage(self.page).verify_loaded()

    def open_featured_product(self, index=0):
        attach_screenshot(self.page, f"Opening featured product at index: {index}")
        self.featured_products.product_at(index).open_product()
        return ProductPage(self.page).verify_loaded()

    def get_featured_product_name(self, index=0):
        attach_screenshot(self.page, f"Getting featured product name at index: {index}")
        return self.featured_products.product_at(index).get_name()

    def open_featured_product_by_name(self, name):
        attach_screenshot(self.page, f"Opening featured product by name: {name}")
        self.featured_products.open_product_by_name(name)
        return ProductPage(self.page).verify_loaded()


    def verify_header_cart_count(self, expected_count):
        self.header.verify_cart_count(expected_count)
        return self
