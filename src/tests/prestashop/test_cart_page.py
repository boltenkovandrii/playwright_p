import allure
import pytest


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("Check cart page structure")
def test_cart_page_structure(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product(0)
    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure()


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("Empty cart structure")
@pytest.mark.skip(reason="Work in progress")
def test_empty_cart_structure(prestashop_home_page):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("Add single product to cart")
@pytest.mark.skip(reason="Work in progress")
def test_add_single_product_to_cart(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("Add multiple quantities")
@pytest.mark.skip(reason="Work in progress")
def test_add_multiple_quantities(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("Remove product from cart")
@pytest.mark.skip(reason="Work in progress")
def test_remove_product_from_cart(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("Update product quantity")
@pytest.mark.skip(reason="Work in progress")
def test_update_product_quantity(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("Continue shopping from cart")
@pytest.mark.skip(reason="Work in progress")
def test_continue_shopping_from_cart(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("Verify cart totals")
@pytest.mark.skip(reason="Work in progress")
def test_verify_cart_totals(prestashop_home_page, profile):
    # Work in progress
    pass


