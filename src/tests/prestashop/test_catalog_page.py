import allure

from pages.prestashop.storefront.CatalogPage import CatalogPage


@allure.suite("PrestaShop storefront")
@allure.title("Check catalog page structure")
def test_catalog_page_structure(prestashop_home_page):
    prestashop_home_page.open().header.open_category("Clothes")
    CatalogPage(prestashop_home_page.page).verify_loaded().check_structure()
