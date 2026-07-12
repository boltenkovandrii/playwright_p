Playwright setup

Run these steps once after installing dependencies to download browser binaries:

Local (developer machine):

1. Install Python deps:
    pip install -e .
2. Install allure-commandline using scoop (on Windows)
   irm get.scoop.sh | iex
   scoop install allure
3. Install Playwright browsers:
   python -m playwright install

CI (GitHub Actions, Ubuntu):

- After installing Python deps, run:
  python -m playwright install --with-deps

- To install only specific browsers (faster):
  python -m playwright install --with-deps firefox chromium

Notes:
- Use `python -m playwright install --with-deps` on CI runners to install system dependencies where available.
- The CI workflow supports specifying the browser set at runtime (workflow_dispatch input `browsers`). Examples:
  - Single browser (feature branch default): firefox
  - Full set (main branch default): firefox chromium
  - Manual run with specific browsers: provide `browsers` input as `firefox` or `firefox,chromium`.
- For Windows developers, `playwright install` is usually sufficient.
