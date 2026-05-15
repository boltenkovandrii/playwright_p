Remove-Item reports/allure-results -Recurse -Force
Remove-Item reports/allure-report -Recurse -Force
pytest  --headed
Copy-Item reports/history reports/allure-results -Recurse -Force
allure generate reports/allure-results --clean -o reports/allure-report
Copy-Item reports/allure-report/history reports -Recurse -Force