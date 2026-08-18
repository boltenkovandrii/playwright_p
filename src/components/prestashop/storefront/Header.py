from playwright.sync_api import expect

from tests.config.profiles import is_phone
from utils.allure_reporting import attach_screenshot
from utils.responsive import BOOTSTRAP_MD
from utils.snapshots import load_snapshot

class Header:
    def __init__(self, page):
        self.page = page
        self.container = page.locator("#header")
        self.menu_button = page.locator("#menu-icon")
        self.mobile_menu = page.locator("#mobile_top_menu_wrapper")
        self.search_input = page.locator("#search_widget input[type='text']")
        self.desktop_cart = page.locator("#_desktop_cart")
        self.mobile_cart = page.locator("#_mobile_cart")
        self.cart_products_count = page.locator(".modal-content .cart-products-count")

    def verify_loaded(self):
        expect(self.container).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.container, "Checking header structure", False)
        expect(self.container).to_be_visible()
        expect(self.search_input).to_be_visible()

        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            expect(self.menu_button).to_be_visible()
            expect(self.mobile_cart).to_be_visible()
            expect(self.desktop_cart).not_to_be_visible()
        else:
            expect(self.menu_button).not_to_be_visible()
            expect(self.mobile_cart).not_to_be_visible()
            expect(self.desktop_cart).to_be_visible()

        # Not the best check - will break on adding categories, ignores many elements hard to verify. TODO: probably should be replaced with direct checks - will do later.
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            snapshot_name = "header_compact"
        else:
            snapshot_name = "header"
        expect(self.container).to_match_aria_snapshot(
            load_snapshot(snapshot_name, namespace="prestashop")
        )

        return self

    def open_mobile_menu(self):
        self.menu_button.click()
        expect(self.mobile_menu).to_be_visible()
        return self

    def click_category(self ,profile,  name):
        if is_phone(profile):
            self.open_mobile_menu()
            category_links = self.page.locator(
                "#mobile_top_menu_wrapper .category > a"
            )
        else:
            category_links = self.page.locator("#top-menu .category > a")

        with self.page.expect_navigation(wait_until="domcontentloaded"):
            category_links.filter(has_text=name).first.click()
        return self

    def click_cart(self):
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            self.desktop_cart.locator("a").click()
        return self

    def verify_cart_count(self, expected_count):
        expect(self.cart_products_count).to_be_visible()
        expect(self.cart_products_count).to_contain_text(str(expected_count))
        return self

    def search(self, query):
        self.search_input.fill(query)
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            self.search_input.press("Enter")
        return self