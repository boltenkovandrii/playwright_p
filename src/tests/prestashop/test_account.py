import uuid

import allure

DEMO_EMAIL = "pub@prestashop.com"
DEMO_PASSWORD = "123456789"


@allure.suite("PrestaShop storefront - Customer Account")
@allure.title("ACCT-01 — Login page structure")
def test_open_login_page(prestashop_home_page):
    login_page = prestashop_home_page.open().open_login_page()
    login_page.check_structure()


@allure.suite("PrestaShop storefront - Customer Account")
@allure.title("ACCT-02 — Registration page structure")
def test_open_registration_page(prestashop_home_page):
    login_page = prestashop_home_page.open().open_login_page()
    registration_page = login_page.open_registration_page()
    registration_page.check_structure()


@allure.suite("PrestaShop storefront - Customer Account")
@allure.title("ACCT-03 — Login validation")
def test_login_validation(prestashop_home_page):
    login_page = prestashop_home_page.open().open_login_page()

    login_page.login_with_invalid("", "")
    login_page.verify_email_error()

    login_page.login_with_invalid("nonexistent.user@example.com", "anypassword")
    login_page.verify_error_message("Authentication failed.")

    login_page.login_with_invalid(DEMO_EMAIL, "wrongpassword")
    login_page.verify_error_message("Authentication failed.")

    home_page = login_page.login(DEMO_EMAIL, DEMO_PASSWORD)
    account_dashboard = home_page.open_account_page()
    account_dashboard.verify_logged_in()


@allure.suite("PrestaShop storefront - Customer Account")
@allure.title("ACCT-04 — Registration validation")
def test_registration_validation(prestashop_home_page):
    login_page = prestashop_home_page.open().open_login_page()
    registration_page = login_page.open_registration_page()

    # Submit the form with all fields empty.
    registration_page = registration_page.submit().as_registration_page()
    registration_page.verify_first_name_error()

    # Enter an invalid email format then submit.
    registration_page =registration_page.fill_with(
        first_name="A",
        last_name="B",
        email="not-an-email",
        password="x",
    ).submit().as_registration_page()
    login_page.verify_email_error()

    # Entering an email address that is already registered
    registration_page = registration_page.fill_with(
        first_name="Jane",
        last_name="Doe",
        email=DEMO_EMAIL,
        password="ValidPass123!",
        birthday="01/01/1990",
    ).submit().as_registration_page()
    registration_page.verify_error_message("The email is already used, please choose another one or sign in")

    # valid input
    unique_email = f"testuser.{uuid.uuid4().hex[:8]}@example.com"
    home_page = registration_page.fill_with(
        first_name="Jane",
        last_name="Doe",
        email=unique_email,
        password="ValidPass123!",
        birthday="01/01/1990",
    ).submit().as_home_page()

    account_dashboard = home_page.open_account_page()
    account_dashboard.verify_logged_in()


@allure.suite("PrestaShop storefront - Customer Account")
@allure.title("ACCT-05 — Logout")
def test_logout(prestashop_home_page):
    login_page = prestashop_home_page.open().open_login_page()
    home_page = login_page.login(DEMO_EMAIL, DEMO_PASSWORD)
    account_dashboard = home_page.open_account_page()
    account_dashboard.verify_logged_in()

    login_page = account_dashboard.sign_out().as_login_page()
    login_page.verify_not_logged_in()

    page = login_page.navigate_to_account_dashboard_directly()
    # includes check that we are redirected to a login page
    login_page = page.as_login_page()
    login_page.verify_not_logged_in()

