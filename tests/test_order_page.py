import pytest

from test_page import TestPage
import url
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.home_page_locators import HomePageLocators

import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

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


class TestOrderPage(TestPage):
    cookie = False
    @pytest.mark.parametrize('order_button , order_input_data',
                             [
                             [HomePageLocators.UP_ORDER, order_input_data_list[0]],
                             [HomePageLocators.DOWN_ORDER, order_input_data_list[1]]
                             ]
                             )
    def test_scooter_order(self, order_button, order_input_data):

        self.driver.get(url.HOME_PAGE)
        home_page = HomePage(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_order_button(order_button)

        order_page = OrderPage(self.driver)
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
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.YANDEX))
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.HOME_PAGE))
        actually_value = self.driver.current_url
        expected_value = url.HOME_PAGE
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'