"""Reusable browser workflows shared by UI tests."""
from selenium.webdriver.support.ui import WebDriverWait

from constants import LOGIN_URL, MAIN_PAGE_URL
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


def login(browser, test_user):
    browser.get(LOGIN_URL)
    LoginPage(browser).login(test_user['email'], test_user['password'])


def place_order(browser, test_user):
    login(browser, test_user)
    browser.get(MAIN_PAGE_URL)
    page = ConstructorPage(browser)
    page.add_bun('Краторная булка N-200i')
    page.add_ingredient('Соус Spicy-X')
    page.place_order()
    WebDriverWait(browser, 20).until(lambda _: page.order_modal_visible())
    order_number = page.get_order_number()
    assert order_number and order_number != '0', 'Номер созданного заказа должен отображаться'
    page.close_modal()
    return order_number
