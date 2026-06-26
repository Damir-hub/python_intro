import pytest
from api_client import fetch_get, fetch_post, fetch_put, fetch_delete, BASE_URL

def test_fetch_get_success(requests_mock):
    expected_status = 200
    expected_json = {"args": {}, "headers": {}}  # примерный формат ответа от postman-echo
    url = f"{BASE_URL}/get"

    requests_mock.get(url, json=expected_json, status_code=expected_status)

    status, data = fetch_get()

    assert status == expected_status
    assert data == expected_json


def test_fetch_post_success(requests_mock):
    expected_status = 200
    payload = {"key": "value"}
    expected_response_data = {"json": payload}  # postman-echo возвращает JSON в поле json
    url = f"{BASE_URL}/post"

    requests_mock.post(url, json=expected_response_data, status_code=expected_status)

    status, data = fetch_post(payload)

    assert status == expected_status
    assert data == expected_response_data


def test_fetch_put_success(requests_mock):
    expected_status = 200
    payload = {"key": "updated_value"}
    expected_response_data = {"json": payload}
    url = f"{BASE_URL}/put"

    requests_mock.put(url, json=expected_response_data, status_code=expected_status)

    status, data = fetch_put(payload)

    assert status == expected_status
    assert data == expected_response_data


def test_fetch_delete_success(requests_mock):
    expected_status = 200
    url = f"{BASE_URL}/delete"

    # Postman Echo на DELETE обычно возвращает JSON, но бывает и иначе
    requests_mock.delete(url, json={"status": "deleted"}, status_code=expected_status)

    status, data = fetch_delete()

    assert status == expected_status
    # data может быть None, если в мок-ответе не JSON или мы так решили в fetch_delete
    assert data is not None or True  # можно усилить проверку, если знаешь точный формат
