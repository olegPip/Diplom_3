from selenium.webdriver.common.by import By

ORDER_LINKS = (
    By.CSS_SELECTOR,
    'a[class*="OrderHistory_link"]'
)

ORDER_MODAL = (
    By.XPATH,
    "//div[contains(@class,'Modal_modal__contentBox')][.//p[contains(@class,'text_type_digits-default')]]"
)

MODAL_CLOSE = (
    By.CSS_SELECTOR,
    'button[class*="Modal_modal__close"]'
)


TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p[contains(@class,'OrderFeed_number')]")
TODAY_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[contains(@class,'OrderFeed_number')]")

FEED_ORDER_ITEMS = (By.CSS_SELECTOR, 'ul[class*="OrderFeed_list"] > li[class*="OrderHistory_listItem"]')
IN_WORK_ITEMS = (By.CSS_SELECTOR, 'div[class*="OrderFeed_orderStatusBox"] ul[class*="OrderFeed_orderList"]:not([class*="OrderFeed_orderListReady"]) > li')
FEED_ORDER_NUMBER = (By.CSS_SELECTOR, 'p.text_type_digits-default')