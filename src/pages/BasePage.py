class BasePage:

    def __init__(self, page):
        self.page = page


    def verify_loaded(self):
        raise NotImplementedError(
            "Page must implement verify_loaded() method"
        )
