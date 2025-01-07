from selenium.webdriver.common.by import By

class HomePageLocators:
    class Answer:
        COST_AND_PAY = (By.XPATH, ".//div[@id='accordion__panel-0' and not(@hidden)]")
        ORDER_SOME_SCOOTERS = (By.XPATH, ".//div[@id='accordion__panel-1' and not(@hidden)]")
    class Question:
        COST_AND_PAY = (By.ID, 'accordion__heading-0')
        ORDER_SOME_SCOOTERS = (By.ID, 'accordion__heading-1')
