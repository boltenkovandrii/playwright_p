import pytest

from tests.config.profiles import get_profile, is_desktop
from utils.allure_reporting import attach_screenshot, attach_playwright_artifacts


pytest_plugins = [
    "fixtures.pages",
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed and "output_path" in item.funcargs:
        attach_playwright_artifacts(item.funcargs["output_path"])
