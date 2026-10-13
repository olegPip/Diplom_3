import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from locators.auth_locators import RECOVERY_EMAIL, RECOVERY_BUTTON


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля')
    def test_open_forgot_password(self, browser, base_url):
        browser.get(f'{base_url}/login')
        LoginPage(browser).open_forgot_password()
        assert '/forgot-password' in browser.current_url

    @allure.title('Ввод email и нажатие «Восстановить»')
    def test_recover_password(self, browser, base_url, test_user):
        browser.get(f'{base_url}/forgot-password')

        page = ForgotPasswordPage(browser)
        page.recover(test_user['email'])

        assert page.get_email() == test_user['email']

    @allure.title('Переключение видимости пароля')
    def test_password_visibility_toggle(self, browser, base_url):
        browser.get(f'{base_url}/forgot-password')

        recovery_page = ResetPasswordPage(browser)

        # Вводим email
        recovery_page.type(RECOVERY_EMAIL, 'olegpipulin@mail.ru')
        recovery_page.click(RECOVERY_BUTTON)

        page = ResetPasswordPage(browser)

        # Вводим пароль
        page.enter_password('Test123')

        # До клика поле имеет тип password
        before = page.password_container_class()

        assert 'input_type_password' in before

        # Нажимаем на иконку показать/скрыть пароль
        page.toggle_password()

        # После клика поле имеет тип text
        after = page.password_container_class()
