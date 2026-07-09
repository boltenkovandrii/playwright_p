import pytest
from playwright.sync_api import sync_playwright

from utils.allure_reporting import attach_screenshot

pytest_plugins = [
    "tests.fixtures.pages",
    "tests.fixtures.locale",
]
'''
@pytest.fixture(scope="session")
def browser_f():
    with sync_playwright() as p:
        browser_f = p.chromium.launch(headless=False, slow_mo=1000, channel="msedge")
        print(browser_f.version)
        yield browser_f

        browser_f.close()

@pytest.fixture
def page_f(browser_f):
    context = browser_f.new_context()
    page_f = context.new_page()

    yield page_f

    context.close()
'''

@pytest.fixture
def browser_context_args(browser_context_args):

    return {
        **browser_context_args,
        "viewport": {
#            "width": 2560,
#            "height": 1600
            "width": 1920,
            "height": 1080
        }
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