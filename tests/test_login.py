from pages.loginpage import LoginPage

def test_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert page.is_logged_in()

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("yyyyyyy", "xxxxxx")
    assert page.has_error()
    msg = page.get_error_message()
    assert msg != ""