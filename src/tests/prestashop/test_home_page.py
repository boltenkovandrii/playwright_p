import allure


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("HOME-01 — Check home page structure")
def test_home_page_structure(prestashop_home_page):
    prestashop_home_page.open().check_structure()


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("HOME-02 — Check featured products block structure")
def test_featured_products_displayed(prestashop_home_page):
    home_page = prestashop_home_page.open()
    home_page.featured_products.check_structure()


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("HOME-03 — Navigate to category from main menu")
def test_navigate_to_category_from_main_menu(prestashop_home_page):
    catalog_page = prestashop_home_page.open().open_category("Clothes")
    catalog_page.verify_category_name("Clothes")
    catalog_page.check_subcategories_list("Men", "Women")
    catalog_page.check_displayed_results_count(2)
    catalog_page.check_structure()


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("HOME-04 — Open featured product details page")
def test_navigate_to_product_from_featured_products_section(prestashop_home_page):
    home_page = prestashop_home_page.open()
    product_name = "Hummingbird printed t-shirt"
    product_page = home_page.open_featured_product_by_name(product_name)
    product_page.verify_product_name(product_name)
    product_page.check_structure()

