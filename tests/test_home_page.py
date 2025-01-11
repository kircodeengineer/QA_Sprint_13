import allure
from selenium import webdriver

from pages.home_page import HomePage
import url

class TestHomePage:
    @allure.title('Проверка выпадающего меню с вопросом - Сколько это стоит? И как оплатить?')  # декораторы
    @allure.description('На странице ищем элемент с ответом на вопрос и проверяем, что его значение == "Сутки — 400 рублей. Оплата курьеру — наличными или картой.')
    @allure.testcase('ссылка на тест-кейс', 'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    def test_question_cost_and_pay(self, page_driver):
        home_page = HomePage(page_driver)
        home_page.check_cookies()
        home_page.click_question_cost_and_pay()
        home_page.wait_for_cost_and_pay_drop_answer()
        actually_value = home_page.get_cost_and_pay_answer_text()
        expected_value = HomePage.Answers.COST_AND_PAY
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value }", получено "{actually_value}"'

    @allure.title('Проверка выпадающего меню с вопросом - Хочу сразу несколько самокатов! Так можно?')  # декораторы
    @allure.description(
        'На странице ищем элемент с ответом на вопрос и проверяем, что его значение == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    def test_question_order_some_scooters(self, page_driver):
        home_page = HomePage(page_driver)
        home_page.check_cookies()
        home_page.click_question_order_some_scooters()
        home_page.wait_for_order_some_scooters_answer()
        actually_value = home_page.get_order_some_scooters_answer_text()
        expected_value = HomePage.Answers.ORDER_SOME_SCOOTERS
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.title('Проверка выпадающего меню с вопросом - Как рассчитывается время аренды?')  # декораторы
    @allure.description(
        'На странице ищем элемент с ответом на вопрос и проверяем, что его значение == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    def test_question_rental_time(self, page_driver):
        home_page = HomePage(page_driver)
        home_page.check_cookies()
        home_page.click_question_rental_time()
        home_page.wait_for_rental_time_answer()
        actually_value = home_page.get_rental_time_answer_text()
        expected_value = HomePage.Answers.RENTAL_TIME
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.title('Проверка выпадающего меню с вопросом - Можно ли заказать самокат прямо на сегодня?')  # декораторы
    @allure.description(
        'На странице ищем элемент с ответом на вопрос и проверяем, что его значение == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    def test_question_order_today(self, page_driver):
        home_page = HomePage(page_driver)
        home_page.check_cookies()
        home_page.click_question_order_today()
        home_page.wait_for_order_today_answer()
        actually_value = home_page.get_order_today_text()
        expected_value = HomePage.Answers.ORDER_TODAY
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.title('Проверка выпадающего меню с вопросом - Можно ли продлить заказ или вернуть самокат раньше?')  # декораторы
    @allure.description(
        'На странице ищем элемент с ответом на вопрос и проверяем, что его значение == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    def test_question_extend_order(self, page_driver):
        home_page = HomePage(page_driver)
        home_page.check_cookies()
        home_page.click_question_extend_order()
        home_page.wait_for_extend_order_answer()
        actually_value = home_page.get_extend_order_text()
        expected_value = HomePage.Answers.EXTEND_ORDER
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.title(
        'Проверка выпадающего меню с вопросом - Вы привозите зарядку вместе с самокатом?')  # декораторы
    @allure.description(
        'На странице ищем элемент с ответом на вопрос и проверяем, что его значение == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    def test_question_charger_included(self, page_driver):
        home_page = HomePage(page_driver)
        home_page.check_cookies()
        home_page.click_question_charger_included()
        home_page.wait_for_charger_included_answer()
        actually_value = home_page.get_charger_included_text()
        expected_value = HomePage.Answers.CHARGER_INCLUDED
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.title(
        'Проверка выпадающего меню с вопросом - Можно ли отменить заказ?')  # декораторы
    @allure.description(
        'На странице ищем элемент с ответом на вопрос и проверяем, что его значение == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    def test_question_cancel_order(self, page_driver):
        home_page = HomePage(page_driver)
        home_page.check_cookies()
        home_page.click_question_cancel_order()
        home_page.wait_for_cancel_order_answer()
        actually_value = home_page.get_cancel_order_text()
        expected_value = HomePage.Answers.CANCEL_ORDER
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.title(
        'Проверка выпадающего меню с вопросом - Я жизу за МКАДом, привезёте?')  # декораторы
    @allure.description(
        'На странице ищем элемент с ответом на вопрос и проверяем, что его значение == "Да, обязательно. Всем самокатов! И Москве, и Московской области."')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    def test_question_beyond_mkad(self, page_driver):
        home_page = HomePage(page_driver)
        home_page.check_cookies()
        home_page.click_question_beyond_mkad()
        home_page.wait_for_beyond_mkad_answer()
        actually_value = home_page.get_beyond_mkad_text()
        expected_value = HomePage.Answers.BEYOND_MKAD
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'