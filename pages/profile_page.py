from .base_page import BasePage
from locators.account_locators import ORDER_HISTORY_LINK, LOGOUT_BUTTON


class ProfilePage(BasePage):
    def open_order_history(self):
        self.click(ORDER_HISTORY_LINK)

    def logout(self):
        self.click(LOGOUT_BUTTON)
        self.url_contains('/login')