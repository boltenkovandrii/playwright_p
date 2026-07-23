from components.prestashop.storefront.ProductGrid import ProductGrid
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect


class HomePage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.carousel = page.locator("#carousel")
        self.featured_products = ProductGrid(page.locator(".featured-products"))

    def open(self):
        return super().open()

    def verify_loaded(self):
        super().verify_loaded()
        expect(self.carousel).to_be_visible()
        self.featured_products.verify_loaded()
        return self
