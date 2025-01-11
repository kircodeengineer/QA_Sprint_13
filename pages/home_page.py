import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

import url
from locators.common_locators import CommonLocators
from pages.page import Page
from locators.home_page_locators import HomePageLocators

class HomePage(Page):
    class Answers:
        COST_AND_PAY = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        ORDER_SOME_SCOOTERS = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        RENTAL_TIME = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        ORDER_TODAY = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        EXTEND_ORDER = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        CHARGER_INCLUDED = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        CANCEL_ORDER = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        BEYOND_MKAD = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

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

    @allure.step('Выполняем клик по меню с вопросом - Сколько это стоит? И как оплатить?')
    def click_question_cost_and_pay(self):
        self._click_locator(HomePageLocators.Question.COST_AND_PAY)

    @allure.step('Ожидаем появление на странице элемента с ответом на вопрос - Сколько это стоит? И как оплатить?')
    def wait_for_cost_and_pay_drop_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.COST_AND_PAY))

    @allure.step('Получаем текстовое значение элемента с ответом на вопрос - Сколько это стоит? И как оплатить?')
    def get_cost_and_pay_answer_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.COST_AND_PAY).text

    @allure.step('Выполняем клик по меню с вопросом - Хочу сразу несколько самокатов! Так можно?')
    def click_question_order_some_scooters(self):
        self._click_locator(HomePageLocators.Question.ORDER_SOME_SCOOTERS)

    @allure.step('Ожидаем появление на странице элемента с ответом на вопрос - Хочу сразу несколько самокатов! Так можно?')
    def wait_for_order_some_scooters_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.ORDER_SOME_SCOOTERS))

    @allure.step('Получаем текстовое значение элемента с ответом на вопрос - Хочу сразу несколько самокатов! Так можно?')
    def get_order_some_scooters_answer_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.ORDER_SOME_SCOOTERS).text

    @allure.step('Выполняем клик по меню с вопросом - Как рассчитывается время аренды?')
    def click_question_rental_time(self):
        self._click_locator(HomePageLocators.Question.RENTAL_TIME)

    @allure.step(
        'Ожидаем появление на странице элемента с ответом на вопрос - Как рассчитывается время аренды?')
    def wait_for_rental_time_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.RENTAL_TIME))

    @allure.step(
        'Получаем текстовое значение элемента с ответом на вопрос - Как рассчитывается время аренды?')
    def get_rental_time_answer_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.RENTAL_TIME).text

    @allure.step('Выполняем клик по меню с вопросом - Можно ли заказать самокат прямо на сегодня?')
    def click_question_order_today(self):
        self._click_locator(HomePageLocators.Question.ORDER_TODAY)

    @allure.step(
        'Ожидаем появление на странице элемента с ответом на вопрос - Можно ли заказать самокат прямо на сегодня?')
    def wait_for_order_today_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.ORDER_TODAY))

    @allure.step(
        'Получаем текстовое значение элемента с ответом на вопрос - Можно ли заказать самокат прямо на сегодня?')
    def get_order_today_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.ORDER_TODAY).text

    @allure.step('Выполняем клик по меню с вопросом - Можно ли продлить заказ или вернуть самокат раньше?')
    def click_question_extend_order(self):
        self._click_locator(HomePageLocators.Question.EXTEND_ORDER)

    @allure.step(
        'Ожидаем появление на странице элемента с ответом на вопрос - Можно ли продлить заказ или вернуть самокат раньше?')
    def wait_for_extend_order_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.EXTEND_ORDER))

    @allure.step(
        'Получаем текстовое значение элемента с ответом на вопрос - Можно ли продлить заказ или вернуть самокат раньше?')
    def get_extend_order_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.EXTEND_ORDER).text

    @allure.step('Выполняем клик по меню с вопросом - Вы привозите зарядку вместе с самокатом?')
    def click_question_charger_included(self):
        self._click_locator(HomePageLocators.Question.CHARGER_INCLUDED)

    @allure.step(
        'Ожидаем появление на странице элемента с ответом на вопрос - Вы привозите зарядку вместе с самокатом?')
    def wait_for_charger_included_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.CHARGER_INCLUDED))

    @allure.step(
        'Получаем текстовое значение элемента с ответом на вопрос - Вы привозите зарядку вместе с самокатом?')
    def get_charger_included_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.CHARGER_INCLUDED).text

    @allure.step('Выполняем клик по меню с вопросом - Можно ли отменить заказ?')
    def click_question_cancel_order(self):
        self._click_locator(HomePageLocators.Question.CANCEL_ORDER)

    @allure.step(
        'Ожидаем появление на странице элемента с ответом на вопрос - Можно ли отменить заказ?')
    def wait_for_cancel_order_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.CANCEL_ORDER))

    @allure.step(
        'Получаем текстовое значение элемента с ответом на вопрос - Можно ли отменить заказ?')
    def get_cancel_order_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.CANCEL_ORDER).text

    @allure.step('Выполняем клик по меню с вопросом - Я жизу за МКАДом, привезёте?')
    def click_question_beyond_mkad(self):
        self._click_locator(HomePageLocators.Question.BEYOND_MKAD)

    @allure.step(
        'Ожидаем появление на странице элемента с ответом на вопрос - Я жизу за МКАДом, привезёте?')
    def wait_for_beyond_mkad_answer(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.Answer.BEYOND_MKAD))

    @allure.step(
        'Получаем текстовое значение элемента с ответом на вопрос - Я жизу за МКАДом, привезёте?')
    def get_beyond_mkad_text(self):
        return self.driver.find_element(*HomePageLocators.Answer.BEYOND_MKAD).text

    @allure.step('Выполняем клик по кнопке Заказать {order_button}')
    def click_order_button(self, order_button):
        self._click_locator(HomePageLocators.BUTTONS[order_button])