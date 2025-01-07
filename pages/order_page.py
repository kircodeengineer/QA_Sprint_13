import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.order_page_locators import OrderPageLocators
from pages.page import Page
import url

@allure.step('Получаем числовое значение номера заказа из текста {text}')
def get_digits(text):
    return ''.join(c for c in text if c.isdigit())

class OrderPage(Page):
    @allure.step('Ожидаем загрузку страницы оформления заказа')
    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.ORDER_PAGE))

    @allure.step('Задаём Имя {name}')
    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.Fields.NAME).send_keys(name)

    @allure.step('Задаём Фамилию {surname}')
    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.Fields.SURNAME).send_keys(surname)

    @allure.step('Задаём Адрес {address}')
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.Fields.ADDRESS).send_keys(address)

    @allure.step('Ожидаем загрузку выпадающего меню со станциями метро')
    def wait_for_load_stations_menu(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.StationsMenu.STATIONS_MENU))

    @allure.step('Выбираем станцию по индексу {station_index}')
    def set_station(self, station_index):
        self.driver.find_element(*OrderPageLocators.Fields.STATION).click()
        self.wait_for_load_stations_menu()
        self.driver.find_element(*OrderPageLocators.StationsMenu.STATIONS[station_index]).click()

    @allure.step('Задаём Телефонный номер {phone_number}')
    def set_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.Fields.PHONE_NUMBER).send_keys(phone_number)

    @allure.step('Заполняем форму Для кого самокат {name}, {surname}, {address}, {station_index}, {phone_number}')
    def set_form_who_is_scooter_for(self, name, surname, address, station_index, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station_index)
        self.set_phone_number(phone_number)

    @allure.step('Кликаем по кнопке Далее')
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.Buttons.NEXT).click()

    @allure.step('Ожидаем загрузку формы Про аренду')
    def wait_for_load_about_rent_form(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.ABOUT_RENT))  # wait for load

    @allure.step('Кликаем по полю Когда привезти самокат')
    def click_date_field(self):
        self.driver.find_element(*OrderPageLocators.Fields.DATE).click()

    @allure.step('Ожидаем загрузку календаря')
    def wait_for_load_calendar(self, date_index):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.DATES[date_index]))  # wait for load

    @allure.step('Кликаем по дате с индексом {date_index}')
    def click_date_in_calendar(self, date_index):
        self.driver.find_element(*OrderPageLocators.DATES[date_index]).click()

    @allure.step('Задаём дату с индексом {date_index}')
    def set_date(self, date_index):
        self.click_date_field()
        self.wait_for_load_calendar(date_index)
        self.click_date_in_calendar(date_index)

    @allure.step('Кликаем по полю Срок аренды')
    def click_rental_period_field(self):
        self.driver.find_element(*OrderPageLocators.Fields.RENTAL_PERIOD).click()

    @allure.step('Ожидаем загрузку меню с периодами')
    def wait_for_load_rental_period_menu(self, rental_period_index):
        period_locator = OrderPageLocators.RENTAL_PERIODS[rental_period_index]
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(period_locator))  # wait for load

    @allure.step('Выбираем период аренды по индексу {rental_period_index}')
    def click_rental_period(self, rental_period_index):
        period_locator = OrderPageLocators.RENTAL_PERIODS[rental_period_index]
        self.driver.find_element(*period_locator).click()

    @allure.step('Задаем период аренды по индексу {rental_period_index}')
    def set_rental_period(self, rental_period_index):
        self.click_rental_period_field()
        self.wait_for_load_rental_period_menu(rental_period_index)
        self.click_rental_period(rental_period_index)

    @allure.step('Задаем цвет {color}')
    def set_color(self, color):
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLORS[color]).click()

    @allure.step('Задаем комментарий {comment}')
    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.Fields.COMMENT).send_keys(comment)

    @allure.step('Заполняем форму Про аренду {date_index}, {rental_period_index}, {color}, {comment}')
    def set_form_about_rent(self, date_index, rental_period_index, color, comment):
        self.wait_for_load_about_rent_form()
        self.set_date(date_index)
        self.set_rental_period(rental_period_index)
        self.set_color(color)
        self.set_comment(comment)

    @allure.step('Кликаем по кнопке Заказать')
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.Buttons.DOWN_ORDER).click()

    @allure.step('Ожидаем загрузку всплывающего Окна подтверждения заказа')
    def wait_for_load_pop_up_window_approve_order(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.Buttons.POP_UP_APPROVE_ORDER))

    @allure.step('Кликаем по кнопке Да для подтверждения заказа')
    def click_approve_order_button(self):
        self.driver.find_element(*OrderPageLocators.Buttons.POP_UP_APPROVE_ORDER).click()

    @allure.step('Ожидаем загрузку всплывающего Окна номером заказа')
    def wait_for_load_pop_up_window_track_id(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.Buttons.POP_UP_CHECK_STATUS))

    @allure.step('Выполняем переход в Окно со статусом заказа')
    def move_to_track_id_page(self):
        track_id = get_digits(self.driver.find_element(*OrderPageLocators.TRACK_ID).text)
        self.driver.find_element(*OrderPageLocators.Buttons.POP_UP_CHECK_STATUS).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.TRACK_PAGE + track_id))