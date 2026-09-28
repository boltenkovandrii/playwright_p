from __future__ import annotations

from playwright.sync_api import Page, expect
from typing import Self

from pages.prestashop.backoffice.BaseBackofficePage import BaseBackofficePage


class DashboardPage(BaseBackofficePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.dashboard = page.get_by_test_id("content")

    def verify_loaded(self) -> Self:
        super().verify_loaded()
        expect(self.dashboard).to_be_visible()
        return self
