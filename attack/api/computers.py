import requests
import logging
from os import urandom
from random import randint, choice


class Computers():

    post_headers = {
        "Content-Type": "application/json"
    }

    dummy_computer = {
        "hostname": "",
        "ip": "",
        "groupe": ""
    }

    def __init__(self, api_url: str, logger: logging.Logger) -> None:
        self.target = f'{api_url}/computers'
        self.logger = logger

        self.list_cpts()

    def list_cpts(self) -> None:
        r = requests.get(self.target)
        if r.status_code == 200:
            self.cpts = r.json()

    def test_computer_creation(self):
        # Test if we can create a cpt named Admin and overwrite the existing one
        cpt = self.dummy_computer.copy()
        cpt['hostname'] = urandom.hex()
        cpt['ip'] = f'{randint(100, 256)}.{randint(100, 256)}.{randint(100, 256)}.{randint(100, 256)}'
        r = requests.post(self.target, headers=self.post_headers, json=cpt)
        if r.status_code == 200:
            self.logger.info('Created a computer')

    def test_computer_update(self):
        # Test if we can update the password of a cpt
        cpt = choice(self.cpts).copy()

        cpt['ip'] = f'{randint(100, 256)}.{randint(100, 256)}.{randint(100, 256)}.{randint(100, 256)}'

        r = requests.post(f'{self.target}/{cpt["id"]}', headers=self.post_headers, json=cpt)
        if r.status_code == 200:
            self.logger.info('Changed the password of a cpt')

        cpt = choice(self.cpts).copy()

        cpt['groupe'] = 'group4'

        r = requests.post(f'{self.target}/{cpt["id"]}', headers=self.post_headers, json=cpt)
        if r.status_code == 200:
            self.logger.info('Changed the group of a cpt')

    def test_cpt_delete(self):
        cpt = choice(self.cpts).copy()

        r = requests.delete(f'{self.target}/{cpt["id"]}')
        if r.status_code == 200:
            self.logger.info('Deleted a cpt')
