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
        self.active_filters = page.locator("#js-active-search-filters")

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

    def check_subcategories_list(self, *names):
        expect(self.subcategory_links).to_have_count(len(names))
        for name in names:
            expect(self.subcategory_links.filter(has_text=re.compile(rf"^\s*{re.escape(name)}\s*$"))).to_be_visible()
        return self

    def check_displayed_results_count(self, count):
        expect(self.product_grid.cards).to_have_count(count)
        return self

    def sort_by(self, criteria):
        sort_link = self.page.locator(
            ".products-sort-order .dropdown-menu a",
            has_text=criteria,
        ).first
        self.page.goto(sort_link.get_attribute("href"))
        return CatalogPage(self.page).verify_loaded()

    def apply_price_filter(self, min_price, max_price):
        price_facet = self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").first
        slider_track = price_facet.locator(".ui-slider").first
        slider_handles = price_facet.locator(".ui-slider-handle")

        expect(price_facet).to_be_visible()

        slider_min = float(price_facet.get_attribute("data-slider-min"))
        slider_max = float(price_facet.get_attribute("data-slider-max"))

        self._drag_price_slider_handle(
            slider_handles.first,
            slider_track,
            slider_min,
            slider_max,
            float(min_price),
        )
        self._drag_price_slider_handle(
            slider_handles.nth(1),
            slider_track,
            slider_min,
            slider_max,
            float(max_price),
        )

        expect(self.active_filters).to_contain_text(re.compile(r"price", re.IGNORECASE))
        return CatalogPage(self.page).verify_loaded()

    def apply_manufacturer_filter(self, name):
        manufacturer_link = self.page.locator(
            "#search_filters .facet[data-name='Brand'] a.js-search-link",
            has_text=name,
        ).first
        expect(manufacturer_link).to_be_visible()
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            manufacturer_link.click()
        return CatalogPage(self.page).verify_loaded()

    def verify_active_filter_contains(self, text):
        expect(self.active_filters).to_be_visible()
        expect(self.active_filters).to_contain_text(re.compile(re.escape(text), re.IGNORECASE))
        return self

    def _drag_price_slider_handle(self, handle, slider_track, slider_min, slider_max, target_value):
        track_box = slider_track.bounding_box()
        handle_box = handle.bounding_box()
        if not track_box or not handle_box:
            raise AssertionError("Price slider is not ready for interaction")

        bounded_target = max(slider_min, min(slider_max, target_value))
        ratio = (bounded_target - slider_min) / (slider_max - slider_min)
        target_x = track_box["x"] + ratio * track_box["width"]
        target_y = handle_box["y"] + (handle_box["height"] / 2)

        handle.hover()
        self.page.mouse.down()
        self.page.mouse.move(target_x, target_y, steps=12)
        self.page.mouse.up()

