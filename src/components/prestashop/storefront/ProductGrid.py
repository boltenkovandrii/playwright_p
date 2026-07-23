from components.prestashop.storefront.ProductCard import ProductCard
from playwright.sync_api import expect


class ProductGrid:
    def __init__(self, parent):
        self.container = parent.locator(".products.row")
        self.cards = self.container.locator(".product-miniature")

    def verify_loaded(self):
        expect(self.container).to_be_visible()
        return self

    def product_at(self, index):
        return ProductCard(self.cards.nth(index))
