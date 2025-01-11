import allure
import pytest

import url
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from input_data import order_input_data_list

class TestOrderPage:
    cookie = False

    @allure.title(
        'Проверка позитивного сценария заказа самоката.')  # декораторы
    @allure.description(
        'Из чего состоит позитивный сценарий:\n'
        'Нажать кнопку «Заказать». На странице две кнопки заказа.\n'
        'Заполнить форму заказа.\n'
        'Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.\n'
        'Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».\n'
        'Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.\n')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    @pytest.mark.parametrize('order_button , order_input_data',
                             [
                             [HomePageLocators.UP_ORDER, order_input_data_list[0]],
                             [HomePageLocators.DOWN_ORDER, order_input_data_list[1]]
                             ]
                             )
    def test_scooter_order(self, page_driver, order_button, order_input_data):
        home_page = HomePage(page_driver)
        home_page.check_cookies()

        home_page.click_order_button(order_button)

        order_page = OrderPage(page_driver)
        order_page.wait_for_load_order_page()

        order_page.set_form_who_is_scooter_for(order_input_data.name,
                                               order_input_data.surname,
                                               order_input_data.address,
                                               order_input_data.station_index,
                                               order_input_data.phone_number)

        order_page.click_next_button()

        order_page.set_form_about_rent(order_input_data.date_index,
                                       order_input_data.rental_period_index,
                                       order_input_data.color,
                                       order_input_data.comment)

        order_page.click_order_button()

        order_page.wait_for_load_pop_up_window_approve_order()

        order_page.click_approve_order_button()

        order_page.wait_for_load_pop_up_window_track_id()

        actually_value = order_page.check_status_button_text()
        expected_value = 'Посмотреть статус'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.title(
        'Проверка клика по Лого приложения')  # декораторы
    @allure.description(
        'Выполняется переход со страницы заказа на начальную страницу приложения')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    def test_logo(self, page_driver):
        home_page = HomePage(page_driver)
        home_page.click_order_button(HomePageLocators.UP_ORDER)
        order_page = OrderPage(page_driver)
        order_page.wait_for_load_order_page()
        home_page.click_logo()
        home_page.check_cookies()
        assert page_driver.current_url == url.HOME_PAGE

    @allure.title(
        'Проверка клика по Лого Яндекса')  # декораторы
    @allure.description(
        'Выполняется переход со главную страницу Дзена')
    @allure.testcase('ссылка на тест-кейс',
                     'https://practicum.yandex.ru/learn/qa-engineer-full-stack/courses/c8400844-cd6d-4bdc-80ea-aca5b24f3a4d/sprints/371240/topics/152222da-6b24-4ebe-936e-e5bb5f8cb37c/lessons/84de1174-4db2-426e-8c85-215190f90ef4/')
    def test_yandex(self, page_driver):
        home_page = HomePage(page_driver)
        home_page.click_yandex()
        home_page.wait_for_load_yandex_page()
        assert page_driver.current_url == url.YANDEX