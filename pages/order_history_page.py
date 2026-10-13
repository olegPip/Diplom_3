from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from locators.account_locators import ORDER_HISTORY_ITEMS, ORDER_HISTORY_NUMBER


class OrderHistoryPage(BasePage):

    def has_orders(self):
        return bool(self.driver.find_elements(*ORDER_HISTORY_ITEMS))

    def get_first_order_number(self):
        item = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ORDER_HISTORY_ITEMS)
        )

        return item.find_element(
            *ORDER_HISTORY_NUMBER
        ).text.lstrip('#')