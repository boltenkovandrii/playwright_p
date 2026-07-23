import allure
import pytest
from playwright.sync_api import expect

from resources.translations import TRANSLATIONS
from utils.allure_reporting import attach_screenshot


@pytest.mark.parametrize(
    "locale",
    ["en", "nl", "uk"],
    indirect=True
)
@allure.title("Testing main page title")
@allure.suite("Main page")
#@pytest.mark.skip(reason="Will be deleted later - only storing for the reference")
def test_main_page_title(main_page):
    main_page.open()
    expect(main_page.page).to_have_title(TRANSLATIONS[main_page.locale]["main_page_title"])


@pytest.mark.parametrize(
    "locale",
    ["en", "nl", "uk"],
    indirect=True
)
@allure.suite("Main page")
@allure.title("Check page structure")
#@pytest.mark.skip(reason="Will be deleted later - only storing for the reference")
def test_main_page_structure(main_page):
    main_page.open()
    main_page.header.check_structure()
    main_page.content_main.check_structure()


@pytest.mark.parametrize(
    "locale",
    ["en", "nl", "uk"],
    indirect=True
)
@allure.suite("Main page")
@allure.title("Check font selection")
#@pytest.mark.skip(reason="Will be deleted later - only storing for the reference")
def test_main_page_font_selection(main_page):
    main_page = main_page.open()
    main_page = main_page.set_small_text_size()
    attach_screenshot(main_page.page, "After selecting small text")
    assert main_page.get_text_size()=="14px"

    main_page = main_page.set_standard_text_size()
    attach_screenshot(main_page.page, "After selecting standard text")
    assert main_page.get_text_size()=="16px"

    main_page = main_page.set_large_text_size()
    attach_screenshot(main_page.page, "After selecting large text")
    assert main_page.get_text_size()=="20px"

    main_page = main_page.set_small_text_size()
    attach_screenshot(main_page.page, "After selecting small text")
    assert main_page.get_text_size()=="14px"