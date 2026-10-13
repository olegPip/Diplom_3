from selenium.webdriver.common.by import By

ACCOUNT_LINK = (
    By.CSS_SELECTOR,
    'a[href="/account/profile"]'
)
ORDER_HISTORY_LINK = (By.CSS_SELECTOR, 'a[href="/account/order-history"]')
LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")
ORDER_HISTORY_ITEMS = (
    By.CSS_SELECTOR,
    'li[class*="OrderHistory_listItem"]'
)
ORDER_HISTORY_NUMBER = (By.CSS_SELECTOR, 'p.text_type_digits-default')