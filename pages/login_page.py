from .base_page import BasePage
from locators.auth_locators import LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_PASSWORD_TOGGLE, LOGIN_BUTTON, FORGOT_PASSWORD_LINK
from constants import LOGIN_URL


class LoginPage(BasePage):
    def login(self, email, password):
        self.type(LOGIN_EMAIL, email)
        self.type(LOGIN_PASSWORD, password)
        self.click(LOGIN_BUTTON)
        self.wait_until(lambda _: self.current_url().rstrip('/') != LOGIN_URL.rstrip('/'), timeout=15)
        self.wait_until(lambda _: self.execute_script(
            "return document.querySelector('#root') && document.querySelector('#root').children.length > 0"
        ), timeout=15)

    def open_forgot_password(self):
        self.click(FORGOT_PASSWORD_LINK)

    def toggle_password(self):
        self.click(LOGIN_PASSWORD_TOGGLE)

    def password_type(self):
        return self.attribute(LOGIN_PASSWORD, 'type')
