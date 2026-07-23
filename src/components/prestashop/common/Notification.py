from playwright.sync_api import expect


class Notification:
    def __init__(self, parent):
        self.container = parent.locator("#notifications")

    def verify_loaded(self):
        expect(self.container).to_be_attached()
        return self
