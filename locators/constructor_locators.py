from selenium.webdriver.common.by import By

INGREDIENT_MODAL = (
    By.XPATH,
    "//div[contains(@class,'Modal_modal__container')][not(.//*[normalize-space()='идентификатор заказа'])]"
)
ORDER_MODAL = (
    By.XPATH,
    "//div[contains(@class,'Modal_modal__container')][.//*[normalize-space()='идентификатор заказа']]"
)
MODAL_CLOSE = (By.CSS_SELECTOR, 'button[class*="Modal_modal__close"]')
ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
ORDER_NUMBER = (By.CSS_SELECTOR, 'div[class*="Modal_modal__contentBox"] h2')
INGREDIENT_TARGET = (By.CSS_SELECTOR, 'ul[class*="BurgerConstructor_basket__list"]')
INGREDIENT_CARD_BY_NAME = "//a[contains(@class,'BurgerIngredient_ingredient')][.//p[text()={name}]]"
INGREDIENT_COUNTER = "//p[contains(@class,'counter_counter__num')]"
