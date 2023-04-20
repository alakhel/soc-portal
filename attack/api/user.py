import requests
import logging
from os import urandom


# TODO: save the traffic of a bunch of users using a proxy and replay to simulate a true attack
class Users():

    post_headers = {
        "Content-Type": "application/json"
    }

    dummy_user = {
        "prenom": "John",
        "nom": "Doe",
        "username": "",
        "password": "mypassword",
        "groupe": ""
    }

    def __init__(self, api_url: str, logger: logging.Logger) -> None:
        self.target = f'{api_url}/users'
        self.logger = logger

    def test_user_creation(self):
        # Test if we can create a user named Admin and overwrite the existing one
        user = self.dummy_user.copy()
        user['username'] = "admin"
        r = requests.post(self.target, headers=self.post_headers, json=user)
        if r.status_code == 200:
            self.logger.info('Created a user "Admin"')

        # Test if we can create a user in the group "admin"
        user['username'] = "eve"
        user['groupe'] = "admin"
        r = requests.post(self.target, headers=self.post_headers, json=user)
        if r.status_code == 200:
            self.logger.info('Created a user in the group "admin"')

    def test_user_update(self):
        # Test if we can update the password of a user
        user = self.dummy_user.copy()
        user['password'] = urandom(16).hex()
        r = requests.post(f'{self.target}/_id', headers=self.post_headers, json=user)
        if r.status_code == 200:
            self.logger.info('Changed the password of a user')

        user['password'] = ''
        user['groupe'] = 'admin'
        r = requests.post(f'{self.target}/_id', headers=self.post_headers, json=user)
        if r.status_code == 200:
            self.logger.info('Changed the group of a user')

    def test_user_delete(self):
        r = requests.delete(f'{self.target}/_id')
        if r.status_code == 200:
            self.logger.info('Deleted a user')
