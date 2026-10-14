from constants import BASE_URL
import allure

from pages.header import Header
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.feature('Личный кабинет')
class TestPersonalAccount:
    def _login(self, browser, test_user):
        browser.get(f'{BASE_URL}/login')

        LoginPage(browser).login(
            test_user['email'],
            test_user['password']
        )

    @allure.title('Переход в личный кабинет')
    def test_open_personal_account(self, browser, test_user):
        self._login(browser, test_user)
        browser.get(BASE_URL)

        Header(browser).open_personal_account()

        assert '/account' in browser.current_url

    @allure.title('Переход в историю заказов')
    def test_open_order_history(self, browser, test_user):
        self._login(browser, test_user)
        browser.get(f'{BASE_URL}/account')

        ProfilePage(browser).open_order_history()

        assert '/account/order-history' in browser.current_url

    @allure.title('Выход из личного кабинета')
    def test_logout(self, browser, test_user):
        self._login(browser, test_user)
        browser.get(f'{BASE_URL}/account')

        ProfilePage(browser).logout()

        assert '/login' in browser.current_url