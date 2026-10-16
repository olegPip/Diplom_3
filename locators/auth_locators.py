from selenium.webdriver.common.by import By

LOGIN_EMAIL = (By.NAME, 'name')
LOGIN_PASSWORD = (By.NAME, 'Пароль')
LOGIN_PASSWORD_TOGGLE = (By.CSS_SELECTOR, '.input__icon-action')
LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')
RECOVERY_EMAIL = (By.NAME, 'name')
RECOVERY_BUTTON = (By.XPATH, "//button[normalize-space()='Восстановить']")
RESET_PASSWORD = (By.NAME, 'Введите новый пароль')
RESET_PASSWORD_TOGGLE = (By.CSS_SELECTOR, '.input_type_password .input__icon-action')
RESET_EMAIL_CODE = (By.XPATH, "//label[normalize-space()='Введите код из письма']/following-sibling::input")
RESET_SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Сохранить']")