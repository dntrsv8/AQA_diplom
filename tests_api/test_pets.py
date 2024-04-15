import pytest
from api.pet_service import PetService
import allure


@allure.title("TC021:Adding new pet")
@allure.description("Checking that new pet has been added")
@pytest.mark.parametrize("pet_data", [{
    "id": 922337203685402090,
    "name": "TestPet",
    "status": "available"
}])
def test_add_new_pet(pet_data):
    response = PetService.add_new_pet(pet_data)
    assert response.status_code == 200
    assert response.json()['id'] == pet_data['id']


@allure.title("TC022:Uploading image for an existing pet")
@allure.description("Checking that image has been uploaded for an existing pet")
def test_upload_image():
    pet_id = 922337203685402090
    image_path = "data/test_image.jpg"
    response = PetService.upload_image(pet_id, image_path)
    assert response.status_code == 200


@allure.title("TC023:Finding pet by id")
@allure.description("Checking that pet can be found by pet id")
@pytest.mark.parametrize("pet_id", [922337203685402090])
def test_get_pet_by_id(pet_id):
    response = PetService.get_pet_by_id(pet_id)
    assert response.status_code == 200
    assert response.json().get('id') == pet_id
