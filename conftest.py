import uuid
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from api_client import StellarBurgersApi
from constants import BASE_URL


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', choices=['chrome', 'firefox'])
    parser.addoption('--headless', action='store_true', default=False)


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    if browser_name == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless=new')
        options.add_argument('--window-size=1440,1000')
        driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def test_user():
    api = StellarBurgersApi()
    email = f'qa_{uuid.uuid4().hex[:10]}@example.com'
    password = f'Qa_{uuid.uuid4().hex[:12]}!'
    name = 'QA Test User'
    data = api.register_user(name, email, password)
    access_token = data.get('accessToken')
    yield {'name': name, 'email': email, 'password': password}
    if access_token:
        api.delete_user(access_token)
