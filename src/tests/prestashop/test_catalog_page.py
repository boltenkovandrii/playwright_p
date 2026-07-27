import allure

from pages.prestashop.storefront.CatalogPage import CatalogPage


@allure.suite("PrestaShop storefront")
@allure.title("Check catalog page structure")
def test_catalog_page_structure(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    catalog_page.check_structure(profile)
