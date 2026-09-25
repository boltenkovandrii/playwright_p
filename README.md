## Overview
- This project is created to demonstrate usage of pytest+playwright combination.
- Prestashop sandbox docker image is used as application under test
- CI: GitHub Actions (runs on commits/PRs to main and feature/* branches)
- Reporting: Allure
- Project supports various combinations of browsers and profiles (desktop, mobile, tablet) for testing.
- Test coverage is rather limited, but it is enough to demonstrate the approach.

## Run tests
- Start required application(s) with docker-compose using docker/docker-compose-prestashop.yml
- Use resources/scripts/test_run.ps1 for local runs

## Prestashop
- Start application: **docker-compose -f docker/docker-compose-prestashop.yml up -d**
- Set `PRESTASHOP_BASE_URL` in `.env` to configure the application root URL for tests.
- Default URL: http://localhost:8090
- Default Admin URL: http://localhost:8090/admin-dev/ (not covered in tests)
- Admin credentials: demo@prestashop.com/prestashop_demo
- One employee per language is created with the same password (demo<iso_code>@prestashop.com) - i.e. demofr@prestashop.com

## Reporting
- For local run reports are generated at reports directory. The easiest way to view allure report is to use "Open in -> Browser" on reports/allure-report/index.html
- CI test results are attached to a run. You can unpack them and view allure report with: 
  ```bash
  cd test-artifacts\allure-results
  python -m http.server 8080
      ```

## Notes
- It would be better to use dedicated test id instead of 'id' attribute. Working with what we have. 