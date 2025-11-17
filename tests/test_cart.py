from pages.loginpage import LoginPage
from pages.productspage import ProductsPage
from pages.cartpage import CartPage

def test_cart_load(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_page_loaded()
    assert cart_page.count_items() == 1

def test_cart_item_description(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    item_name = cart_page.get_item_name()
    item_price = cart_page.get_item_price()

    assert item_name and item_price != None

def test_cart_remove_item(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.remove_first_item()
    assert cart_page.count_items() == 0