# Playwright Setup

This file is a short setup reference.
For the primary onboarding flow, execution examples, and framework scope, see `README.md`.

## Local setup

```powershell
pip install -e .
python -m playwright install
```

Optional on Windows for generating Allure HTML reports locally:

```powershell
scoop install allure
```

## CI setup

On CI runners, use:

```powershell
python -m playwright install --with-deps
```

To install only a subset of browsers:

```powershell
python -m playwright install --with-deps firefox chromium
```

## Notes

- For Windows developers, `python -m playwright install` is usually sufficient.
- The active automated scope in this repository is the **PrestaShop storefront**.
