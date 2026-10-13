from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from locators.feed_locators import (
    ORDER_LINKS,
    ORDER_MODAL,
    MODAL_CLOSE,
    TOTAL_ORDERS,
    TODAY_ORDERS,
    FEED_ORDER_ITEMS,
    IN_WORK_ITEMS,
    FEED_ORDER_NUMBER,
)


class FeedPage(BasePage):

    def open_first_order(self):
        first_order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ORDER_LINKS)
        )
        first_order.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ORDER_MODAL)
        )

    def close_modal(self):
        close_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MODAL_CLOSE)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            close_button
        )

        WebDriverWait(self.driver, 10).until(
            lambda driver: not any(
                element.is_displayed()
                for element in driver.find_elements(*MODAL_CLOSE)
            )
        )

    def order_modal_visible(self):
        elements = self.driver.find_elements(*ORDER_MODAL)

        return any(
            element.is_displayed()
            for element in elements
        )

    def get_total_orders(self):
        return int(self.text(TOTAL_ORDERS))

    def get_today_orders(self):
        return int(self.text(TODAY_ORDERS))

    def has_order_in_feed(self, order_number):
        expected = order_number.lstrip('#')

        return any(
            item.find_element(*FEED_ORDER_NUMBER).text.lstrip('#') == expected
            for item in self.driver.find_elements(*FEED_ORDER_ITEMS)
        )

    def get_in_work_order_numbers(self):
        return [
            item.find_element(*FEED_ORDER_NUMBER).text.lstrip('#')
            for item in self.driver.find_elements(*IN_WORK_ITEMS)
        ]

    def has_order_in_work(self, order_number):
        numbers = self.get_in_work_order_numbers()

        print("Ожидаемый заказ:", order_number)
        print("Заказы в работе:", numbers)

        return order_number.lstrip('#') in numbers
