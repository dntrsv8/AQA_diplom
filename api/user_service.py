from api.base_api import BaseAPI
from api.api_logging import log_info, log_error
import requests


class UserService:

    @staticmethod
    def create_users(users):
        headers = {'Content-Type': 'application/json'}
        data = [{"id": user["id"],
                 "username": user["username"],
                 "firstName": user["firstName"],
                 "lastName": user["lastName"],
                 "email": user["email"],
                 "password": user["password"],
                 "phone": user["phone"],
                 "userStatus": user["userStatus"]} for user in users]

        response = requests.post(
            f"{BaseAPI.base_url}/user/createWithArray",
            headers=headers,
            json=data)

        if response.status_code == 200:
            log_info(
                f"Create Users {users}, Response: {response.status_code}, {response.json()}")
        else:
            log_error(
                f"Failed to create Users {users}, Response: {response.status_code}, {response.text}")

        return response

    @staticmethod
    def update_user(user_id, user_data):
        headers = {'Content-Type': 'application/json'}
        response = requests.put(
            f"{BaseAPI.base_url}/user/{user_id}",
            headers=headers,
            json=user_data)

        if response.status_code == 200:
            log_info(
                f"Update User {user_id} with data {user_data}, Response: {response.status_code}, {response.json()}")
        else:
            log_error(
                f"Failed to update User {user_id} with data {user_data}, Response: {response.status_code}, {response.text}")

        return response
