from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from url import Url

class HomePage:
    class Answers:
        COST_AND_PAY = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        ORDER_SOME_SCOOTERS = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        RENTAL_TIME = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        ORDER_TODAY = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        EXTEND_ORDER = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        CHARGER_INCLUDED = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        CANCEL_ORDER = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        BEYOND_MKAD = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    def __click_question(self, locator):
        question = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(Url.HOME_PAGE))

    # cost_and_pay
    def click_question_cost_and_pay(self):
        self.__click_question(HomePageLocators.Question.COST_AND_PAY)

    def wait_for_cost_and_pay_drop_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.COST_AND_PAY))

    def get_cost_and_pay_answer_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.COST_AND_PAY).text

    # order_some_scooters
    def click_question_order_some_scooters(self):
        self.__click_question(HomePageLocators.Question.ORDER_SOME_SCOOTERS)

    def wait_for_order_some_scooters_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.ORDER_SOME_SCOOTERS))

    def get_order_some_scooters_answer_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.ORDER_SOME_SCOOTERS).text

    # rental_time
    def click_question_rental_time(self):
        self.__click_question(HomePageLocators.Question.RENTAL_TIME)

    def wait_for_rental_time_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.RENTAL_TIME))

    def get_rental_time_answer_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.RENTAL_TIME).text

    # order_today
    def click_question_order_today(self):
        self.__click_question(HomePageLocators.Question.ORDER_TODAY)

    def wait_for_order_today_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.ORDER_TODAY))

    def get_order_today_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.ORDER_TODAY).text

    # extend_order
    def click_question_extend_order(self):
        self.__click_question(HomePageLocators.Question.EXTEND_ORDER)

    def wait_for_extend_order_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.EXTEND_ORDER))

    def get_extend_order_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.EXTEND_ORDER).text

    # charger_included
    def click_question_charger_included(self):
        self.__click_question(HomePageLocators.Question.CHARGER_INCLUDED)

    def wait_for_charger_included_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.CHARGER_INCLUDED))

    def get_charger_included_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.CHARGER_INCLUDED).text

    # cancel_order
    def click_question_cancel_order(self):
        self.__click_question(HomePageLocators.Question.CANCEL_ORDER)

    def wait_for_cancel_order_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.CANCEL_ORDER))

    def get_cancel_order_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.CANCEL_ORDER).text

    # beyond_mkad
    def click_question_beyond_mkad(self):
        self.__click_question(HomePageLocators.Question.BEYOND_MKAD)

    def wait_for_beyond_mkad_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.BEYOND_MKAD))

    def get_beyond_mkad_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.BEYOND_MKAD).text