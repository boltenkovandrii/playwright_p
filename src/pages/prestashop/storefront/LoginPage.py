import re

from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from resources.translations import UI_TEXT
from pages.prestashop.storefront.HomePage import HomePage
from utils.allure_reporting import attach_screenshot


class LoginPage(BaseStorefrontPage):
    def __init__(self, page, locale="en"):
        super().__init__(page, locale)
        self.heading = page.get_by_role("heading", name=UI_TEXT[self.locale]["login_heading"])
        self.email_input = page.get_by_test_id("field-email")
        self.password_input = page.get_by_test_id("field-password")
        self.submit_button = page.get_by_role("button", name=UI_TEXT[self.locale]["sign_in_link"])
        self.register_link = page.get_by_role("link", name=UI_TEXT[self.locale]["register_link"])
        self.login_error_message = page.locator(".login-form .alert-danger")

    def open(self, path="login"):
        super().open(path)
        return self

    def verify_loaded(self):
        attach_screenshot(self.page, "Login page")
        super().verify_loaded()
        expect(self.heading).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking login page structure")
        super().check_structure()
        expect(self.heading).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.submit_button).to_be_visible()
        expect(self.register_link).to_be_visible()
        return self

    def open_registration_page(self):
        attach_screenshot(self.page, "Navigating to registration page")
        self.register_link.click()
        from pages.prestashop.storefront.RegistrationPage import RegistrationPage
        return RegistrationPage(self.page, self.locale).verify_loaded()

    def login(self, email, password):
        attach_screenshot(self.page, f"Logging in as {email}")
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
        return HomePage(self.page, self.locale).verify_loaded()

    def login_with_invalid(self, email, password):
        attach_screenshot(self.page, f"Submitting login with email: {email}")
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
        return self

    def verify_email_error(self):
        # Don't check error message itself - it is browser-dependent and de-facto is not prestashop functionality
        expect(self.email_input).to_have_js_property("validity.valid", False)
        return self

    def verify_password_error(self):
        # Don't check error message itself - it is browser-dependent and de-facto is not prestashop functionality
        expect(self.password_input).to_have_js_property("validity.valid", False)
        return self

    def verify_error_message(self, message):
        expect(self.login_error_message).to_be_visible()
        expect(self.login_error_message).to_have_text(message)
        return self
