import allure

from pages.prestashop.storefront.CatalogPage import CatalogPage
from pages.prestashop.storefront.ProductPage import ProductPage


@allure.suite("PrestaShop storefront")
@allure.title("Check product page structure")
def test_product_page_structure(prestashop_home_page):
    prestashop_home_page.open().header.open_category("Clothes")
    catalog_page = CatalogPage(prestashop_home_page.page).verify_loaded()
    catalog_page.product_grid.product_at(0).open()
    ProductPage(prestashop_home_page.page).verify_loaded().check_structure()
