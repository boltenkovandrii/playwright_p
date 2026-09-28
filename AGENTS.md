# AGENTS.md

## Project Snapshot
- Python Playwright + pytest automation framework with current active coverage on the **PrestaShop storefront**.
- Core pattern is Page Object Model: page objects in `src/pages/prestashop/storefront/` compose reusable UI components from `src/components/prestashop/storefront/`.
- Every page object inherits `BasePage` and must implement `verify_loaded()` (see `src/pages/BasePage.py`).

## Architecture That Matters
- Tests live in `src/tests/` and use fixtures from `src/fixtures/` (loaded via `pytest_plugins` in `src/tests/conftest.py`).
- Data flow is fixture-driven: pytest creates `page` -> page fixture builds page object -> tests call fluent page methods.
- Locale-aware storefront pages use `resources/translations.py` + localized storefront URLs (example: `src/pages/prestashop/storefront/HomePage.py`).
- Device profile behavior is centralized in `src/tests/config/profiles.py`; profile selection is injected via fixtures/options.
- Failure artifacts are attached by pytest hooks/utilities (`src/tests/conftest.py`, `src/utils/allure_reporting.py`).

## Working Conventions (Project-Specific)
- Prefer `expect(...)` assertions from Playwright, not plain `assert`, in page/test UI checks.
- Keep page methods chainable by returning `self` after actions.
- Use test metadata decorators consistently (`@allure.suite`, `@allure.title`) as seen in `src/tests/prestashop/test_home_page.py`.
- Parametrize locales with `indirect=True`:
  `@pytest.mark.parametrize("locale", ["en", "nl"], indirect=True)` together with a test signature such as `def test_example(prestashop_home_page, locale):`.
- Selector convention is nonstandard: test-id attribute is configured as `id` (see `pytest.ini` + README notes).

## Browser/Profile Rules You Must Respect
- Supported browsers include `firefox`, `chromium`, `webkit` in config/docs, but profile emulation has a known Firefox limitation.
- Non-desktop profile + Firefox is intentionally skipped (logic in `src/tests/conftest.py`).
- Default profile fixture value is desktop-oriented (`desktop_1920x1200`) unless overridden.

## Dev Workflows
- Install deps: `pip install -e .`
- Install browsers: `python -m playwright install`
- Fast local run script (PowerShell): `resources/scripts/test_run.ps1`
- Typical direct run examples:
  - `pytest -n auto --browser chromium`
  - `pytest src/tests/prestashop/test_home_page.py::test_home_page_structure --browser chromium`
- Reporting outputs:
  - raw: `reports/allure-results/`
  - HTML: `reports/allure-report/index.html`

## Integration Points
- AUT endpoints are externalized (for example `PRESTASHOP_BASE_URL` via `.env`; see README/fixtures usage).
- Docker compose files for local AUT stacks are under `docker/`.
- CI is GitHub Actions oriented, with browser/profile matrix behavior documented in repo docs.

## When Adding/Editing Tests
- Reuse existing fixtures first, especially `prestashop_home_page` from `src/fixtures/prestashop/pages.py`.
- Mirror the existing layout: storefront tests under `src/tests/prestashop/`, storefront pages under `src/pages/prestashop/storefront/`, and storefront components under `src/components/prestashop/storefront/`.
- For new pages/components, follow the existing split and implement `verify_loaded()` on every page object.
- Keep Allure artifacts useful: attach screenshots intentionally and rely on failure hooks for traces/videos.

## Coverage Documentation
- Storefront scenario design documents live under `docs/prestashop/storefront/`.
- Use these markdown files as the business-readable coverage map when extending or reviewing the suite.

