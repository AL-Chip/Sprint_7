import requests
from config import URL, ENDPOINT_TRACK, ENDPOINT_ORDER
import allure


class TestOrderList:

    @allure.title('Проверка cписока заказов по курьеру')
    def test_order_list(self, courier_login, create_order):

        response_track = requests.get(f"{URL}{ENDPOINT_TRACK}", params={"t": create_order.json()["track"]})
        requests.put(f"{URL}{ENDPOINT_ORDER}/accept/{response_track.json()["order"]["id"]}",
                     params={"courierId": courier_login.json()["id"]})

        response_order_list = requests.get(f"{URL}{ENDPOINT_ORDER}",
                                           params={"courierId": courier_login.json()["id"]})
        assert response_order_list.status_code == 200
        assert isinstance(response_order_list.json()["orders"], list)
