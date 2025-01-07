from locators.common_locators import CommonLocators

class Page:
    def __init__(self, driver):
        self.driver = driver

    def _click_locator(self, locator):
        locator_to_click = self.driver.find_element(*locator)
        locator_to_click.click()

    def click_logo(self):
        self._click_locator(CommonLocators.LOGO)

    def click_yandex(self):
        self._click_locator(CommonLocators.YANDEX)

    def click_cookie(self):
        self._click_locator(CommonLocators.COOKIE_BUTTON)
