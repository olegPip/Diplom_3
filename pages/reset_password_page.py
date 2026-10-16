from .base_page import BasePage
from locators.auth_locators import RESET_PASSWORD, RESET_PASSWORD_TOGGLE


class ResetPasswordPage(BasePage):
    def enter_password(self, password):
        self.type(RESET_PASSWORD, password)

    def toggle_password(self):
        self.click(RESET_PASSWORD_TOGGLE)

    def password_type(self):
        return self.attribute(RESET_PASSWORD, 'type')

    def password_container_class(self):
        return self.find(RESET_PASSWORD).find_element('xpath', './..').get_attribute('class')
