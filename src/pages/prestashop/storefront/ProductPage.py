import re

from pages.prestashop.storefront.CartPage import CartPage
from pages.prestashop.storefront.BaseStorefrontPage import BaseStorefrontPage
from playwright.sync_api import expect

from resources.translations import UI_TEXT
from utils.allure_reporting import attach_screenshot


class ProductPage(BaseStorefrontPage):
    def __init__(self, page, locale="en"):
        super().__init__(page, locale)
        self.product = page.get_by_test_id("main")
        self.product_name = self.product.locator("h1")
        self.product_information = page.locator(".product-information")

        self.cover_image = page.locator(".product-cover .img-fluid")
        self.price = page.locator(".current-price .current-price-value")
        self.regular_price = page.locator(".product-discount .regular-price")
        self.description_short = page.locator("div[id*='product-description-short-'] p")

        self.description_tab = page.get_by_role("tab", name=UI_TEXT[self.locale]["product_description_tab"])
        self.description_tab_panel = page.get_by_test_id("description")
        self.description_full = page.locator(".tab-content .product-description")

        self.product_details_tab = page.get_by_role("tab", name=UI_TEXT[self.locale]["product_details_tab"])
        self.product_details_tab_panel = page.get_by_test_id("product-details")
        self.in_stock = page.locator(".product-quantities span")

        self.short_description = self.product_information.locator("p").filter(has_text=re.compile(r"\S")).first

        self.add_to_cart_button = page.locator("[data-button-action='add-to-cart']")


        self.cart_modal = page.get_by_test_id("blockcart-modal")
        self.cart_modal_title = self.cart_modal.locator(".modal-title")
        self.cart_modal_product_name = self.cart_modal.locator(".product-name")
        self.cart_modal_product_quantity = self.cart_modal.locator(".product-quantity strong")
        self.cart_modal_item_count = self.cart_modal.locator(".cart-products-count")
        self.cart_modal_total_value = self.cart_modal.locator(".product-total .value")
        self.cart_modal_subtotal_value = self.cart_modal.locator(".subtotal.value")
        self.modal_continue_shopping_button = page.get_by_role("button", name=UI_TEXT[self.locale]["continue_shopping_link"])
        self.modal_proceed_to_checkout_link = page.get_by_role("link", name=UI_TEXT[self.locale]["proceed_to_checkout_link"])

        self.quantity_input = page.get_by_test_id("quantity_wanted")
        self.quantity_increase_button = page.locator(".bootstrap-touchspin-up")
        self.quantity_decrease_button = page.locator(".bootstrap-touchspin-down")
        self.size_select = page.get_by_label(UI_TEXT[self.locale]["product_size_label"])
        self.size_options = self.size_select.locator("option")
        self.selected_size_option = self.size_select.locator("option:checked")
        self.color_options = page.locator(".input-color")

    def verify_loaded(self):
        attach_screenshot(self.page, "Product page")
        super().verify_loaded()
        expect(self.product).to_be_visible()
        return self

    def verify_current_language(self, locale):
        super().verify_current_language(locale)
        expect(self.description_tab).to_be_visible()
        expect(self.product_details_tab).to_be_visible()
        expect(self.size_select).to_be_visible()
        return self

    def check_structure(self):
        attach_screenshot(self.page, "Checking product page structure")
        super().check_structure()
        expect(self.product).to_be_visible()
        expect(self.cover_image).to_be_visible()
        expect(self.product_information).to_be_visible()
        expect(self.short_description).to_be_visible()
        expect(self.description_tab).to_be_visible()
        expect(self.product_details_tab).to_be_visible()
        expect(self.add_to_cart_button).to_be_visible()
        return self

    def verify_product_name(self, expected_name):
        attach_screenshot(self.page, "Verifying product name")
        expect(self.product_name).to_contain_text(
            re.compile(re.escape(expected_name), re.IGNORECASE)
        )
        return self

    def verify_regular_price(self, expected_price):
        expect(self.regular_price).to_have_text(f"€{expected_price}")
        return self

    def verify_price(self, expected_price):
        expect(self.price).to_have_text(f"€{expected_price}")
        return self

    def verify_short_description(self, expected_text):
        expect(self.description_short).to_contain_text(expected_text)
        return self

    def verify_full_description(self, expected_text):
        self._open_description_tab()
        expect(self.description_full).to_be_visible()
        expect(self.description_full).to_contain_text(expected_text)
        return self

    def verify_in_stock_count(self, count):
        self._open_product_details_tab()
        expect(self.in_stock).to_be_visible()
        expect(self.in_stock).to_have_text(f"{count} Items")
        return self

    def _open_description_tab(self):
        self.description_tab.click()
        expect(self.description_tab_panel).to_be_visible()
        return self

    def _open_product_details_tab(self):
        self.product_details_tab.click()
        expect(self.product_details_tab_panel).to_be_visible()
        return self

    def add_to_cart(self):
        attach_screenshot(self.page, "Adding product to cart")
        self.add_to_cart_button.click()
        expect(self.cart_modal).to_be_visible()
        attach_screenshot(self.page, "After adding item to a cart")
        return self

    def verify_add_to_cart_confirmation(self, expected_product_name, expected_quantity, expected_total, expected_subtotal):
        expect(self.cart_modal).to_be_visible()
        expect(self.cart_modal_title).to_contain_text(UI_TEXT[self.locale]["product_added_confirmation"])
        expect(self.cart_modal_product_name).to_have_text(expected_product_name)
        expect(self.cart_modal_product_quantity).to_have_text(str(expected_quantity))
        expect(self.cart_modal_item_count).to_have_text(self._cart_items_count_text(expected_quantity))
        expect(self.cart_modal_total_value).to_be_visible()
        expect(self.cart_modal_total_value).to_have_text(f"€{expected_total}")
        expect(self.cart_modal_subtotal_value).to_be_visible()
        expect(self.cart_modal_subtotal_value).to_have_text(f"€{expected_subtotal}")
        expect(self.modal_continue_shopping_button).to_be_visible()
        expect(self.modal_proceed_to_checkout_link).to_be_visible()
        return self

    def continue_shopping(self):
        attach_screenshot(self.page, "Continuing shopping from cart confirmation")
        expect(self.cart_modal).to_be_visible()
        self.modal_continue_shopping_button.click()
        expect(self.cart_modal).to_be_hidden()
        return self

    def verify_add_to_cart_confirmation_closed(self):
        expect(self.cart_modal).to_be_hidden()
        return self

    def verify_header_cart_count(self, expected_count):
        self.header.verify_cart_count(expected_count)
        return self

    def increase_quantity(self):
        self.quantity_increase_button.click()
        return self

    def decrease_quantity(self):
        self.quantity_decrease_button.click()
        return self

    def set_quantity(self, value):
        self.quantity_input.fill(str(value))
        self.quantity_input.press("Tab")
        return self

    def verify_quantity_is_equal(self, expected_quantity):
        expect(self.quantity_input).to_have_value(str(expected_quantity))
        return self

    def verify_size_options(self, *expected_sizes):
        expect(self.size_select).to_be_visible()
        expect(self.size_options).to_have_count(len(expected_sizes))
        expect(self.size_options).to_have_text(list(expected_sizes))
        return self

    def verify_color_options_count_equals(self, expected_count):
        expect(self.color_options.first).to_be_visible()
        expect(self.color_options).to_have_count(expected_count)
        return self

    def verify_selected_size(self, expected_size):
        expect(self.selected_size_option).to_have_text(expected_size)
        return self

    def select_size(self, size):
        attach_screenshot(self.page, f"Selecting size: {size}")
        self.size_select.select_option(label=size)
        expect(self.selected_size_option).to_have_text(size)
        return self

    def verify_selected_color(self, expected_color):
        expect(self._color_option(expected_color)).to_be_checked()
        return self

    def select_color(self, color):
        if not self._color_option(color).is_checked():
            attach_screenshot(self.page, f"Selecting color: {color}")
            original_image = self.get_image_source()
            self._color_option(color).check(force=True)
            expect(self._color_option(color)).to_be_checked()
            expect(self.cover_image).not_to_have_attribute("src", original_image)
        else :
            attach_screenshot(self.page, f"Color: {color} is already selected")
        return self

    def verify_product_context_visible(self):
        expect(self.product_name).to_be_visible()
        expect(self.add_to_cart_button).to_be_visible()
        return self

    def get_image_source(self):
        return self.cover_image.get_attribute("src")

    def go_to_cart(self):
        return self.proceed_to_checkout()

    def proceed_to_checkout(self):
        attach_screenshot(self.page, "Going to cart")
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            self.modal_proceed_to_checkout_link.click()
        attach_screenshot(self.page, "After navigating to the cart")
        return CartPage(self.page, self.locale).verify_loaded()

    def go_to_category_from_breadcrumb(self, category_name):
        attach_screenshot(self.page, "Going to category from breadcrumb")
        from pages.prestashop.storefront.CatalogPage import CatalogPage
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            self.page.locator("nav.breadcrumb a").filter(has_text=category_name).click()
        return CatalogPage(self.page, self.locale).verify_loaded()

    def _color_option(self, color):
        return self.page.locator(f".input-color[title='{color}'], .input-color[aria-label='{color}']")

    def _cart_items_count_text(self, count):
        if count == 1:
            return UI_TEXT[self.locale]["product_added_items_singular"]
        return UI_TEXT[self.locale]["product_added_items_plural"].format(count=count)
