import pytest
from playwright.sync_api import Page

from pages.prestashop.backoffice.LoginPage import LoginPage
from pages.prestashop.storefront.HomePage import HomePage


@pytest.fixture
def prestashop_home_page(page: Page, locale: str) -> HomePage:
    return HomePage(page, locale)


@pytest.fixture
def prestashop_backoffice_login_page(page: Page) -> LoginPage:
    return LoginPage(page)
