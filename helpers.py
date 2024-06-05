import random
import string


def get_payload_courier() -> dict:
    payload = {
        "login": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
        "password": ''.join(random.choice(string.ascii_lowercase) for j in range(10)),
        "firstName": ''.join(random.choice(string.ascii_lowercase) for f in range(10))
    }
    return payload


def get_payload_order() -> dict:
    payload = {
        "firstName": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
        "lastName": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
        "address": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
        "metroStation": random.randint(0, 9),
        "phone": "+7 800 355 35 35",
        "rentTime": random.randint(0, 9),
        "deliveryDate": "2020-06-06",
        "comment": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
        "color": random.sample(["BLACK", "GREY"], 1)
    }
    return payload


