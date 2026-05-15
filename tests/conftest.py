import pytest
from playwright.sync_api import sync_playwright

# TODO: (probably) delete - sticking to pytest-playwright objects\fixtures. Also does not work as it is.

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