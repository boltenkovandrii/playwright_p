from components.prestashop.common.Notification import Notification
from components.prestashop.storefront.Footer import Footer
from components.prestashop.storefront.Header import Header
from pages.BasePage import BasePage
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot
from utils.environment import get_env_variable
from utils.responsive import BOOTSTRAP_MD


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

    def verify_logged_in(self):
        return self.header.verify_logged_in()

    def verify_not_logged_in(self):
        return self.header.verify_not_logged_in()

    def get_account_name(self):
        return self.header.get_account_name()

    def check_structure(self):
        expect(self.content).to_be_visible()
        self.header.check_structure()
        self.notifications.check_structure()
        self.footer.check_structure()
        return self

    def search(self, query):
        from pages.prestashop.storefront.SearchResultsPage import SearchResultsPage

        attach_screenshot(self.page, f"Performing search by query: {query}")
        self.header.search(query)
        return SearchResultsPage(self.page).verify_loaded()

    def open_login_page(self):
        attach_screenshot(self.page, "Opening login page via account menu")
        self.header.open_login_page()
        from pages.prestashop.storefront.LoginPage import LoginPage
        return LoginPage(self.page).verify_loaded()

    def open_account_page(self):
        attach_screenshot(self.page, "Opening to account page")
        self.header.open_account_page()
        from pages.prestashop.storefront.AccountDashboardPage import AccountDashboardPage
        return AccountDashboardPage(self.page).verify_loaded()

    def sign_out(self):
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            return self.sign_out_with_footer_link()
        else:
            return self.sign_out_with_header_link()

    def sign_out_with_header_link(self):
        attach_screenshot(self.page, "Signing out with header link")
        if self.page.viewport_size["width"] < BOOTSTRAP_MD:
            raise ValueError("Signing out with header link is not possible for the current screen width. Use footer menu instead.")
        self.header.sign_out()
        # could be redirected to various pages, so returning generic object
        return BaseStorefrontPage(self.page)

    def sign_out_with_footer_link(self):
        attach_screenshot(self.page, "Signing out with footer link")
        self.footer.sign_out()
        # could be redirected to various pages, so returning generic object
        return BaseStorefrontPage(self.page)

    def as_home_page(self):
        # Lazy import to avoid circular import from page
        from pages.prestashop.storefront.HomePage import HomePage
        return HomePage(self.page).verify_loaded()

    def as_login_page(self):
        # Lazy import to avoid circular import from page
        from pages.prestashop.storefront.LoginPage import LoginPage
        return LoginPage(self.page).verify_loaded()
