import logging
from bruteforce import bruteforce_login, fuzz_website
from api import Users, Computers
from consts import API_URL
from random import randint, choice
from time import time, sleep


logger = logging.getLogger(__name__)

# Set the logger level to INFO
logger.setLevel(logging.DEBUG)

# Create a console handler with a message format
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(ch)

users = Users(API_URL, logger)
computers = Computers(API_URL, logger)

api_attacks = [
    users.test_user_creation,
    users.test_user_delete,
    users.test_user_update,
    computers.test_computer_creation,
    computers.test_computer_update,
    computers.test_cpt_delete
]


logger.info('Starting Login Bruteforce')
bruteforce_login()
logger.info('Finished Login Bruteforce')


logger.info('Starting API spam')
current_time = time()
while True:
    sleep(randint(1, 10))

    method = choice(api_attacks)
    method()

    if time() > current_time + 30 * 60:
        logger.info('Finishing API spam')
        break
