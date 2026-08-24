Remove-Item reports/allure-results -Recurse -Force
Remove-Item reports/allure-report -Recurse -Force
#pytest  -n 8 --browser firefox
#pytest  --headed  -n 8 --browser firefox
#pytest  --headed  -n auto --browser chromium
pytest  -n auto --browser chromium --profile=desktop_1920x1200
#pytest   -n auto --browser chromium --profile=desktop_2560x1600  --profile=tablet --profile=mobile --profile=tablet_landscape --profile=mobile_landscape src/tests/prestashop/test_checkout.py
#pytest   -n auto --browser chromium --profile=desktop_1920x1200 src/tests/prestashop/test_checkout.py
#pytest  --headed  -n auto --browser chromium --profile=desktop_2560x1600 src/tests/prestashop/test_catalog_page.py
#pytest  --headed  -n auto --browser firefox --profile=desktop_2560x1600 src/tests/prestashop/test_catalog_page.py
#pytest  --headed  -n auto --browser chromium --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser chromium --profile=tablet_landscape --profile=mobile_landscape
#pytest  --headed  -n auto --browser chromium --profile=tablet --profile=mobile --profile=desktop_1920x1200
#pytest  -n auto --browser chromium --profile=tablet --profile=mobile --profile=desktop_1920x1200
#pytest  -n 8 --browser chromium --profile=tablet --profile=mobile --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser chromium --profile=mobile
#pytest  -n auto --browser chromium --browser firefox --profile=tablet --profile=mobile --profile=desktop_2560x1600 --profile=tablet_landscape --profile=mobile_landscape --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser chromium --browser firefox --profile=tablet --profile=mobile --profile=desktop_2560x1600 --profile=tablet_landscape --profile=mobile_landscape --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser firefox --profile=tablet --profile=mobile --profile=desktop_2560x1600 --profile=tablet_landscape --profile=mobile_landscape --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser chromium --profile=tablet --profile=mobile --profile=desktop_2560x1600 --profile=tablet_landscape --profile=mobile_landscape --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser chromium --profile=tablet_landscape
#pytest  --headed  -n auto --browser chromium --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser chromium --profile=tablet --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser firefox --profile=tablet
#pytest  --headed  -n auto --browser firefox --profile=desktop_1920x1200 --profile=desktop_2560x1600
#pytest  --headed  -n auto --browser firefox --profile=desktop_2560x1600
#pytest  --headed  -n auto --browser firefox --profile=desktop_1920x1200
#pytest  --headed  -n auto --browser firefox src/tests/test_main_page.py
#pytest  --headed  -n auto --browser chromium --profile=mobile src/tests/test_main_page.py
#pytest  --headed  -n 0 --browser firefox  --browser chromium
#pytest  --headed  -n auto --browser firefox  --browser chromium
Copy-Item reports/history reports/allure-results -Recurse -Force
allure generate reports/allure-results --clean -o reports/allure-report
Copy-Item reports/allure-report/history reports -Recurse -Force