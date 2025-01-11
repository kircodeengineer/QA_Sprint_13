from locators.order_page_locators import OrderPageLocators

class Answers:
    COST_AND_PAY = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ORDER_SOME_SCOOTERS = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    RENTAL_TIME = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    ORDER_TODAY = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    EXTEND_ORDER = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    CHARGER_INCLUDED = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    CANCEL_ORDER = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    BEYOND_MKAD = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

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