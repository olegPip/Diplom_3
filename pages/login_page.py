from selenium.webdriver.support.ui import WebDriverWait


from .base_page import BasePage
from locators.auth_locators import (
    LOGIN_EMAIL,
    LOGIN_PASSWORD,
    LOGIN_PASSWORD_TOGGLE,
    LOGIN_BUTTON,
    FORGOT_PASSWORD_LINK,
)


class LoginPage(BasePage):
    def login(self, email, password):
        self.type(LOGIN_EMAIL, email)
        self.type(LOGIN_PASSWORD, password)

        self.click(LOGIN_BUTTON)

        WebDriverWait(self.driver, 15).until(
            lambda driver: driver.current_url !=
            'https://stellarburgers.education-services.ru/login'
        )

        WebDriverWait(self.driver, 15).until(
            lambda driver: driver.execute_script(
                "return document.querySelector('#root') && "
                "document.querySelector('#root').children.length > 0"
            )
        )

    def open_forgot_password(self):
        self.click(FORGOT_PASSWORD_LINK)

    def toggle_password(self):
        self.click(LOGIN_PASSWORD_TOGGLE)

    def password_type(self):
        return self.find(LOGIN_PASSWORD).get_attribute('type')