# Copilot Instructions for Playwright Automation Framework

## Important for AI Tools

**Never commit or push changes unless directly told to do so.** Always ask before making commits or pushing to any branch.

---

## Quick Start

### Build and Test

#### Run all tests (locally)
```powershell
# From repository root
resources/scripts/test_run.ps1
```

#### Run tests with pytest directly
```powershell
# All tests with parallelization
pytest -n auto --browser chromium

# Single browser
pytest --browser firefox

# All browsers (main branch default)
pytest --browser firefox --browser chromium --browser webkit

# With specific profile (device emulation)
pytest --browser chromium --profile=desktop_1920x1200
pytest --browser chromium --profile=mobile
pytest --browser chromium --profile=tablet_landscape
```

#### Run a single test
```powershell
pytest src/tests/prestashop/test_home_page.py::test_home_page_structure --browser chromium

# Run a full storefront suite file
pytest src/tests/prestashop/test_home_page.py --browser chromium
```

#### View test reports
- Local reports are generated in `reports/allure-report/` directory
- Open `reports/allure-report/index.html` in a browser to view results
- Test run artifacts (screenshots, traces, videos) are stored in `reports/allure-results/`

### Initial Setup

Before running tests:
```powershell
# Install Python dependencies
pip install -e .

# Install Playwright browsers
python -m playwright install

# (Windows) Install Allure for reports (optional, uses scoop)
scoop install allure
```

---

## Architecture

### Page Object Model Pattern

The codebase uses the Page Object Model (POM) pattern to abstract page interactions:

- **Base Pages** (`src/pages/BasePage.py`): All page objects inherit from `BasePage`, which provides the Playwright `page` object
- **Page Objects** (`src/pages/prestashop/storefront/*.py`): Encapsulate storefront elements and actions (e.g., `HomePage`, `CatalogPage`, `ProductPage`, `CheckoutPage`)
- **Components** (`src/components/prestashop/storefront/*.py`): Reusable storefront UI components (e.g., `Header`, `Footer`, `ProductGrid`, `ProductCard`)
- **Tests** (`src/tests/prestashop/test_*.py`): Test files use fixtures that instantiate page objects and components

### Test Structure

```
src/
├── pages/           # Base page + PrestaShop storefront page objects
├── components/      # Reusable PrestaShop storefront UI components
├── fixtures/        # Pytest fixtures (locale, profile, PrestaShop pages)
├── tests/           # Test files and shared pytest configuration
└── utils/           # Utilities (allure_reporting, etc.)
```

### Key Test Concepts

#### Locales
The framework is designed so more storefront languages can be added easily. The currently demonstrated locale coverage is `en` and `nl`:
```python
@pytest.mark.parametrize("locale", ["en", "nl"], indirect=True)
def test_example(prestashop_home_page, locale):
    # prestashop_home_page.locale is automatically set by fixture
    pass
```

#### Device Profiles
Tests can run against multiple device profiles defined in `src/tests/config/profiles.py`:
- **Desktop**: `desktop_1920x1200`, `desktop_2560x1600`
- **Mobile**: `mobile`, `mobile_landscape` (iPhone 13)
- **Tablet**: `tablet`, `tablet_landscape` (iPad Mini)

Run with `--profile=<profile_name>` or parametrize tests using the `profile` fixture.

#### Browsers
Supported browsers: `firefox`, `chromium`, `webkit`

Use `--browser=<browser>` to specify browsers or provide multiple `--browser` flags.

---

## Key Conventions

### Page Objects
- All page objects inherit from `BasePage` and must implement `verify_loaded()` method
- Page methods should return `self` to enable method chaining
- Use `self.page` to access the Playwright page context
- Locators should use the test ID attribute (`id` attribute) where possible; avoid relying on generic selectors

### Components
- Components are organized by AUT area; current active coverage uses `prestashop/storefront/`
- Components provide methods to verify structure (e.g., `check_structure()`)
- Components are passed a `page` object or parent container for element interaction

### Test Files
- Prefix test functions with `test_`
- Use Allure decorators for documentation: `@allure.title()`, `@allure.suite()`, `@allure.description()`
- Use Playwright's `expect()` for assertions
- Attach artifacts with `attach_screenshot()` for visual debugging
- Keep tests parametrized for multiple locales/profiles when applicable

