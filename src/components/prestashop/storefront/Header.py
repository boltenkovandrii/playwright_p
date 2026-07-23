from playwright.sync_api import expect


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

    def open_mobile_menu(self):
        self.menu_button.click()
        expect(self.mobile_menu).to_be_visible()
        return self

    def search(self, query):
        self.search_input.fill(query)
        self.search_input.press("Enter")
        return self
