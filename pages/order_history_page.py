from .base_page import BasePage
from locators.account_locators import ORDER_HISTORY_ITEMS, ORDER_HISTORY_NUMBER


class OrderHistoryPage(BasePage):
    def has_orders(self):
        return bool(self.find_all(ORDER_HISTORY_ITEMS))

    def get_first_order_number(self):
        item = self.wait.until(lambda _: self.find(ORDER_HISTORY_ITEMS))
        return item.find_element(*ORDER_HISTORY_NUMBER).text.lstrip('#')
