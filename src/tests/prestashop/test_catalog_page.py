import allure
import pytest

@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Check catalog page structure")
def test_catalog_page_structure(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    catalog_page.check_structure()


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Browse products in a category")
@pytest.mark.skip(reason="Work in progress")
def test_browse_products_in_a_category(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Open product details page")
@pytest.mark.skip(reason="Work in progress")
def test_open_product_details_page(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Navigate using breadcrumbs")
@pytest.mark.skip(reason="Work in progress")
def test_navigate_using_breadcrumbs(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Change product sorting")
@pytest.mark.skip(reason="Work in progress")
def test_change_product_sorting(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Change products per page")
@pytest.mark.skip(reason="Work in progress")
def test_change_products_per_page(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Navigate through catalog pagination")
@pytest.mark.skip(reason="Work in progress")
def test_navigate_through_catalog_pagination(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Filter products by price")
@pytest.mark.skip(reason="Work in progress")
def test_filter_products_by_price(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Filter products by manufacturer")
@pytest.mark.skip(reason="Work in progress")
def test_filter_products_by_manufacturer(prestashop_home_page, profile):
    # Work in progress
    pass

