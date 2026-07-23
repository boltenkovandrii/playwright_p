import pytest

from pages.prestashop.backoffice.LoginPage import LoginPage
from pages.prestashop.storefront.HomePage import HomePage


@pytest.fixture
def prestashop_home_page(page):
    return HomePage(page)


@pytest.fixture
def prestashop_backoffice_login_page(page):
    return LoginPage(page)
