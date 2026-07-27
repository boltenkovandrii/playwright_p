import allure


@allure.suite("PrestaShop storefront")
@allure.title("Check cart page structure")
def test_cart_page_structure(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category("Clothes")
    product_page = catalog_page.open_product(0)
    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure(profile)

