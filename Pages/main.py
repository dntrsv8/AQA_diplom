import allure
from selenium.webdriver.common.by import By
from Pages.basepage import BasePage
from locators.main_locators import MainLocators
from data.urls import URLS


class MainPage(BasePage, MainLocators):

    @allure.step("Opening main page with cookies decline")
    def open_main(self):
        self.driver_chrome.get(URLS.MAIN_PAGE)
        self.wait_for_element(self.BUTTON_XPATH)
        button = self.driver_chrome.find_element(By.XPATH, self.BUTTON_XPATH)
        self.forced_click(button)

    @allure.step("Opening Women section through top menu")
    def open_women_section(self):
        women_element = self.driver_chrome.find_element(
            By.XPATH, self.WOMAN_TAB_XPATH)
        women_element.click()

    @allure.step("Clicking the chat button")
    def chat_open_button(self):
        chat_button = self.driver_chrome.find_element(
            By.XPATH, self.CHAT_POPUP_BUTTON_XPATH)
        return chat_button

    @allure.step("Finding chat popup header")
    def chat_open_header(self):
        chat_popup = self.driver_chrome.find_element(
            By.XPATH, self.CHAT_POPUP_HEADER_XPATH)
        return chat_popup

    @allure.step("Finding chat popup container")
    def chat_popup(self):
        popup = self.driver_chrome.find_element(
            By.XPATH, self.CHAT_POPUP_CONTAINER)
        return popup

    @allure.step("Finding login button")
    def login_button(self):
        login_button = self.driver_chrome.find_element(
            By.XPATH, self.LOGIN_BUTTON_XPATH)
        return login_button

    @allure.step("Finding login popup")
    def login_popup(self):
        login_popup = self.driver_chrome.find_element(
            By.XPATH, self.LOGIN_BUTTON_POPUP)
        return login_popup

    @allure.step("Finding email field on the popup")
    def login_email(self):
        login_email = self.driver_chrome.find_element(
            By.XPATH, self.EMAIL_POPUP)
        return login_email

    @allure.step("Finding login popup button")
    def login_popup_button(self):
        login_popup_button = self.driver_chrome.find_element(
            By.XPATH, self.LOGIN_BUTTON_POPUP)
        return login_popup_button

    @allure.step("Finding the popup validation")
    def login_popup_email_validation(self):
        email_validation = self.driver_chrome.find_element(
            By.XPATH, self.VALIDATION_PATH_POPUP)
        return email_validation

    @allure.step("Finding the search bar")
    def search_bar(self):
        search_field = self.driver_chrome.find_element(
            By.XPATH, self.SEARCH_BAR_XPATH)
        return search_field

    @allure.step("Finding the search button")
    def search_button(self):
        search_button = self.driver_chrome.find_element(
            By.XPATH, self.SEARCH_BUTTON_XPATH)
        return search_button

    @allure.step("Finding the localization popup")
    def footer_localization(self):
        localization_popup = self.driver_chrome.find_element(
            By.XPATH, self.LOCALIZATION_FOOTER)
        return localization_popup

    @allure.step("Finding the KZ localization option")
    def kz_site(self):
        local = self.driver_chrome.find_element(By.XPATH, self.KZ_LOCAL)
        return local

    @allure.step("Finding the RU localization option")
    def ru_site(self):
        local = self.driver_chrome.find_element(By.XPATH, self.RU_LOCAL)
        return local

    @allure.step("Finding the BY localization option")
    def by_site(self):
        local = self.driver_chrome.find_element(By.XPATH, self.BY_LOCAL)
        return local

    @allure.step("Finding the email field in the subscription feature")
    def subscription_footer_email(self):
        email = self.driver_chrome.find_element(
            By.XPATH, self.SUBSCRIPTION_EMAIL)
        return email

    @allure.step("Finding the subscribe button")
    def subscription_submit_button(self):
        button = self.driver_chrome.find_element(
            By.XPATH, self.SUBSCRIPTION_BUTTON)
        return button

    @allure.step("Finding the email validation message for subscription")
    def subscription_validation_email(self):
        validation = self.driver_chrome.find_element(
            By.XPATH, self.EMAIL_VALIDATION)
        return validation

    @allure.step("Clicking the subscription conditions hyperlink")
    def acceptance_link_click(self):
        link = self.driver_chrome.find_element(By.XPATH, self.ACCEPTANCE_LINK)
        link.click()

    @allure.step("Finding the VK element")
    def footer_vk(self):
        vk_link = self.driver_chrome.find_element(By.XPATH, self.VK_XPATH)
        return vk_link

    @allure.step("Finding the Twitter element")
    def footer_twitter(self):
        twitter_link = self.driver_chrome.find_element(
            By.XPATH, self.TWITTER_XPATH)
        return twitter_link

    @allure.step("Finding the OK element")
    def footer_ok(self):
        ok_link = self.driver_chrome.find_element(By.XPATH, self.OK_XPATH)
        return ok_link
