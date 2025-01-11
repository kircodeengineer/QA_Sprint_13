import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.common_locators import CommonLocators
import url

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по элементу по локатору {locator}')
    def _click_locator(self, locator):
        locator_to_click = self.driver.find_element(*locator)
        locator_to_click.click()

    @allure.step('Клик по Лого приложения')
    def click_logo(self):
        self._click_locator(CommonLocators.LOGO)

    @allure.step('Клик по Лого Яндекса')
    def click_yandex(self):
        self._click_locator(CommonLocators.YANDEX)

    @allure.step('Клик по кнопки Куки')
    def click_cookie(self):
        self._click_locator(CommonLocators.COOKIE_BUTTON)

    @allure.step('Ожидаем загрузку страницы Дзена')
    def wait_for_load_yandex_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.YANDEX))

    @allure.step('Возвращаемся со страницы Дзена на страницу приложения')
    def move_from_yandex_page_to_order_scooter_page(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.HOME_PAGE))