from .base_page import BasePage
from locators.feed_locators import (
    ORDER_LINKS, ORDER_MODAL, MODAL_CLOSE, TOTAL_ORDERS, TODAY_ORDERS,
    FEED_ORDER_ITEMS, IN_WORK_ITEMS, FEED_ORDER_NUMBER,
)


class FeedPage(BasePage):
    def open_first_order(self):
        self.click(ORDER_LINKS)
        self.wait.until(lambda _: self.order_modal_visible())

    def close_modal(self):
        self.click(MODAL_CLOSE)
        self.wait.until(lambda _: not self.order_modal_visible())

    def order_modal_visible(self):
        return self.is_any_visible(ORDER_MODAL)

    def get_total_orders(self):
        return int(self.text(TOTAL_ORDERS))

    def get_today_orders(self):
        return int(self.text(TODAY_ORDERS))

    def has_order_in_feed(self, order_number):
        expected = order_number.lstrip('#')
        return any(item.find_element(*FEED_ORDER_NUMBER).text.lstrip('#') == expected
                   for item in self.find_all(FEED_ORDER_ITEMS))

    def get_in_work_order_numbers(self):
        return [item.find_element(*FEED_ORDER_NUMBER).text.lstrip('#')
                for item in self.find_all(IN_WORK_ITEMS)]

    def has_order_in_work(self, order_number):
        return order_number.lstrip('#') in self.get_in_work_order_numbers()
