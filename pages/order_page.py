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

    def set_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.Fields.PHONE_NUMBER).send_keys(phone_number)

    def set_who_is_scooter_for(self, name, surname, address, station_index, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station_index)
        self.set_phone_number(phone_number)

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.Buttons.NEXT).click()

    def wait_for_load_about_rent_form(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.ABOUT_RENT))  # wait for load

    def click_date_field(self):
        self.driver.find_element(*OrderPageLocators.Fields.DATE).click()

    def wait_for_load_calendar(self, date_index):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.DATES[date_index]))  # wait for load

    def click_date_in_calendar(self, date_index):
        self.driver.find_element(*OrderPageLocators.DATES[date_index]).click()

    def set_date(self, date_index):
        self.click_date_field()
        self.wait_for_load_calendar(date_index)
        self.click_date_in_calendar(date_index)

    def click_rental_period_field(self):
        self.driver.find_element(*OrderPageLocators.Fields.RENTAL_PERIOD).click()

    def wait_for_load_rental_period_menu(self, rental_period_index):
        period_locator = OrderPageLocators.RENTAL_PERIODS[rental_period_index]
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(period_locator))  # wait for load

    def click_rental_period(self, rental_period_index):
        period_locator = OrderPageLocators.RENTAL_PERIODS[rental_period_index]
        self.driver.find_element(*period_locator).click()

    def set_rental_period(self, rental_period_index):
        self.click_rental_period_field()
        self.wait_for_load_rental_period_menu(rental_period_index)
        self.click_rental_period(rental_period_index)

    def set_color(self, color):
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLORS[color]).click()