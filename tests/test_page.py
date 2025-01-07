from selenium import webdriver

class TestPage:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()