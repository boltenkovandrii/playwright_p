from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot
from utils.snapshots import load_snapshot


class Footer:
    def __init__(self, page):
        self.page = page
        self.container = page.locator("#footer")

    def verify_loaded(self):
        expect(self.container).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.container, "Checking footer structure")
        snapshot_name = (
            "footer_mobile"
            if self.page.locator("#menu-icon").is_visible()
            else "footer"
        )
        expect(self.container).to_match_aria_snapshot(
            load_snapshot(snapshot_name, namespace="prestashop")
        )
        return self
