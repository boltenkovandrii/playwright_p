from __future__ import annotations

from playwright.sync_api import Page
from typing import Self


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def verify_loaded(self) -> Self:
        raise NotImplementedError("Page must implement verify_loaded() method")
