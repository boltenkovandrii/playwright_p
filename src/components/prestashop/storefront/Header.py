from playwright.sync_api import expect

from resources.translations import UI_TEXT
from tests.config.profiles import is_phone
from utils.allure_reporting import attach_screenshot
from utils.responsive import BOOTSTRAP_MD
from utils.snapshots import load_snapshot

class Header:
    def __init__(self, page):
        self.page = page
        self.container = page.locator("#header")
        self.desktop_language_selector = page.locator("#_desktop_language_selector button")
        self.mobile_language_selector = page.locator("#_mobile_language_selector select")
        self.menu_button = page.locator("#menu-icon")
        self.mobile_menu = page.locator("#mobile_top_menu_wrapper")
        self.search_input = self.container.locator("#search_widget input[type='text']")
        self.desktop_cart = page.locator("#_desktop_cart")
        self.mobile_cart = page.locator("#_mobile_cart")
        self.desktop_cart_products_count = self.desktop_cart.locator(".cart-products-count")
        self.mobile_cart_products_count = self.mobile_cart.locator(".cart-products-count")
        self.account_link = self.page.locator(".account")
        self.desktop_user_info = page.locator("#_desktop_user_info")
        self.mobile_user_info = page.locator("#_mobile_user_info")

    def verify_loaded(self):
        expect(self.container).to_be_visible()
        return self

    def verify_current_language(self, locale):
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            self.open_mobile_menu()
            expect(self.mobile_language_selector).to_contain_text(UI_TEXT[locale]["language"])
            self.close_mobile_menu()
        else:
            expect(self.desktop_language_selector).to_contain_text(UI_TEXT[locale]["language"])
        return self

    def verify_search_placeholder(self, locale):
        expect(self.search_input).to_have_attribute("placeholder", UI_TEXT[locale]["search_placeholder"])
        return self

    def select_language(self, current_locale, target_locale):
        if current_locale == target_locale:
            return self

        attach_screenshot(self.page, f"Selecting storefront language: {target_locale}")
        target_language = UI_TEXT[target_locale]["language"]

        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            self.open_mobile_menu()
            with self.page.expect_navigation(wait_until="domcontentloaded"):
                self.mobile_language_selector.select_option(label=target_language)
        else:
            self.desktop_language_selector.click()
            with self.page.expect_navigation(wait_until="domcontentloaded"):
                self.page.get_by_role("link", name=target_language, exact=True).click()

        return self

    def check_structure(self, locale="en"):
        attach_screenshot(self.container, "Checking header structure", False)
        expect(self.container).to_be_visible()
        expect(self.search_input).to_be_visible()

        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            expect(self.menu_button).to_be_visible()
            expect(self.mobile_cart).to_be_visible()
            expect(self.desktop_cart).not_to_be_visible()
            expect(self.desktop_language_selector).not_to_be_visible()
        else:
            expect(self.menu_button).not_to_be_visible()
            expect(self.mobile_cart).not_to_be_visible()
            expect(self.desktop_cart).to_be_visible()
            expect(self.desktop_language_selector).to_be_visible()

        # Not the best check - will break on adding categories, ignores many elements hard to verify.
        # Probably direct checks of the elements would be better. Left as is to demonstrate usage of snapshots
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            snapshot_name = "header_compact"
        else:
            snapshot_name = "header"
        expect(self.container).to_match_aria_snapshot(
            load_snapshot(snapshot_name, locale=locale, namespace="prestashop")
        )


    def _active_language_selector(self):
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            return self.page.locator("#_mobile_language_selector, #language_selector, .language-selector")
        return self.page.locator("#_desktop_language_selector, #language_selector, .language-selector")

    def _language_selector_toggle(self):
        return self._active_language_selector().locator(".expand-more, .dropdown-toggle, button, a, .current").first

    def open_mobile_menu(self):
        self.menu_button.click()
        expect(self.mobile_menu).to_be_visible()
        return self

    def close_mobile_menu(self):
        self.menu_button.click()
        expect(self.mobile_menu).not_to_be_visible()
        return self

    def click_category(self ,profile,  name):
        if is_phone(profile):
            self.open_mobile_menu()
            category_links = self.page.locator(
                "#mobile_top_menu_wrapper .category > a"
            )
        else:
            category_links = self.page.locator("#top-menu .category > a")

        category_links.filter(has_text=name).first.click()
        return self

    def click_cart(self):
        self.desktop_cart.locator("a").click()
        return self

    def verify_cart_count(self, expected_count):
        expected_text = f"({expected_count})"

        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            cart_products_count = self.mobile_cart_products_count
        else:
            cart_products_count = self.desktop_cart_products_count

        expect(cart_products_count).to_be_visible()
        expect(cart_products_count).to_have_text(expected_text)
        return self

    def search(self, query):
        self.search_input.fill(query)
        self.search_input.press("Enter")
        return self

    def open_account_page(self):
        self._active_user_info().locator(".account").click()
        return self

    def verify_logged_in(self):
        expect(self._active_user_info().locator(".account")).to_be_visible()
        return self

    def verify_not_logged_in(self):
        expect(self._active_user_info().locator(".account")).not_to_be_visible()
        return self

    def get_account_name(self):
        return self._active_user_info().locator(".account span").text_content().strip()

    def open_login_page(self):
        self._active_user_info().locator("a").first.click()
        return self

    def sign_out(self):
        self._active_user_info().locator(".logout").click()
        return self

    def _active_user_info(self):
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            return self.mobile_user_info
        return self.desktop_user_info
