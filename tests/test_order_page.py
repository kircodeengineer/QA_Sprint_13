from test_page import TestPage
from url import Url
from pages.home_page import HomePage
from pages.order_page import OrderPage

import time

class TestOrderPage(TestPage):
    def test_scooter_order(self):
        self.driver.get(Url.HOME_PAGE)
        home_page = HomePage(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_up_order_button()
        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page()
        time.sleep(2)