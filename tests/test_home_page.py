import time

from selenium import webdriver

#tests on start
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage

class TestHomePage:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    def test_question_cost_and_pay(self):
        # перешли на страницу тестового приложения
        url = 'https://qa-scooter.praktikum-services.ru/'
        self.driver.get(url)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))
        home_page = HomePage(self.driver)
        home_page.click_question_cost_and_pay()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.ANSWER_COST_AND_PAY_VISIBLE))
        answer_cost_and_pay = self.driver.find_element(*HomePageLocators.ANSWER_COST_AND_PAY_VISIBLE)
        actually_value = answer_cost_and_pay.text
        expected_value  = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert actually_value ==  expected_value, f'Ожидалось значение: "{expected_value }", получено "{actually_value}"'

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()