from contextvars import ContextVar
from pathlib import Path
from typing import Any, cast

import allure
from playwright.sync_api import Locator, Page

# Context variables to track screenshot behavior
_screenshots_enabled_context: ContextVar[bool] = ContextVar("screenshots_enabled", default=True)
_is_retry_context: ContextVar[bool] = ContextVar("is_retry", default=False)


def set_screenshot_context(screenshots_enabled: bool = True, is_retry: bool = False) -> None:
    """
    Set the context for screenshot handling.

    Args:
        screenshots_enabled: Whether screenshots are enabled globally
        is_retry: Whether this is a retry of a failed test
    """
    _screenshots_enabled_context.set(screenshots_enabled)
    _is_retry_context.set(is_retry)


def attach_screenshot(target: Page | Locator, name: str, full_page: bool = True) -> None:
    """
    Attach a screenshot to the Allure report.

    Args:
        target: The Playwright page or locator object
        name: The name of the screenshot
        full_page: Whether to capture the full page (default: True)

    If screenshots_enabled is False and is_retry is False, a text step is added instead of a screenshot.
    Screenshots are always attached if screenshots_enabled is True or if is_retry is True.
    """
    # Use context values if not explicitly provided
    is_retry = _is_retry_context.get()
    screenshots_enabled = _screenshots_enabled_context.get()

    with allure.step(name):
        if not screenshots_enabled and not is_retry:
            pass  # Add a text step instead of a screenshot
        else:
            # Attach screenshot on first run (if enabled) or on any retry
            if isinstance(target, Page):
                screenshot = target.screenshot(full_page=full_page)
            else:
                screenshot = target.screenshot()

            allure.attach(
                screenshot,
                name=name,
                attachment_type=allure.attachment_type.PNG,
            )


def attach_playwright_artifacts(output_path: str | Path) -> None:
    output_dir = Path(output_path)
    attach_file = cast(Any, allure.attach.file)
    for trace in output_dir.glob("trace*.zip"):
        attach_file(
            str(trace),
            name="Trace",
            attachment_type=allure.attachment_type.ZIP,
        )

    for video in output_dir.glob("video*.webm"):
        attach_file(
            str(video),
            name="Video",
            attachment_type="video/webm",
        )
