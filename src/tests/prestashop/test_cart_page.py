import allure

from helpers.prestashop.ProductSpec import ProductSpec


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("CART-01 — Check cart page structure")
def test_cart_page_structure(prestashop_home_page, profile):
    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product(0)
    cart_page = product_page.add_to_cart().go_to_cart()
    cart_page.check_structure()


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("CART-02 — Add single product to cart")
def test_add_single_product_to_cart(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"

    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)
    cart_page = product_page.add_to_cart().go_to_cart()

    cart_page.verify_product_count(1)
    cart_page.verify_product_quantity(ProductSpec(name=product_name), 1)


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("CART-03 — Add multiple quantities from Product Page")
def test_add_multiple_quantities(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"

    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)

    product_page.verify_header_cart_count(0)

    product_page.set_quantity(3)
    cart_page = product_page.add_to_cart().go_to_cart()

    cart_page.verify_product_count(1)
    cart_page.verify_product_quantity(ProductSpec(name=product_name), 3)


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("CART-04 — Remove product from cart")
def test_remove_product_from_cart(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"

    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)
    cart_page = product_page.add_to_cart().go_to_cart()

    cart_page.remove_product(ProductSpec(name=product_name))
    cart_page.check_empty_structure()


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("CART-05 — Update product quantity in cart")
def test_update_product_quantity(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"

    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)
    cart_page = product_page.add_to_cart().go_to_cart()

    product_spec = ProductSpec(name=product_name)

    cart_page.verify_product_quantity(product_spec, 1)
    cart_page.verify_products_subtotal(22.94)
    cart_page.verify_total(22.94)

    cart_page.set_product_quantity(product_spec, 2)
    cart_page.verify_product_quantity(product_spec, 2)
    cart_page.verify_products_subtotal(45.89)
    cart_page.verify_total(45.89)


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("CART-06 — Continue shopping from cart")
def test_continue_shopping_from_cart(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"

    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)
    cart_page = product_page.add_to_cart().go_to_cart()

    home_page = cart_page.continue_shopping()
    home_page.verify_header_cart_count(1)

    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)
    cart_page = product_page.add_to_cart().go_to_cart()

    home_page = cart_page.continue_shopping()
    home_page.verify_header_cart_count(2)


@allure.suite("PrestaShop storefront - Shopping Cart")
@allure.title("CART-07 — Verify cart totals for multiple variants")
def test_verify_cart_totals(prestashop_home_page, profile):
    product_name = "Hummingbird printed t-shirt"

    catalog_page = prestashop_home_page.open().open_category(profile, "Clothes")
    product_page = catalog_page.open_product_by_name(product_name)

    product_page = product_page.select_size("M")
    product_page = product_page.select_color("Black")
    product_page.set_quantity(2)
    product_page = product_page.add_to_cart().continue_shopping()

    product_page = product_page.select_size("XL")
    product_page = product_page.select_color("White")
    product_page.set_quantity(3)
    cart_page = product_page.add_to_cart().go_to_cart()

    product_spec1 =  ProductSpec(name=product_name, attributes={"size": "M", "color": "Black"})
    product_spec2 =  ProductSpec(name=product_name, attributes={"size": "XL", "color": "White"})

    cart_page.verify_product_count(2)
    cart_page.verify_product_quantity(product_spec1, 2)
    cart_page.verify_product_quantity(product_spec2, 3)

    cart_page.verify_products_subtotal(114.72)
    cart_page.verify_total(114.72)
