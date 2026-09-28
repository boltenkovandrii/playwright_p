# Repository Agent Instructions

## Project

This is a Python + Playwright + pytest UI automation portfolio project. Current automated coverage targets the PrestaShop storefront.

The project demonstrates maintainable E2E automation rather than exhaustive coverage of the AUT.

## Architecture

* Tests live under `src/tests/`.
* Pytest fixtures live under `src/fixtures/`.
* Page Objects live under `src/pages/`.
* Reusable UI components live under `src/components/`.
* Shared helpers live under `src/helpers/` and `src/utils/`.
* Storefront Page Objects inherit from `BaseStorefrontPage`; all Page Objects implement `verify_loaded()`.
* Tests express user behavior and business expectations.
* UI locators and UI interaction logic belong in Page Objects/components, not tests.
* Same-page Page Object actions return `Self`; navigation actions return the appropriate destination Page Object.

## Engineering Rules

* Prefer existing abstractions over introducing new ones.
* Keep changes focused on the requested behavior.
* Prefer Playwright web-first assertions and auto-waiting.
* Do not use `time.sleep()` or arbitrary waits.
* Use stable, user-facing or accessibility-based locators where possible.
* Do not use positional locators merely to suppress strict-mode errors.
* Keep tests independent and suitable for parallel execution.
* Add screenshots only at useful diagnostic/state-transition points.
* Use existing reporting and fixture infrastructure rather than duplicating it.
* Do not silently work around unexpected AUT behavior; document intentional limitations.
* Do not change unrelated files or architecture without a concrete reason.

## Validation

After implementation, run the smallest relevant test scope first, then broader checks when practical.

The repository uses Ruff, mypy, pytest, Playwright and Allure. Follow the commands documented in `README.md`.

## Documentation

Business-readable test scenarios are stored under `docs/prestashop/storefront/`.

When adding or changing coverage, keep the scenario documentation and automated tests consistent.
