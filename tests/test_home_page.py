import allure
import pytest

from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from input_data import Answers

class TestHomePage:
    @allure.title(
        'Проверка выпадающего меню с вопросом для ответа {answer_text}')  # декораторы
    @allure.description(
        'На странице ищем элемент с ответом на вопрос')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    @pytest.mark.parametrize('question_locator , answer_locator, answer_text',
                             [
                                 [HomePageLocators.Question.COST_AND_PAY, HomePageLocators.Answer.COST_AND_PAY,
                                  Answers.COST_AND_PAY],
                                 [HomePageLocators.Question.ORDER_SOME_SCOOTERS,
                                  HomePageLocators.Answer.ORDER_SOME_SCOOTERS, Answers.ORDER_SOME_SCOOTERS],
                                 [HomePageLocators.Question.RENTAL_TIME, HomePageLocators.Answer.RENTAL_TIME,
                                  Answers.RENTAL_TIME],
                                 [HomePageLocators.Question.ORDER_TODAY, HomePageLocators.Answer.ORDER_TODAY,
                                  Answers.ORDER_TODAY],
                                 [HomePageLocators.Question.EXTEND_ORDER, HomePageLocators.Answer.EXTEND_ORDER,
                                  Answers.EXTEND_ORDER],
                                 [HomePageLocators.Question.CHARGER_INCLUDED, HomePageLocators.Answer.CHARGER_INCLUDED,
                                  Answers.CHARGER_INCLUDED],
                                 [HomePageLocators.Question.CANCEL_ORDER, HomePageLocators.Answer.CANCEL_ORDER,
                                  Answers.CANCEL_ORDER],
                                 [HomePageLocators.Question.BEYOND_MKAD, HomePageLocators.Answer.BEYOND_MKAD,
                                  Answers.BEYOND_MKAD]
                             ]
                             )
    def test_question(self, page_driver, question_locator, answer_locator, answer_text):
        home_page = HomePage(page_driver)
        home_page.check_cookies()
        home_page.click_locator(question_locator)
        home_page.wait_for_answer_by_locator(answer_locator)
        actually_value = home_page.get_answer_text_by_locator(answer_locator)
        expected_value = answer_text
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'