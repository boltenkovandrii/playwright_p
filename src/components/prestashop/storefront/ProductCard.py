class ProductCard:
    def __init__(self, container):
        self.container = container
        self.product_link = container.locator(".product-title a")
        self.price = container.locator(".price")

    def open(self):
        self.product_link.click()
