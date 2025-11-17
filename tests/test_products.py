from pages.productspage import ProductsPage
from pages.loginpage import LoginPage

def test_products_loaded(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductsPage(driver)
    assert products_page.is_page_loaded()
    assert products_page.count_products() > 0

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()

    assert products_page.get_cart_count() == "1"

