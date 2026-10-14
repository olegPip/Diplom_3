import requests
from constants import BASE_URL, API_REGISTER_ENDPOINT, API_USER_ENDPOINT


class StellarBurgersApi:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url.rstrip('/')

    def register_user(self, name, email, password):
        response = requests.post(
            f'{self.base_url}{API_REGISTER_ENDPOINT}',
            json={'email': email, 'password': password, 'name': name},
            timeout=15,
        )
        response.raise_for_status()
        return response.json()

    def delete_user(self, access_token):
        return requests.delete(
            f'{self.base_url}{API_USER_ENDPOINT}',
            headers={'Authorization': access_token},
            timeout=15,
        )
