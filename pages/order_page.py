from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.order_page_locators import OrderPageLocators
from pages.page import Page
import url

class OrderPage(Page):
    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.ORDER_PAGE))

    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.Fields.NAME).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.Fields.SURNAME).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.Fields.ADDRESS).send_keys(address)

    def wait_for_load_stations_menu(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.StationsMenu.STATIONS_MENU))

    def set_station(self, station_index):
        self.driver.find_element(*OrderPageLocators.Fields.STATION).click()
        self.wait_for_load_stations_menu()
        self.driver.find_element(*OrderPageLocators.StationsMenu.STATIONS[station_index]).click()