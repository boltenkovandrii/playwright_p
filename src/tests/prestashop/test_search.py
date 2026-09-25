import allure


@allure.suite("PrestaShop storefront - Search")
@allure.title("SRCH-01 — Search by full product name")
def test_search_by_full_product_name(prestashop_home_page):
    search_results = prestashop_home_page.open().search("Hummingbird printed t-shirt")
    search_results.check_structure()
    search_results.verify_products_match("Hummingbird printed t-shirt")
    search_results.check_displayed_results_count(1)


@allure.suite("PrestaShop storefront - Search")
@allure.title("SRCH-02 — Search by partial product name")
def test_search_by_partial_product_name(prestashop_home_page):
    search_results = prestashop_home_page.open().search("Hummingbird")
    search_results.check_structure()
    search_results.verify_products_match("Hummingbird")
    search_results.check_displayed_results_count(5)


@allure.suite("PrestaShop storefront - Search")
@allure.title("SRCH-03 — Search with no matching results")
def test_search_with_no_matching_results(prestashop_home_page):
    search_results = prestashop_home_page.open().search("zzzz-no-match-12345")
    search_results.check_structure()
    search_results.check_displayed_results_count(0)
    search_results.check_no_matches_message()
    search_results = search_results.search("Hummingbird")
    search_results.check_displayed_results_count(5)


@allure.suite("PrestaShop storefront - Search")
@allure.title("SRCH-04 — Search from catalog page")
def test_search_from_catalog_page(prestashop_home_page):
    catalog_page = prestashop_home_page.open().open_category("Clothes")
    search_results = catalog_page.search("Hummingbird")
    search_results.check_structure()
    search_results.verify_products_match("Hummingbird")
    search_results.check_displayed_results_count(5)


@allure.suite("PrestaShop storefront - Search")
@allure.title("SRCH-05 — Navigate through search pagination")
def test_navigate_through_search_pagination(prestashop_home_page):
    # don't have enough products, so using workaround to check pagination
    search_results = prestashop_home_page.open_search_results("home")
    search_results.check_pagination_visible(False)
    search_results = prestashop_home_page.open_search_results("home", results_per_page=8)
    search_results.check_displayed_results_count(8)
    search_results.check_pagination_visible(True)
    search_results = search_results.go_to_page_number(2)
    search_results.check_displayed_results_count(3)
    search_results.check_pagination_visible(True)