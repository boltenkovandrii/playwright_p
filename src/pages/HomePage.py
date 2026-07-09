from playwright.sync_api import expect

from pages.ArticlePage import ArticlePage
from pages.BasePage import BasePage
from pages.MainPage import MainPage
from resources.translations import TRANSLATIONS
from utils.allure_reporting import attach_screenshot


class HomePage(BasePage):

    URL = "https://wikipedia.org/"

    @property
    def toggle_languages(self):
        return self.page.get_by_role("button", name="Read Wikipedia in your")

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def verify_loaded(self):
        expect(self.page.get_by_label("Top languages")).to_be_visible()
        return self

    def open(self):
        self.page.goto(self.URL)
        attach_screenshot(self.page, "Home page")
        return self

    def close_donation_banner(self):
        if self.page.get_by_role("button", name="Close").is_visible():
            self.page.get_by_role("button", name="Close").click()
            attach_screenshot(self.page, "Donation banner closed")
        else:
            attach_screenshot(self.page, "Donation banner is absent")
        return self

    def search(self, text):
        self.page.get_by_role("searchbox").fill(text)
        self.page.get_by_role("button", name="Search").click()
        attach_screenshot(self.page, "Search performed")
        return ArticlePage(self.page).verify_loaded()

    def to_home_page(self, locale):
        if self.page.locator("#js-link-box-"+locale).is_visible():
            self.page.locator("#js-link-box-"+locale).click()
        else:
            self.toggle_languages.click()
            self.page.get_by_role("link", name=TRANSLATIONS[locale]["language"]).click()
        attach_screenshot(self.page, "After navigation to the Home Page")
        return MainPage(self.page, locale).verify_loaded()
