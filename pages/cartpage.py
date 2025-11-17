from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class CartPage(BasePage):
    CART_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_ITEM_NAME = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Checkout')]")

    def is_page_loaded(self):
        return  self.is_visible(self.CART_TITLE)

    def get_item_name(self):
        elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return [el.text.strip() for el in elements]

    def get_item_price(self):
        elements = self.driver.find_elements(*self.INVENTORY_ITEM_PRICE)
        return [el.text.strip() for el in elements]

    def count_items(self):
        elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return len(elements)

    def remove_first_item(self):
        remove_buttons = self.driver.find_elements(*self.REMOVE_ITEM_NAME)
        if remove_buttons:
            remove_buttons[0].click()
        else:
            raise Exception("No buttons found")

    def checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)

