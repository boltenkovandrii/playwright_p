from components.prestashop.storefront.ProductGrid import ProductGrid
from pages.prestashop.storefront.CatalogPage import CatalogPage
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from pages.prestashop.storefront.ProductPage import ProductPage
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class HomePage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.carousel = page.locator("#carousel")
        self.featured_products = ProductGrid(page.locator(".featured-products"))

    def open(self, path=""):
        super().open()
#        attach_screenshot(self.page, "Home page")
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

    def open_category(self, profile, name):
        self.header.click_category(profile, name)
        return CatalogPage(self.page).verify_loaded()

    def open_featured_product(self, index=0):
        self.featured_products.product_at(index).open_product()
        return ProductPage(self.page).verify_loaded()

    def get_featured_product_name(self, index=0):
        return self.featured_products.product_at(index).get_name()

    def open_featured_product_by_name(self, name):
        self.featured_products.open_product_by_name(name)
        return ProductPage(self.page).verify_loaded()
