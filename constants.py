import os

BASE_URL = os.getenv('BASE_URL', 'https://stellarburgers.education-services.ru').rstrip('/')

# UI routes
MAIN_PAGE_URL = f'{BASE_URL}/'
LOGIN_URL = f'{BASE_URL}/login'
REGISTER_URL = f'{BASE_URL}/register'
FORGOT_PASSWORD_URL = f'{BASE_URL}/forgot-password'
RESET_PASSWORD_URL = f'{BASE_URL}/reset-password'
ACCOUNT_URL = f'{BASE_URL}/account'
ORDER_HISTORY_URL = f'{BASE_URL}/account/order-history'
FEED_URL = f'{BASE_URL}/feed'

# API endpoints
API_REGISTER_ENDPOINT = '/api/auth/register'
API_USER_ENDPOINT = '/api/auth/user'
