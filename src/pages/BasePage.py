from __future__ import annotations

from typing import Self

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def verify_loaded(self) -> Self:
        raise NotImplementedError("Page must implement verify_loaded() method")
