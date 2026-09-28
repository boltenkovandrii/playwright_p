from __future__ import annotations

from typing import Self

from playwright.sync_api import Locator, expect

from components.prestashop.storefront.ProductCard import ProductCard
from utils.allure_reporting import attach_screenshot


class ProductGrid:
    def __init__(self, parent: Locator) -> None:
        self.container = parent.locator(".products.row")
        self.cards = self.container.locator(".product-miniature")

    def verify_loaded(self) -> Self:
        expect(self.container).to_be_visible()
        return self

    def check_structure(self) -> Self:
        attach_screenshot(self.container, "Checking product grid structure", False)
        expect(self.container).to_be_visible()
        expect(self.cards.first).to_be_visible()
        self.product_at(0).check_structure()
        return self

    def product_at(self, index: int) -> ProductCard:
        return ProductCard(self.cards.nth(index))

    def get_names(self) -> list[str]:
        return [self.product_at(index).get_name() for index in range(self.cards.count())]

    def get_prices(self) -> list[float]:
        return [self.product_at(index).get_price() for index in range(self.cards.count())]

    def open_product_by_name(self, name: str) -> None:
        ProductCard(self.cards.filter(has_text=name).first).open_product()
