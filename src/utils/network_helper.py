from typing import Any

from playwright.sync_api import Page


def expect_response(page: Page, url_fragment: str) -> Any:
    return page.expect_response(lambda response: url_fragment in response.url and response.ok)
