from playwright.sync_api import expect

from components.Appearance import Appearance
from utils.allure_reporting import attach_screenshot


class ContentMain:

    def __init__(self, page, parent, locale="en"):
        self.page = page
        self.parent = parent
        self.locale = locale
        self.container = self.parent.get_by_test_id("content")
        self.left_navigation = self.parent.get_by_test_id("left-navigation")
        self.right_navigation = self.parent.get_by_test_id("right-navigation")
        self.body_content = self.parent.get_by_test_id("bodyContent")
        self.appearance = Appearance(page, self.container, locale)

    def check_structure(self):
        attach_screenshot(self.container, "Checking structure: ContentMain:")
        expect(self.container).to_be_visible()
        expect(self.left_navigation).to_be_visible()
        expect(self.right_navigation).to_be_visible()
        expect(self.body_content).to_be_visible()
        self.appearance.check_structure()

    def get_text_size(self):
        return self.container.get_by_test_id("bodyContent").evaluate(
            "el => getComputedStyle(el).fontSize"
        )