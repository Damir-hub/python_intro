import requests

BASE_URL = "https://postman-echo.com"

def fetch_get():
    response = requests.get(f"{BASE_URL}/get")
    if response.status_code >= 400:
        return response.status_code, None
    return response.status_code, response.json()


def fetch_post(data=None):
    # Если данные не переданы — используем дефолтные
    if data is None:
        data = {"key": "value"}
    response = requests.post(f"{BASE_URL}/post", json=data)
    if response.status_code >= 400:
        return response.status_code, None
    return response.status_code, response.json()


def fetch_put(data=None):
    if data is None:
        data = {"key": "updated_value"}
    response = requests.put(f"{BASE_URL}/put", json=data)
    if response.status_code >= 400:
        return response.status_code, None
    return response.status_code, response.json()


def fetch_delete():
    response = requests.delete(f"{BASE_URL}/delete")
    # У DELETE часто нет тела, поэтому JSON может отсутствовать
    if response.status_code >= 400:
        return response.status_code, None
    try:
        return response.status_code, response.json()
    except ValueError:
        # Если JSON нет — возвращаем None вместо падения
        return response.status_code, None
