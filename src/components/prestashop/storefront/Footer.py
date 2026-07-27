from playwright.sync_api import expect

from tests.config.profiles import is_desktop, is_tablet
from utils.allure_reporting import attach_screenshot
from utils.snapshots import load_snapshot


class Footer:
    def __init__(self, page):
        self.page = page
        self.container = page.locator("#footer")

    def verify_loaded(self):
        expect(self.container).to_be_visible()
        return self

    def check_structure(self, profile):
        attach_screenshot(self.container, "Checking footer structure")
        if is_desktop(profile) or is_tablet(profile):
            snapshot_name = "footer"
        else:
            snapshot_name = "footer_phone"
        expect(self.container).to_match_aria_snapshot(
            load_snapshot(snapshot_name, namespace="prestashop")
        )
        return self
