import requests
from config import URL, ENDPOINT_COURIER_CREATING


class TestsCourierLogin:

    def test_login_courier(self, courier_login):
        assert courier_login.status_code == 200
        assert isinstance(courier_login.json()["id"], int)
