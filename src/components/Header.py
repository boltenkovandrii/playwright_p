from resources.translations import TRANSLATIONS
from utils.allure_reporting import attach_screenshot
from playwright.sync_api import expect

from utils.snapshots import load_snapshot


class Header:

    def __init__(self, page, parent, locale="en"):
        self.page = page
        self.parent = parent
        self.locale = locale
        self.component = parent.get_by_role("banner")


    @property
    def search_input(self):
        return self.component.get_by_role("searchbox")

    @property
    def search_button(self):
        return self.component.get_by_role("button", name=TRANSLATIONS[self.locale]["search_button"])


    def search(self, text):
        attach_screenshot(self.page, "Before search")
        self.search_input.fill(text)
        self.search_button.click()
        attach_screenshot(self.page, "Search performed")


    def check_structure(self):
        # using snapshots is not the best idea here, actually. Only added to demonstrate how does it work. Other components use another approach
        attach_screenshot(self.component, "Checking structure: Header:")
        expect(self.component).to_match_aria_snapshot(
            load_snapshot("header", self.locale)
        )
