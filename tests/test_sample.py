import time
import allure

from utils.allure_reporting import attach_screenshot


#@allure.feature("Some feature") ???
@allure.title("Some test")
#@allure.description("Some testttt")
#@allure.label("flaky", "true")
@allure.suite("Test suite")
def test_sample(page):
    page.goto("https://www.wikipedia.org/")
    time.sleep(1)

#    if random.randrange(2)%2==-0 :
#        expect(page).to_have_title("Wikipedia--")
#    else:
#        expect(page).to_have_title("Wikipedia")

    page.get_by_role("button", name="Close").click()
    page.get_by_role("searchbox").fill("TypeScript")

    attach_screenshot(page,"Before search")


    page.get_by_role("button", name="Search").click()

#    page.pause()