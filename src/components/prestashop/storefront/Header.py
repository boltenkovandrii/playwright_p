from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class Header:
    def __init__(self, page):
        self.page = page
        self.container = page.locator("#header")
        self.menu_button = page.locator("#menu-icon")
        self.mobile_menu = page.locator("#mobile_top_menu_wrapper")
        self.search_input = page.locator("#search_widget input[type='text']")
        self.desktop_cart = page.locator("#_desktop_cart")
        self.mobile_cart = page.locator("#_mobile_cart")

    def verify_loaded(self):
        expect(self.container).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.container, "Checking header structure")
        expect(self.container).to_be_visible()
        expect(self.search_input).to_be_visible()
        expect(self.menu_button).to_be_attached()
        expect(self.desktop_cart).to_be_attached()
        expect(self.mobile_cart).to_be_attached()
        return self

    def open_mobile_menu(self):
        self.menu_button.click()
        expect(self.mobile_menu).to_be_visible()
        return self

    def search(self, query):
        self.search_input.fill(query)
        self.search_input.press("Enter")
        return self

    def open_category(self, name):
        category_links = self.page.locator("#top-menu .category > a")
        if not category_links.first.is_visible():
            self.open_mobile_menu()
            category_links = self.page.locator(
                "#mobile_top_menu_wrapper .category > a"
            )

        with self.page.expect_navigation(wait_until="domcontentloaded"):
            category_links.filter(has_text=name).first.click()
        return self

    def open_cart(self):
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            self.desktop_cart.locator("a").click()
        return self
