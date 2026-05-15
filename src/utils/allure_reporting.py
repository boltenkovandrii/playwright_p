import allure



def attach_screenshot(page, name):
    allure.attach(
        page.screenshot(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )