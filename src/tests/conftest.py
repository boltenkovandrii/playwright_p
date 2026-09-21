import pytest

from tests.config.profiles import get_profile, is_desktop
from utils.allure_reporting import attach_screenshot, attach_playwright_artifacts, set_screenshot_context


pytest_plugins = [
    "fixtures.locale",
    "fixtures.profile",
    "fixtures.prestashop.pages",
]


def pytest_addoption(parser):
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

def pytest_generate_tests(metafunc):
    if "profile" not in metafunc.fixturenames:
        return

    profiles = metafunc.config.getoption("profile")

    if not profiles:
        profiles = ["desktop_1920x1200"]

    metafunc.parametrize("profile", profiles)

@pytest.fixture
def browser_context_args(browser_context_args, playwright, profile, browser_name):

    if browser_name == "firefox" and not is_desktop(profile):
        pytest.skip("Firefox doesn't support device emulation (non-desktop profiles)")

    return {
        **browser_context_args,
        **get_profile(playwright, profile),
    }

# final screenshot
@pytest.fixture
def page(context):
    page = context.new_page()

    yield page

    attach_screenshot(page, "Final state")
    page.close()


@pytest.fixture(scope="session", autouse=True)
def selectors(playwright):
    playwright.selectors.set_test_id_attribute("id")


def pytest_runtest_setup(item):
    """Set up screenshot context for the test before it runs."""
    screenshots_enabled = item.config.getoption("--allure-screenshots") == "on"
    # pytest-rerunfailures execution_count is 1-based:
    # 1 = initial execution, 2+ = reruns.
    is_retry = getattr(item, "execution_count", 1) > 1
    set_screenshot_context(screenshots_enabled=screenshots_enabled, is_retry=is_retry)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed and "output_path" in item.funcargs:
        attach_playwright_artifacts(item.funcargs["output_path"])
