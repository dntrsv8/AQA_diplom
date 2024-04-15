import allure
import pytest
import json
from api.user_service import UserService


class TestUser:
    user_service = UserService()

    @allure.title("TC025:Creating users")
    @allure.description("Checking that users were created")
    @pytest.mark.parametrize("user_data", [
        [{
            "id": 8888,
            "username": "test_user1",
            "firstName": "Test",
            "lastName": "User1",
            "email": "test1@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 0
        },
            {
                "id": 8889,
                "username": "test_user2",
                "firstName": "Test",
                "lastName": "User2",
                "email": "test2@example.com",
                "password": "password123",
                "phone": "1234567890",
                "userStatus": 0
        }]
    ])
    def test_create_users_with_array(self, user_data):
        response = self.user_service.create_users(user_data)
        assert response.status_code == 200
        assert json.loads(
            response.text) == {
            "code": 200,
            "type": "unknown",
            "message": "ok"}

    @allure.title("TC026:User data getting updated")
    @allure.description("Checking that user data is getting updated")
    @pytest.mark.parametrize("user_id, user_data", [(8888, {
        "id": 8888,
        "username": "updated_user",
        "firstName": "Updated",
        "lastName": "User",
        "email": "updated@example.com",
        "password": "newpassword123",
        "phone": "0987654321",
        "userStatus": 1
    })])
    def test_update_user(self, user_id, user_data):
        updated_user_info = self.user_service.update_user(
            user_id, user_data).json()
        assert updated_user_info[
            "code"] == 200, f"Expected code is 200, but got {updated_user_info['code']}"
        assert updated_user_info["message"] == str(
            user_data["id"]), f"Expected message {user_data['id']}, but got {updated_user_info['status']}"
