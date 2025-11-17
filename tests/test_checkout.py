from operator import contains

from pages.loginpage import LoginPage
from pages.productspage import ProductsPage
from pages.cartpage import CartPage
from pages.checkoutpage import CheckoutPage

def test_checkout_load(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    check_out_page = CheckoutPage(driver)
    assert check_out_page.is_page_loaded()

def test_products_count(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    check_out_page = CheckoutPage(driver)
    check_out_page.fill_details("Tester", "Selenium", "123456")
    check_out_page.continue_to_overview()
    assert check_out_page.count_items() == 1

def test_final_price(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    check_out_page = CheckoutPage(driver)
    check_out_page.fill_details("Tester", "Selenium", "123456")
    check_out_page.continue_to_overview()
    assert check_out_page.get_total_price() != None

def test_checkout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    check_out_page = CheckoutPage(driver)
    check_out_page.fill_details("Tester", "Selenium", "123456")
    check_out_page.continue_to_overview()
    assert "Thank you for your order!" in check_out_page.complete_checkout()