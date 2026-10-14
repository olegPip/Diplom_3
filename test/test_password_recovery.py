from constants import BASE_URL
import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля')
    def test_open_forgot_password(self, browser):
        browser.get(f'{BASE_URL}/login')
        LoginPage(browser).open_forgot_password()
        assert '/forgot-password' in browser.current_url

    @allure.title('Ввод email и нажатие «Восстановить»')
    def test_recover_password(self, browser, test_user):
        browser.get(f'{BASE_URL}/forgot-password')

        page = ForgotPasswordPage(browser)
        page.recover(test_user['email'])

        assert page.get_email() == test_user['email']

    @allure.title('Переключение видимости пароля')
    def test_password_visibility_toggle(self, browser):
        browser.get(f'{BASE_URL}/forgot-password')

        recovery_page = ForgotPasswordPage(browser)

        # Вводим email
        recovery_page.recover('olegpipulin@mail.ru')

        page = ResetPasswordPage(browser)

        # Вводим пароль
        page.enter_password('Test123')

        # До клика поле имеет тип password
        before = page.password_container_class()

        page.toggle_password()
        after = page.password_container_class()

        assert 'input_type_password' in before and 'input_type_text' in after
