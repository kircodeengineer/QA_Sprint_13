from selenium.webdriver.common.by import By

class CommonLocators:
    LOGO = (By.XPATH, ".//img[@src='/assets/scooter.svg']")
    YANDEX = (By.XPATH, ".//img[@src='/assets/ya.svg']")
    COOKIE_BUTTON = (By.XPATH, ".//button[@id='rcc-confirm-button' and @class='App_CookieButton__3cvqF']")