import allure
from selenium.webdriver.support.ui import WebDriverWait

from pages.constructor_page import ConstructorPage
from pages.header import Header
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.order_history_page import OrderHistoryPage



@allure.feature('Лента заказов')
class TestOrderFeed:
    def _login(self, browser, base_url, test_user):
        browser.get(f'{base_url}/login')
        LoginPage(browser).login(test_user['email'], test_user['password'])

    def _place_order(self, browser, base_url, test_user):
        self._login(browser, base_url, test_user)
        browser.get(base_url)
        page = ConstructorPage(browser)
        page.add_bun('Краторная булка N-200i')
        page.add_ingredient('Соус Spicy-X')
        page.place_order()
        WebDriverWait(browser, 20).until(page.order_modal_visible)
        order_number = page.get_order_number()
        page.close_modal()
        return order_number

    @allure.title('Переход в ленту заказов')
    def test_open_order_feed(self, browser, base_url):
        browser.get(base_url)
        Header(browser).open_order_feed()
        assert '/feed' in browser.current_url

    @allure.title('Открытие деталей заказа')
    def test_open_order_details(self, browser, base_url):
        browser.get(f'{base_url}/feed')
        page = FeedPage(browser)
        page.open_first_order()
        assert page.order_modal_visible()

    @allure.title('Закрытие деталей заказа')
    def test_close_order_details(self, browser, base_url):
        browser.get(f'{base_url}/feed')
        page = FeedPage(browser)
        page.open_first_order()
        page.close_modal()
        assert not page.order_modal_visible()

    @allure.title('Отображение статистики ленты заказов')
    def test_feed_statistics_exist(self, browser, base_url):
        browser.get(f'{base_url}/feed')
        page = FeedPage(browser)
        assert page.get_total_orders() >= 0
        assert page.get_today_orders() >= 0

    @allure.title('Заказ из истории пользователя отображается в ленте')
    def test_user_order_is_in_feed(self, browser, base_url, test_user):
        self._place_order(browser, base_url, test_user)
        browser.get(f'{base_url}/account/order-history')
        order_number = OrderHistoryPage(browser).get_first_order_number()
        browser.get(f'{base_url}/feed')
        feed = FeedPage(browser)
        assert feed.has_order_in_feed(order_number)


    @allure.title('Количество выполненных заказов за всё время увеличивается после заказа')
    def test_total_orders_increases_after_new_order(self, browser, base_url, test_user):
        browser.get(f'{base_url}/feed')
        before = FeedPage(browser).get_total_orders()
        self._place_order(browser, base_url, test_user)
        browser.get(f'{base_url}/feed')
        after = FeedPage(browser).get_total_orders()
        assert after >= before + 1

    @allure.title('Количество выполненных заказов за сегодня увеличивается после заказа')
    def test_today_orders_increases_after_new_order(self, browser, base_url, test_user):
        browser.get(f'{base_url}/feed')
        before = FeedPage(browser).get_today_orders()
        self._place_order(browser, base_url, test_user)
        browser.get(f'{base_url}/feed')
        after = FeedPage(browser).get_today_orders()
        assert after >= before + 1

    @allure.title('После оформления заказа его номер появляется в блоке «В работе»')
    def test_new_order_appears_in_work(self, browser, base_url, test_user):
        order_number = self._place_order(browser, base_url, test_user)
        browser.get(f'{base_url}/feed')
        feed = FeedPage(browser)
        WebDriverWait(browser, 20).until(lambda _: feed.has_order_in_work(order_number))
        assert feed.has_order_in_work(order_number)
