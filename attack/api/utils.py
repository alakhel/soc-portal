import requests
from ..consts import API_URL


def login(username: str, password: str) -> list:
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "username": username,
        "password": password
    }

    r = requests.post(f'{API_URL}/login', headers=headers, json=data)

    if r.status_code != 200:
        return {"success": False}

    return {"success": True, **r.json()}
