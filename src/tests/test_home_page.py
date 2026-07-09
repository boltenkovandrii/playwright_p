import allure
from playwright.sync_api import expect

from resources.translations import TRANSLATIONS


@allure.suite("Home page")
@allure.title("Search from home page")
def test_home_page_search(home_page):
    article_page = (home_page
     .open()
     .close_donation_banner()
     .search("playwright"))

    expect(article_page.page).to_have_title("Playwright - Wikipedia")

@allure.suite("Home page")
@allure.title("Navigate to the main page")
def test_navigate_to_the_main_page(home_page, locale):
    main_page = (home_page
     .open()
     .close_donation_banner()
     .to_home_page(locale))

    expect(main_page.page).to_have_title(TRANSLATIONS[locale]["main_page_title"])

