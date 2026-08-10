import allure
@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Check catalog page structure")
def test_catalog_page_structure(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    catalog_page.check_structure()


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Browse products in a category")
def test_browse_products_in_a_category(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Accessories")
    catalog_page.verify_category_name("Accessories")
    catalog_page.check_displayed_results_count(11)
    catalog_page.product_grid.product_at(0).check_structure()
    catalog_page.product_grid.product_at(1).check_structure()

    product_names = catalog_page.product_grid.get_names()
    assert len(product_names) >= 2
    assert product_names[0] != product_names[1]


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Open product details page")
def test_open_product_details_page(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product(0)
    product_page.verify_product_name("Hummingbird printed t-shirt")
    product_page.check_structure()


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Navigate using breadcrumbs")
def test_navigate_using_breadcrumbs(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product(0)
    catalog_page = product_page.go_to_category_from_breadcrumb("Clothes")
    catalog_page.verify_category_name("Clothes")


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Change product sorting")
def test_change_product_sorting(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Accessories")
    initial_prices = catalog_page.product_grid.get_prices()
    catalog_page = catalog_page.sort_by("Price, high to low")
    sorted_prices = catalog_page.product_grid.get_prices()
    assert sorted_prices != initial_prices
    assert sorted_prices == sorted(sorted_prices, reverse=True)


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Change products per page")
def test_change_products_per_page(prestashop_home_page, profile):
    # TODO: probably we don't need this test at all
    # don't have enough products, so using workaround to check pagination
    search_results = prestashop_home_page.open_search_results("home", results_per_page=8)
    search_results.check_displayed_results_count(8)
    search_results = prestashop_home_page.open_search_results("home", results_per_page=4)
    search_results.check_displayed_results_count(4)
    search_results.check_pagination_visible(True)


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Navigate through catalog pagination")
def test_navigate_through_catalog_pagination(prestashop_home_page, profile):
    # don't have enough products, so using workaround to check pagination
    search_results = prestashop_home_page.open_search_results("home")
    search_results.check_pagination_visible(False)
    search_results = prestashop_home_page.open_search_results("home", results_per_page=8)
    search_results.check_displayed_results_count(8)
    search_results = search_results.go_to_page_number(2)
    search_results.check_displayed_results_count(3)
    search_results.check_pagination_visible(True)


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Filter products by price")
def test_filter_products_by_price(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Accessories")
    catalog_page.check_displayed_results_count(11)
    catalog_page = catalog_page.apply_price_filter(22, 42)
    catalog_page.check_displayed_results_count(4)
    catalog_page.verify_active_filter_contains("Price")


@allure.suite("PrestaShop storefront - Navigation & catalog")
@allure.title("Filter products by manufacturer")
def test_filter_products_by_manufacturer(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Accessories")
    catalog_page.check_displayed_results_count(11)
    catalog_page = catalog_page.apply_manufacturer_filter("Studio Design")
    catalog_page.check_displayed_results_count(7)
    catalog_page.verify_active_filter_contains("Studio Design")

