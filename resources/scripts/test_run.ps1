# file contains various commands for running tests with different configurations
# Used for debug and somewhat messy. Will be cleaned up in some (relatively far) future.

Remove-Item reports/allure-results -Recurse -Force
Remove-Item reports/allure-report -Recurse -Force

#pytest  -n 12 --browser firefox
#pytest  --headed  -n 8 --browser firefox
pytest  -n 4 --browser chromium src/tests/prestashop/test_localization1.py

#pytest  --headed  -n auto --browser firefox  --browser chromium
#pytest  --headed  -n 0 --browser firefox  --browser chromium
#pytest  -n 8 --browser chromium --profile=desktop_1920x1200
#pytest   -n 8 --browser chromium --profile=desktop_2560x1600  --profile=tablet --profile=mobile --profile=tablet_landscape --profile=mobile_landscape src/tests/prestashop/test_localization.py
#pytest   -n 8 --browser firefox --browser chromium --browser webkit --profile=desktop_1920x1200 src/tests/prestashop/test_account.py
#pytest   -n 8 --browser chromium --profile=desktop_1920x1200 src/tests/prestashop/test_account.py
#pytest  --headed  -n auto --browser chromium --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser chromium --profile=tablet_landscape --profile=mobile_landscape
#pytest  -n 8 --browser chromium --profile=tablet --profile=mobile --profile=desktop_1920x1200 src/tests/prestashop/test_localization.py
#pytest  -n 8 --browser chromium --profile=tablet --profile=mobile --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser chromium --profile=mobile
#pytest  -n 8 --browser chromium --browser webkit --browser firefox --profile=tablet --profile=mobile --profile=desktop_2560x1600 --profile=tablet_landscape --profile=mobile_landscape --profile=desktop_1920x1200
#pytest  -n 8 --browser chromium --profile=tablet --profile=mobile --profile=desktop_2560x1600 --profile=tablet_landscape --profile=mobile_landscape --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser chromium --browser firefox --profile=tablet --profile=mobile --profile=desktop_2560x1600 --profile=tablet_landscape --profile=mobile_landscape --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser chromium --profile=mobile src/tests/test_main_page.py

Copy-Item reports/history reports/allure-results -Recurse -Force
allure generate reports/allure-results --clean -o reports/allure-report
Copy-Item reports/allure-report/history reports -Recurse -Force