from selenium.webdriver.common.by import By

class HomePageLocators:
    class Answer:
        COST_AND_PAY = (By.XPATH, ".//div[@id='accordion__panel-0' and not(@hidden)]")
        ORDER_SOME_SCOOTERS = (By.XPATH, ".//div[@id='accordion__panel-1' and not(@hidden)]")
        RENTAL_TIME = (By.XPATH, ".//div[@id='accordion__panel-2' and not(@hidden)]")
        ORDER_TODAY = (By.XPATH, ".//div[@id='accordion__panel-3' and not(@hidden)]")
        EXTEND_ORDER = (By.XPATH, ".//div[@id='accordion__panel-4' and not(@hidden)]")
        CHARGER_INCLUDED = (By.XPATH, ".//div[@id='accordion__panel-5' and not(@hidden)]")
        CANCEL_ORDER = (By.XPATH, ".//div[@id='accordion__panel-6' and not(@hidden)]")
        BEYOND_MKAD = (By.XPATH, ".//div[@id='accordion__panel-7' and not(@hidden)]")

    class Button:
        UP_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']")
        DOWN_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp' and text()='Заказать']")

    class Question:
        COST_AND_PAY = (By.ID, 'accordion__heading-0')
        ORDER_SOME_SCOOTERS = (By.ID, 'accordion__heading-1')
        RENTAL_TIME = (By.ID, 'accordion__heading-2')
        ORDER_TODAY = (By.ID, 'accordion__heading-3')
        EXTEND_ORDER = (By.ID, 'accordion__heading-4')
        CHARGER_INCLUDED = (By.ID, 'accordion__heading-5')
        CANCEL_ORDER = (By.ID, 'accordion__heading-6')
        BEYOND_MKAD = (By.ID, 'accordion__heading-7')