import allure

from constants import ACCOUNT_URL, MAIN_PAGE_URL, ORDER_HISTORY_URL, LOGIN_URL
from helpers import login
from pages.header import Header
from pages.profile_page import ProfilePage


@allure.feature('Личный кабинет')
class TestPersonalAccount:
    @allure.title('Переход в личный кабинет')
    def test_open_personal_account(self, browser, test_user):
        login(browser, test_user)
        browser.get(MAIN_PAGE_URL)
        Header(browser).open_personal_account()
        assert ACCOUNT_URL in browser.current_url

    @allure.title('Переход в историю заказов')
    def test_open_order_history(self, browser, test_user):
        login(browser, test_user)
        browser.get(ACCOUNT_URL)
        ProfilePage(browser).open_order_history()
        assert ORDER_HISTORY_URL in browser.current_url

    @allure.title('Выход из личного кабинета')
    def test_logout(self, browser, test_user):
        login(browser, test_user)
        browser.get(ACCOUNT_URL)
        ProfilePage(browser).logout()
        assert LOGIN_URL in browser.current_url
