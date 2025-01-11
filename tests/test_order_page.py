import allure
import pytest

import url
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.home_page_locators import HomePageLocators

class OrderInputData:
    def __init__(self, name, surname, address, station_index, phone_number, date_index, rental_period_index, color, comment):
        self.name = name
        self.surname = surname
        self.address = address
        self.station_index = station_index
        self.phone_number = phone_number
        self.date_index = date_index
        self.rental_period_index = rental_period_index
        self.color = color
        self.comment = comment

order_input_data_list = [ OrderInputData("Иван",
                                         "Петров",
                                         "Любой адрес" ,
                                         0,
                                         "12345678901",
                                         0,
                                         0,
                                         OrderPageLocators.BLACK,
                                         "До утра"),
                          OrderInputData("Пётр",
                                         "Иванов",
                                         "Другой Любой адрес" ,
                                         1,
                                         "10987654321",
                                         1,
                                         1,
                                         OrderPageLocators.GREY,
                                         "До вечера")]


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
        home_page.wait_for_load_home_page()
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

        order_page.move_to_track_id_page()

        order_page.click_logo()
        home_page.wait_for_load_home_page()
        home_page.click_yandex()

        home_page.wait_for_load_yandex_page()

        home_page.move_from_yandex_page_to_order_scooter_page()

        actually_value = page_driver.current_url
        expected_value = url.HOME_PAGE
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'