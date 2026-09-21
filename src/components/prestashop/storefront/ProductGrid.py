from components.prestashop.storefront.ProductCard import ProductCard
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class ProductGrid:
    def __init__(self, parent):
        self.container = parent.locator(".products.row")
        self.cards = self.container.locator(".product-miniature")

    def verify_loaded(self):
        expect(self.container).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.container, "Checking product grid structure", False)
        expect(self.container).to_be_visible()
        expect(self.cards.first).to_be_visible()
        self.product_at(0).check_structure()
        return self

    def product_at(self, index):
        return ProductCard(self.cards.nth(index))

    def get_names(self):
        return [self.product_at(index).get_name() for index in range(self.cards.count())]

    def get_prices(self):
        return [self.product_at(index).get_price() for index in range(self.cards.count())]

    def open_product_by_name(self, name):
        ProductCard(self.cards.filter(has_text=name)).open_product()
