import allure
import pytest

@allure.suite("PrestaShop storefront - Product Details")
@allure.title("Check product page structure")
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
@allure.title("Change product quantity")
@pytest.mark.skip(reason="Work in progress")
def test_change_product_quantity(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("Select product combination")
@pytest.mark.skip(reason="Work in progress")
def test_select_product_combination(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("Add product to cart")
@pytest.mark.skip(reason="Work in progress")
def test_add_product_to_cart(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("Continue shopping after adding a product")
@pytest.mark.skip(reason="Work in progress")
def test_continue_shopping_after_adding_a_product(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("Navigate to cart from the confirmation dialog")
@pytest.mark.skip(reason="Work in progress")
def test_navigate_to_cart_from_confirmation_dialog(prestashop_home_page, profile):
    # Work in progress
    pass
