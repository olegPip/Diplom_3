from selenium.webdriver.common.by import By

INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__container')][not(.//*[normalize-space()='идентификатор заказа'])]")
ORDER_MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__container')][.//*[normalize-space()='идентификатор заказа']]")
MODAL_CLOSE = (By.CSS_SELECTOR, 'button[class*="Modal_modal__close"]')
ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
ORDER_NUMBER = (By.CSS_SELECTOR, 'div[class*="Modal_modal__contentBox"] h2')
INGREDIENT_TARGET = (By.CSS_SELECTOR, 'ul[class*="BurgerConstructor_basket__list"]')
INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class,'counter_counter__num')]")

def ingredient_card(name):
    return (By.XPATH, f"//a[contains(@class,'BurgerIngredient_ingredient')][.//p[normalize-space()={xpath_literal(name)}]]")

def xpath_literal(value):
    if "'" not in value:
        return f"'{value}'"
    if '"' not in value:
        return f'"{value}"'
    parts = value.split("'")
    return "concat(" + ', \'"\'\', '.join(f"'{part}'" for part in parts) + ")"
