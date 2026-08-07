import allure
import pytest

@allure.suite("PrestaShop storefront - Product Details")
@allure.title("Check product page structure")
def test_product_page_structure(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product(0)
    product_page.check_structure()


@allure.suite("PrestaShop storefront - Product Details")
@allure.title("View product information")
@pytest.mark.skip(reason="Work in progress")
def test_view_product_information(prestashop_home_page, profile):
    # Work in progress
    pass


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
