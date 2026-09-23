from playwright.sync_api import expect

from resources.translations import UI_TEXT
from utils.allure_reporting import attach_screenshot
from utils.responsive import BOOTSTRAP_MD
from utils.snapshots import load_snapshot


class Footer:
    def __init__(self, page, locale="en"):
        self.page = page
        self.locale = locale
        self.container = page.get_by_test_id("footer")
        self.account_infos = self.page.get_by_test_id("block_myaccount_infos")
        self.sign_out_link = self.account_infos.get_by_role("link", name=UI_TEXT[self.locale]["sign_out_link"])

    def verify_loaded(self):
        expect(self.container).to_be_visible()
        return self

    def check_structure(self, locale="en"):
        attach_screenshot(self.container, "Checking footer structure", False)
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            snapshot_name = "footer_compact"
        else:
            snapshot_name = "footer"
        # Actual links in the footer could depend on the fact if user is logged in. So snapshots perform only partial (but still substantial) assertion to not make it overcomplicated.
        expect(self.container).to_match_aria_snapshot(
            load_snapshot(snapshot_name, locale=locale, namespace="prestashop")
        )
        return self

    def sign_out(self):
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            self.account_infos.click()
        self.sign_out_link.click()
        return self