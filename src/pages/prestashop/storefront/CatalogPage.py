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

    def open_product_by_name(self, name):
        attach_screenshot(self.page, f"Opening product by name: {name}")
        self.product_grid.open_product_by_name(name)
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
        sort_link = self.page.locator(".products-sort-order .dropdown-menu a", has_text=criteria)
        self.page.goto(sort_link.get_attribute("href"))
        return CatalogPage(self.page).verify_loaded()

    def apply_manufacturer_filter(self, name):
        attach_screenshot(self.page, f"Applying manufacturer filter: {name}")
        self._open_mobile_filters_if_needed("Brand")
        manufacturer_link = self.page.locator(".facet[data-name='Brand'] a", has_text=name)
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

    def apply_price_filter(self, min_price, max_price):
        attach_screenshot(self.page, "Applying price filter")
        self._open_mobile_filters_if_needed("Price")

        self._drag_price_slider_handle(0, float(min_price))
        # Applying the filter triggers an AJAX update/re-render.
        self._wait_for_price_slider_value(0, min_price)

        self._drag_price_slider_handle(1, float(max_price))
        # Applying the filter triggers an AJAX update/re-render.
        self._wait_for_price_slider_value(1, max_price)

        self._close_mobile_filters_if_needed()

        expect(self.active_filters).to_contain_text(re.compile(r"price", re.IGNORECASE))
        return CatalogPage(self.page).verify_loaded()

    def _drag_price_slider_handle(self, handle_index, target_value):
        price_facet = self.page.locator(".faceted-slider[data-slider-label='Price']")

        slider_track = price_facet.locator(".ui-slider")
        handle = price_facet.locator(".ui-slider-handle").nth(handle_index)
        expect(handle).to_be_visible()

        price_slider_min = float(price_facet.get_attribute("data-slider-min"))
        price_slider_max = float(price_facet.get_attribute("data-slider-max"))

        track_box = slider_track.bounding_box()
        handle_box = handle.bounding_box()
        if not track_box or not handle_box:
            raise AssertionError(f"Price slider is not ready for interaction. Track_box: {track_box}, handle_box: {handle_box}.")

        bounded_target = max(price_slider_min, min(price_slider_max, target_value))
        ratio = (bounded_target - price_slider_min) / (price_slider_max - price_slider_min)
        target_x = track_box["x"] + ratio * track_box["width"]
        target_y = handle_box["y"] + (handle_box["height"] / 2)
        handle.hover()
        self.page.mouse.down()
        self.page.mouse.move(target_x, target_y, steps=12)
        self.page.mouse.up()

    def _wait_for_price_slider_value(self, handle_index, expected_value):
        selector = ".faceted-slider[data-slider-label='Price']"

        self.page.wait_for_function(
            """
            ([selector, index, expected]) => {
                const facet = document.querySelector(selector);

                if (!facet) {
                    return false;
                }

                const value = facet.getAttribute("data-slider-values");

                if (!value) {
                    return false;
                }

                try {
                    const values = JSON.parse(value);
                    return values[index] === String(expected);
                } catch {
                    return false;
                }
            }
            """,
            arg=[selector, handle_index, expected_value],
        )

    def _open_mobile_filters_if_needed(self, filter_name):
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            attach_screenshot(self.page, "Opening filters for mobile")
            self.page.get_by_test_id("search_filter_toggler").click()
            self.page.locator(f".facet[data-name='{filter_name}']").click()

    def _close_mobile_filters_if_needed(self):
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            attach_screenshot(self.page, "Closing filters for mobile")
            self.page.locator("#search_filter_controls button").click()


    '''
    TODO: remove after new implementation is proved to be stable
    
        def apply_price_filter(self, min_price, max_price):
        attach_screenshot(self.page, "Applying price filter")
        self._open_mobile_filters_if_needed("Price")

        self._drag_price_slider_handle(0, float(min_price))
        print ("#####1" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))

        # The first drag may trigger an AJAX update/re-render.
        self._drag_price_slider_handle(1, float(max_price))
        print ("#####2" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))

        self._close_mobile_filters_if_needed()

        expect(self.active_filters).to_contain_text(re.compile(r"price", re.IGNORECASE))
        return CatalogPage(self.page).verify_loaded()
    
    def _drag_price_slider_handle(self, handle_index, target_value):
        print ("!!!!!!1" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))
        price_facet = self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']")
        self._wait_for_price_slider_interactable(price_facet)
        print ("!!!!!!2" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))

        slider_track = price_facet.locator(".ui-slider")
        handle = price_facet.locator(".ui-slider-handle").nth(handle_index)
        print ("!!!!!!3" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))
        expect(handle).to_be_visible()
        print ("!!!!!!4" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))


        price_slider_min = float(price_facet.get_attribute("data-slider-min"))
        price_slider_max = float(price_facet.get_attribute("data-slider-max"))
        print ("!!!!!!5" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))

        track_box = slider_track.bounding_box()
        handle_box = handle.bounding_box()
        print ("!!!!!!6" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))
        if not track_box or not handle_box:
            # The facet can be briefly visible while its slider is still re-rendering after AJAX updates.
            self._wait_for_price_slider_interactable(price_facet)
            track_box = slider_track.bounding_box()
            handle_box = handle.bounding_box()
        print ("!!!!!!7" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))
        if not track_box or not handle_box:
            raise AssertionError(f"Price slider is not ready for interaction. Track_box: {track_box}, handle_box: {handle_box}.")

        print ("!!!!!!8" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))

        bounded_target = max(price_slider_min, min(price_slider_max, target_value))
        ratio = (bounded_target - price_slider_min) / (price_slider_max - price_slider_min)
        target_x = track_box["x"] + ratio * track_box["width"]
        target_y = handle_box["y"] + (handle_box["height"] / 2)
        print ("!!!!!!9" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))
        handle.hover()
        self.page.mouse.down()
        self.page.mouse.move(target_x, target_y, steps=12)
        print ("#####" + self.page.locator("#search_filters .faceted-slider[data-slider-label='Price']").get_attribute("data-slider-values"))
        self.page.mouse.up()
    
    
        def _wait_for_price_slider_interactable(self, price_facet):
        expect(price_facet).to_be_visible()
        # we may need more time for the slider to be fully interactive after AJAX updates, so we wait for the handles to be visible
        expect(price_facet.locator(".ui-slider")).to_be_visible(timeout=10_000)
        expect(price_facet.locator(".ui-slider-handle").nth(0)).to_be_visible(timeout=10_000)
        expect(price_facet.locator(".ui-slider-handle").nth(1)).to_be_visible(timeout=10_000)
    '''