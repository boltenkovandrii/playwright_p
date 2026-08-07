import allure
import pytest


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Home page structure")
def test_home_page_structure(prestashop_home_page):
    prestashop_home_page.open().check_structure()

@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Featured products are displayed")
@pytest.mark.skip(reason="Work in progress")
def test_featured_projects_displayed(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Navigate to a category from the main menu")
@pytest.mark.skip(reason="Work in progress")
def test_navigate_to_category_from_main_menu(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Navigate to a category from the featured products section")
@pytest.mark.skip(reason="Work in progress")
def test_navigate_to_category_from_featured_products_section(prestashop_home_page, profile):
    # Work in progress
    pass


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Search from the home page")
@pytest.mark.skip(reason="Work in progress")
def test_search_from_home_page(prestashop_home_page):
    # Work in progress
    pass

