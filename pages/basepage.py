from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            print("Timed out")
            return None

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            element.click()

    def type_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            element.send_keys(text)

    def is_visible(self, locator, timeout=10):
        try:
            element = self.find_element(locator, timeout)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def get_text(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        if element:
            return element.text.strip()
        return ""

    def get_current_url(self):
        return self.driver.current_url