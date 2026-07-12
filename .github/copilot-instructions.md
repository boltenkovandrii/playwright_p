# Copilot Instructions for python_playwright

## Important: Git Commits & Pushes

**Never commit or push changes unless directly told to do so.** Always verify requested changes are working correctly first, and wait for explicit instruction before committing.

## Quick Start

This is a **Playwright test automation framework** for Wikipedia (AUT: https://www.wikipedia.org/). It uses pytest for test organization and Allure for reporting.

### Setup
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
python -m playwright install
```

## Build, Test & Lint

### Run All Tests
```powershell
./resources/scripts/test_run.ps1
```

### Run Single Test
```powershell
pytest src/tests/test_home_page.py::test_home_page_search --headed -n 0
```

### Run Tests in Headless Mode (CI)
```powershell
pytest --headed=false
```

### Run with Specific Browser
```powershell
pytest --headed -n 8 --browser firefox
```

### View Allure Report
After running tests:
```powershell
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
```

## Architecture

### Page Object Model (POM)
This project follows the **Page Object Model pattern** for maintainability:

- **BasePage** (`src/pages/BasePage.py`): Abstract base class with `verify_loaded()` method
- **Page classes** (`src/pages/`): Inherit from BasePage, encapsulate page-specific selectors and interactions
  - Each page implements `verify_loaded()` to verify the page is in expected state
  - Methods are chainable and return the next page object (supports fluent API)
  - Use Playwright's built-in selectors (role-based, accessibility-friendly)

### Component Model
- **Components** (`src/components/`): Reusable UI components (Header, Appearance, ContentMain, ContentArticle)
- Used by page objects to structure complex pages

### Fixtures & Conftest
- **`src/tests/conftest.py`**: 
  - Configures pytest-playwright fixtures (browser, context, page)
  - Sets viewport to 1920x1080 by default
  - Attaches final screenshot on test completion
  - Sets `"id"` as test ID attribute for selectors
  - Loads plugin fixtures from `tests.fixtures.pages` and `tests.fixtures.locale`

- **`src/tests/fixtures/pages.py`**: Page fixtures (home_page, article_page, main_page)
- **`src/tests/fixtures/locale.py`**: Locale fixture for multilingual testing

### Test Organization
- **`src/tests/test_*.py`**: Test files (pytest discovers with `test_*` pattern)
- Tests are marked with `@allure.suite()` and `@allure.title()` for reporting
- Tests use page fixtures and fluent API for readability:
  ```python
  home_page.open().close_donation_banner().search("playwright")
  ```

### Utils & Resources
- **`src/utils/allure_reporting.py`**: Screenshot attachment helpers
- **`src/utils/snapshots.py`**: Snapshot-based testing utilities
- **`resources/translations.py`**: Multilingual content (en, uk, nl)
- **`resources/snapshots/`**: YAML snapshot files for visual regression testing

## Key Conventions

1. **Fluent API**: Page methods should return `self` (for same page) or new page objects to support chaining
   ```python
   def search(self, text):
       self.page.get_by_role("searchbox").fill(text)
       self.page.get_by_role("button", name="Search").click()
       return ArticlePage(self.page).verify_loaded()  # Returns next page
   ```

2. **Selector Preference**:
   - Prefer role-based selectors: `page.get_by_role()`
   - Use accessibility-first approach: `page.get_by_label()`
   - Avoid CSS/XPath when possible (fragile); use only when necessary
   - Selectors configured to use `"id"` attribute as test ID (set in conftest)

3. **Screenshot Attachments**: Use `attach_screenshot(page, "description")` to add screenshots to Allure reports
   - Screenshots auto-attach on test completion
   - Manually attach on key interactions for better reporting

4. **Verify Loaded**: Every page object must implement `verify_loaded()` to confirm page state
   ```python
   def verify_loaded(self):
       expect(self.page.get_by_label("Top languages")).to_be_visible()
       return self
   ```

5. **pytest Configuration** (`pytest.ini`):
   - Auto-retry failed tests (1 retry, 1 sec delay)
   - Trace/video retained only on failure (no overhead on passing tests)
   - Allure results go to `reports/allure-results`

6. **Multilingual Testing**: Use `locale` fixture to parameterize tests across languages (en, uk, nl)

7. **Parallel Execution**: Default to 8 workers (`-n 8`). Adjust based on resource availability

## CI/CD Pipeline

Tests run automatically on every commit/PR to `main` and `feature/*` branches via GitHub Actions:

- **Parallel Execution**: Tests run concurrently across Firefox and Chromium (4 workers each)
- **Artifacts**: Allure reports, test traces, and videos uploaded to workflow run
- **Retention**: Artifacts kept for 3 days
- **Report**: Merged Allure report combining results from all browser runs
- **PR Comments**: Workflow comments on PRs with link to Allure report

## Important Notes

- **Snapshot Testing Caveat**: Wiki is multilingual; component structure varies by language. Snapshots are for demonstration only—not reliable for multilingual apps. Prefer explicit assertions.
- **Browser Binaries**: Windows developers use `python -m playwright install`. CI runners use `python -m playwright install --with-deps` to install system dependencies.
