from selenium.webdriver.common.by import By

class OrderPageLocators:
    class Fields:
        NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
        SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
        ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
        PHONE_NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
        STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    NEXT_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")
    STATIONS_MENU = (By.XPATH,".//div[@class='select-search__select']")
    STATIONS = [(By.XPATH, ".//div[@class='Order_Text__2broi' and text()='Красносельская']"),
                (By.XPATH, ".//div[@class='Order_Text__2broi' and text()='Сокольники']")]