import allure

@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Check home page structure")
def test_home_page_structure(prestashop_home_page):
    prestashop_home_page.open().check_structure()
