import allure
import pytest
from api.store_service import StoreService


@allure.title("TC024:Order is deleted using order id")
@allure.description("Checking that order has been deleted using order id ")
@pytest.mark.parametrize("order_id", [44])
def test_delete_order_by_id(order_id):
    response = StoreService.delete_order_by_id(order_id)
    assert response.status_code == 200
