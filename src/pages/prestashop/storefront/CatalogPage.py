import re

from components.prestashop.storefront.ProductGrid import ProductGrid
from pages.prestashop.storefront.ProductPage import ProductPage
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot
from utils.responsive import BOOTSTRAP_MD


class CatalogPage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.product_grid = ProductGrid(page.locator("#js-product-list"))
        self.heading = page.locator("#js-product-list-header")
        self.subcategory_links = page.locator(".subcategory-name")
        self.active_filters = page.locator("#js-active-search-filters")
        # no price filters for mobile
        if self.page.viewport_size["width"] >= BOOTSTRAP_MD:
            self.price_facet = self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").first
            self.slider_track = self.price_facet.locator(".ui-slider").first
            slider_handles = self.price_facet.locator(".ui-slider-handle")
            self.price_slider_handle_left = slider_handles.nth(0)
            self.price_slider_handle_right = slider_handles.nth(1)
            self.price_slider_min = float(self.price_facet.get_attribute("data-slider-min"))
            self.price_slider_max = float(self.price_facet.get_attribute("data-slider-max"))

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
        attach_screenshot(self.page, "Opening product")
        self.product_grid.product_at(index).open_product()
        return ProductPage(self.page).verify_loaded()

    def verify_category_name(self, name):
        attach_screenshot(self.page, "Verifying category name")
        expect(self.heading).to_contain_text(re.compile(re.escape(name), re.IGNORECASE))
        return self

    def check_subcategories_list(self, *names):
        attach_screenshot(self.page, "Checking subcategories list")
        expect(self.subcategory_links).to_have_count(len(names))
        for name in names:
            expect(self.subcategory_links.filter(has_text=re.compile(rf"^\s*{re.escape(name)}\s*$"))).to_be_visible()
        return self

    def check_displayed_results_count(self, count):
        attach_screenshot(self.page, "Checking displayed results count")
        expect(self.product_grid.cards).to_have_count(count)
        return self

    def sort_by(self, criteria):
        attach_screenshot(self.page, f"Sorting by {criteria}")
        sort_link = self.page.locator(
            ".products-sort-order .dropdown-menu a",
            has_text=criteria,
        ).first
        self.page.goto(sort_link.get_attribute("href"))
        return CatalogPage(self.page).verify_loaded()

    def apply_price_filter(self, min_price, max_price):
        attach_screenshot(self.page, "Applying price filter")
        expect(self.price_facet).to_be_visible()
        self._drag_price_slider_handle(
            self.price_slider_handle_left,
            float(min_price),
        )
        self._drag_price_slider_handle(
            self.price_slider_handle_right,
            float(max_price),
        )
        expect(self.active_filters).to_contain_text(re.compile(r"price", re.IGNORECASE))
        return CatalogPage(self.page).verify_loaded()

    def apply_manufacturer_filter(self, name):
        attach_screenshot(self.page, f"Applying manufacturer filter: {name}")
        self._open_mobile_filters_if_needed()
        manufacturer_link = self.page.locator(
            "#search_filters .facet[data-name='Brand'] a",
            has_text=name,
        ).first
        expect(manufacturer_link).to_be_visible()
        manufacturer_link.click()
        self._close_mobile_filters_if_needed()
        return CatalogPage(self.page).verify_loaded()

    def verify_active_filter_contains(self, text):
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            attach_screenshot(self.page, "No active filters displayed for a narrow viewport")
            expect(self.active_filters).not_to_be_visible()
        else:
            attach_screenshot(self.page, "Checking active filters")
            expect(self.active_filters).to_be_visible()
            expect(self.active_filters).to_contain_text(re.compile(re.escape(text), re.IGNORECASE))
        return self

    def _drag_price_slider_handle(self, handle, target_value):
        track_box = self.price_facet.locator(".ui-slider").first.bounding_box()
        handle_box = handle.bounding_box()
        if not track_box or not handle_box:
            raise AssertionError("Price slider is not ready for interaction")

        bounded_target = max(self.price_slider_min, min(self.price_slider_max, target_value))
        ratio = (bounded_target - self.price_slider_min) / (self.price_slider_max - self.price_slider_min)
        target_x = track_box["x"] + ratio * track_box["width"]
        target_y = handle_box["y"] + (handle_box["height"] / 2)

        handle.hover()
        self.page.mouse.down()
        self.page.mouse.move(target_x, target_y, steps=12)
        self.page.mouse.up()

    def _open_mobile_filters_if_needed(self):
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            attach_screenshot(self.page, "Opening filters for mobile")
            self.page.get_by_test_id("search_filter_toggler").click()
            self.page.locator("#search_filters .facet[data-name='Brand']").click()

    def _close_mobile_filters_if_needed(self):
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            attach_screenshot(self.page, "Closing filters for mobile")
            self.page.locator("#search_filter_controls button").click()