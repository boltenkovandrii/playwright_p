from playwright.sync_api import expect

from components.ContentMain import ContentMain
from components.Header import Header
from pages.ArticlePage import ArticlePage
from pages.BasePage import BasePage
from resources.translations import TRANSLATIONS
from utils.allure_reporting import attach_screenshot


class MainPage(BasePage):

    URLS = {
        "en": "https://en.wikipedia.org/wiki/Main_Page",
        "nl": "https://nl.wikipedia.org/wiki/Hoofdpagina",
        "uk": "https://uk.wikipedia.org/wiki/Головна_сторінка",
    }

    def __init__(self, page, locale="en"):
        super().__init__(page)
        self.page = page
        self.locale = locale
        self.t = TRANSLATIONS[locale]
        self.header = Header(page, page, locale)
        self.content_main = ContentMain(page, page, locale)

    def verify_loaded(self):
        expect(self.page.locator("#bodyContent")).to_be_visible()
        expect(self.page).to_have_title(TRANSLATIONS[self.locale]["main_page_title"])
        return self

    def open(self):
        self.page.goto(self.URLS[self.locale])
        attach_screenshot(self.page, "Main page")
        return self

    def search(self, text):
        self.header.search(text)
        return ArticlePage(self.page, self.locale).verify_loaded()

    def set_small_text_size(self):
        self.content_main.appearance.set_small_text_size()
        return self

    def set_standard_text_size(self):
        self.content_main.appearance.set_standard_text_size()
        return self

    def set_large_text_size(self):
        self.content_main.appearance.set_large_text_size()
        return self

    def get_text_size(self):
        return self.content_main.get_text_size()