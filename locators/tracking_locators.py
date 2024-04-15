class TrackingLocators:
    BUTTON_XPATH = "//*[contains(text(),'Отклонить')]"
    ORDER_NUMBER_XPATH = "//*[@name='input-order-number']"
    ORDER_VALIDATION_XPATH = "//div[@class='input__validation-message input__validation-message_default-theme']"
    PHONE_NUMBER_XPATH = "//*[@name='input-phone']"
    PHONE_VALIDATION_XPATH = "//*[@id='vue-root']//form//div[2]//div[contains(@class, 'input__validation-message')]"
    CHECK_BUTTON_XPATH = '//*[@class="x-button x-button_primaryFilledWeb7184 x-button_40 x-button_intrinsic-width"]'
    MY_ORDERS_XPATH = "//*[@role='link' and text()='Мои заказы']"
