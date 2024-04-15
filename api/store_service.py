from api.base_api import BaseAPI
from api.api_logging import log_info, log_error


class StoreService:

    @staticmethod
    def delete_order_by_id(order_id):
        response = BaseAPI.delete(f"store/order/{order_id}")

        if response.status_code == 200:
            log_info(
                f"Delete Order by ID {order_id}, Response: {response.status_code}, {response.json()}")
        else:
            log_error(
                f"Failed to delete Order by ID {order_id}, Response: {response.status_code}, {response.text}")

        return response
