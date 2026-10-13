from .base_page import BasePage
from locators.auth_locators import RESET_PASSWORD, RESET_PASSWORD_TOGGLE

from selenium.webdriver.common.by import By

class ResetPasswordPage(BasePage):
    def enter_password(self, password):
        self.type(RESET_PASSWORD, password)

    def toggle_password(self):
        self.click(RESET_PASSWORD_TOGGLE)

    def password_type(self):
        return self.find(RESET_PASSWORD).get_attribute('type')

    def password_container_class(self):
        password = self.find(RESET_PASSWORD)
        return password.find_element(By.XPATH, "./..").get_attribute("class")