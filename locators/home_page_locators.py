from selenium.webdriver.common.by import By

class HomePageLocators:
    ANSWER_COST_AND_PAY_VISIBLE = (By.XPATH, ".//div[@id='accordion__panel-0' and not(@hidden)]")
    QUESTION_COST_AND_PAY = (By.ID, 'accordion__heading-0')