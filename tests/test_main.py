import pyautogui
import pytest
import allure
from selenium.webdriver.common.by import By
from pages.main import MainPage
from data.urls import URLS


@allure.title("TC001:Correct page is opened for Women top menu tab")
@allure.description("Checking that correct page (url) is opened when 'Women' tab is clicked")
def test_open_women_section(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.open_women_section()
    main_page.wait_for_url(URLS.WOMEN_TOP)
    assert driver_chrome.current_url == URLS.WOMEN_TOP


@allure.title("TC002:Login pop-up is displayed")
@allure.description("Checking that login pop-up appears when 'Login' button is being clicked")
def test_navigate_to_login(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    button = main_page.login_button()
    main_page.forced_click(button)
    main_page.wait_for_element(main_page.LOGIN_BUTTON_POPUP)
    popup_element = main_page.login_popup()
    assert popup_element is not None


@allure.title("TC003:Search by item number opens item's page")
@allure.description("Checking that url of the opened through search page has an item's number in it")
def test_search_by_item_number(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.wait_for_element(main_page.SEARCH_BAR_XPATH)
    input_element = main_page.search_bar()
    item_number = "rtlack740303"
    input_element.send_keys(item_number)
    search_button = main_page.search_button()
    main_page.forced_click(search_button)
    main_page.wait_url_contains(item_number)
    assert item_number in driver_chrome.current_url


@allure.title("TC004:Login button is disabled when password field is empty")
@allure.description("Checking that login button is disabled if only login field is populated")
@pytest.mark.parametrize("email",
                         ['dziyana.tarasava@gmail.com',
                          'dziyana@',
                          'dziyana@gmail'])
def test_login_disabled_button(driver_chrome, email):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    button = main_page.login_button()
    main_page.forced_click(button)
    main_page.wait_for_element(main_page.LOGIN_BUTTON_POPUP)
    pyautogui.typewrite(email)
    login_button_check = main_page.login_popup_button()
    assert not login_button_check.is_enabled()


@allure.title("TC005:Validation message appears for invalid email in login popup")
@allure.description("Checking that validation appears for wrong email entered")
@pytest.mark.parametrize("invalid_email",
                         ['dziyana', 'dziyana@', 'dziyana@gmail'])
def test_login_email_validation(driver_chrome, invalid_email):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.wait_for_element(main_page.LOGIN_BUTTON_XPATH)
    button = main_page.login_button()
    main_page.forced_click(button)
    main_page.wait_for_element(main_page.LOGIN_BUTTON_POPUP)
    main_page.enter_text_pyautogui_current(invalid_email)
    pyautogui.press('tab')
    validation_check = main_page.login_popup_email_validation()
    assert validation_check.text == 'Пожалуйста, проверьте, правильно ли указан адрес'


@allure.title("TC006:Correct page is opened for the VK icon from footer")
@allure.description("Checking that correct page is opened if VK icon is clicked from the footer")
def test_vk_link(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.VK_XPATH)
    element = main_page.footer_vk()
    element.click()
    main_page.switch_to_second_tab()
    assert driver_chrome.current_url == URLS.VK_FOOTER


@allure.title("TC007:Correct page is opened for the Twitter icon from footer")
@allure.description("Checking that correct page is opened if Twitter icon is clicked from the footer")
def test_twitter_link(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.TWITTER_XPATH)
    element = main_page.footer_twitter()
    element.click()
    main_page.switch_to_second_tab()
    assert driver_chrome.current_url == URLS.TWITTER_FOOTER


@allure.title("TC008:Correct page is opened for the OK icon from footer")
@allure.description("Checking that correct page is opened if OK icon is clicked from the footer of the main page")
def test_ok_link(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.OK_XPATH)
    element = main_page.footer_ok()
    element.click()
    main_page.switch_to_second_tab()
    assert driver_chrome.current_url == URLS.OK_FOOTER


@allure.title("TC009:KZ localization of the website is opened")
@allure.title("Checking that KZ localization of the website is opened when clicked from the footer popup")
def test_site_localization_kz(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element_visibility(main_page.BY_LOCAL)
    country = main_page.by_site()
    main_page.hover_over_element(country)
    kz = main_page.kz_site()
    main_page.forced_click(kz)
    assert driver_chrome.current_url == URLS.KZ_SITE


@allure.title("TC010:RU localization of the website is opened")
@allure.title("Checking that RU localization of the website is opened when clicked from the footer popup")
def test_site_localization_ru(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element_visibility(main_page.BY_LOCAL)
    country = main_page.by_site()
    main_page.hover_over_element(country)
    ru = main_page.ru_site()
    main_page.forced_click(ru)
    assert driver_chrome.current_url == URLS.RU_SITE


@allure.title("TC011:Email validation appears for subscription with invalid emails")
@allure.description("Checking that email validation appears for the subscription feature from the footer")
@pytest.mark.parametrize("emails", ['dziyana',
                         'dziyana@', 'dziyana@test', 'dziyana@test.'])
def test_subscription_validation_email(driver_chrome, emails):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.SUBSCRIPTION_EMAIL)
    field = main_page.subscription_footer_email()
    field.click()
    main_page.enter_text_pyautogui_current(emails)
    pyautogui.press('tab')
    main_page.wait_for_element(main_page.EMAIL_VALIDATION)
    validation = main_page.subscription_validation_email()
    assert validation.text == 'Пожалуйста, проверьте, правильно ли указан адрес'


@allure.title("TC012:Correct page is opened for consent agreement from subscription")
@allure.description("Checking url of the opened consent agreement page from the subscription feature")
def test_acceptance_link(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.scroll_to_footer()
    main_page.wait_for_element(main_page.ACCEPTANCE_LINK)
    main_page.acceptance_link_click()
    main_page.switch_to_second_tab()
    assert driver_chrome.current_url == URLS.CONSENT_PDF


@allure.title("TC013:Chat popup appears")
@allure.description("Checking that chat popup appears with correct header text")
def test_chat_open_popup(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.open_main()
    main_page.wait_for_element(main_page.CHAT_POPUP_BUTTON_XPATH)
    button = main_page.chat_open_button()
    main_page.hover_over_element(button)
    button.click()
    main_page.switch_to_iframe((By.XPATH, main_page.CHAT_IFRAME_XPATH))
    main_page.wait_for_element(main_page.CHAT_POPUP_HEADER_XPATH)
    popup_element = main_page.chat_open_header()
    assert "Напишите нам, операторы в сети!" in popup_element.text
