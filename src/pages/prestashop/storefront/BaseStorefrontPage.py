from components.prestashop.common.Notification import Notification
from components.prestashop.storefront.Footer import Footer
from components.prestashop.storefront.Header import Header
from pages.BasePage import BasePage
from playwright.sync_api import expect

from utils.environment import get_env_variable


class BaseStorefrontPage(BasePage):
    BASE_URL = get_env_variable(
        "PRESTASHOP_BASE_URL",
        "http://localhost:8090",
    ) + "/en/"

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)
        self.footer = Footer(page)
        self.notifications = Notification(page)
        self.content = page.locator("#main")

    def open(self, path=""):
        self.page.goto(f"{self.BASE_URL}{path}")
        self.verify_loaded()
        return self

    def verify_loaded(self):
        expect(self.content).to_be_visible()
        self.header.verify_loaded()
        self.notifications.verify_loaded()
        return self

    def check_structure(self, profile):
        expect(self.content).to_be_visible()
        self.header.check_structure()
        self.notifications.check_structure()
        self.footer.check_structure(profile)
        return self
