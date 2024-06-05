import requests
from config import URL, ENDPOINT_ORDER
import json
import pytest
import allure


class TestsCreateOrder:

    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize(
        "color",  [
            [],
            ["BLACK"],
            ["BLACK", "GRAY"],
        ]
    )
    def test_create_order(self, color):
        payload = {
            "color": color
        }
        payload_json = json.dumps(payload)
        response = requests.post(f"{URL}{ENDPOINT_ORDER}", data=payload_json)
        assert response.status_code == 201
        assert isinstance(response.json()["track"], int)
