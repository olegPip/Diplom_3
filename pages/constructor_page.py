from .base_page import BasePage
from locators.constructor_locators import (
    INGREDIENT_MODAL, ORDER_MODAL, MODAL_CLOSE, ORDER_BUTTON, ORDER_NUMBER,
    INGREDIENT_TARGET, INGREDIENT_COUNTER, ingredient_card,
)


class ConstructorPage(BasePage):
    def open_ingredient(self, name):
        self.click(ingredient_card(name))

    def get_ingredient_counter(self, name):
        card = self.find(ingredient_card(name))
        return int(card.find_element(*INGREDIENT_COUNTER).text)

    def add_ingredient(self, name):
        self.drag_and_drop(self.find(ingredient_card(name)), self.find(INGREDIENT_TARGET))

    def add_bun(self, name):
        self.add_ingredient(name)

    def close_modal(self):
        self.click(MODAL_CLOSE)
        self.wait_invisible(ORDER_MODAL)
        self.wait_invisible(INGREDIENT_MODAL)

    def place_order(self):
        self.click(ORDER_BUTTON)

    def get_order_number(self):
        return self.text(ORDER_NUMBER).lstrip("#")

    def ingredient_modal_visible(self):
        return self.is_any_visible(INGREDIENT_MODAL)

    def order_modal_visible(self):
        return self.is_any_visible(ORDER_MODAL)
