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
pytest --browser chromium --profile=desktop
pytest --browser chromium --profile=mobile
pytest --browser chromium --profile=tablet_landscape
```

#### Run a single test
```powershell
pytest src/tests/test_main_page.py::test_main_page_title --browser chromium

# With specific parametrized locale (en, nl, uk)
pytest src/tests/test_main_page.py::test_main_page_title[en] --browser chromium
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
- **Page Objects** (`src/pages/*.py`): Encapsulate page elements and actions (e.g., `MainPage`, `HomePage`, `ArticlePage`)
- **Components** (`src/components/*.py`): Reusable UI components used by pages (e.g., `Header`, `ContentMain`)
- **Tests** (`src/tests/test_*.py`): Test files use fixtures that instantiate page objects and components

### Test Structure

```
src/
├── pages/           # Page objects (MainPage, HomePage, ArticlePage, BasePage)
├── components/      # Reusable UI components (Header, ContentMain, Appearance, etc.)
├── fixtures/        # Pytest fixtures (pages, locale, profile)
├── tests/           # Test files (test_*.py) and conftest.py
└── utils/           # Utilities (allure_reporting, etc.)
```

### Key Test Concepts

#### Locales
Tests use the `locale` fixture to parametrize tests across multiple languages (`en`, `nl`, `uk`):
```python
@pytest.mark.parametrize("locale", ["en", "nl", "uk"], indirect=True)
def test_example(main_page):
    # main_page.locale is automatically set by fixture
    pass
```

#### Device Profiles
Tests can run against multiple device profiles defined in `src/tests/config/profiles.py`:
- **Desktop**: `desktop`, `desktop_1920x1200`, `desktop_2560x1600`
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
- Components are organized by AUT (Application Under Test) in subdirectories (`mediawiki/`, `prestashop/`)
- Components provide methods to verify structure (e.g., `check_structure()`)
- Components are passed a `page` object or parent container for element interaction

### Test Files
- Prefix test functions with `test_`
- Use Allure decorators for documentation: `@allure.title()`, `@allure.suite()`, `@allure.description()`
- Use Playwright's `expect()` for assertions
- Attach artifacts with `attach_screenshot()` for visual debugging
- Keep tests parametrized for multiple locales/profiles when applicable

### Fixtures (in conftest.py)
- `main_page`: MainPage fixture with locale support
- `home_page`: HomePage fixture
- `article_page`: ArticlePage fixture with locale support
- `profile`: Device profile fixture (desktop, mobile, tablet)
- `locale`: Locale fixture (en, nl, uk)
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

- **Wikipedia** (`https://www.wikipedia.org/`): Main test subject (MainPage, ArticlePage, HomePage)
- **Prestashop** (Docker image): Work in progress (WIP)
- **MediaWiki Sandbox** (Docker image): Work in progress (WIP)

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
1. Create a test function in `src/tests/test_*.py` with `test_` prefix
2. Use page fixtures (`main_page`, `home_page`, etc.)
3. Add Allure decorators for reporting
4. Parametrize with `locale` fixture if testing multi-language behavior
5. Use `expect()` for assertions and `attach_screenshot()` for visual artifacts

### Add a new page
1. Create `PageName.py` in `src/pages/`
2. Inherit from `BasePage` and implement `verify_loaded()`
3. Define locators and interaction methods
4. Methods should return `self` for chaining
5. Add a pytest fixture in `src/fixtures/pages.py`

### Add a new component
1. Create component in `src/components/` (or subdirectory for specific AUT)
2. Provide a `check_structure()` method for verification
3. Implement element interaction methods
4. Import and use in page objects

### Run tests for a specific feature branch
```powershell
# Feature branches default to firefox; manually add other browsers:
pytest --browser firefox --browser chromium --profile=desktop

# Or use the resources/scripts/test_run.ps1 and edit as needed
```

### Debug a failing test
1. Check the Allure report in `reports/allure-report/` for screenshots and traces
2. Re-run with `--headed` flag to see browser in action: `pytest --headed --browser chromium src/tests/test_file.py::test_name`
3. Use `--trace=on` to record Playwright traces (useful for debugging element interactions)
4. Videos and traces are retained on failure by default; view in Allure or use Playwright Inspector

---

## Notes

- Tests are demonstrational; not all are production-ready
- Test IDs use `id` attribute instead of the standard `data-testid` (working with what's available)
- Allure report history is persisted in `reports/history/` for trend analysis
- Windows developers: `playwright install` is usually sufficient; CI uses `--with-deps` for system dependencies
