import allure

from pages.prestashop.storefront.CartPage import CartPage
from pages.prestashop.storefront.CatalogPage import CatalogPage
from pages.prestashop.storefront.ProductPage import ProductPage


@allure.suite("PrestaShop storefront")
@allure.title("Check cart page structure")
def test_cart_page_structure(prestashop_home_page):
    prestashop_home_page.open().header.open_category("Clothes")
    catalog_page = CatalogPage(prestashop_home_page.page).verify_loaded()
    catalog_page.product_grid.product_at(0).open()
    product_page = ProductPage(prestashop_home_page.page).verify_loaded()
    product_page.add_to_cart().go_to_cart()
    CartPage(prestashop_home_page.page).verify_loaded().check_structure()
