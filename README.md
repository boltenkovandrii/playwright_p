## Overview
- This project is created to demonstrate usage of pytest+playwright combination.
- AUT's: 
  - https://www.wikipedia.org/ (will be remover in the future)
  - https://demo.opencart.com/ )WIP_
  - MediaWiki sandbox docker image (WIP)
- CI: GitHub Actions (runs on commits/PRs to main and feature/* branches)
- Reporting: Allure
- Tests themselves are not very meaningful and only serve for demonstrational purposes

## Run tests
- Use resources/scripts/test_run.ps1 for local runs

## Reporting
- For local run reports are generated at reports directory. The easiest way to view allure report is to use "Open in -> Browser" on reports/allure-report/index.html
- CI test results are attached to a run. You can unpack them and view allurer report with: 
  ```bash
  cd test-artifacts\allure-results
  python -m http.server 8080
      ```

## Notes
- It would be better to use dedicated test id instead of 'id' attribute. Working with what we have. 