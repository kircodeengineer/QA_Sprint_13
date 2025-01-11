import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

from locators.common_locators import CommonLocators
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    @allure.step('Проверяем наличие на странице элемента по локатору {locator}')  # декоратор
    def check_exists_by_locator(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Ожидаем загрузку начальной страницы')
    def check_cookies(self):
        # необходимо принять куки, иначе selenium не видит нижней кнопки Заказать и выпадающего меню
        if self.check_exists_by_locator(CommonLocators.COOKIE_BUTTON):
            self.click_cookie()

    @allure.step('Выполняем клик по кнопке Заказать {order_button}')
    def click_order_button(self, order_button):
        self.click_locator(HomePageLocators.BUTTONS[order_button])

    @allure.step('Ждём ответа по локатору {locator}')
    def wait_for_answer_by_locator(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получаем текст ответа по локатору {locator}')
    def get_answer_text_by_locator(self, locator):
        return self.driver.find_element(*locator).text