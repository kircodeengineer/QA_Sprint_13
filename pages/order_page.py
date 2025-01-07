from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from url import Url

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(Url.ORDER_PAGE))