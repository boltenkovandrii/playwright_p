from components.prestashop.storefront.ProductGrid import ProductGrid
from pages.prestashop.storefront.CatalogPage import CatalogPage
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class HomePage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.carousel = page.locator("#carousel")
        self.featured_products = ProductGrid(page.locator(".featured-products"))

    def open(self):
        super().open()
        attach_screenshot(self.page, "Home page")
        return self

    def verify_loaded(self):
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

    def open_category(self, profile, name):
        self.header.click_category(profile, name)
        return CatalogPage(self.page).verify_loaded()