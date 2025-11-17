from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class ProductsPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEM = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")

    def is_page_loaded(self):
        return self.is_visible(self.PAGE_TITLE)

    def get_all_products(self):
        return self.driver.find_elements(*self.PRODUCT_ITEM)

    def count_products(self):
        return len(self.get_all_products())

    def add_first_product_to_cart(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if len(buttons) > 0:
            buttons[0].click()
        else:
            raise Exception("No Add-to-Cart buttons found on products page.")

    def get_cart_count(self, timeout=5):
        if self.is_visible(self.CART_BADGE, timeout):
            return self.get_text(self.CART_BADGE)
        return "0"

    def open_cart(self):
        self.click_element(self.CART_BUTTON)
