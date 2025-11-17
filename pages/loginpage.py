from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class LoginPage(BasePage):

    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    PAGE_TITLE = (By.ID, 'page-title')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error-message-container')

    def open(self, url = "https://www.saucedemo.com"):
        self.open_url(url)
        return self

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)
        return self

    def is_logged_in(self):
        return "inventory" in self.get_current_url()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def has_error(self):
        return self.is_visible(self.ERROR_MESSAGE)