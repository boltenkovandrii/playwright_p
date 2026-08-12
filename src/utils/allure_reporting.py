from pathlib import Path

import allure


def attach_screenshot(target, name, full_page=True):
    if full_page:
        screenshot = target.screenshot(full_page=True)
    else:
        screenshot = target.screenshot()

    allure.attach(
        screenshot,
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )

def attach_playwright_artifacts(output_path):
    output_dir = Path(output_path)
    for trace in output_dir.glob("trace*.zip"):
        allure.attach.file(
            str(trace),
            name="Trace",
            attachment_type=allure.attachment_type.ZIP,
        )

    for video in output_dir.glob("video*.webm"):
        allure.attach.file(
            str(video),
            name="Video",
            attachment_type="video/webm",
        )