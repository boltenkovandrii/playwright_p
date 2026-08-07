import re

from components.prestashop.storefront.ProductGrid import ProductGrid
from pages.prestashop.storefront.ProductPage import ProductPage
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class CatalogPage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.product_grid = ProductGrid(page.locator("#js-product-list"))
        self.heading = page.locator("#js-product-list-header")
        self.subcategory_links = page.locator(".subcategory-name")

    def verify_loaded(self):
        attach_screenshot(self.page, "Catalog page")
        super().verify_loaded()
        expect(self.heading).to_be_visible()
        self.product_grid.verify_loaded()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking catalog page structure")
        super().check_structure()
        expect(self.heading).to_be_visible()
        self.product_grid.check_structure()
        return self

    def open_product(self, index):
        self.product_grid.product_at(index).open_product()
        return ProductPage(self.page).verify_loaded()

    def verify_category_name(self, name):
        expect(self.heading).to_contain_text(re.compile(re.escape(name), re.IGNORECASE))
        return self

    def verify_has_subcategories(self, *names):
        for name in names:
            exact = re.compile(r'^\s*' + re.escape(name) + r'\s*$', re.IGNORECASE)
            expect(self.subcategory_links.filter(has_text=exact)).to_be_visible()
        return self

    def get_displayed_results_count(self):
        return self.product_grid.cards.count()
