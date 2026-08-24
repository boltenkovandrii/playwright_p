import re

from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from utils.allure_reporting import attach_screenshot


class OrderConfirmationPage(BaseStorefrontPage):
    def __init__(self, page):
        super().__init__(page)
        self.confirmation_block = page.get_by_test_id("content-hook_order_confirmation")
        self.confirmation_heading = self.confirmation_block.get_by_role("heading", name="Your order is confirmed")
        self.order_items_section = page.get_by_test_id("order-items")
        self.order_items = self.order_items_section.locator(".order-line")
        self.order_summary_table = page.locator(".order-confirmation-table table")
        self.order_details = page.get_by_test_id("order-details")

        self.order_reference = page.get_by_test_id("order-reference-value")

    def verify_loaded(self):
        attach_screenshot(self.page, "Order confirmation page")
        super().verify_loaded()
        expect(self.page).to_have_url(re.compile(r"order-confirmation"))
        expect(self.confirmation_block).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking order confirmation structure")
        expect(self.confirmation_block).to_be_visible()
        expect(self.confirmation_heading).to_be_visible()
        expect(self.order_items.first).to_be_visible()
        expect(self.order_summary_table).to_be_visible()
        expect(self.order_details).to_be_visible()
        return self

    def verify_order_reference_present(self):
        expect(self.order_reference).to_contain_text(re.compile(r"Order reference:\s*[A-Z0-9]+"))
        return self

    def verify_product_with_name_present(self, product_name):
        expect(self.order_items_section).to_contain_text(product_name)
        return self

    def verify_shipping_method(self, shipping_method):
        expect(self.order_details).to_contain_text(shipping_method)
        return self

    def verify_payment_method(self, payment_method):
        expect(self.order_details).to_contain_text(payment_method)
        return self

    def verify_total_amount(self, expected_total):
        self._verify_summary_row_amount("Total (tax incl.)", expected_total)
        return self

    def verify_subtotal_amount(self, expected_subtotal):
        self._verify_summary_row_amount("Subtotal", expected_subtotal)
        return self

    def verify_shipping_amount(self, expected_shipping):
        self._verify_summary_row_amount("Shipping and handling", expected_shipping)
        return self

    def _verify_summary_row_amount(self, row_label, expected_amount):
        row = self.order_summary_table.locator("tr", has_text=row_label)
        amount = row.locator("td").last.inner_text().replace("€", "").replace("\u00a0", "").strip()
        if not abs(float(amount) - float(expected_amount)) < 0.01:
            raise AssertionError(
                f"Expected amount {expected_amount} was not found in row '{row_label}'. "
            )
        return self



