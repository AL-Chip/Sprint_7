import requests
from config import URL, ENDPOINT_COURIER_CREATING


class TestsCourierCreate:

    def test_create_courier(self, courier_create):
        assert courier_create['response'].status_code == 201
        assert courier_create['response'].json() == {'ok': True}

    def test_create_courier_login_exists(self, courier_create):
        payload = {
            "login": courier_create['login_pass'][0],
            "password": "1234",
            "firstName": "saske"
        }
        response = requests.post(f"{URL}{ENDPOINT_COURIER_CREATING}", data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    def test_create_courier_missing_parameter(self):
        payload = {
            "login": "1",
            "firstName": "saske"
        }
        response = requests.post(f"{URL}{ENDPOINT_COURIER_CREATING}", data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

