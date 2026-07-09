from playwright.sync_api import expect

from components.ContentArticle import ContentArticle
from components.Header import Header
from pages.BasePage import BasePage
from resources.translations import TRANSLATIONS
from utils.allure_reporting import attach_screenshot


class ArticlePage(BasePage):

    URLS = {
        "en": "https://en.wikipedia.org/wiki/",
        "nl": "https://nl.wikipedia.org/wiki/",
        "uk": "https://uk.wikipedia.org/wiki/",
    }

    def __init__(self, page, locale="en"):
        super().__init__(page)
        self.page = page
        self.locale = locale
        self.t = TRANSLATIONS[locale]
        self.header = Header(page, page, locale)
        self.content_article = ContentArticle(page, page, locale)

    def verify_loaded(self):
        #Actually almost every page has this element. And page is built quite differently for different languages. Better than nothing, though.
        expect(self.page.locator("#bodyContent")).to_be_visible()
        return self

    def open(self, article):
        self.page.goto(self.URLS[self.locale]+article)
        attach_screenshot(self.page, self.URLS[self.locale]+article)
        return self

    def search(self, text):
        self.header.search(text)
        return ArticlePage(self.page, self.locale).verify_loaded()

    def set_small_text_size(self):
        self.content_article.appearance.set_small_text_size()
        return self

    def set_standard_text_size(self):
        self.content_article.appearance.set_standard_text_size()
        return self

    def set_large_text_size(self):
        self.content_article.appearance.set_large_text_size()
        return self

    def get_text_size(self):
        return self.content_article.get_text_size()
