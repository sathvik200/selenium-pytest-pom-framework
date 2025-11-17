from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.basepage import BasePage

def test_open_website():
    driver = webdriver.Chrome()
    page = BasePage(driver)
    page.open_url("https://www.saucedemo.com")
    page.type_text((By.ID, "user-name"), "standard_user")
    page.type_text((By.ID, "password"), "secret_sauce")

    page.click_element((By.ID, "login-button"))

    assert "inventory" in driver.current_url

    driver.quit()