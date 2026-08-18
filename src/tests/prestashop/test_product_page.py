import allure
import pytest

@allure.suite("PrestaShop storefront - Product Details")
@allure.title("PDP-01 — Check product page structure")
def test_product_page_structure(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product(0)
    product_page.check_structure()


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("PDP-02 — View product information")
def test_view_product_information(prestashop_home_page, profile):
    product_name = "Hummingbird printed sweater"
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)

    product_page.verify_product_name(product_name)
    product_page.verify_regular_price(43.08)
    product_page.verify_price(34.46)
    product_page.verify_short_description("Regular fit, round neckline, long sleeves. 100% cotton, brushed inner side for extra comfort.")

    product_page.verify_in_stock_count(1200)
    product_page.verify_full_description("Studio Design' PolyFaune collection features classic products with colorful patterns, "
                                         "inspired by the traditional japanese origamis. To wear with a chino or jeans. "
                                         "The sublimation textile printing process provides an exceptional color rendering and a color, guaranteed overtime.")


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("Browse product images")
@pytest.mark.skip(reason="Work in progress")
def test_browse_product_images(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("PDP-04 — Change product quantity")
def test_change_product_quantity(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)

    # Check default quantity
    product_page.verify_quantity_is_equal(1)

    # Increase the quantity to 2 using arrows.
    product_page.increase_quantity()
    product_page.verify_quantity_is_equal(2)

    # Decrease the quantity back to 1 using arrows.
    product_page.decrease_quantity()
    product_page.verify_quantity_is_equal(1)

    # Attempt to decrease the quantity below 1 (e.g., to 0 or negative) using arrows
    product_page.decrease_quantity()
    product_page.verify_quantity_is_equal(1)

    # Attempt to manually enter a value below 1 using direct input.
    product_page.set_quantity(0)
    product_page.verify_quantity_is_equal(1)

    # Attempt to manually enter a value of greater than 1 using direct input.
    product_page.set_quantity(3)
    product_page.verify_quantity_is_equal(3)



@allure.suite("PrestaShop storefront - Product Details")
@allure.title("PDP-05 — Select product combination")
def test_select_product_combination(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)

    product_page.verify_size_options("S", "M", "L", "XL")
    product_page.verify_color_options_count_equals(2)
    product_page.verify_selected_size("S")
    product_page.verify_selected_color("White")

    product_page = product_page.select_size("M")
    product_page.verify_selected_size("M")
    product_page.verify_product_context_visible()

    original_image  = product_page.get_image_source()
    product_page = product_page.select_color("Black")
    product_page.verify_selected_color("Black")
    product_page.verify_product_context_visible()
    new_image = product_page.get_image_source()
    assert original_image != new_image, "The product image did not change after selecting a different color."


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("PDP-06 — Add product to cart")
def test_add_product_to_cart(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"

    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)

    product_page.set_quantity(2)
    product_page.add_to_cart()
    product_page.verify_add_to_cart_confirmation(product_name, 2, 45.89, 45.89)
    product_page.verify_header_cart_count(2)


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("PDP-07 — Continue shopping after adding a product")
def test_continue_shopping_after_adding_a_product(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"

    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)

    product_page.add_to_cart()
    product_page.verify_add_to_cart_confirmation(product_name, 1, 22.94, 22.94)
    product_page.continue_shopping()
    product_page.verify_add_to_cart_confirmation_closed()
    product_page.verify_product_name(product_name)
    product_page.verify_product_context_visible()
    product_page.verify_header_cart_count(1)

    product_page.add_to_cart()
    product_page.verify_add_to_cart_confirmation(product_name, 2, 45.89, 45.89)
    product_page.continue_shopping()
    product_page.verify_add_to_cart_confirmation_closed()
    product_page.verify_product_name(product_name)
    product_page.verify_product_context_visible()
    product_page.verify_header_cart_count(2)


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("PDP-08 — Navigate to cart from the confirmation dialog")
def test_navigate_to_cart_from_confirmation_dialog(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"

    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)

    product_page.add_to_cart()
    product_page.verify_add_to_cart_confirmation(product_name, 1, 22.94, 22.94)

    cart_page = product_page.proceed_to_checkout()
    cart_page.verify_product_count(1)
    cart_page.verify_product_name(product_name)
    cart_page.verify_product_price(22.94)
    cart_page.verify_products_subtotal(22.94)
    cart_page.verify_total(22.94)
