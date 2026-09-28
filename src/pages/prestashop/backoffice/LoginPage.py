from __future__ import annotations

from playwright.sync_api import Page, expect
from typing import Self

from pages.prestashop.backoffice.BaseBackofficePage import BaseBackofficePage


class LoginPage(BaseBackofficePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_form = page.locator("form")

    def open(self, path: str = "") -> Self:
        return super().open(path)

    def verify_loaded(self) -> Self:
        super().verify_loaded()
        expect(self.login_form).to_be_visible()
        return self
