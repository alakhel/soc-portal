import requests
import logging
from os import urandom
from random import choice


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

        self.list_users()

    def list_users(self) -> None:
        self.logger.info('Listing users')
        r = requests.get(self.target)
        if r.status_code == 200:
            self.users = r.json()
        else:
            tmp = self.dummy_user.copy()
            tmp['id'] = '1337'
            self.users = [tmp]

    def test_user_creation(self):
        self.logger.info('Trying to create a User named "admin"')
        # Test if we can create a user named Admin and overwrite the existing one
        user = self.dummy_user.copy()

        user['username'] = "admin"

        r = requests.post(self.target, headers=self.post_headers, json=user)
        if r.status_code == 200:
            self.logger.info('Created a user "Admin"')

        self.logger.info('Trying to create a User in the group "admin"')
        # Test if we can create a user in the group "admin"
        user['username'] = "eve"
        user['groupe'] = "admin"

        r = requests.post(self.target, headers=self.post_headers, json=user)
        if r.status_code == 200:
            self.logger.info('Created a user in the group "admin"')

    def test_user_update(self):
        self.logger.info('Trying to update the password of a user')
        # Test if we can update the password of a user
        user = choice(self.users).copy()

        user['password'] = urandom(16).hex()

        r = requests.post(f'{self.target}/{user["id"]}', headers=self.post_headers, json=user)
        if r.status_code == 200:
            self.logger.info('Changed the password of a user')

        self.logger.info('Trying to update the group of a user')
        # Test if we can change the group of a user
        user = choice(self.users).copy()

        user['groupe'] = 'admin'
        r = requests.post(f'{self.target}/{user["id"]}', headers=self.post_headers, json=user)
        if r.status_code == 200:
            self.logger.info('Changed the group of a user')

    def test_user_delete(self):
        self.logger.info('Trying to delete a user')
        # Test if we can delete a user
        user = choice(self.users).copy()

        r = requests.delete(f'{self.target}/{user["id"]}')
        if r.status_code == 200:
            self.logger.info('Deleted a user')
