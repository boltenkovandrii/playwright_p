from playwright.sync_api import expect

from pages.BasePage import BasePage
from utils.environment import get_env_variable


class BaseBackofficePage(BasePage):
    BASE_URL = (
        get_env_variable(
            "PRESTASHOP_BASE_URL",
            "http://localhost:8090",
        )
        + "/admin-dev/"
    )

    def open(self, path=""):
        self.page.goto(f"{self.BASE_URL}{path}")
        return self

    def verify_loaded(self):
        expect(self.page.locator("body")).to_be_visible()
        return self
