from __future__ import annotations

from collections.abc import Iterator
from typing import Any, cast

import pytest
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item
from _pytest.python import Metafunc
from _pytest.runner import CallInfo
from playwright.sync_api import BrowserContext, Page, Playwright

from tests.config.profiles import get_profile, is_desktop
from utils.allure_reporting import attach_playwright_artifacts, attach_screenshot, set_screenshot_context

pytest_plugins = [
    "fixtures.locale",
    "fixtures.profile",
    "fixtures.prestashop.pages",
]


def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        "--profile",
        action="append",
        help="Profile name",
    )
    parser.addoption(
        "--allure-screenshots",
        action="store",
        default="off",
        choices=["on", "off"],
        help="Whether to attach screenshots to Allure report (default: off)",
    )


def pytest_generate_tests(metafunc: Metafunc) -> None:
    if "profile" not in metafunc.fixturenames:
        return

    profiles = metafunc.config.getoption("profile")

    if not profiles:
        profiles = ["desktop_1920x1200"]

    metafunc.parametrize("profile", profiles)


@pytest.fixture
def browser_context_args(
    browser_context_args: dict[str, object],
    playwright: Playwright,
    profile: str,
    browser_name: str,
) -> dict[str, object]:

    if browser_name == "firefox" and not is_desktop(profile):
        pytest.skip("Firefox doesn't support device emulation (non-desktop profiles)")

    return {
        **browser_context_args,
        **get_profile(playwright, profile),
    }


# final screenshot
@pytest.fixture
def page(context: BrowserContext) -> Iterator[Page]:
    page = context.new_page()

    yield page

    attach_screenshot(page, "Final state")
    page.close()


@pytest.fixture(scope="session", autouse=True)
def selectors(playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("id")


def pytest_runtest_setup(item: Item) -> None:
    """Set up screenshot context for the test before it runs."""
    screenshots_enabled = item.config.getoption("--allure-screenshots") == "on"
    # pytest-rerunfailures execution_count is 1-based:
    # 1 = initial execution, 2+ = reruns.
    is_retry = getattr(item, "execution_count", 1) > 1
    set_screenshot_context(screenshots_enabled=screenshots_enabled, is_retry=is_retry)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo[Any]) -> Iterator[None]:
    outcome: Any = yield
    report = outcome.get_result()
    funcargs = cast(dict[str, object], getattr(item, "funcargs", {}))

    if report.when == "call" and report.failed and "output_path" in funcargs:
        attach_playwright_artifacts(cast(str, funcargs["output_path"]))
