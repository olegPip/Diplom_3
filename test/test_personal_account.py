import allure

from pages.header import Header
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.feature('Личный кабинет')
class TestPersonalAccount:
    def _login(self, browser, base_url, test_user):
        browser.get(f'{base_url}/login')

        LoginPage(browser).login(
            test_user['email'],
            test_user['password']
        )

    @allure.title('Переход в личный кабинет')
    def test_open_personal_account(self, browser, base_url, test_user):
        self._login(browser, base_url, test_user)
        browser.get(base_url)

        Header(browser).open_personal_account()

        assert '/account' in browser.current_url

    @allure.title('Переход в историю заказов')
    def test_open_order_history(self, browser, base_url, test_user):
        self._login(browser, base_url, test_user)
        browser.get(f'{base_url}/account')

        ProfilePage(browser).open_order_history()

        assert '/account/order-history' in browser.current_url

    @allure.title('Выход из личного кабинета')
    def test_logout(self, browser, base_url, test_user):
        self._login(browser, base_url, test_user)
        browser.get(f'{base_url}/account')

        ProfilePage(browser).logout()

        assert '/login' in browser.current_url