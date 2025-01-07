import pytest

from test_page import TestPage
from url import Url
from pages.home_page import HomePage
from pages.order_page import OrderPage

import time
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class OrderInputData:
    def __init__(self, name, surname, address, station_index, phone_number):
        self.name = name
        self.surname = surname
        self.address = address
        self.station_index = station_index
        self.phone_number = phone_number

order_input_data_list = [ OrderInputData("Иван", "Петров", "Любой адрес" , 0, "12345678901"),
                          OrderInputData("Пётр", "Иванов", "Другой Любой адрес" , 1, "10987654321"),]

class TestOrderPage(TestPage):
    @pytest.mark.parametrize('order_input_data', order_input_data_list)
    def test_scooter_order(self, order_input_data):
        self.driver.get(Url.HOME_PAGE)
        home_page = HomePage(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_up_order_button()
        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page()
        field = self.driver.find_element(*OrderPageLocators.Fields.NAME)
        field.send_keys(order_input_data.name)
        field = self.driver.find_element(*OrderPageLocators.Fields.SURNAME)
        field.send_keys(order_input_data.surname)
        field = self.driver.find_element(*OrderPageLocators.Fields.ADDRESS)
        field.send_keys(order_input_data.address)
        field = self.driver.find_element(*OrderPageLocators.Fields.STATION)
        field.click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.STATIONS_MENU))
        field = self.driver.find_element(*OrderPageLocators.STATIONS[order_input_data.station_index])
        field.click()
        field = self.driver.find_element(*OrderPageLocators.Fields.PHONE_NUMBER)
        field.send_keys(order_input_data.phone_number)
        field = self.driver.find_element(*OrderPageLocators.NEXT_BUTTON)
        field.click()
        '''
        order_page.click_logo()
        home_page.wait_for_load_home_page()
        home_page.click_down_order_button()
        order_page.wait_for_load_order_page()
        '''
        time.sleep(2)