import allure
from selenium.webdriver.support.ui import WebDriverWait

from constants import FEED_URL, MAIN_PAGE_URL
from helpers import login
from pages.constructor_page import ConstructorPage
from pages.header import Header


@allure.feature('Конструктор')
class TestConstructor:
    @allure.title('Переход в конструктор')
    def test_open_constructor(self, browser):
        browser.get(FEED_URL)
        Header(browser).open_constructor()
        assert browser.current_url.rstrip('/') == MAIN_PAGE_URL.rstrip('/')

    @allure.title('Открытие модального окна ингредиента')
    def test_open_ingredient_modal(self, browser):
        browser.get(MAIN_PAGE_URL)
        page = ConstructorPage(browser)
        page.open_ingredient('Краторная булка N-200i')
        assert page.ingredient_modal_visible()

    @allure.title('Закрытие модального окна ингредиента')
    def test_close_ingredient_modal(self, browser):
        browser.get(MAIN_PAGE_URL)
        page = ConstructorPage(browser)
        page.open_ingredient('Краторная булка N-200i')
        page.close_modal()
        WebDriverWait(browser, 5).until(lambda _: not page.ingredient_modal_visible())
        assert not page.ingredient_modal_visible()

    @allure.title('Увеличение счётчика ингредиента при добавлении')
    def test_ingredient_counter_increases(self, browser):
        browser.get(MAIN_PAGE_URL)
        page = ConstructorPage(browser)
        before = page.get_ingredient_counter('Соус Spicy-X')
        page.add_ingredient('Соус Spicy-X')
        after = page.get_ingredient_counter('Соус Spicy-X')
        assert after == before + 1

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_place_order(self, browser, test_user):
        login(browser, test_user)
        page = ConstructorPage(browser)
        page.add_bun('Краторная булка N-200i')
        page.add_ingredient('Соус Spicy-X')
        page.place_order()
        WebDriverWait(browser, 20).until(lambda _: page.order_modal_visible())
        assert page.get_order_number().isdigit()
