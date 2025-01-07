from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from url import Url
from locators.common_locators import CommonLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(Url.ORDER_PAGE))

    def __click_locator(self, locator):
        locator_to_click = self.driver.find_element(*locator)
        locator_to_click.click()

    def click_logo(self):
        self.__click_locator(CommonLocators.LOGO)