Remove-Item reports/allure-results -Recurse -Force
Remove-Item reports/allure-report -Recurse -Force
pytest  --headed  -n 8 --browser firefox
#pytest  --headed  -n auto --browser firefox
#pytest  --headed  -n auto --browser firefox src/tests/test_main_page.py
#pytest  --headed  -n 0 --browser firefox  --browser chromium
#pytest  --headed  -n auto --browser firefox  --browser chromium
Copy-Item reports/history reports/allure-results -Recurse -Force
allure generate reports/allure-results --clean -o reports/allure-report
Copy-Item reports/allure-report/history reports -Recurse -Force