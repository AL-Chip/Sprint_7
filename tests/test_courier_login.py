import requests
from config import URL, ENDPOINT_LOGIN
import allure


class TestsCourierLogin:

    @allure.title('Проверка логина курьера')
    def test_login_courier(self, courier_login):
        assert courier_login.status_code == 200
        assert isinstance(courier_login.json()["id"], int)

    @allure.title('Проверка попытки логина с некорректным паролем')
    def test_login_courier_incorrect_password(self, courier_create):
        payload = {
            "login": courier_create['login_pass'][0],
            "password": "12347"
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN}", data=payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Проверка попытки логина с пердачей не всех данных')
    def test_login_courier_missing_parameter_login(self, courier_create):
        payload = {
            "password": courier_create['login_pass'][1]
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN}", data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"