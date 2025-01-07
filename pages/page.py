from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.common_locators import CommonLocators
import url

class Page:
    def __init__(self, driver):
        self.driver = driver

    def _click_locator(self, locator):
        locator_to_click = self.driver.find_element(*locator)
        locator_to_click.click()

    def click_logo(self):
        self._click_locator(CommonLocators.LOGO)

    def click_yandex(self):
        self._click_locator(CommonLocators.YANDEX)

    def click_cookie(self):
        self._click_locator(CommonLocators.COOKIE_BUTTON)

    def wait_for_load_yandex_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.YANDEX))

    def move_from_yandex_page_to_order_scooter_page(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.HOME_PAGE))