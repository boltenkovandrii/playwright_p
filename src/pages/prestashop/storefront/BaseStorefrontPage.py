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
    ).rstrip("/")

    def __init__(self, page, locale="en"):
        super().__init__(page)
        self.locale = locale
        self.header = Header(page)
        self.footer = Footer(page, locale)
        self.content = page.locator("#main")

    def _localized_url(self, path="", locale=None):
        if locale is None:
            locale = self.locale
        normalized_path = path.lstrip("/")
        suffix = f"{normalized_path}" if normalized_path else ""
        return f"{self.BASE_URL}/{locale}/{suffix}"

    def open(self, path=""):
        self.page.goto(self._localized_url(path))
        self.verify_loaded()
        return self

    def verify_loaded(self):
        expect(self.content).to_be_visible()
        self.header.verify_loaded()
        self.header.verify_current_language(self.locale)
        return self

    def verify_current_language(self, locale):
        self.header.verify_current_language(locale)
        return self

    def verify_search_placeholder(self):
        self.header.verify_search_placeholder(self.locale)
        return self

    def switch_language(self, locale):
        attach_screenshot(self.page, f"Switching storefront language to: {locale}")
        self.header.select_language(self.locale, locale)
        return self.__class__(self.page, locale).verify_loaded()

    def verify_logged_in(self):
        return self.header.verify_logged_in()

    def verify_not_logged_in(self):
        return self.header.verify_not_logged_in()

    def get_account_name(self):
        return self.header.get_account_name()

    def check_structure(self):
        expect(self.content).to_be_visible()
        self.header.check_structure(self.locale)
        self.header.verify_current_language(self.locale)
        self.footer.check_structure(self.locale)
        return self

    def search(self, query):
        from pages.prestashop.storefront.SearchResultsPage import SearchResultsPage

        attach_screenshot(self.page, f"Performing search by query: {query}")
        self.header.search(query)
        return SearchResultsPage(self.page, self.locale).verify_loaded()

    def open_login_page(self):
        attach_screenshot(self.page, "Opening login page via account menu")
        self.header.open_login_page()
        from pages.prestashop.storefront.LoginPage import LoginPage
        return LoginPage(self.page, self.locale).verify_loaded()

    def open_account_page(self):
        attach_screenshot(self.page, "Opening to account page")
        self.header.open_account_page()
        from pages.prestashop.storefront.AccountDashboardPage import AccountDashboardPage
        return AccountDashboardPage(self.page, self.locale).verify_loaded()

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
        return BaseStorefrontPage(self.page, self.locale).verify_loaded()

    def sign_out_with_footer_link(self):
        attach_screenshot(self.page, "Signing out with footer link")
        self.footer.sign_out()
        # could be redirected to various pages, so returning generic object
        return BaseStorefrontPage(self.page, self.locale).verify_loaded()

    def navigate_to_account_dashboard_directly(self):
        """Navigate directly to the account dashboard URL to test redirect behavior for unauthenticated users."""
        self.page.goto(self._localized_url("my-account"))
        return BaseStorefrontPage(self.page, self.locale).verify_loaded()

    def as_home_page(self, locale=None):
        # Lazy import to avoid circular import from page
        from pages.prestashop.storefront.HomePage import HomePage
        if locale is None:
            locale = self.locale
        return HomePage(self.page, locale).verify_loaded()

    def as_login_page(self, locale=None):
        # Lazy import to avoid circular import from page
        from pages.prestashop.storefront.LoginPage import LoginPage
        if locale is None:
            locale = self.locale
        return LoginPage(self.page, locale).verify_loaded()

    def as_registration_page(self, locale=None):
        # Lazy import to avoid circular import from page
        from pages.prestashop.storefront.RegistrationPage import RegistrationPage
        if locale is None:
            locale = self.locale
        return RegistrationPage(self.page, locale).verify_loaded()
