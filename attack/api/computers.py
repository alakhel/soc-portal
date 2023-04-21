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
        self.logger.info('Listing computers')
        r = requests.get(self.target)
        if r.status_code == 200:
            self.cpts = r.json()
        else:
            tmp = self.dummy_computer.copy()
            tmp['id'] = '1337'
            self.cpts = [tmp]

    def test_computer_creation(self):
        self.logger.info('Trying to create a computer named')
        # Test if we can create a cpt
        cpt = self.dummy_computer.copy()

        cpt['hostname'] = urandom(10).hex()
        cpt['ip'] = f'{randint(100, 256)}.{randint(100, 256)}.{randint(100, 256)}.{randint(100, 256)}'
        cpt['groupe'] = "groupe 4"

        r = requests.post(self.target, headers=self.post_headers, json=cpt)
        if r.status_code == 200:
            self.logger.info('Created a computer')

    def test_computer_update(self):
        self.logger.info('Trying to update the IP of a computer')
        # Test if we can update the IP of a cpt
        cpt = choice(self.cpts).copy()

        cpt['ip'] = f'{randint(100, 256)}.{randint(100, 256)}.{randint(100, 256)}.{randint(100, 256)}'

        r = requests.post(f'{self.target}/{cpt["id"]}', headers=self.post_headers, json=cpt)
        if r.status_code == 200:
            self.logger.info('Changed the IP of a cpt')

        self.logger.info('Trying to update the group of a computer')

        cpt = choice(self.cpts).copy()

        cpt['groupe'] = 'group4'

        r = requests.post(f'{self.target}/{cpt["id"]}', headers=self.post_headers, json=cpt)
        if r.status_code == 200:
            self.logger.info('Changed the group of a cpt')

    def test_cpt_delete(self):
        self.logger.info('Trying to delete the IP of a computer')
        cpt = choice(self.cpts).copy()

        r = requests.delete(f'{self.target}/{cpt["id"]}')
        if r.status_code == 200:
            self.logger.info('Deleted a cpt')
