from selenium import webdriver

from pages.home_page import HomePage
from url import Url

class TestHomePage:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    def test_question_cost_and_pay(self):
        # перешли на страницу тестового приложения
        self.driver.get(Url.HOME_PAGE)
        home_page = HomePage(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_question_cost_and_pay()
        home_page.wait_for_cost_and_pay_drop_answer()
        actually_value = home_page.get_cost_and_pay_answer_text()
        expected_value = HomePage.Answers.COST_AND_PAY
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value }", получено "{actually_value}"'

    def test_question_order_some_scooters(self):
        self.driver.get(Url.HOME_PAGE)
        home_page = HomePage(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_question_order_some_scooters()
        home_page.wait_for_order_some_scooters_answer()
        actually_value = home_page.get_order_some_scooters_answer_text()
        expected_value = HomePage.Answers.ORDER_SOME_SCOOTERS
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    def test_question_rental_time(self):
        self.driver.get(Url.HOME_PAGE)
        home_page = HomePage(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_question_rental_time()
        home_page.wait_for_rental_time_answer()
        actually_value = home_page.get_rental_time_answer_text()
        expected_value = HomePage.Answers.RENTAL_TIME
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()