from .base_page import BasePage
from locators.common_locators import HEADER_CONSTRUCTOR, HEADER_ORDER_FEED, HEADER_PERSONAL_ACCOUNT


class Header(BasePage):
    def open_constructor(self):
        self.click(HEADER_CONSTRUCTOR)

    def open_order_feed(self):
        self.click(HEADER_ORDER_FEED)

    def open_personal_account(self):
        self.click(HEADER_PERSONAL_ACCOUNT)
