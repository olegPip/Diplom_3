from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def text(self, locator):
        return self.find(locator).text

    def attribute(self, locator, name):
        return self.find(locator).get_attribute(name)

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def is_any_visible(self, locator):
        return any(element.is_displayed() for element in self.find_all(locator))

    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_until(self, condition, timeout=None):
        return WebDriverWait(self.driver, timeout or 10).until(condition)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def drag_and_drop(self, source, target):
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(self.driver).click_and_hold(source).move_to_element(target).release().perform()

    def url_contains(self, value):
        self.wait.until(EC.url_contains(value))
        return True

    def current_url(self):
        return self.driver.current_url

    def open(self, url):
        self.driver.get(url)
