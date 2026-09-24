import allure

DEMO_EMAIL = "pub@prestashop.com"
DEMO_PASSWORD = "123456789"
PRODUCT_NAME = "Hummingbird printed t-shirt"

# TODO: remove the whole class
def _open_dutch_home(prestashop_home_page):
    return prestashop_home_page.open().switch_language("nl")

@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-01 — Switch storefront language")
def test_switch_storefront_language(prestashop_home_page):
    home_page = prestashop_home_page.open()
    home_page.verify_current_language("en")
    home_page.verify_search_placeholder()

    home_page = home_page.switch_language("nl")
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-02 — Preserve storefront language across core pages")
def test_preserve_storefront_language_across_core_pages(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.check_structure()
    product_page.verify_current_language("nl")

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure()
    cart_page.verify_current_language("nl")

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.check_structure()
    checkout_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-03 — Verify localization of core storefront pages")
def test_verify_translated_ui(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    search_results_page = home_page.search("zzzz-no-match-12345")
    search_results_page.verify_current_language("nl")
    search_results_page.check_no_matches_message()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.verify_current_language("nl")
    product_page.check_structure()

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.verify_current_language("nl")
    cart_page.check_structure()

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.verify_current_language("nl")
    checkout_page.check_structure()

    login_page = prestashop_home_page.open().switch_language("nl").open_login_page()
    login_page.verify_current_language("nl")
    login_page.check_structure()

    registration_page = login_page.open_registration_page()
    registration_page.verify_current_language("nl")
    registration_page.check_structure()

    authenticated_home_page = prestashop_home_page.open().switch_language("nl").open_login_page().login(DEMO_EMAIL, DEMO_PASSWORD)
    account_page = authenticated_home_page.open_account_page()
    account_page.verify_current_language("nl")
    account_page.check_structure()


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-01 — Switch storefront language")
def test_switch_storefront_language1(prestashop_home_page):
    home_page = prestashop_home_page.open()
    home_page.verify_current_language("en")
    home_page.verify_search_placeholder()

    home_page = home_page.switch_language("nl")
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-02 — Preserve storefront language across core pages")
def test_preserve_storefront_language_across_core_pages1(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.check_structure()
    product_page.verify_current_language("nl")

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure()
    cart_page.verify_current_language("nl")

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.check_structure()
    checkout_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-03 — Verify localization of core storefront pages")
def test_verify_translated_ui1(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    search_results_page = home_page.search("zzzz-no-match-12345")
    search_results_page.verify_current_language("nl")
    search_results_page.check_no_matches_message()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.verify_current_language("nl")
    product_page.check_structure()

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.verify_current_language("nl")
    cart_page.check_structure()

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.verify_current_language("nl")
    checkout_page.check_structure()

    login_page = prestashop_home_page.open().switch_language("nl").open_login_page()
    login_page.verify_current_language("nl")
    login_page.check_structure()

    registration_page = login_page.open_registration_page()
    registration_page.verify_current_language("nl")
    registration_page.check_structure()

    authenticated_home_page = prestashop_home_page.open().switch_language("nl").open_login_page().login(DEMO_EMAIL, DEMO_PASSWORD)
    account_page = authenticated_home_page.open_account_page()
    account_page.verify_current_language("nl")
    account_page.check_structure()


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-01 — Switch storefront language")
def test_switch_storefront_language2(prestashop_home_page):
    home_page = prestashop_home_page.open()
    home_page.verify_current_language("en")
    home_page.verify_search_placeholder()

    home_page = home_page.switch_language("nl")
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-02 — Preserve storefront language across core pages")
def test_preserve_storefront_language_across_core_pages2(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.check_structure()
    product_page.verify_current_language("nl")

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure()
    cart_page.verify_current_language("nl")

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.check_structure()
    checkout_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-03 — Verify localization of core storefront pages")
def test_verify_translated_ui2(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    search_results_page = home_page.search("zzzz-no-match-12345")
    search_results_page.verify_current_language("nl")
    search_results_page.check_no_matches_message()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.verify_current_language("nl")
    product_page.check_structure()

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.verify_current_language("nl")
    cart_page.check_structure()

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.verify_current_language("nl")
    checkout_page.check_structure()

    login_page = prestashop_home_page.open().switch_language("nl").open_login_page()
    login_page.verify_current_language("nl")
    login_page.check_structure()

    registration_page = login_page.open_registration_page()
    registration_page.verify_current_language("nl")
    registration_page.check_structure()

    authenticated_home_page = prestashop_home_page.open().switch_language("nl").open_login_page().login(DEMO_EMAIL, DEMO_PASSWORD)
    account_page = authenticated_home_page.open_account_page()
    account_page.verify_current_language("nl")
    account_page.check_structure()


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-01 — Switch storefront language")
def test_switch_storefront_language3(prestashop_home_page):
    home_page = prestashop_home_page.open()
    home_page.verify_current_language("en")
    home_page.verify_search_placeholder()

    home_page = home_page.switch_language("nl")
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-02 — Preserve storefront language across core pages")
def test_preserve_storefront_language_across_core_pages3(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.check_structure()
    product_page.verify_current_language("nl")

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure()
    cart_page.verify_current_language("nl")

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.check_structure()
    checkout_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-03 — Verify localization of core storefront pages")
def test_verify_translated_ui3(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    search_results_page = home_page.search("zzzz-no-match-12345")
    search_results_page.verify_current_language("nl")
    search_results_page.check_no_matches_message()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.verify_current_language("nl")
    product_page.check_structure()

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.verify_current_language("nl")
    cart_page.check_structure()

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.verify_current_language("nl")
    checkout_page.check_structure()

    login_page = prestashop_home_page.open().switch_language("nl").open_login_page()
    login_page.verify_current_language("nl")
    login_page.check_structure()

    registration_page = login_page.open_registration_page()
    registration_page.verify_current_language("nl")
    registration_page.check_structure()

    authenticated_home_page = prestashop_home_page.open().switch_language("nl").open_login_page().login(DEMO_EMAIL, DEMO_PASSWORD)
    account_page = authenticated_home_page.open_account_page()
    account_page.verify_current_language("nl")
    account_page.check_structure()

@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-01 — Switch storefront language")
def test_switch_storefront_language4(prestashop_home_page):
    home_page = prestashop_home_page.open()
    home_page.verify_current_language("en")
    home_page.verify_search_placeholder()

    home_page = home_page.switch_language("nl")
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

'''
@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-02 — Preserve storefront language across core pages")
def test_preserve_storefront_language_across_core_pages4(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.check_structure()
    product_page.verify_current_language("nl")

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure()
    cart_page.verify_current_language("nl")

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.check_structure()
    checkout_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-03 — Verify localization of core storefront pages")
def test_verify_translated_ui4(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    search_results_page = home_page.search("zzzz-no-match-12345")
    search_results_page.verify_current_language("nl")
    search_results_page.check_no_matches_message()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.verify_current_language("nl")
    product_page.check_structure()

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.verify_current_language("nl")
    cart_page.check_structure()

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.verify_current_language("nl")
    checkout_page.check_structure()

    login_page = prestashop_home_page.open().switch_language("nl").open_login_page()
    login_page.verify_current_language("nl")
    login_page.check_structure()

    registration_page = login_page.open_registration_page()
    registration_page.verify_current_language("nl")
    registration_page.check_structure()

    authenticated_home_page = prestashop_home_page.open().switch_language("nl").open_login_page().login(DEMO_EMAIL, DEMO_PASSWORD)
    account_page = authenticated_home_page.open_account_page()
    account_page.verify_current_language("nl")
    account_page.check_structure()

@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-01 — Switch storefront language")
def test_switch_storefront_language5(prestashop_home_page):
    home_page = prestashop_home_page.open()
    home_page.verify_current_language("en")
    home_page.verify_search_placeholder()

    home_page = home_page.switch_language("nl")
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-02 — Preserve storefront language across core pages")
def test_preserve_storefront_language_across_core_pages5(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.check_structure()
    product_page.verify_current_language("nl")

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure()
    cart_page.verify_current_language("nl")

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.check_structure()
    checkout_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-03 — Verify localization of core storefront pages")
def test_verify_translated_ui5(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    search_results_page = home_page.search("zzzz-no-match-12345")
    search_results_page.verify_current_language("nl")
    search_results_page.check_no_matches_message()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.verify_current_language("nl")
    product_page.check_structure()

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.verify_current_language("nl")
    cart_page.check_structure()

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.verify_current_language("nl")
    checkout_page.check_structure()

    login_page = prestashop_home_page.open().switch_language("nl").open_login_page()
    login_page.verify_current_language("nl")
    login_page.check_structure()

    registration_page = login_page.open_registration_page()
    registration_page.verify_current_language("nl")
    registration_page.check_structure()

    authenticated_home_page = prestashop_home_page.open().switch_language("nl").open_login_page().login(DEMO_EMAIL, DEMO_PASSWORD)
    account_page = authenticated_home_page.open_account_page()
    account_page.verify_current_language("nl")
    account_page.check_structure()

@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-01 — Switch storefront language")
def test_switch_storefront_language6(prestashop_home_page):
    home_page = prestashop_home_page.open()
    home_page.verify_current_language("en")
    home_page.verify_search_placeholder()

    home_page = home_page.switch_language("nl")
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-02 — Preserve storefront language across core pages")
def test_preserve_storefront_language_across_core_pages6(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.check_structure()
    product_page.verify_current_language("nl")

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure()
    cart_page.verify_current_language("nl")

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.check_structure()
    checkout_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-03 — Verify localization of core storefront pages")
def test_verify_translated_ui6(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    search_results_page = home_page.search("zzzz-no-match-12345")
    search_results_page.verify_current_language("nl")
    search_results_page.check_no_matches_message()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.verify_current_language("nl")
    product_page.check_structure()

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.verify_current_language("nl")
    cart_page.check_structure()

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.verify_current_language("nl")
    checkout_page.check_structure()

    login_page = prestashop_home_page.open().switch_language("nl").open_login_page()
    login_page.verify_current_language("nl")
    login_page.check_structure()

    registration_page = login_page.open_registration_page()
    registration_page.verify_current_language("nl")
    registration_page.check_structure()

    authenticated_home_page = prestashop_home_page.open().switch_language("nl").open_login_page().login(DEMO_EMAIL, DEMO_PASSWORD)
    account_page = authenticated_home_page.open_account_page()
    account_page.verify_current_language("nl")
    account_page.check_structure()

@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-01 — Switch storefront language")
def test_switch_storefront_language7(prestashop_home_page):
    home_page = prestashop_home_page.open()
    home_page.verify_current_language("en")
    home_page.verify_search_placeholder()

    home_page = home_page.switch_language("nl")
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-02 — Preserve storefront language across core pages")
def test_preserve_storefront_language_across_core_pages7(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.check_structure()
    product_page.verify_current_language("nl")

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure()
    cart_page.verify_current_language("nl")

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.check_structure()
    checkout_page.verify_current_language("nl")


@allure.suite("PrestaShop storefront - Localization")
@allure.title("LOCA-03 — Verify localization of core storefront pages")
def test_verify_translated_ui7(prestashop_home_page):
    home_page = _open_dutch_home(prestashop_home_page)
    home_page.verify_current_language("nl")
    home_page.verify_search_placeholder()

    search_results_page = home_page.search("zzzz-no-match-12345")
    search_results_page.verify_current_language("nl")
    search_results_page.check_no_matches_message()

    catalog_page = home_page.open_category("Clothes") #Should be localized?
    catalog_page.verify_current_language("nl")

    product_page = catalog_page.open_product_by_name(PRODUCT_NAME)
    product_page.verify_current_language("nl")
    product_page.check_structure()

    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.verify_current_language("nl")
    cart_page.check_structure()

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.verify_current_language("nl")
    checkout_page.check_structure()

    login_page = prestashop_home_page.open().switch_language("nl").open_login_page()
    login_page.verify_current_language("nl")
    login_page.check_structure()

    registration_page = login_page.open_registration_page()
    registration_page.verify_current_language("nl")
    registration_page.check_structure()

    authenticated_home_page = prestashop_home_page.open().switch_language("nl").open_login_page().login(DEMO_EMAIL, DEMO_PASSWORD)
    account_page = authenticated_home_page.open_account_page()
    account_page.verify_current_language("nl")
    account_page.check_structure()

'''