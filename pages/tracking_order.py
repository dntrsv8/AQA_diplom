import allure
from data.urls import URLS
from pages.basepage import BasePage
from locators.tracking_locators import TrackingLocators
from selenium.webdriver.common.by import By


class Tracking(BasePage, TrackingLocators):

    @allure.step("Opening the Tracking order page with cookies decline")
    def open_tracking(self):
        self.driver_chrome.get(URLS.TRACKING_PAGE)
        self.wait_for_element(self.BUTTON_XPATH)
        button = self.driver_chrome.find_element(By.XPATH, self.BUTTON_XPATH)
        self.forced_click(button)

    @allure.step("Finding the order number field")
    def order_number_field(self):
        order_number = self.driver_chrome.find_element(
            By.XPATH, self.ORDER_NUMBER_XPATH)
        return order_number

    @allure.step("Finding the Order validation message")
    def validation_order_number(self):
        validation = self.driver_chrome.find_element(
            By.XPATH, self.ORDER_VALIDATION_XPATH)
        return validation

    @allure.step("Finding the phone number field")
    def phone_number_field(self):
        phone_number = self.driver_chrome.find_element(
            By.XPATH, self.PHONE_NUMBER_XPATH)
        return phone_number

    @allure.step("Finding the phone number validation")
    def validation_phone_number(self):
        validation = self.driver_chrome.find_element(
            By.XPATH, self.PHONE_VALIDATION_XPATH)
        return validation

    @allure.step("Finding the tracking order button")
    def button_tracking_order(self):
        button = self.driver_chrome.find_element(
            By.XPATH, self.CHECK_BUTTON_XPATH)
        return button

    @allure.step("Clicking my orders button")
    def my_orders_click(self):
        link = self.driver_chrome.find_element(By.XPATH, self.MY_ORDERS_XPATH)
        link.click()
