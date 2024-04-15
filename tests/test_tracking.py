import pytest
import allure
from Pages.tracking_order import Tracking
from data.urls import URLS


@allure.title("TC014:Page title is correct for the tracking order page")
@allure.description("Checking title of the tracking order page")
def test_tracking_order_title(driver_chrome):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    assert "Проверить заказ по номеру" in tracking_page.title()


@allure.title("TC015:Correct page is opened for orders history")
@allure.description("Checking that url is correct for the order history opened from the tracking order")
def test_my_order_link(driver_chrome):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.MY_ORDERS_XPATH)
    tracking_page.my_orders_click()
    tracking_page.wait_for_url(URLS.ORDER_HISTORY_FROM_TRACK)
    assert driver_chrome.current_url == URLS.ORDER_HISTORY_FROM_TRACK


@allure.title("TC016:Tracking order button is enabled")
@allure.description("Checking that if all required data is entered as needed tracking order button is enabled")
def test_tracking_button_enabled(driver_chrome):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.ORDER_NUMBER_XPATH)
    input_order = tracking_page.order_number_field()
    input_order.send_keys("BY123456-123456")
    input_phone = tracking_page.phone_number_field()
    input_phone.send_keys("375331234567")
    check_button = tracking_page.button_tracking_order()
    assert check_button.is_enabled()


@allure.title("TC017:Tracking order button is disabled when phone is missing")
@allure.description("Checking that if phone number field is empty, tracking order button is disabled")
def test_tracking_button_order_disabled(driver_chrome):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.ORDER_NUMBER_XPATH)
    input_order = tracking_page.order_number_field()
    input_order.send_keys("BY123456-123456")
    check_button = tracking_page.button_tracking_order()
    assert not check_button.is_enabled()


@allure.title("TC018:Tracking order button is disabled when order is missing")
@allure.description("Checking that if order number field is empty, tracking order button is disabled")
def test_tracking_button_phone_disabled(driver_chrome):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.ORDER_NUMBER_XPATH)
    input_phone = tracking_page.phone_number_field()
    input_phone.send_keys("375331234567")
    check_button = tracking_page.button_tracking_order()
    assert not check_button.is_enabled()


@allure.title("TC019:Validation message appears for invalid order number")
@allure.description("Checking that correct validation appears for invalid order number for the tracking page")
@pytest.mark.parametrize("order_number", ["BY123456-2", "12ABCJAJA"])
def test_track_order_number(driver_chrome, order_number):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.ORDER_NUMBER_XPATH)
    input_element = tracking_page.order_number_field()
    input_element.send_keys(order_number)
    tracking_page.wait_for_text_in_element(
        tracking_page.ORDER_VALIDATION_XPATH,
        "Пожалуйста, проверьте, правильно ли указан номер заказа.")
    assert tracking_page.validation_order_number(
    ).text == "Пожалуйста, проверьте, правильно ли указан номер заказа."


@allure.title("TC020:Validation message appears for invalid phone number")
@allure.description("Checking that correct validation appears if invalid phone number was entered on the tracking page")
@pytest.mark.parametrize("phone_number", ["12312312", "ABCJAJA"])
def test_track_phone_number(driver_chrome, phone_number):
    tracking_page = Tracking(driver_chrome)
    tracking_page.open_tracking()
    tracking_page.wait_for_element(tracking_page.PHONE_NUMBER_XPATH)
    input_element = tracking_page.phone_number_field()
    input_element.send_keys(phone_number)
    tracking_page.wait_for_element(tracking_page.PHONE_VALIDATION_XPATH)
    assert tracking_page.validation_phone_number(
    ).text == "Номер телефона должен состоять из 12 цифр."
