from selenium.webdriver.common.by import By

class OrderPageLocators:
    class Fields:
        NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
        SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
        ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
        PHONE_NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
        STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
        DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
        RENTAL_PERIOD = (By.XPATH, ".//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
        COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    DATES = [(By.XPATH, ".//div[@class='react-datepicker__day react-datepicker__day--001']"),
             (By.XPATH, ".//div[@class='react-datepicker__day react-datepicker__day--002']")]

    RENTAL_PERIODS = [(By.XPATH, ".//div[@class='Dropdown-option' and text()='двое суток']"),
                     (By.XPATH, ".//div[@class='Dropdown-option' and text()='трое суток']")]

    class StationsMenu:
        STATIONS_MENU = (By.XPATH, ".//div[@class='select-search__select']")
        STATIONS = [(By.XPATH, ".//div[@class='Order_Text__2broi' and text()='Красносельская']"),
                    (By.XPATH, ".//div[@class='Order_Text__2broi' and text()='Сокольники']")]

    BLACK = "black"
    GREY = "grey"
    SCOOTER_COLORS = { BLACK : (By.XPATH, ".//input[@class='Checkbox_Input__14A2w' and @id='black']"),
               GREY : (By.XPATH, ".//input[@class='Checkbox_Input__14A2w' and @id='grey']")}

    TRACK_ID = (By.XPATH, ".//div[@class='Order_Text__2broi']")
    class Buttons:
        NEXT = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")
        POP_UP_APPROVE_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
        DOWN_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
        POP_UP_CHECK_STATUS = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")