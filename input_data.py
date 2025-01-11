from locators.order_page_locators import OrderPageLocators

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