import allure
from playwright.sync_api import expect

from resources.translations import TRANSLATIONS


@allure.suite("Home page")
@allure.title("Navigate to the main page")
def test_navigate_to_the_home_page(prestashop_home_page):
    prestashop_home_page = prestashop_home_page.open()


#    expect(main_page.page).to_have_title(TRANSLATIONS[locale]["main_page_title"])

