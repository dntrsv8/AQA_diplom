import allure
import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver_chrome = driver

    @allure.step("Checking browser tab's title")
    def title(self):
        return self.driver_chrome.title

    @allure.step("Forced click on the element")
    def forced_click(self, element):
        self.driver_chrome.execute_script("arguments[0].click();", element)

    @allure.step("Switching the frame")
    def switch_to_iframe(self, locator):
        iframe_element = self.driver_chrome.find_element(*locator)
        self.driver_chrome.switch_to.frame(iframe_element)

    @allure.step("Waiting until url is exact")
    def wait_for_url(self, url):
        WebDriverWait(self.driver_chrome, 10).until(EC.url_to_be(url))

    @allure.step("Wait until url contains")
    def wait_url_contains(self, url):
        WebDriverWait(self.driver_chrome, 10).until(EC.url_contains(url))

    @allure.step("Wait for element to be located")
    def wait_for_element(self, locator):
        WebDriverWait(self.driver_chrome, 10).until(
            EC.presence_of_element_located((By.XPATH, locator)))

    @allure.step("Wait for element's visibility")
    def wait_for_element_visibility(self, locator):
        WebDriverWait(self.driver_chrome, 10).until(
            EC.visibility_of_element_located((By.XPATH, locator)))

    @allure.step("Wait for text in the element")
    def wait_for_text_in_element(self, locator, text):
        WebDriverWait(self.driver_chrome, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, locator), text)
        )

    @allure.step("Enter text using pyautogui")
    def enter_text_pyautogui_current(self, text):
        pyautogui.typewrite(text)

    @allure.step("Hover over element")
    def hover_over_element(self, element):
        action = ActionChains(self.driver_chrome)
        action.move_to_element(element).perform()

    @allure.step("Scroll to the page's footer")
    def scroll_to_footer(self):
        footer = self.driver_chrome.find_element(By.TAG_NAME, "body")
        footer.send_keys(Keys.END)

    @allure.step("Scroll to the end of the page's body")
    def scroll_to_end_of_body(self):
        self.driver_chrome.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Switch to the second tab of the browser")
    def switch_to_second_tab(self):
        current_tab = self.driver_chrome.current_window_handle
        WebDriverWait(
            self.driver_chrome, 10).until(
            EC.number_of_windows_to_be(2))
        all_handles = self.driver_chrome.window_handles
        new_tab_handle = [
            handle for handle in all_handles if handle != current_tab][0]
        self.driver_chrome.switch_to.window(new_tab_handle)
