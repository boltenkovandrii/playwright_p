# Playwright + pytest Automation Framework

## Overview

This repository contains a UI automation framework built with Playwright and pytest.
Its current active scope is **PrestaShop storefront automation**.

- **AUT**: PrestaShop demo storefront
- **Pattern**: Page Object Model (POM)
- **Execution**: pytest + pytest-playwright + pytest-xdist
- **Reporting**: Allure
- **Target usage**: portfolio-quality framework demonstrating scalable UI automation design

## Current Scope

- Active automated coverage is focused on the **PrestaShop storefront** only.
- Tests are organized under `src/tests/prestashop/`.
- Coverage currently includes home page, catalog, product page, cart, checkout, search, account, and localization scenarios.
- The framework is designed to support adding more locales and additional AUT areas later, but the current demonstrated locale coverage is `en` and `nl`.

## Architecture

The framework follows a fixture-driven POM approach:

- `src/pages/BasePage.py` provides the base page abstraction.
- `src/pages/prestashop/storefront/` contains storefront page objects.
- `src/components/prestashop/storefront/` contains reusable storefront UI components.
- `src/fixtures/prestashop/pages.py` provides page fixtures such as `prestashop_home_page`.
- `src/tests/prestashop/` contains executable test suites.
- `src/utils/allure_reporting.py` and `src/tests/conftest.py` handle screenshots, traces, and reporting helpers.

### Project Structure

```text
src/
├── components/
│   └── prestashop/
│       └── storefront/
├── fixtures/
│   ├── locale.py
│   ├── profile.py
│   └── prestashop/
│       └── pages.py
├── pages/
│   ├── BasePage.py
│   └── prestashop/
│       └── storefront/
├── tests/
│   ├── config/
│   ├── conftest.py
│   └── prestashop/
└── utils/
```

## Setup

### 1. Install dependencies

```powershell
pip install -e .
python -m playwright install
```

Optional on Windows for local report generation:

```powershell
scoop install allure
```

### 2. Start the PrestaShop application

```powershell
docker-compose -f docker/docker-compose-prestashop.yml up -d
```

### 3. Configure environment

Set `PRESTASHOP_BASE_URL` in `.env`.

Default local value:

```text
PRESTASHOP_BASE_URL=http://localhost:8090
```

## Running Tests

### Local helper script (not only runs the tests, but also handles allure report generation)

```powershell
resources/scripts/test_run.ps1
```

### Direct pytest examples

Run the full suite on Chromium:

```powershell
pytest -n auto --browser chromium
```

Run a single storefront suite:

```powershell
pytest src/tests/prestashop/test_home_page.py --browser chromium
```

Run a single test:

```powershell
pytest src/tests/prestashop/test_home_page.py::test_home_page_structure --browser chromium
```

Run with specific profiles:

```powershell
pytest --browser chromium --profile=desktop_1920x1200
pytest --browser chromium --profile=mobile
pytest --browser chromium --profile=tablet_landscape
```

## Browsers, Profiles, and Locales

- Supported browsers in the framework configuration: `firefox`, `chromium`, `webkit`
- Supported device profiles are defined in `src/tests/config/profiles.py`
- Current demonstrated locale coverage: `en`, `nl`
- The locale fixture is intentionally simple so additional languages can be added with minimal framework change
- Firefox does not support non-desktop device emulation in this setup, so such combinations are skipped

## Reporting

- Raw Allure results: `reports/allure-results/`
- Generated HTML report: `reports/allure-report/index.html`
- Playwright artifacts on failure are retained according to `pytest.ini`

For local run reports are generated at reports directory. The easiest way to view allure report is to use "Open in -> Browser" on reports/allure-report/index.html
 
CI test results are attached to a run. You can unpack them and view allure report with: 
```powershell
cd test-artifacts\allure-results
python -m http.server 8080
  ```

## Test Design Documentation

Business-readable scenario documentation for the storefront suite is stored under:

- `docs/prestashop/storefront/home.md`
- `docs/prestashop/storefront/catalog.md`
- `docs/prestashop/storefront/product.md`
- `docs/prestashop/storefront/cart.md`
- `docs/prestashop/storefront/checkout.md`
- `docs/prestashop/storefront/search.md`
- `docs/prestashop/storefront/account.md`
- `docs/prestashop/storefront/localization.md`

## Notes

- The framework uses the HTML `id` attribute as the configured Playwright test-id attribute. In a production implementation, dedicated test IDs would be preferable.
- `PLAYWRIGHT_SETUP.md` remains available as a short setup reference, but the primary onboarding flow is documented here.
