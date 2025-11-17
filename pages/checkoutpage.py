from selenium.webdriver.common.by import By
from pages.basepage import BasePage
import re

class CheckoutPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    SUMMARY_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX = (By.CLASS_NAME, "summary_tax_label")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH = (By.ID, "finish")
    FINAL = (By.CLASS_NAME, "complete-header")

    def is_page_loaded(self):
        return self.is_visible(self.PAGE_TITLE)

    def fill_details(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)

    def continue_to_overview(self):
        self.click_element(self.CONTINUE_BUTTON)

    def count_items(self):
        elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return len(elements)

    def get_item_prices(self):
        elements = self.driver.find_elements(*self.INVENTORY_ITEM_PRICE)
        prices = []
        for el in elements:
            txt = (el.text or "").strip()
            num = self._parse_currency(txt)
            prices.append(num)
        return prices

    def get_total_price(self):
        text = self.get_text(self.SUMMARY_TOTAL)
        return self._parse_currency(text)

    def complete_checkout(self):
        self.click_element(self.FINISH)
        text = self.get_text(self.FINAL)
        return text

    def _parse_currency(self, text):
        if not text:
            return 0.0
        match = re.search(r"([0-9]+(?:\.[0-9]+)?)", text.replace(",", ""))
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                return 0.0
        return 0.0
