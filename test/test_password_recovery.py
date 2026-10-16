import allure

from constants import FORGOT_PASSWORD_URL, LOGIN_URL
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля')
    def test_open_forgot_password(self, browser):
        browser.get(LOGIN_URL)
        LoginPage(browser).open_forgot_password()
        assert FORGOT_PASSWORD_URL in browser.current_url

    @allure.title('Ввод email и нажатие «Восстановить»')
    def test_recover_password(self, browser, test_user):
        browser.get(FORGOT_PASSWORD_URL)
        page = ForgotPasswordPage(browser)
        page.recover(test_user['email'])
        assert page.get_email() == test_user['email']

    @allure.title('Переключение видимости пароля')
    def test_password_visibility_toggle(self, browser, test_user):
        browser.get(FORGOT_PASSWORD_URL)
        ForgotPasswordPage(browser).recover(test_user['email'])
        page = ResetPasswordPage(browser)
        page.enter_password('Test123')
        assert page.password_type() == 'password'
        page.toggle_password()
        assert page.password_type() == 'text'
