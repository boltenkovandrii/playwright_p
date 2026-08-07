import allure


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Home page structure")
def test_home_page_structure(prestashop_home_page):
    prestashop_home_page.open().check_structure()


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Featured products are displayed")
def test_featured_projects_displayed(prestashop_home_page, profile):
    home_page = prestashop_home_page.open()
    home_page.featured_products.check_structure()


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Navigate to a category from the main menu")
def test_navigate_to_category_from_main_menu(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    catalog_page.verify_category_name("Clothes")
    catalog_page.verify_has_subcategories("Men", "Women")
    assert catalog_page.get_displayed_results_count() == 2
    catalog_page.check_structure()


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Navigate to a product from the featured products section")
def test_navigate_to_product_from_featured_products_section(prestashop_home_page, profile):
    home_page = prestashop_home_page.open()
    product_name = home_page.get_featured_product_name(0)
    product_page = home_page.open_featured_product_by_name(product_name)
    product_page.verify_product_name(product_name)
    product_page.check_structure()


@allure.suite("PrestaShop storefront - Homepage")
@allure.title("Search from the home page")
def test_search_from_home_page(prestashop_home_page):
    home_page = prestashop_home_page.open()
    search_results = home_page.header.search("cushion")
    assert search_results.get_displayed_results_count() == 3
    search_results.verify_products_contain("cushion")
    search_results.check_structure()
