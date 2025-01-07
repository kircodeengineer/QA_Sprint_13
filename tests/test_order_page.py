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

def get_digits(text):
    return ''.join(c for c in text if c.isdigit())

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

        #set_make_order ???
        order_page.set_name(order_input_data.name)

        # set_surname
        field = self.driver.find_element(*OrderPageLocators.Fields.SURNAME)
        field.send_keys(order_input_data.surname)

        # set_address
        field = self.driver.find_element(*OrderPageLocators.Fields.ADDRESS)
        field.send_keys(order_input_data.address)

        # set_station
        field = self.driver.find_element(*OrderPageLocators.Fields.STATION)
        field.click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.StationsMenu.STATIONS_MENU))
        field = self.driver.find_element(*OrderPageLocators.StationsMenu.STATIONS[order_input_data.station_index]) # wait for load
        field.click()

        # set_phone_number
        field = self.driver.find_element(*OrderPageLocators.Fields.PHONE_NUMBER)
        field.send_keys(order_input_data.phone_number)

        # next
        field = self.driver.find_element(*OrderPageLocators.Buttons.NEXT)
        field.click()

        # set_date
        date_field_locator = OrderPageLocators.Fields.DATE
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(date_field_locator))
        field = self.driver.find_element(*date_field_locator)
        field.click()
        date_locator = OrderPageLocators.DATES[order_input_data.date_index]
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(date_locator)) # wait for load
        field = self.driver.find_element(*date_locator)
        field.click()

        # set_rental_period
        field = self.driver.find_element(*OrderPageLocators.Fields.RENTAL_PERIOD)
        field.click()
        period_locator = OrderPageLocators.RENTAL_PERIODS[order_input_data.rental_period_index]
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(period_locator)) # wait for load
        field = self.driver.find_element(*period_locator)
        field.click()

        #set_color
        field = self.driver.find_element(*OrderPageLocators.SCOOTER_COLORS[order_input_data.color])
        field.click()

        #set_comment
        field = self.driver.find_element(*OrderPageLocators.Fields.COMMENT)
        field.send_keys(order_input_data.comment)

        #make order
        field = self.driver.find_element(*OrderPageLocators.Buttons.DOWN_ORDER)
        field.click()

        #approve order
        approve_order_button_locator = OrderPageLocators.Buttons.POP_UP_APPROVE_ORDER
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(approve_order_button_locator)) # wait for load
        field = self.driver.find_element(*approve_order_button_locator)
        field.click()

        # watch status
        check_status_button_locator = OrderPageLocators.Buttons.POP_UP_CHECK_STATUS
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(check_status_button_locator)) # wait for load
        field = self.driver.find_element(*OrderPageLocators.TRACK_ID)
        track_id = get_digits(field.text)
        field = self.driver.find_element(*check_status_button_locator)
        field.click()

        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.TRACK_PAGE+track_id))

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