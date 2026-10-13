import requests


class StellarBurgersApi:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def register_user(self, name, email, password):
        response = requests.post(
            f'{self.base_url}/api/auth/register',
            json={'email': email, 'password': password, 'name': name},
            timeout=15,
        )
        response.raise_for_status()
        return response.json()

    def delete_user(self, access_token):
        requests.delete(
            f'{self.base_url}/api/auth/user',
            headers={'Authorization': access_token},
            timeout=15,
        )
