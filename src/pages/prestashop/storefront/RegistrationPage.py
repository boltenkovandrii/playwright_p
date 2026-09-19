from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from resources.translations import UI_TEXT
from utils.allure_reporting import attach_screenshot


class RegistrationPage(BaseStorefrontPage):
    def __init__(self, page, locale="en"):
        super().__init__(page, locale)
        self.heading = page.get_by_role("heading", name=UI_TEXT[self.locale]["registration_heading"])
        self.social_title_mr = page.get_by_test_id("field-id_gender-1")
        self.social_title_mrs = page.get_by_test_id("field-id_gender-2")
        self.first_name_input = page.get_by_test_id("field-firstname")
        self.last_name_input = page.get_by_test_id("field-lastname")
        self.email_input = page.get_by_test_id("field-email")
        self.password_input = page.get_by_test_id("field-password")
        self.birthday_input = page.get_by_test_id("field-birthday")
        self.newsletter_checkbox = page.locator("input[name='newsletter']")
        self.offers_checkbox = page.locator("input[name='optin']")
        self.privacy_checkbox = page.locator("input[name='customer_privacy']")
        self.psgdpr_checkbox = page.locator("input[name='psgdpr']")
        self.submit_button = page.get_by_role("button", name=UI_TEXT[self.locale]["registration_submit_button"])
        self.error_alert = page.locator("#notifications .alert-danger")
        self.field_errors = page.locator(".form-group.has-error")
        self.error_message = page.locator(".alert-danger")

    def open(self, path="registration"):
        super().open(path)
        return self

    def verify_loaded(self):
        attach_screenshot(self.page, "Registration page")
        super().verify_loaded()
        expect(self.heading).to_be_visible()
        return self

    def verify_current_language(self, locale):
        super().verify_current_language(locale)
        expect(self.heading).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking registration page structure")
        super().check_structure()
        expect(self.heading).to_be_visible()
        expect(self.social_title_mr).to_be_visible()
        expect(self.social_title_mrs).to_be_visible()
        expect(self.first_name_input).to_be_visible()
        expect(self.last_name_input).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.birthday_input).to_be_visible()
        expect(self.newsletter_checkbox).to_be_visible()
        expect(self.offers_checkbox).to_be_visible()
        expect(self.privacy_checkbox).to_be_visible()
        expect(self.psgdpr_checkbox).to_be_visible()
        expect(self.submit_button).to_be_visible()
        return self

    def submit(self):
        attach_screenshot(self.page, "Submitting the registration form")
        self.submit_button.click()
        # depending on the input, this may lead to either an error or a successful registration (so we will either stay on current page, or will be redirected to the HomePage)
        return BaseStorefrontPage(self.page, self.locale).verify_loaded()


    def fill_with(self, first_name="", last_name="", email="", password="", birthday=""):
        """Fill the specified fields and check required consent checkboxes when present.
        Returns self for error-assertion chaining."""
        attach_screenshot(self.page, "Submitting registration form with partial data")
        if first_name:
            self.first_name_input.fill(first_name)
        if last_name:
            self.last_name_input.fill(last_name)
        if email:
            self.email_input.fill(email)
        if password:
            self.password_input.fill(password)
        if birthday:
            self.birthday_input.fill(birthday)
        if not self.privacy_checkbox.is_checked():
            self.privacy_checkbox.check()
        if not self.psgdpr_checkbox.is_checked():
            self.psgdpr_checkbox.check()
        return self

    def verify_first_name_error(self):
        # Don't check error message itself - it is browser-dependent and de-facto is not prestashop functionality
        expect(self.first_name_input).to_have_js_property("validity.valid", False)
        return self

    def verify_email_error(self, message):
        expect(self.email_input).to_have_js_property("validity.valid", False)
        expect(self.email_input).to_have_js_property("validationMessage", message)
        return self

    def verify_error_message(self, message):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(message)
        return self

    def verify_field_errors_visible(self):
        expect(self.field_errors.first).to_be_visible()
        return self

    def verify_error_message_visible(self):
        expect(self.error_alert).to_be_visible()
        return self


