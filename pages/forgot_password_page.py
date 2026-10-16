from .base_page import BasePage
from locators.auth_locators import RECOVERY_EMAIL, RECOVERY_BUTTON


class ForgotPasswordPage(BasePage):

    def recover(self, email):
        self.type(RECOVERY_EMAIL, email)
        self.click(RECOVERY_BUTTON)

    def get_email(self):
        return self.find(RECOVERY_EMAIL).get_attribute('value')