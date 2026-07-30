import pytest

from pages.ArticlePage import ArticlePage
from pages.HomePage import HomePage
from pages.MainPage import MainPage


@pytest.fixture
def main_page(page, locale):
    return MainPage(page, locale)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def article_page(page, locale):
    return ArticlePage(page, locale)

@pytest.fixture
def article_page_en(page):
    return ArticlePage(page)

