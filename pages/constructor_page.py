from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.constructor_locators import (
    INGREDIENT_MODAL,
    ORDER_MODAL,
    MODAL_CLOSE,
    ORDER_BUTTON,
    ORDER_NUMBER,
    INGREDIENT_TARGET,
    INGREDIENT_CARD_BY_NAME,
    INGREDIENT_COUNTER,
)


class ConstructorPage(BasePage):

    def _ingredient_locator(self, name):
        return (
            By.XPATH,
            INGREDIENT_CARD_BY_NAME.format(
                name=self._xpath_literal(name)
            ),
        )

    def open_ingredient(self, name):
        self.click(self._ingredient_locator(name))

    def get_ingredient_counter(self, name):
        card = self.find(self._ingredient_locator(name))
        return int(
            card.find_element(By.XPATH, f".{INGREDIENT_COUNTER}").text
        )

    def add_ingredient(self, name):
        source = self.find(self._ingredient_locator(name))
        target = self.find(INGREDIENT_TARGET)

        ActionChains(self.driver) \
            .click_and_hold(source) \
            .move_to_element(target) \
            .release() \
            .perform()

    def add_bun(self, name):
        self.add_ingredient(name)

    def close_modal(self):
        close_button = self.find(MODAL_CLOSE)

        self.driver.execute_script(
            "arguments[0].click();",
            close_button
        )

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(ORDER_MODAL)
        )

    def place_order(self):
        self.click(ORDER_BUTTON)

    def get_order_number(self):
        return self.text(ORDER_NUMBER).lstrip("#")

    def ingredient_modal_visible(self, driver):
        return any(
            element.is_displayed()
            for element in driver.find_elements(*INGREDIENT_MODAL)
        )

    def order_modal_visible(self, driver):
        return any(
            element.is_displayed()
            for element in driver.find_elements(*ORDER_MODAL)
        )

    @staticmethod
    def _xpath_literal(value):
        if "'" not in value:
            return f"'{value}'"

        if '"' not in value:
            return f'"{value}"'

        parts = value.split("'")

        return (
            'concat('
            + ', "\'", '.join(f"'{part}'" for part in parts)
            + ')'
        )
