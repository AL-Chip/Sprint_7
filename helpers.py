import random
import string


def get_payload() -> dict:
    payload = {
        "login": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
        "password": ''.join(random.choice(string.ascii_lowercase) for j in range(10)),
        "firstName": ''.join(random.choice(string.ascii_lowercase) for f in range(10))
    }
    return payload