### Fixtures (in conftest.py)
- `prestashop_home_page`: HomePage fixture with locale support
- `prestashop_backoffice_login_page`: Backoffice login fixture exists, but current active automated coverage is storefront-focused
- `profile`: Device profile fixture (desktop_1920x1200, mobile, tablet, etc)
- `locale`: Locale fixture (`en` by default; current demonstrated coverage uses `en` and `nl`)
- `page`: Playwright page context with final screenshot attachment on teardown

### Test Configuration (pytest.ini)
- All tests are configured to generate Allure results in `reports/allure-results/`
- Tests are retried once on failure (`--reruns 1`)
- Screenshots, traces, and videos are retained on failure only
- Test ID attribute is set to `id` (non-standard; typically `data-testid`)

### Translations
- Multi-language support via `resources/translations.py`
- Tests parametrize over locales and use locale-specific translations for assertions

### Parallel Execution
- Use pytest-xdist with `-n auto` for automatic parallel distribution
- Firefox doesn't support mobile emulation (tests skip Firefox with non-desktop profiles)

---

## Testing AUTs (Applications Under Test)

- **PrestaShop Storefront** (`PRESTASHOP_BASE_URL`): Current active automated test scope
- Storefront scenarios are documented under `docs/prestashop/storefront/`
- Backoffice is not part of the current active automated coverage

---

## CI/CD

- Tests run on GitHub Actions for commits/PRs to `main` and `feature/*` branches
- Workflow is triggered by push, pull_request, and workflow_dispatch
- Manual workflow_dispatch allows specifying custom browser/profile combinations
- All test artifacts (Allure reports, screenshots, traces, videos) are uploaded and retained for 3 days
- On main branch: all browsers (firefox, chromium, webkit) run by default
- On feature branches/PRs: firefox runs by default

---

## Common Tasks

### Add a new test
1. Create a test function in `src/tests/prestashop/test_*.py` with `test_` prefix
2. Use existing page fixtures such as `prestashop_home_page`
3. Add Allure decorators for reporting
4. Parametrize with `locale` fixture if testing multi-language behavior
5. Use `expect()` for assertions and `attach_screenshot()` for visual artifacts

### Add a new page
1. Create `PageName.py` in the appropriate package, typically `src/pages/prestashop/storefront/`
2. Inherit from `BasePage` and implement `verify_loaded()`
3. Define locators and interaction methods
4. Methods should return `self` for chaining
5. Add or extend a pytest fixture in `src/fixtures/prestashop/pages.py` when needed

### Add a new component
1. Create component in `src/components/prestashop/storefront/` for storefront coverage
2. Provide a `check_structure()` method for verification
3. Implement element interaction methods
4. Import and use in page objects

### Run tests for a specific feature branch
```powershell
# Feature branches default to firefox; manually add other browsers:
pytest --browser firefox --browser chromium --profile=desktop_1920x1200

# Or use the resources/scripts/test_run.ps1 and edit as needed
```

### Debug a failing test
1. Check the Allure report in `reports/allure-report/` for screenshots and traces
2. Re-run with `--headed` flag to see browser in action: `pytest --headed --browser chromium src/tests/prestashop/test_home_page.py::test_home_page_structure`
3. Use `--trace=on` to record Playwright traces (useful for debugging element interactions)
4. Videos and traces are retained on failure by default; view in Allure or use Playwright Inspector

---

## Notes

- Current active automation is storefront-only
- Tests are demonstrational; not all are production-ready
- Test IDs use `id` attribute instead of the standard `data-testid` (working with what's available)
- Allure report history is persisted in `reports/history/` for trend analysis
- Windows developers: `playwright install` is usually sufficient; CI uses `--with-deps` for system dependencies


Temporary artifacts:

- Temporary scripts, files, logs, screenshots, dumps, and other artifacts
  created solely for investigation must be removed before completing the task.
- Do not add temporary investigation artifacts to the repository unless
  they provide lasting project value.
- Prefer existing project tooling for inspection when practical.
- If a temporary artifact is intentionally retained, explain why.