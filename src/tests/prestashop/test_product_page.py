import allure

@allure.suite("PrestaShop storefront - Product Details")
@allure.title("Check product page structure")
def test_product_page_structure(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product(0)
    product_page.check_structure()