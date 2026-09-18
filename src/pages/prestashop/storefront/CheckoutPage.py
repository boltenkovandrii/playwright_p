import re

from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from pages.prestashop.storefront.OrderConfirmationPage import OrderConfirmationPage
from playwright.sync_api import expect

from resources.translations import UI_TEXT
from utils.allure_reporting import attach_screenshot
from utils.network_helper import expect_response


class CheckoutPage(BaseStorefrontPage):
    def __init__(self, page, locale="en"):
        super().__init__(page, locale)
        self.checkout = page.locator("#checkout")

        self.subtotal_products = page.get_by_test_id("cart-subtotal-products")
        self.subtotal_shipping = page.get_by_test_id("cart-subtotal-shipping")
        self.total = page.locator(".cart-total")

        self.personal_info_step = page.get_by_test_id("checkout-personal-information-step")
        self.addresses_step = page.get_by_test_id("checkout-addresses-step")
        self.shipping_step = page.get_by_test_id("checkout-delivery-step")
        self.payment_step = page.get_by_test_id("checkout-payment-step")

        self.personal_info_heading = page.get_by_role("heading", name=UI_TEXT[self.locale]["checkout_personal_information_heading"])
        self.addresses_heading = page.get_by_role("heading", name=UI_TEXT[self.locale]["checkout_addresses_heading"])
        self.shipping_heading = page.get_by_role("heading", name=UI_TEXT[self.locale]["checkout_shipping_heading"])
        self.payment_heading = page.get_by_role("heading", name=UI_TEXT[self.locale]["checkout_payment_heading"])

        self.personal_info_form = self.personal_info_step.locator("#customer-form")
        self.first_name_input = self.personal_info_form.get_by_test_id("field-firstname")
        self.last_name_input = self.personal_info_form.get_by_test_id("field-lastname")
        self.email_input = self.personal_info_form.get_by_test_id("field-email")
        self.customer_privacy_checkbox = self.personal_info_form.locator("input[name='customer_privacy']")
        self.psgdpr_checkbox = self.personal_info_form.locator("input[name='psgdpr']")
        self.personal_info_continue_button = self.personal_info_form.get_by_role("button", name=UI_TEXT[self.locale]["checkout_continue_button"])

        self.address_input = self.addresses_step.get_by_test_id("field-address1")
        self.city_input = self.addresses_step.get_by_test_id("field-city")
        self.postcode_input = self.addresses_step.get_by_test_id("field-postcode")
        self.country_select = self.addresses_step.get_by_test_id("field-id_country")
        self.state_select = self.addresses_step.get_by_test_id("field-id_state")
        self.phone_input = self.addresses_step.get_by_test_id("field-phone")
        self.address_continue_button = self.addresses_step.get_by_role("button", name=UI_TEXT[self.locale]["checkout_continue_button"])

        self.delivery_options = self.shipping_step.locator(".js-delivery-option")
        self.shipping_option_radios = self.shipping_step.locator("input[type='radio'][name^='delivery_option']")
        self.shipping_continue_button = self.shipping_step.get_by_role("button", name=UI_TEXT[self.locale]["checkout_continue_button"])

        self.payment_options = self.payment_step.locator(".payment-option")
        self.payment_option_radios = self.payment_step.locator("input[name='payment-option']")
        self.terms_checkbox = self.payment_step.locator("input[id='conditions_to_approve[terms-and-conditions]']")
        self.place_order_button = self.payment_step.get_by_role("button", name=UI_TEXT[self.locale]["checkout_place_order_button"])


    def verify_loaded(self):
        attach_screenshot(self.page, "Checkout page")
        self.header.verify_loaded()
        self.notifications.verify_loaded()
        expect(self.checkout).to_be_visible()
        expect(self.personal_info_step).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking checkout page structure")
        self.header.verify_loaded()
        self.notifications.verify_loaded()
        expect(self.checkout).to_be_visible()
        expect(self.subtotal_products).to_be_visible()
        expect(self.subtotal_shipping).to_be_visible()
        expect(self.total).to_be_visible()
        expect(self.personal_info_step).to_be_visible()
        expect(self.addresses_step).to_be_visible()
        expect(self.shipping_step).to_be_visible()
        expect(self.payment_step).to_be_visible()
        return self

    def check_personal_info_structure(self):
        attach_screenshot(self.page, "Checking personal information step structure")
        expect(self.personal_info_step).to_be_visible()
        expect(self.personal_info_heading).to_be_visible()
        expect(self.personal_info_form).to_be_visible()
        expect(self.first_name_input).to_be_visible()
        expect(self.last_name_input).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.personal_info_continue_button).to_be_visible()
        return self

    # Might need to add another parameters or even whole additional layer for workflow interactions, but it is not needed so far
    def fill_personal_info(self, first_name, last_name, email):
        attach_screenshot(self.page, "Filling personal information")
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)

        if not self.customer_privacy_checkbox.is_checked():
            self.customer_privacy_checkbox.check()

        if not self.psgdpr_checkbox.is_checked():
            self.psgdpr_checkbox.check()

        self.personal_info_continue_button.click()
        expect(self.addresses_step).to_have_attribute("class", re.compile(r"js-current-step"))
        return self

    def check_addresses_structure(self):
        attach_screenshot(self.page, "Checking addresses step structure")
        expect(self.addresses_step).to_be_visible()
        expect(self.addresses_heading).to_be_visible()
        expect(self.address_input).to_be_visible()
        expect(self.city_input).to_be_visible()
        expect(self.postcode_input).to_be_visible()
        expect(self.country_select).to_be_visible()
        expect(self.address_continue_button).to_be_visible()
        return self

    # Might need to add another parameters or even whole additional layer for workflow interactions, but it is not needed so far
    def fill_address(self, address_line_1, city, postal_code, country, phone, state=None):
        attach_screenshot(self.page, "Filling address information")
        self.address_input.fill(address_line_1)
        self.city_input.fill(city)
        self.postcode_input.fill(postal_code)
        self.country_select.select_option(label=country)
        self.phone_input.fill(phone)

        # state is mandatory if present, so state=None only valid for countries like France
        if state:
            self.state_select.select_option(label=state)
        else:
            expect(self.state_select).not_to_be_visible()

        self.address_continue_button.click()
        expect(self.shipping_step).to_have_attribute("class", re.compile(r"js-current-step"))
        return self

    def check_shipping_method_structure(self):
        attach_screenshot(self.page, "Checking shipping step structure")
        expect(self.shipping_step).to_be_visible()
        expect(self.shipping_heading).to_be_visible()
        expect(self.shipping_option_radios.first).to_be_visible()
        expect(self.shipping_continue_button).to_be_visible()
        return self


    def fill_shipping_method(self, name):
        attach_screenshot(self.page, "Selecting shipping method")
        shipping_option = self.delivery_options.filter(has=self.page.get_by_text(name))

        # waiting for ajax request to be finished before clicking 'continue'
        with expect_response(self.page, "action=selectDeliveryOption"):
            shipping_option.locator("input[type='radio']").check()

        self.shipping_continue_button.click()
        return self

    def check_payment_structure(self):
        attach_screenshot(self.page, "Checking payment step structure")
        expect(self.payment_step).to_be_visible()
        expect(self.payment_heading).to_be_visible()
        expect(self.payment_option_radios.first).to_be_visible()
        expect(self.terms_checkbox).to_be_visible()
        expect(self.place_order_button).to_be_visible()
        return self

    def select_payment_method(self, method_name):
        attach_screenshot(self.page, "Selecting payment method")

        method = self.payment_options.filter(has=self.page.get_by_text(method_name))
        payment_radio = method.locator("input[type='radio'][name='payment-option']")
        payment_radio.check()
        expect(payment_radio).to_be_checked()
        return self

    def accept_terms(self):
        attach_screenshot(self.page, "Accepting terms and conditions")
        if not self.terms_checkbox.is_checked():
            self.terms_checkbox.check()
        expect(self.terms_checkbox).to_be_checked()
        return self

    def place_order(self):
        attach_screenshot(self.page, "Placing order")
        self.place_order_button.click()
        return OrderConfirmationPage(self.page, self.locale).verify_loaded()








