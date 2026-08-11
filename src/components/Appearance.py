from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class Appearance:

    def __init__(self, page, parent, locale="en"):
        self.page = page
        self.parent = parent
        self.locale = locale
        self.container = self.parent.get_by_test_id("vector-appearance-pinned-container")


    @property
    def text_size_selector(self):
        return self.container.get_by_test_id("skin-client-prefs-vector-feature-custom-font-size")

    @property
    def width_selector(self):
        return self.container.get_by_test_id("skin-client-prefs-vector-feature-limited-width")

    @property
    def theme_selector(self):
        return self.container.get_by_test_id("skin-client-prefs-skin-theme")


    def check_structure(self):
        attach_screenshot(self.container, "Checking structure: Appearance:", False)
        expect(self.container).to_be_visible()
        expect(self.text_size_selector).to_be_visible()
        expect(self.width_selector).to_be_visible()
        expect(self.theme_selector).to_be_visible()


    def set_small_text_size(self):
        attach_screenshot(self.container, "Selecting text size", False)
        self.text_size_selector.locator("input").nth(0).click()

    def set_standard_text_size(self):
        attach_screenshot(self.container, "Selecting text size", False)
        self.text_size_selector.locator("input").nth(1).click()

    def set_large_text_size(self):
        attach_screenshot(self.container, "Selecting text size", False)
        self.text_size_selector.locator("input").nth(2).click()
