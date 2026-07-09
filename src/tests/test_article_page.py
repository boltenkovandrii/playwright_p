import allure
import pytest
from playwright.sync_api import expect

from resources.translations import TRANSLATIONS
from utils.allure_reporting import attach_screenshot


@allure.suite("Article page")
@allure.title("Testing article page title - localized")
@pytest.mark.parametrize(
    "locale",
    ["en", "nl", "uk"],
    indirect=True
)
def test_article_search_chain_localized(article_page):
    article_page.open("Playwright")
    expect(article_page.page).to_have_title("Playwright" + TRANSLATIONS[article_page.locale]["wiki_header_postfix"])
    article_page.search("python")
    expect(article_page.page).to_have_title("Python" + TRANSLATIONS[article_page.locale]["wiki_header_postfix"])

@pytest.mark.parametrize(
    "locale",
    ["en", "nl", "uk"],
    indirect=True
)
@allure.suite("Article page")
@allure.title("Check page structure")
def test_article_page_structure(article_page):
    article_page = article_page.open("Playwright")
    article_page.header.check_structure()
    article_page.content_article.check_structure()


@pytest.mark.parametrize(
    "locale",
    ["en", "nl", "uk"],
    indirect=True
)
@allure.suite("Article page")
@allure.title("Check font selection")
def test_article_page_font_selection(article_page):
    article_page = article_page.open("Playwright")
    article_page = article_page.set_small_text_size()
    attach_screenshot(article_page.page, "After selecting small text")
    assert article_page.get_text_size()=="14px"

    article_page = article_page.set_standard_text_size()
    attach_screenshot(article_page.page, "After selecting standard text")
    assert article_page.get_text_size()=="16px"

    article_page = article_page.set_large_text_size()
    attach_screenshot(article_page.page, "After selecting large text")
    assert article_page.get_text_size()=="20px"

    article_page = article_page.set_small_text_size()
    attach_screenshot(article_page.page, "After selecting small text")
    assert article_page.get_text_size()=="14px"