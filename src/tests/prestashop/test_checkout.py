import allure


@allure.suite("PrestaShop storefront - Checkout (Guest)")
@allure.title("CHK-01 — Guest checkout page structure and checkout flow")
def test_guest_checkout_page_structure(prestashop_home_page):
    product_name = "Hummingbird printed t-shirt"
    first_name = "Jane"
    last_name = "Doe"
    email = "jane.doe.chk01@example.com"
    address_line_1 = "221B Baker Street"
    city = "Paris"
    postal_code = "75001"
    country = "France"
    phone = "5551234567"
    shipping_method = "My carrier"
    payment_method = "Pay by Cash on Delivery"
    payment_method_confirmation = "Cash on delivery (COD)"
    expected_subtotal = 22.94
    expected_shipping = 8.40
    expected_total = 31.34

    catalog_page = prestashop_home_page.open().open_category("Clothes")
    product_page = catalog_page.open_product_by_name(product_name)
    cart_page = product_page.add_to_cart().go_to_cart()

    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.check_structure()

    checkout_page.check_personal_info_structure()
    checkout_page.fill_personal_info(first_name=first_name, last_name=last_name, email=email)

    checkout_page.check_addresses_structure()
    checkout_page.fill_address(address_line_1=address_line_1, city=city, postal_code=postal_code, country=country, phone=phone, state=None)

    checkout_page.check_shipping_method_structure()
    checkout_page.fill_shipping_method(name=shipping_method)
    checkout_page.check_payment_structure()

    order_confirmation_page = (
        checkout_page
        .select_payment_method(method_name=payment_method)
        .accept_terms()
        .place_order()
    )

    order_confirmation_page.check_structure()
    order_confirmation_page.verify_order_reference_present()
    order_confirmation_page.verify_product_with_name_present(product_name)
    order_confirmation_page.verify_subtotal_amount(expected_subtotal)
    order_confirmation_page.verify_shipping_amount(expected_shipping)
    order_confirmation_page.verify_total_amount(expected_total)
    order_confirmation_page.verify_shipping_method(shipping_method)
    order_confirmation_page.verify_payment_method(payment_method_confirmation)

