from locators.home_page_locators import HomePageLocators

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_question_cost_and_pay(self):
        question_cost_and_pay = self.driver.find_element(*HomePageLocators.QUESTION_COST_AND_PAY)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_cost_and_pay)
        question_cost_and_pay.click()

