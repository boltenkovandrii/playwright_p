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

Notes:
- Use `python -m playwright install --with-deps` on CI runners to install system dependencies where available.
- For Windows developers, `playwright install` is usually sufficient.
