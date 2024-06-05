import pytest
import requests
from config import URL, ENDPOINT_COURIER_CREATING, ENDPOINT_LOGIN, ENDPOINT_ORDER
from helpers import get_payload_courier, get_payload_order
import json


@pytest.fixture
def courier_create():
    login_pass = []
    payload = get_payload_courier()
    response = requests.post(f"{URL}{ENDPOINT_COURIER_CREATING}", data=payload)
    if response.status_code == 201:
        login_pass.append(payload["login"])
        login_pass.append(payload["password"])
        login_pass.append(payload["firstName"])
    return {'response': response, 'login_pass': login_pass}


@pytest.fixture
def courier_login(courier_create):
    payload = {
        "login": courier_create['login_pass'][0],
        "password": courier_create['login_pass'][1]
    }
    response_login = requests.post(f"{URL}{ENDPOINT_LOGIN}", data=payload)
    return response_login


@pytest.fixture
def create_order():
    payload = get_payload_order()
    payload_json = json.dumps(payload)
    response = requests.post(f"{URL}{ENDPOINT_ORDER}", data=payload_json)
    return response


