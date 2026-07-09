import allure



def attach_screenshot(element, name):
    allure.attach(
        element.screenshot(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )