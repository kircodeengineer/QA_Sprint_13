from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from url import Url

class HomePage:
    COST_AND_PAY_ANSWER = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ORDER_SOME_SCOOTERS_ANSWER = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(Url.HOME_PAGE))

    def click_question_cost_and_pay(self):
        question_cost_and_pay = self.driver.find_element(*HomePageLocators.Question.COST_AND_PAY)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_cost_and_pay)
        question_cost_and_pay.click()

    def wait_for_cost_and_pay_drop_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.COST_AND_PAY))

    def get_cost_and_pay_answer_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.COST_AND_PAY).text

    def click_question_order_some_scooters(self):
        order_some_scooters = self.driver.find_element(*HomePageLocators.Question.ORDER_SOME_SCOOTERS)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_some_scooters)
        order_some_scooters.click()

    def wait_for_order_some_scooters_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.ORDER_SOME_SCOOTERS))

    def get_order_some_scooters_answer_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.ORDER_SOME_SCOOTERS).text


