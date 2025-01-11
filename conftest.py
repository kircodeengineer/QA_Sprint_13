import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import url

@pytest.fixture(scope='function')
def page_driver(request):
    driver = webdriver.Firefox()
    driver.get(url.HOME_PAGE)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(url.HOME_PAGE))
    yield driver
    driver.quit()