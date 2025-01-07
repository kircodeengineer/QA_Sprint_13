from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.page import Page
import url

class OrderPage(Page):
    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url.ORDER_PAGE))

