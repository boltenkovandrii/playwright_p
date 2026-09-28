# Copilot Instructions

## General behavior

* Do not commit or push changes unless explicitly asked.
* Inspect the repository and existing implementation before making changes.
* Prefer the smallest correct change that follows the existing architecture.
* Do not invent behavior that is not supported by the application, tests, or documentation.
* If requirements conflict with existing architecture or application behavior, explain the conflict before introducing a workaround.
* Avoid unrelated refactoring.

## Choosing the right agent

Use `test-designer` when the task is primarily about:

* analyzing requirements;
* reviewing existing coverage;
* identifying meaningful test gaps;
* creating or updating business-readable test scenarios.

Use `playwright-implementer` when the task requires:

* implementing or changing Playwright/Pytest tests;
* extending Page Objects or components;
* changing fixtures or test infrastructure;
* debugging or validating automation code.

Do not use the implementer merely to produce a test plan when no implementation is requested.

## Repository context

* Current active automation scope is the PrestaShop storefront.
* Storefront scenarios are documented under `docs/prestashop/storefront/`.
* Supported browsers are Chromium, Firefox and WebKit.
* Device profiles are defined in `src/tests/config/profiles.py`.
* Current demonstrated locales are English (`en`) and Dutch (`nl`).
* The HTML `id` attribute is configured as Playwright's test-id attribute because of the AUT's available markup.
* The AUT can occasionally return mixed-language content after runtime locale changes. Do not attempt to "fix" the application in the automation framework; follow the documented localization-test scope.

## Validation

For Python changes, use the repository quality checks where applicable:

```text
ruff check .
ruff format --check .
mypy .
```

For automation changes, run the smallest relevant pytest scope first.

Use the existing Allure, trace, video and screenshot infrastructure for diagnostics.

## Test design principles

* Prefer meaningful user-facing scenarios over exhaustive combinations.
* Reuse existing Page Objects/components and fixtures.
* Keep browser/profile/locale parametrization purposeful.
* Do not put UI locators or DOM-level interaction logic directly in tests.
* Do not introduce framework abstractions for one-off interactions.
