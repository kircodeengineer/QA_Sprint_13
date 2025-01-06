import time

from selenium.webdriver.common.by import By
from selenium import webdriver

#tests on start
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver

# класс с автотестом
class TestHomePage:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    def test_question_cost_and_pay(self):
        # перешли на страницу тестового приложения
        url = 'https://qa-scooter.praktikum-services.ru/'
        self.driver.get(url)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))
        assert self.driver.current_url == url
        # Найди футер
        element = self.driver.find_element(By.ID, 'accordion__heading-0')
        # Прокрути страницу до футера
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        #element_attribute_to_include
        element.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@id='accordion__panel-0' and not(@hidden)]")))
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()

