import requests
from api.api_logging import log_info, log_error


class BaseAPI:

    base_url = "https://petstore.swagger.io/v2"

    @staticmethod
    def get(endpoint, params=None):
        url = f"{BaseAPI.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        log_info(
            f"GET {url}, Response: {response.status_code}, {response.json()}")
        return response

    @staticmethod
    def post(endpoint, data=None):
        url = f"{BaseAPI.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        log_info(
            f"POST {url}, Request: {data}, Response: {response.status_code}, {response.json()}")
        return response

    @staticmethod
    def put(endpoint, data=None):
        url = f"{BaseAPI.base_url}/{endpoint}"
        response = requests.put(url, json=data)
        log_info(
            f"PUT {url}, Request: {data}, Response: {response.status_code}, {response.json()}")
        return response

    @staticmethod
    def delete(endpoint):
        url = f"{BaseAPI.base_url}/{endpoint}"
        response = requests.delete(url)
        log_info(
            f"DELETE {url}, Response: {response.status_code}, {response.json()}")
        return response
