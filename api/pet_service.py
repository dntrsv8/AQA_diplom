from api.base_api import BaseAPI
import requests
from api.api_logging import log_info, log_error


class PetService:

    @staticmethod
    def get_pet_by_id(pet_id):
        response = BaseAPI.get(f"pet/{pet_id}")

        if response.status_code == 200:
            log_info(
                f"Get Pet by ID {pet_id}, Response: {response.status_code}, {response.json()}")
        else:
            log_error(
                f"Failed to get Pet by ID {pet_id}, Response: {response.status_code}, {response.text}")

        return response

    @staticmethod
    def add_new_pet(pet_data):
        response = BaseAPI.post("pet", pet_data)

        if response.status_code == 200:
            log_info(
                f"Add new Pet {pet_data}, Response: {response.status_code}, {response.json()}")
        else:
            log_error(
                f"Failed to add new Pet {pet_data}, Response: {response.status_code}, {response.text}")

        return response

    @staticmethod
    def upload_image(pet_id, image_path):
        with open(image_path, 'rb') as image_file:
            files = {'file': ('test_image.jpg', image_file, 'image/jpeg')}
            response = requests.post(
                f"{BaseAPI.base_url}/pet/{pet_id}/uploadImage", files=files)
        if response.status_code == 200:
            log_info(
                f"Upload Image for Pet {pet_id}, Response: {response.status_code}, {response.json()}")
        else:
            log_error(
                f"Upload Image for Pet {pet_id} failed, Response: {response.status_code}, {response.text}")

        return response
